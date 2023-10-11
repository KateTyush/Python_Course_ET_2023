import json
import csv


with open('../users.json', "r") as users_file:
    users = json.load(users_file)

result = []
for user in users:
    result.append(
        {
            'name': user['name'],
            'gender': user['gender'],
            'address': user['address'],
            'age': user['age'],
            'books': []
        }
    )

with open('../books.csv', "r") as books_file:
    books = csv.DictReader(books_file)
    i = 0
    for book in books:
        result[i % len(result)]['books'].append(
            {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            }
        )
        i += 1

with open('result.json', 'w') as result_file:
    json.dump(result, result_file, indent=4)
