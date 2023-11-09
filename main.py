import csv
import random
def count():
    with open('books-en.csv', 'r') as f:
        file_reader = csv.reader(f, delimiter = ';')
        k30 = 0
        for row in file_reader:
            if int(len(row[1])>30):
                k30+=1
        print(k30)

def author_search():
    with open('books-en.csv', 'r') as f:
        title = f.readline()
        file_reader = csv.reader(f, delimiter = ';')
        book_author = input()
        for row in file_reader:
            if int(row[3]) > 1918:
                a = row[2]
                if book_author == a[:int(len(book_author))]:
                    print(row)

def to_the_file():
    with open('books-en.csv', 'r') as f:
        title = f.readline()
        file_reader = csv.reader(f, delimiter = ';')
        file = open('result.txt', 'w')
        k = 0
        count = 1
        arr = []
        for i in range(20):
            rand = int(random.random() * 9410)
            arr.append(rand)
        for row in file_reader:
            k+=1
            a = str(count) + '.' + row[2] + '.' + row[1] + '-' + row[3] + '\n'
            a = str(a)
            if k in arr:
                file.write(a)
                count+=1
        file.close()  
print('press 1 to see amount of books with title longer than 30 symbols')
print('press 2 to search by author name')
print('press 3 to write 20 random titles and authors into the text file')
a = int(input())
if a == 1:
    count()
if a == 2:
    author_search()
if a == 3:
    to_the_file()

