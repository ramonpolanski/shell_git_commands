import random

def generate_random_numbers(n):
    numbers = [random.randint(1, 10) for _ in range(n)]
    sorted_numbers = sorted(numbers)
    disregarded_numbers = sorted_numbers[1:-1]
    return sorted_numbers, disregarded_numbers

# Example usage
sorted_numbers, disregarded_numbers = generate_random_numbers(5)
print("Sorted Numbers:", sorted_numbers)
print("Random Numbers:", disregarded_numbers)
