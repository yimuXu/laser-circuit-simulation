from photon import Photon

'''

Mirror - A surface that reflect photons, changing the direction in which they 
travel. A photon may also become lost depending on the type of mirror and the
photon's initial direction when it reaches the mirror.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class Mirror:
    

    def __init__(self, symbol: str, x: int, y: int):

        self.symbol = symbol
        self.x = x
        self.y = y
        self.component_type = 'mirror'



    def reflect_photon(self, photon: Photon) -> None:
        
        if photon.is_absorbed() == True:
            return
        # modify the direction based on the symbol of mirror that it get collided with
        if photon.get_direction() == 'N':
            if self.get_symbol() == '^' or self.get_symbol() == 'v':
                photon.got_absorbed()
            elif self.get_symbol() == '>' or self.get_symbol() == '/':
                photon.set_direction('E')
            elif self.get_symbol() == '<' or self.get_symbol() == '\\':
                photon.set_direction('W')
        elif photon.get_direction() == 'S':
            if self.get_symbol() == '^' or self.get_symbol() == 'v':
                photon.got_absorbed()
            elif self.get_symbol() == '>' or self.get_symbol() == '\\':
                photon.set_direction('E')
            elif self.get_symbol() == '<' or self.get_symbol() == '/':
                photon.set_direction('W')
        elif photon.get_direction() == 'E':
            if self.get_symbol() == '<' or self.get_symbol() == '>':
                photon.got_absorbed()
            elif self.get_symbol() == '^' or self.get_symbol() == '/':
                photon.set_direction('N')
            elif self.get_symbol() == 'v' or self.get_symbol() == '\\':
                photon.set_direction('S')
        elif photon.get_direction() == 'W':
            if self.get_symbol() == '<' or self.get_symbol() == '>':
                photon.got_absorbed()
            elif self.get_symbol() == '^' or self.get_symbol() == '\\':
                photon.set_direction('N')
            elif self.get_symbol() == 'v' or self.get_symbol() == '/':
                photon.set_direction('S')
                            
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
