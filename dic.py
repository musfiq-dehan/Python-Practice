student = {
    'name': 'John',
    'age': 20,
    'gpa': 4.00
}

# squares = {}
# for x in range(5):
#     squares[x] = x**2


del student['age']
squares = {x: x**2 for x in range(5)}
print(squares)
