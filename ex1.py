import random

"""
Ex 1.
Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.
Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    -1000 ≤ inputArray[i] ≤ 1000.

"""
def largest_product(list_nums):
    try:
        if len(list_nums) < 2 or len(list_nums) > 10:
            raise ValueError("You just can enter a list larger than lenght 2 or smaller than lenght 10")
        return max(a*b for a, b in zip(list_nums, list_nums[1:]))
    except ValueError as ve:
        return print(ve)


def run():
    lenght_list = int(input("What's the list's lenght you want to generate?: "))
    given = [random.randint(-1000, 1000) for i in range(lenght_list)]
    # this is another way to handle the lenght constraint
    # assert lenght_list >= 2 and lenght_list <= 10, "You just can enter a list larger than lenght 2 or smaller than lenght 10"
    print(f"Random array: {given}")
    prod = largest_product(given)
    print(f'The largest product in the array is: {prod}')

if __name__ == '__main__':
    run()