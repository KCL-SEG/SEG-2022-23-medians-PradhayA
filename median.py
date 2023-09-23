"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

solution = 0
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        if len(numbers) % 2 == 1:
            solution = numbers[len(numbers)//2]
        else:
            solution = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1])/2
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(solution)