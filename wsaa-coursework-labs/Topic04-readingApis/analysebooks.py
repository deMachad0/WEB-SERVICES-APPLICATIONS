from bookapidao import getAllBooks

books = getAllBooks()
total = 0
count = 0
for book in books:
    total += book["price"]
    count += 1

print("average of ", count, " book is ", total/count)