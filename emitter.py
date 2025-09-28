from photon import Photon

'''

Emitter - A laser that emits a photon with a frequency and direction.
The frequency and direction of the photon it emits is determined by the
pulse  sequence.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class Emitter:


    def __init__(self, symbol: str, x: int, y: int):

        self.component_type = 'emitter'
        self.symbol = symbol
        self.x = x
        self.y = y
        self.frequency = 0
        self.direction = None
        self.pulse_sequence_set = False
        
    def emit_photon(self) -> Photon:
        photon=Photon(self.x,self.y,self.frequency,self.direction)
        return photon


    def set_pulse_sequence(self, frequency: int, direction: str) -> None:
        if frequency<=0:
            return
        else:
            if direction == 'N' or direction == 'E' or direction == 'W' or direction == 'S':
                self.direction = direction
                self.frequency = frequency
                self.pulse_sequence_set = True


    def is_pulse_sequence_set(self) -> bool:
        return self.pulse_sequence_set


    def get_frequency(self) -> int:
        return self.frequency


    def get_direction(self) -> str:
        '''Returns direction.'''
        return self.direction


    def get_component_type(self) -> str:
        '''Returns component type.'''
        return self.component_type


    def get_symbol(self) -> str:
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        '''Returns y.'''
        return self.y


    def __str__(self) -> str:

        if self.get_direction() == 'S':
            result=f'{self.get_symbol()}: {self.get_frequency()}THz, South'
        if self.get_direction() == 'N':
            result=f'{self.get_symbol()}: {self.get_frequency()}THz, North'
        if self.get_direction() == 'W':
            result=f'{self.get_symbol()}: {self.get_frequency()}THz, West'
        if self.get_direction() == 'E':
            result=f'{self.get_symbol()}: {self.get_frequency()}THz, East' 
        if self.get_direction()==None:
            result=f'{self.get_symbol()}: {self.get_frequency()}THz, None'
        return result
