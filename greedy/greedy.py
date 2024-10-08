# Function to implement greedy algorithm for coin change problem
def greedy_coin_change(coins, amount):
    coins_used = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)
    return coins_used

# Test cases based on the image
test_cases = [
    ([25, 10, 5, 1], 177),  # Case (1)
    ([20, 15, 10, 5, 1], 103),  # Case (2)
    ([25, 20, 10, 5, 2, 1], 178),  # Case (3)
    ([9000, 3000, 1000, 500, 200, 100], 8900),  # Case (4)
]

# Running the greedy algorithm for each test case
results = {f"Case {i+1}": greedy_coin_change(coins, amount) for i, (coins, amount) in enumerate(test_cases)}

# Print the results
for case, result in results.items():
    print(f"{case}: {result}")

