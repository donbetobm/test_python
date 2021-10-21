import random

"""
Given a sequence of integers as an array, determine whether it is possible to obtain
 a strictly increasing sequence by removing no more than one element from the array.
 2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.
	- [output] boolean
	- Return true if it is possible to remove one element from the array in order to get 
        a strictly increasing sequence, otherwise return false.

"""

def first_searching_round(sequence):
    """Return the first index of a pair of elements where the earlier
    element is not less than the later elements. If no such pair
    exists, return -1"""
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1


def second_searching_round(sequence, j):
    """Return whether it is possible to obtain a strictly increasing
    sequence by removing no more than one element from the array"""
    if j == -1:
        return True  # List is increasing
    if first_searching_round(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True  # Deleting earlier element makes increasing
    if first_searching_round(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True  # Deleting later element makes increasing
    return False  # Deleting either does not make increasing



def run():
    lenght_list = int(input("What's the list's lenght you want to generate?: "))
    assert lenght_list >= 2 and lenght_list <= 105, "You should use an array larger than 2 and shorter than 105 elements"
    given = [random.randint(-105, 105) for i in range(lenght_list)]
    print(f'Array given: {given}')

    test = first_searching_round(given)
    round_2 = second_searching_round(given, test)
    print(round_2)

if __name__ == '__main__':
    run()