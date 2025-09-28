from emitter import Emitter
from receiver import Receiver
from mirror import Mirror

'''

input_parser - A module that parses the inputs of the program. 
We define parsing as checking the validity of what has been entered 
to determine if it's valid. If it's not valid, an appropriate message 
should be printed. Whenever we retrieve input in the program, we 
should be using functions from this module to validate it.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def parse_size(user_input: str) -> tuple[int, int] | None:
    
    board_size = user_input.split()
    # s1 check the lenth of input
    if len(board_size) != 2:
        print('Error: <width> <height>')
        return
    # s2 check the type of the width and height
    else:
        try:
            num1=int(board_size[0])
        except ValueError:
            print('Error: width is not an integer')
            return
        try:
            num2=int(board_size[1])
        except ValueError:
            print('Error: height is not an integer')
            return
        # s3 check if the number is greater than zero
        if num1 <= 0:
            print('Error: width must be greater than zero')
            return
        if num2 <= 0:
            print('Error: height must be greater than zero')
            return
    
    return num1,num2


def parse_emitter(user_input: str) -> Emitter | None:

    emi = user_input.split()
    # s1 check the length
    if len(emi) != 3:
        print('Error: <symbol> <x> <y>, type \'END EMITTERS\' to quit')
        return
    # s2 check if the symbol is in A-J
    else:
        if not ('A'<=emi[0]<='J') or len(emi[0])!=1:
            print('Error: symbol is not between \'A\'-\'J\'')
            return
    # s3 if the croodinates is valid
        else:
            try:
                x=int(emi[1])
            except ValueError:
                print('Error: x is not an integer')
                return
            try:
                y=int(emi[2])
            except ValueError:
                print('Error: y is not an integer')
                return
            if x < 0:
                print('Error: x cannot be negative')
                return
            if y < 0:
                print('Error: y cannot be negative')
                return
    emitter = Emitter(emi[0],x,y)
    return emitter             


def parse_receiver(user_input: str) -> Receiver | None:
    rec = user_input.split()
    # s1 check the length of input
    if len(rec) != 3:
        print('Error: <symbol> <x> <y>, type \'END RECEIVERS\' to quit')
        return
    # s2 check if the symbol is valid
    else:
        if len(rec[0])!=2 or rec[0][0] != 'R'or not (0<=int(rec[0].strip('R'))<=9):
            print('Error: symbol is not between R0-R9')
            return
    # s3 check if the coordinates is valid
        else:
            try:
                x=int(rec[1])
            except ValueError:
                print('Error: x is not an integer')
                return
            try:
                y=int(rec[2])
            except ValueError:
                print('Error: y is not an integer')
                return
            if x < 0:
                print('Error: x cannot be negative')
                return
            if y < 0:
                print('Error: y cannot be negative')
                return
    receiver = Receiver(rec[0],x,y)
    return receiver


def parse_pulse_sequence(line: str) -> tuple[str, int, str] | None:

    ls = line.split()
    # s1 check the length of input
    if len(ls)!=3:
        print('Error: <symbol> <frequency> <direction>')
        return
    # s2 check if the symbol is valid
    else:
        symbol = ls[0]
        frequency = ls[1]
        direction = ls[2]
        if len(symbol)!=1 or symbol>'J':
            print('Error: symbol is not between A-J')
            return
    # s3 check if frequency is integer and is greater than zero
        try:
            int(frequency)
        except ValueError:
            print('Error: frequency is not an integer')
            return
        if int(frequency) < 0:
            print('Error: frequency must be greater than zero')
            return
    # s4 check if the direation is valid
        if direction != 'N' and direction != 'S' and direction != 'E' and direction != 'W':
            print('Error: direction must be \'N\', \'E\', \'S\' or \'W\'')
            return
        return symbol,int(frequency),direction
        


def parse_mirror(user_input: str) -> Mirror | None:

    ls = user_input.split()
    # s1 check the length of input
    if len(ls) != 3:
        print('Error: <symbol> <x> <y>, type \'END MIRRORS\' to quit')
        return
    # s2 check if symbol is valid
    else:
        symbol = ls[0]
        x = ls[1]
        y = ls[2]
        if symbol != '/' and symbol != '\\' and symbol != '>' and symbol != '<' and symbol != '^' and symbol != 'v':
            print('Error: symbol must be \'/\', \'\\\', \'>\', \'<\', \'^\' or \'v\'')
            return
    # s3 check if coordinates is valid
        else:
            try:
                int(x)
            except ValueError:
                print('Error: x is not an integer')
                return
            try:
                int(y)
            except ValueError:
                print('Error: y is not an integer')
                return
            if int(x)< 0:
                print('Error: x cannot be negative')
                return
            else:
                if int(y)< 0:
                    print('Error: y cannot be negative')
                    return
    mirror = Mirror(symbol,int(x),int(y))
    return mirror








