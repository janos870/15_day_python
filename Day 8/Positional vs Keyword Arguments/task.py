# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in? {location}")
#
# greet_with(name="John", location="Budapest")

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    love_score = int(f"{true_count}{love_count}")
    print(f"Your love score is: {love_score}")

# Example usage
calculate_love_score("Janos", "Fruzsina")
