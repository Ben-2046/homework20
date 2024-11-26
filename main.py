# Initial Values
total = 0
n = 1

# The while loop
while True:
    term = 1 / n**2  # Calculate the current term
    if term < 0.0000000000001:  # Check the threshold
        break
    total += term  # Add the current term to the total
    n += 1  # Increment n for the next term

# The answer
print("Total:", total)