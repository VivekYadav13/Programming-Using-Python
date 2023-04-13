'''
A DNA sequence is made by a combination of ATCG block combinations. Generate 20 random DNA sequences containing 8 blocks each. Write a code to match DNA sequence. User enters a set of blocks of a sequence and tries to find the possible match. An example is A**A****. The user would like to know which of the DNA in the list fit with their pattern. In the example just given, the matching strings are the first and fourth. One way to solve this problem is to create a dictionary whose keys are the indices in the user’s string of the non-asterisk characters and whose values are those characters. Write a program implementing this approach (or some other approach) to find the strings that match a user-entered string.
'''

from random import choice
sequences = []
final_sequences = []
for i in range(20):
    sequence = ''
    for j in range(8):
        sequence += choice(['A', 'T', 'C', 'G'])
    sequences += [sequence]
given_sequence = input(
    "Enter a 8 blocks long DNA sequence (Enter (*) for random): ")
for j in range(len(sequences)):
    for i in range(8):
        if given_sequence[i] != sequences[j][i] and given_sequence[i] != '*':
            break
    else:
        final_sequences += [sequences[j]]
print("Sequences generated were:", sequences)
print("Sequences matching your pattern were:", final_sequences)
