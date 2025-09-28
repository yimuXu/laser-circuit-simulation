from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    '''
    Positive test case to verify the set_pulse_sequence function.

    Paramaters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    '''
    
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'A'
    expected1_direction = 'S'
    expected1_frequency = 100
    expected2_symbol = 'B'
    expected2_direction = 'E'
    expected2_frequency = 256
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    observed2_symbol = my_circuit.emitters[1].get_symbol()
    observed2_direction = my_circuit.emitters[1].get_direction()
    observed2_frequency = my_circuit.emitters[1].get_frequency()
    assert expected1_symbol == observed1_symbol, 'something went wrong!'
    assert expected1_direction == observed1_direction,'something went wrong!'
    assert expected1_frequency == observed1_frequency, 'something went wrong!'
    assert expected2_symbol == observed2_symbol, 'something went wrong!'
    assert expected2_direction == observed2_direction, 'something went wrong!'
    assert expected2_frequency == observed2_frequency, 'something went wrong!'


    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    # file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'A'
    expected1_direction = 'N'
    expected1_frequency = 255
    expected2_symbol = 'B'
    expected2_direction = 'S'
    expected2_frequency = 33
    expected3_symbol = 'C'
    expected3_direction = 'W'
    expected3_frequency = 12
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    observed2_symbol = my_circuit.emitters[1].get_symbol()
    observed2_direction = my_circuit.emitters[1].get_direction()
    observed2_frequency = my_circuit.emitters[1].get_frequency()
    observed3_symbol = my_circuit.emitters[2].get_symbol()
    observed3_direction = my_circuit.emitters[2].get_direction()
    observed3_frequency = my_circuit.emitters[2].get_frequency()
    assert expected1_symbol == observed1_symbol, 'something went wrong!'
    assert expected1_direction == observed1_direction, 'something went wrong!'
    assert expected1_frequency == observed1_frequency, 'something went wrong!'
    assert expected2_symbol == observed2_symbol, 'something went wrong!'
    assert expected2_direction == observed2_direction, 'something went wrong!'
    assert expected2_frequency == observed2_frequency, 'something went wrong!'
    assert expected3_symbol == observed3_symbol, 'something went wrong!'
    assert expected3_direction == observed3_direction, 'something went wrong!'
    assert expected3_frequency == observed3_frequency, 'something went wrong!'
    # file_obj.close()
def negaitive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    # file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'Z'
    expected1_direction = 'S'
    expected1_frequency = 255
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    
    assert expected1_symbol != observed1_symbol, 'something went wrong!'

def negaitive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    # file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'A'
    expected1_direction = 'S'
    expected1_frequency = -5
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    # file_obj.close()
    assert expected1_frequency != observed1_frequency, 'something went wrong!'

def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'A'
    expected1_direction = 'W'
    expected1_frequency = 1
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    file_obj.close()
    assert expected1_direction != observed1_direction, 'something went wrong!'
    assert  expected1_frequency != observed1_frequency, 'something went wrong!'

def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, pulse_file_path)
    expected1_symbol = 'a'
    expected1_direction = 'S'
    expected1_frequency = 100
    observed1_symbol = my_circuit.emitters[0].get_symbol()
    observed1_direction = my_circuit.emitters[0].get_direction()
    observed1_frequency = my_circuit.emitters[0].get_frequency()
    file_obj.close()
    assert expected1_symbol != observed1_symbol, 'something went wrong!'

if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), 'input/pulse_sequence.in')
    positive_test_2(get_my_lasercircuit(), 'input/pulse_sequence1.in')
    negaitive_test_1(get_my_lasercircuit(), 'input/pulse_sequence2.in')
    negaitive_test_2(get_my_lasercircuit(), 'input/pulse_sequence3.in')
    edge_test_1(get_my_lasercircuit(), 'input/pulse_sequence4.in')
    edge_test_2(get_my_lasercircuit(), 'input/pulse_sequence5.in')
    # You should have more below...


