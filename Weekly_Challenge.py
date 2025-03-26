#1. Write a program that accepts user input to create a list of integers. 
#    Then, compute the sum of all the integers in the list


#step 1: Initialize an empty list where to store the integers entered by the user
numbers = []

#Asks user to enter the number of integers
n = int(input("Enter the number of Integers: "))

for i in range(n):
    num = int(input(f"Enter the integer {i+1}: "))
    numbers.append(num)
    
#Compute the total number of integers in the list
total_sum = sum(numbers)
print(f"The sum of the Entered Integers: {total_sum}")



# 2. Create a tuple containing the names of five of your favorite books. 
#Then, use a for loop to print each book name on a separate line.

# tuples are represented using parenthesis, and are immutable

favourite_books = (
    
    "Kidagaa Kimemwozea",
    "Siku Njema",
    "Things Fall Apart",
    "Pride and Prejudice",
    "Chozi la Heri",
    "The River and The Source"
    
)
#Use for loop to print each favourite book line by line
for book in favourite_books:
    print(book)
    
# 3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color.
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

Person = {}

Person["name"] = input("Enter your name: ")
Person["age"]  = input("Enter your age: ")
Person["favourite_color"] = input("Enter your favourite color: ")

print("\nPersonal Information: ")
print(Person)
 

# 4. Write a program that accepts user input to create two sets of integers. 
#Then, create a new set that contains only the elements that are common to both sets.
    
def get_user_input(prompt):
    return set(map(int, input(prompt).split()))

set1 = get_user_input("Enter the first set of integers (separated by spaces): ")
set2 = get_user_input("Enter the second set of integers: ")

common_values = set1.intersection(set2)
print(f"New set with common elements in both sets: {common_values}")
    

# 5. Create a program that stores a list of words. 
#Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print(f"New list with words having odd number of characters: {odd_length_words} ")
