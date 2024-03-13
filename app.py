import random

def generate_random_numbers(n):
    numbers = [random.randint(1, 10) for _ in range(n)]
    sorted_numbers = sorted(numbers)
    median_number = sorted_numbers[len(sorted_numbers) // 2]
    disregarded_numbers = sorted_numbers[1:-1]
    return sorted_numbers, disregarded_numbers, median_number

# Example usage
sorted_numbers, disregarded_numbers, median_number = generate_random_numbers(5)
print("Sorted Numbers:", sorted_numbers)
print("Random Numbers:", disregarded_numbers)
print("Median Number:", median_number)
