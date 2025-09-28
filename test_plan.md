
**Test Cases**
Table 1. Summary of test cases for parse_pulse_sequence
| File Name             | Function Name   | Description                                            | Expected Error Message(s) (if any) | Pass/Fail |
| --------------------- | ----------------| ------------------------------------------------------ | ---------------------------------- | --------- |
| pulse_sequence.in     | positive_test_1 | Positive Case - Configure the frequency for 2 emitters | None                               | pass      |
| pulse_sequence1.in    | positive_test_2 | Positive Case - Configure the frequency and direction  | None                               | pass      |
| pulse_sequence2.in    | nagetive_test_1 | negaitive Case - Configure the symbol of emitter       | symbol is not between A-J          | pass      |
| pulse_sequence3.in    | nagetive_test_2 | negaitive Case - Configure the frequency of emitter    | frequency must be greater than zero| pass      |
| pulse_sequence4.in    | edge_test_1     | Edge Case Configure the line in file without whitespace| None                               | fail      |
| pulse_sequence5.in    | edge_test_2     | Edge Case Configure - lowercase symbol of emitter      | symbol is not between A-J          | pass      |

