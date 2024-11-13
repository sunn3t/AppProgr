import numpy as np


def simulate_games(n, a, b, N):
    r_a = n - a
    r_b = n - b
    max_rounds = 2 * max(r_a, r_b)

    wins = np.random.randint(0, 2, size=(N, max_rounds))
    c_a = np.cumsum(wins, axis=1) + a
    c_b = np.cumsum(1 - wins, axis=1) + b

    game_ended = np.logical_or(c_a >= n, c_b >= n)
    ending_rounds = game_ended.argmax(axis=1)
    A_won = c_a[np.arange(N), ending_rounds] >= n
    B_won = c_b[np.arange(N), ending_rounds] >= n

    A_wins = np.sum(A_won)
    B_wins = np.sum(B_won)

    prob_A_wins = A_wins / N
    prob_B_wins = B_wins / N

    return prob_A_wins, prob_B_wins


n = 10  # Кількість балів для перемоги
a = 5   # бали гравця A
b = 3   # бали гравця B
N_simulations = 10000  # Кількість симуляцій

prob_A_wins, prob_B_wins = simulate_games(n, a, b, N_simulations)

print(f"Ймовірність перемоги гравця A: {prob_A_wins:.4f}")
print(f"Ймовірність перемоги гравця B: {prob_B_wins:.4f}")


total_pot = 100000  # Загальний банк
A_share = total_pot * prob_A_wins
B_share = total_pot * prob_B_wins

print(f"Гравець A повинен отримати: {A_share:.2f} одиниць")
print(f"Гравець B повинен отримати: {B_share:.2f} одиниць")
