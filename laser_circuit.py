import sorter
from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror
from board_displayer import BoardDisplayer

'''

LaserCircuit - Responsible for storing all the components of the circuit and
handling the computation of running the circuit. It's responsible for delegating 
tasks to the specific components e.g. making each emitter emit a photon, getting 
each photon to move and interact with components, etc. In general, this class is
responsible for handling any task related to the circuit.

You are free to add more attributes and methods, as long as you aren't 
modifying the existing scaffold.
'''


class LaserCircuit:


    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height
        self.clock = 0
        self.emitters = []
        self.receivers = []
        self.photons = []
        self.mirrors = []
        self.board_displayer = BoardDisplayer(width, height)


    def emit_photons(self) -> None:

        # set photons with the same value as emitter respectively
        i = 0
        while i < len(self.emitters):
            pho = self.emitters[i].emit_photon()
            self.photons.append(pho)
            i += 1


    def is_finished(self) -> bool:
        # check whether every photons are absorbed
        i = 0
        while i < len(self.photons):
            if self.photons[i].is_absorbed() == True:
                i += 1
            else:
                return False
        return True


    def print_emit_photons(self) -> None:
        filename = 'output/emit_photons.out'
        fobj = open(filename,'w')
        i = 0
        print('0ns: Emitting photons.')
        while i < len(self.emitters):
            print(f'{self.emitters[i].__str__()}', file=fobj)
            print(f'{self.emitters[i].__str__()}')
            i += 1
        fobj.close()


    def print_activation_times(self) -> None:

        filename = 'output/activation_times.out'
        f = open(filename,'w')
        i = 0
        new_ls = sorter.sort_receivers_by_activation_time(self.receivers)
        print('\nActivation times:')
        while i < len(new_ls):
            if new_ls[i].is_activated() == True:
                f.write(f'R{new_ls[i].get_symbol()}: {new_ls[i].get_activation_time()}ns\n')
                print(f'R{new_ls[i].get_symbol()}: {new_ls[i].get_activation_time()}ns')
            i += 1
        f.close()


    def print_total_energy(self) -> None:

        filename = 'output/total_energy.out'
        f = open(filename,'w')
        i = 0
        print('\nTotal energy absorbed:')
        new_ls = sorter.sort_receivers_by_total_energy(self.receivers)
        while i < len(new_ls):
            if new_ls[i].is_activated() == True:
                print(f'R{new_ls[i].get_symbol()}: {new_ls[i].get_total_energy():.02f}eV ({new_ls[i].photons_absorbed})', file=f)
                print(f'R{new_ls[i].get_symbol()}: {new_ls[i].get_total_energy():.02f}eV ({new_ls[i].photons_absorbed})')
            i += 1
        f.close()
 
    def print_board(self) -> None:
        '''Calls the print_board method in board_displayer.'''
        self.board_displayer.print_board()

    def get_collided_emitter(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Emitter | None:

        # remove the line below once you start implementing this function
        x = int(entity.get_x())
        y = int(entity.get_y())
        i = 0
        while i < len(self.emitters):
            if x == self.emitters[i].get_x() and y == self.emitters[i].get_y():
                return self.emitters[i]
                break
            i += 1


    def get_collided_receiver(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Receiver | None:
        # remove the line below once you start implementing this function
        x = int(entity.get_x())
        y = int(entity.get_y())
        i = 0
        while i < len(self.receivers):
            if x == self.receivers[i].x and y == self.receivers[i].y:
                return self.receivers[i]
                break
            i += 1
        # return None



    def get_collided_mirror(self, entity: Emitter | Receiver | Photon | Mirror | None) -> Mirror | None:

        # remove the line below once you start implementing this function
        x = entity.get_x()
        y = entity.get_y()
        ls = self.mirrors
        i = 0
        while i < len(ls):
            if x == ls[i].x and y == ls[i].y:
                return ls[i]
            i += 1
        return

    def get_collided_component(self, photon: Photon) -> Emitter | Receiver | Mirror | None:
        # check if photon get collided with component

        check1 = self.get_collided_emitter(photon)
        check2 = self.get_collided_receiver(photon)
        check3 = self.get_collided_mirror(photon)
        if check1 != None:
            return check1
        if check2 != None:
            return check2
        if check3 != None:
            return check3
        return


    def tick(self) -> None:
        while True:
            self.clock += 1
            if len(self.emitters) == 0:
                self.clock -= 1
                break
            if self.is_finished() == True:
                break
            photon_index = 0
        # check if this photon is absorbed, if it is, skip it, else, move it.
            while photon_index < len(self.photons):
                if self.photons[photon_index].is_absorbed() == True:
                    photon_index += 1
                    continue
                self.photons[photon_index].move(self.width, self.height)
                 # check if it gets collided and what it gets collided with 
                collided_component = self.get_collided_component(self.photons[photon_index])
                if isinstance(collided_component, Receiver):
                    collided_component.absorb_photon(self.photons[photon_index], self.clock)
                elif isinstance(collided_component, Mirror):
                    collided_component.reflect_photon(self.photons[photon_index])
                # add component to the board
                else:
                    self.board_displayer.add_photon_to_board(self.photons[photon_index])
                photon_index += 1

            break


    def run_circuit(self) -> None:
        print('='*24+'\n   RUNNING CIRCUIT...\n'+'='*24+'\n')
        # print the photon that have been set frequency and direation
        self.print_emit_photons()
        # move photon, and print the board every 5 ns or when the last photon is absorbed
        while True:
            self.tick()
            if self.clock % 5 == 0 or self.is_finished() == True:
                # calculate how many receivers have been activated
                receiver_index = 0
                activated_receiver_num = 0
                while receiver_index < len(self.receivers):
                    if self.receivers[receiver_index].is_activated() is True:
                        activated_receiver_num += 1
                    receiver_index += 1
                print(f'\n{self.clock}ns: {activated_receiver_num}/{len(self.receivers)} receiver(s) activated.')
                self.print_board()
                # check if all the photons are absorbed
                if self.is_finished() == True:
                    break
        self.print_activation_times()
        self.print_total_energy()
        print('\n' + '=' * 24 + '\n   CIRCUIT FINISHED!\n' + '=' * 24)


    def add_emitter(self, emitter: Emitter) -> bool:
        # s1 check if it is a instance of Emitter
        if not isinstance(emitter, Emitter):
            return False
        # s2 check if the coordinats is valid
        else:
            x = emitter.get_x()
            y = emitter.get_y()
            set_symbol = emitter.get_symbol()
            width = self.get_width()
            height = self.get_height()
            if not (0 <= x < width and 0 <= y < height):
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            # s3 check if it get collided with other emitter
            else:
                test = self.get_collided_emitter(emitter)
                if test != None:
                    print(f'Error: position ({x}, {y}) is already taken by emitter \'{test.get_symbol()}\'')
                    return False
                # s4 check if symbol has been taken
                else:
                    if len(self.emitters) == 0:
                        self.emitters.append(emitter)
                        self.board_displayer.add_component_to_board(emitter)
                        return True
                    else:
                        index = 0
                        symbol = self.emitters[index].get_symbol()
                        while index < len(self.emitters):
                            if set_symbol == symbol:
                                print(f'Error: symbol \'{symbol}\' is already taken.')
                                return False
                            else:
                                index += 1
                        # s5 put it into the list 
                        self.emitters.append(emitter)
                        self.board_displayer.add_component_to_board(emitter)
                        return True


    def get_emitters(self) -> list[Emitter]:
        '''Returns emitters.'''
        result = sorter.sort_receivers_by_symbol(self.emitters)
        return result

    
    def add_receiver(self, receiver: Receiver) -> bool:
        # s1 check if it is a instance of receiver
        if not isinstance(receiver,Receiver):
            return False
        # S2 check if its coordinates is valid
        else:
            x=receiver.get_x()
            y=receiver.get_y()
            set_symbol=receiver.get_symbol()
            width = self.get_width()
            height = self.get_height()
            if not (0 <= x < width and 0 <= y < height):
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            # s3 check if it get collided with other receivers or emitters
            else:
                test1 = self.get_collided_emitter(receiver)
                test2 = self.get_collided_receiver(receiver)
                if test1 != None:
                    print(f'Error: position ({x}, {y}) is already taken by emitter \'{test1.get_symbol()}\'')
                    return False
                if test2 != None:
                    print(f'Error: position ({x}, {y}) is already taken by receiver \'R{test2.get_symbol()}\'')
                    return False
                # s4 check if symbol has been taken
                else:
                    if len(self.receivers) == 0:
                        self.receivers.append(receiver)
                        self.board_displayer.add_component_to_board(receiver)
                        return True
                    else:
                        receiver_index = 0
                        while receiver_index < len(self.receivers):
                            symbol = self.receivers[receiver_index].get_symbol()
                            if set_symbol == symbol:
                                print(f'Error: symbol \'R{symbol}\' is already taken')
                                return False
                            else:
                                receiver_index += 1
                        # s5 put it into list
                        self.receivers.append(receiver)
                        self.board_displayer.add_component_to_board(receiver)
                        return True


    def get_receivers(self) -> list[Receiver]:
        '''Returns receivers.'''
        result = sorter.sort_receivers_by_symbol(self.receivers)
        return result


    def add_photon(self, photon: Photon) -> bool:

        if isinstance(photon,Photon):
            self.photons.append(photon)
            return True
        else:
            False


    def get_photons(self) -> list[Photon]:
        '''Returns photons.'''
        return self. photons


    def add_mirror(self, mirror: Mirror) -> bool:
        # s1 check if it is a instance of mirror
        if not isinstance(mirror, Mirror):
            return False
        # s2 check if its coordinates is valid
        else:
            x=mirror.get_x()
            y = mirror.get_y()
            if x >= self.width or y >= self.height:
                print(f'Error: position ({x}, {y}) is out-of-bounds of {self.width}x{self.height} circuit board')
                return False
            # s3 check if it get collided with other receivers or emitters or mirrors
            if self.get_collided_mirror(mirror):
                print(f'Error: position ({x}, {y}) is already taken by mirror \'{self.get_collided_mirror(mirror).get_symbol()}\'')
                return False
            if self.get_collided_emitter(mirror):
                print(f'Error: position ({x}, {y}) is already taken by emitter \'{self.get_collided_emitter(mirror).get_symbol()}\'')
                return False
            if self.get_collided_receiver(mirror):
                print(f'Error: position ({x}, {y}) is already taken by receiver \'{self.get_collided_receiver(mirror).get_symbol()}\'')
                return False
            # s4 put it into list
            self.mirrors.append(mirror)
            self.board_displayer.add_component_to_board(mirror)
            return True
            
    def get_mirrors(self) -> list[Mirror]:
        '''Returns mirrors.'''
        return self.mirrors

    
    def get_width(self) -> int:
        '''Returns width.'''
        return self.width

    def get_height(self) -> int:
        '''Returns height.'''
        return self.height
