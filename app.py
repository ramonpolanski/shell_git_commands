import random

def generate_random_numbers(n):
    numbers = sorted(random.sample(range(1, 11), n))
    median_number = numbers[n // 2]
    disregarded_numbers = numbers[1:-1]
    return numbers, disregarded_numbers, median_number

# Example usage
sorted_numbers, disregarded_numbers, median_number = generate_random_numbers(5)
print("Sorted Numbers:", sorted_numbers)
print("Random Numbers:", disregarded_numbers)
print("Median Number:", median_number)
