import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit

'''


run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    i = 0 
    while i < len(sys.argv):
        if sys.argv[i] == '-RUN-MY-CIRCUIT':
            return True
        i += 1
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:

    i = 0
    while i < len(args):
        if args[i] == '-ADD-MY-MIRRORS':
            return True
        i += 1
    return False 


def initialise_circuit() -> LaserCircuit:

    print('Creating circuit board...')
    while True:
        # s1 initialise the board
        user_in = input('> ')
        size = input_parser.parse_size(user_in)
        if size != None:
            print(f'{size[0]}x{size[1]} board created.\n')
            la_cir = LaserCircuit(size[0],size[1])
            break
    # s2 add emitter
    print('Adding emitter(s)...')
    set_emitter_num = 0
    while set_emitter_num < 10:
        input_emitter = input('> ')
        if input_emitter == 'END EMITTERS':
            break
        emitter = input_parser.parse_emitter(input_emitter)
        if emitter == None:
            continue
        successfully_add_emitter = la_cir.add_emitter(emitter)
        if not successfully_add_emitter:
            continue
        set_emitter_num += 1
    print(f'{len(la_cir.emitters)} emitter(s) added.')
    # s3 add receiver
    print('\nAdding receiver(s)...')
    set_receiver_num = 0
    while set_receiver_num < 10:
        input_receiver = input('> ')
        if input_receiver == 'END RECEIVERS':
            break
        receiver = input_parser.parse_receiver(input_receiver)
        if receiver == None:
            continue
        successfully_add_receiver = la_cir.add_receiver(receiver)
        if not successfully_add_receiver:
            continue
        set_receiver_num += 1
    print(f'{len(la_cir.receivers)} receiver(s) added.')
    # s4 add mirror if flag has been detected
    commend_line=0
    while commend_line < len(sys.argv):
        if sys.argv[commend_line] == '-ADD-MY-MIRRORS':
            print('\n<ADD-MY-MIRRORS FLAG DETECTED!>\n')
            add_mirrors(la_cir)
        commend_line += 1
    return la_cir



def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # s1 set the pulse sequence 
    print('\nSetting pulse sequence...')
    # get the number of lines
    f = open(file_obj,'r')
    a = f.readlines()
    f.close()
    # 
    f = open(file_obj,'r')
    total_of_line = 0
    number_of_line = 1
    while total_of_line < len(a):
        # get line in file
        ori_line = f.readline()
        line = ori_line.strip('\n')
        ls = line.split()
        if ls == []:
            break
        string = '-- ('
        j = 0
        # print the emitter that have not been set
        be_set=[]
        while j < len(circuit.emitters):
            if circuit.emitters[j].is_pulse_sequence_set() == False:
                string+=circuit.emitters[j].get_symbol()+', '
            # put emitter have not been set into list
            else:
                be_set.append(circuit.emitters[j].get_symbol())
            j += 1
        string1 = string.strip(', ')+')'
        # check if it is empty
        # if string1 != '-- ()':
        print(string1)
        print(f'Line {number_of_line}: {line}')
        number_of_line+=1
        if input_parser.parse_pulse_sequence(line) == None:
            continue
        else:
            x = 0
            while x < len(be_set):
                if ls[0] == be_set[x]:
                    print(f'Error: emitter \'{ls[0]}\' already has its pulse sequence set')
                x += 1
            # find the corresponding emitter and set frequency and direction
            y = 0
            while y < len(circuit.emitters):
                if ls[0] == circuit.emitters[y].get_symbol():
                    circuit.emitters[y].set_pulse_sequence(int(ls[1]), ls[2])
                    p = circuit.emitters[y].emit_photon()
                    circuit.photons.append(p)

                    circuit.emitters[y].pulse_sequence_set = True
                    break
                
                if y == len(circuit.emitters)-1:
                    print(f'Error: emitter \'{ls[0]}\' does not exist')
                y += 1
        total_of_line += 1
    f.close()
    print('Pulse sequence set.\n')


def add_mirrors(circuit: LaserCircuit) -> None:

    print('Adding mirror(s)...')
    while True:
        add_new_mirror = input('> ')
        if add_new_mirror == 'END MIRRORS':
            num = len(circuit.mirrors)
            print(f'{num} mirror(s) added.')
            break
        # check if it is valid
        new_mirror = input_parser.parse_mirror(add_new_mirror)
        if new_mirror != None:
            circuit.add_mirror(new_mirror)
def main(args: list[str]) -> None:
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''

    #remove the line below once you start implementing this function
    cir = initialise_circuit()
    print()
    cir.print_board()
    print()
    i = 0
    while i < len(sys.argv):
        
        if sys.argv[i] == '-RUN-MY-CIRCUIT':
            print('<RUN-MY-CIRCUIT FLAG DETECTED!>')
            try:
                filename = 'input/pulse_sequence.in'
                f = open(filename)
            except FileNotFoundError:
                print('\nError: -RUN-MY-CIRCUIT flag detected but input/pulse_sequence.in does not exist')
                break
            f.close()
            set_pulse_sequence(cir, filename)
            cir.run_circuit()
        
        i += 1
if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
    pass
