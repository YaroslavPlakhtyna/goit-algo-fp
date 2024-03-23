import random

import matplotlib.pyplot as plt


PROBABILITIES = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def monte_carlo(tries):
    all_sums = [sum([random.randint(1, 6), random.randint(1, 6)])
                for _ in range(tries)]
    result = {v: 0 for v in PROBABILITIES}
    for v in all_sums:
        result[v] += 1
    for v in PROBABILITIES:
        result[v] = result[v] / tries * 100
    return result


if __name__ == "__main__":
    results = {}
    for i in (100, 1000, 10000):
        results[i] = monte_carlo(i)

    plt.figure(figsize=(6, 6))

    plt.plot(PROBABILITIES.keys(), PROBABILITIES.values(),
             label="Calculated", color="red")
    colors = ("green", "blue", "orange")
    for value, c in zip(results, colors):
        plt.plot(PROBABILITIES.keys(), results[value].values(), label=f"{value} rolls", color=c)

    plt.xticks(list(PROBABILITIES.keys()))
    plt.xlabel("Sum of the roll")
    plt.ylabel("Probability (%)")
    plt.title("'Monte-Carlo' 2 dices roll probabilities")

    plt.legend()
    plt.grid()
    plt.show()
