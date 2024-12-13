#!/usr/bin/python3

def determine_prime_game_winner(x, nums):
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

    maria_wins = 0
    ben_wins = 0

    # Generate a list of prime numbers up to the maximum number in the input list
    max_number = max(nums)
    prime_numbers = [True] * (max_number + 1)
    prime_numbers[0] = prime_numbers[1] = False

    for potential_prime in range(2, int(max_number ** 0.5) + 1):
        if prime_numbers[potential_prime]:
            for multiple in range(potential_prime ** 2, max_number + 1, potential_prime):
                prime_numbers[multiple] = False

    # Count the number of prime numbers less than each input number
    for num in nums:
        prime_count = sum(prime_numbers[2:num + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'