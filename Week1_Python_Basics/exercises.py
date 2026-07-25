"""
Week 1 - Beginner Python Exercises
Covers: lists, dicts, loops, functions, file I/O
"""

# 1. Sum of a list
def sum_list(numbers):
    return sum(numbers)


# 2. Find the maximum number in a list
def find_max(numbers):
    return max(numbers)


# 3. Reverse a string
def reverse_string(text):
    return text[::-1]


# 4. Check if a string is a palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


# 5. Count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)


# 6. Factorial of a number (using loop)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 7. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 8. Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


# 9. Remove duplicates from a list
def remove_duplicates(items):
    return list(set(items))


# 10. Count occurrences of each word in a sentence (using dict)
def word_count(sentence):
    words = sentence.lower().split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


# 11. Merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# 12. Find common elements between two lists
def common_elements(list1, list2):
    return list(set(list1) & set(list2))


# 13. Sort a list of dictionaries by a key
def sort_by_key(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])


# 14. Flatten a nested list
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# 15. Simple class using OOP basics
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return f"{self.name}: avg = {self.average():.2f}"


# 16. Write a list of numbers to a file
def write_numbers_to_file(numbers, filename="numbers.txt"):
    with open(filename, "w") as f:
        for num in numbers:
            f.write(f"{num}\n")


# 17. Read numbers from a file and return their sum
def read_and_sum_file(filename="numbers.txt"):
    with open(filename, "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip()]
    return sum(numbers)


# 18. Count total lines and words in a text file
def file_stats(filename="numbers.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    return total_lines, total_words


# 19. Check if a list is sorted
def is_sorted(numbers):
    return numbers == sorted(numbers)


# 20. Simple grade calculator using loops/conditionals
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"


if __name__ == "__main__":
    print("Exercise 1 - Sum:", sum_list([1, 2, 3, 4, 5]))
    print("Exercise 2 - Max:", find_max([4, 9, 2, 7]))
    print("Exercise 3 - Reverse:", reverse_string("hello"))
    print("Exercise 4 - Palindrome:", is_palindrome("Was it a car or a cat I saw"))
    print("Exercise 5 - Vowels:", count_vowels("Beautiful Day"))
    print("Exercise 6 - Factorial(5):", factorial(5))
    print("Exercise 7 - Is 17 prime:", is_prime(17))
    print("Exercise 8 - Fibonacci(7):", fibonacci(7))
    print("Exercise 9 - Remove duplicates:", remove_duplicates([1, 2, 2, 3, 3, 3]))
    print("Exercise 10 - Word count:", word_count("this is a test this is fun"))
    print("Exercise 11 - Merge dicts:", merge_dicts({"a": 1}, {"b": 2}))
    print("Exercise 12 - Common elements:", common_elements([1, 2, 3], [2, 3, 4]))

    students = [{"name": "Amit", "score": 88}, {"name": "Sita", "score": 75}]
    print("Exercise 13 - Sorted by score:", sort_by_key(students, "score"))

    print("Exercise 14 - Flatten:", flatten_list([1, [2, 3, [4, 5]], 6]))

    s = Student("Bhaskar", [80, 90, 85])
    print("Exercise 15 - Student class:", s)

    write_numbers_to_file([10, 20, 30, 40])
    print("Exercise 16 - Wrote numbers to file")
    print("Exercise 17 - Sum from file:", read_and_sum_file())
    print("Exercise 18 - File stats (lines, words):", file_stats())
    print("Exercise 19 - Is sorted [1,2,3]:", is_sorted([1, 2, 3]))
    print("Exercise 20 - Grade for 82:", get_grade(82))