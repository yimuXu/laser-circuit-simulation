from photon import Photon

'''
Receiver - A photodetector which absorbs photons and stores its energy. 
When a photon reaches a receiver, the receiver will absorb the photon and
abosrb its energy. Once a receiver absorbs a photon, the receiver becomes
activated. An activated receiver can keep absorbing photons.

You are free to add more attributes and methods, as long as you aren't
modifying the existing scaffold.
'''


class Receiver:


    def __init__(self, symbol: str, x: int, y: int):

        self.component_type = 'receiver'
        self.symbol = symbol
        self.x = x
        self.y = y
        self.total_energy = 0.00
        self.photons_absorbed = 0
        self.activation_time = 0
        self.activated = False



    def convert_frequency_to_energy(frequency: int) -> float:
        # define our constants
        PLANCKS_CONSTANT = 6.62607015 * 10**-34
        THZ_TO_HZ = 10**12
        JOULES_TO_EV = 1.60217662*10**-19

        # calculate the joules then convert to electronvolts
        joules = PLANCKS_CONSTANT * frequency * THZ_TO_HZ
        electronvolts = joules / JOULES_TO_EV
        return electronvolts


    def absorb_photon(self, photon: Photon, timestamp: int) -> None:
        if photon.x == self.get_x() and photon.y == self.get_y():
            photon_frequency = photon.frequency
            photon_energy = Receiver.convert_frequency_to_energy(photon_frequency)
            self.total_energy += photon_energy
            if self.is_activated() == False:
                self.activated = True
                self.photons_absorbed += 1
                self.activation_time = timestamp
            else:
                self.photons_absorbed += 1
            photon.got_absorbed()

            

    def is_activated(self) -> bool:
        '''Returns whether or not this receiver is activated. '''
        return self.activated 

    
    def get_total_energy(self) -> float:
        '''Returns total_energy.'''
        return self.total_energy


    def get_activation_time(self) -> int:
        '''Returns activation_time.'''
        return self.activation_time


    def get_component_type(self) -> str:
        '''Returns component type.'''
        return self.component_type


    def get_symbol(self) -> str:

        num = str(self.symbol[1])
        return num


    def get_x(self) -> int:
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        '''Returns y.'''
        return self.y

    
    def __str__(self) -> str:
        result = f'{self.symbol}: {self.total_energy:.02f}eV ({self.photons_absorbed})'
        return result
