#!/usr/bin/python3

""" Module for solving the Prime Game question """


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x (int): Number of turns
        nums (list): List of numbers for each turn

    Returns:
        str: Winner of the game ('Maria' or 'Ben') or None if it's a tie
    """

    # Handle invalid input
    if not nums or x < 1:
        return None

    # Find the maximum number in the input list
    max_num = max(nums)

    # Initialize a boolean array to track prime numbers
    my_filter = [True for _ in range(max(max_num + 1, 2))]

    # Apply the Sieve of Eratosthenes algorithm to find prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False

    # Exclude 0 and 1 from prime numbers
    my_filter[0] = my_filter[1] = False

    # Count prime numbers less than each input number
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y

    # Determine the winner based on the count of prime numbers
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1

    # Check for a tie
    if player1 * 2 == len(nums):
        return None

    # Return the winner
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
