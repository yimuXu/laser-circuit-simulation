from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror

'''

BoardDisplayer - A helper class used to display the circuit board.
Each time a component is added to the circuit, this board is updated to 
store the component's symbol in its assigned position on the board.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class BoardDisplayer:


    def __init__(self, width: int, height: int):

        #initialise the variable
        self.width = width
        self.height = height
        self.board = self.create_board()


    def create_board(self) -> list[list[str]]:

        
        cell = ' ' 
        ls = [] 
        i = 0
        while i < self.height:
            cell_ls = []
            j = 0
            while j < self.width:
                cell_ls.append(cell)
                j+=1
            ls.append(cell_ls)
            i+=1
        return ls


    def add_component_to_board(self, component: Emitter | Receiver | Mirror) -> None:

        sym = component.get_symbol()
        x1 = int(component.get_x())
        y1 = int(component.get_y())
        self.board[y1][x1] = sym
        

    def add_photon_to_board(self, photon: Photon) -> None:
        
        x = photon.get_x()
        y = photon.get_y()
        if self.board[y][x] == ' ': #check if the coordinates is empty
            self.board[y][x] = '.'
        

    def print_board(self) -> None:

        w = self.width
        h = self.height
        border1 = '+' + '-' * w + '+'
        border2 = '+' + '-' * w + '+'
        j=0
        print(border1)
        while j<h:
            i=0
            string='|'
            while i<w:
                string+=self.board[j][i]
                i+=1
                if i==w:
                    string+= '|'
                    print(string)
            j+=1
        print(border2)

board=BoardDisplayer(18,6)









