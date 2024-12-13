#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of turns in the game.
        nums (list): A list of numbers for each turn.

    Returns:
        str: The winner of the game, either 'Maria' or 'Ben', or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_number = max(nums)
    prime_numbers = [True] * (max_number + 1)
    prime_numbers[0] = prime_numbers[1] = False

    # Filter out non-prime numbers
    for x in range(2, int(max_number ** 0.5) + 1):
        if prime_numbers[x]:
            for multiple in range(x ** 2, max_number + 1, x):
                prime_numbers[multiple] = False

    # Count prime numbers less than each input number
    maria_wins = sum(1 for num in nums if sum(prime_numbers[2:num + 1]) % 2 != 0)
    ben_wins = len(nums) - maria_wins

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
