# LAB 3 Calvert Duong

# Task 1: Strings
food = "cheese cake"

print("The first 3 characters of my food variable string are:", food[0:3])
print("The last 3 characters of my food variable string are:", food[-3:])

first_last = food[0] + food[-1]
print(first_last)

split_string = food.split()
print("The split method:", split_string)

join_string = " ".join(split_string)
print("The join method:", join_string)

# Task 2: List
number_list = [1, 2, 3, 4, 5]
number_list.append(6)
number_list(3, 4)

print("The first 3 characters of my number_list variable string are:", number_list[0:3])
print("The last 3 characters of my number_list variable string are:", number_list[-3:])

number_list.remove(2)
print(number_list)


# Task 3: Working with Dictionaries
books =  {'Dr. Seuss': 'Cat in the Hat',
    'J.K. Rowling': 'Harry Potter',
    'George Orwell': '1984',
    'Harper Lee': 'To Kill a Mockingbird'}
print(books.keys())
print(books.values())
print(books.get("Harper Lee"))

third_key = list(books.keys())[2]
books.pop(third_key)
print(books)

first_key = list(books.keys())[0]
del books[first_key]
print(books)

