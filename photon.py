'''

Photon - A particle of light that are emitted by emitters and travels along the
circuit board. Photons have a frequency (THz) and direction. They can interact 
with components in the circuit in which it may be absorbed. When a photon is
absorbed, they no longer move.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.

Warning: Importing other components in this module will cause a circular import
error, as those components require this module to be fully initialised before
it can finish initialising itself. If you need to query the type of a component,
use the component_type attribute that each component has defined instead.
'''

class Photon:

    def __init__(self, x: int, y: int, frequency: int, direction: str):
        self.x = x
        self.y = y
        self.frequency = frequency
        self.direction = direction
        self.absorbed = False
        self.symbol = '.'


    def move(self, board_width: int, board_height: int) -> None:
        # move the photon to right direction 
        if self.get_direction() == 'N':
            if self.y == 0:
                self.got_absorbed()
            else:
                self.y -= 1
        elif self.get_direction() == 'S':
            
            if self.y == board_height-1:
                self.got_absorbed()
            else:
                self.y += 1
        elif self.get_direction() == 'E':
            if self.x == board_width-1:
                self.got_absorbed()
            else:
                self.x += 1
        elif self.get_direction() == 'W':
            
            if self.x == 0:
                self.got_absorbed()
            else:
                self.x -= 1

    def interact_with_component(self, component: object, timestamp: int) -> None:
        if self.absorbed == True:
            return
        else:
            tp = component.get_component_type()
            if tp == 'Receiver':
                self.absorbed = True
            if tp == 'mirror':
                component.reflect_photon(self)
                



    def got_absorbed(self) -> None:
        '''Updates the absorbed attribute to represent an absorption.'''
        self.absorbed = True


    def is_absorbed(self) -> bool:
        '''Returns absorbed.'''
        return self.absorbed


    def set_direction(self, direction: str) -> None:

        if direction == 'N' or direction == 'W' or direction == 'E' or direction == 'S': 
            self.direction = direction


    def get_direction(self) -> str:
        '''Returns direction.'''
        return self.direction

        
    def get_frequency(self) -> int:
        '''Returns frequency.'''
        return self.frequency


    def get_symbol(self) -> str:
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        '''Returns x.'''
        return int(self.x)


    def get_y(self) -> int:
        '''Returns y.'''
        return int(self.y)
