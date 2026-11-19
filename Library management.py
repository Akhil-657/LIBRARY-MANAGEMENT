books = []

while True:

    print("\n===== LIBRARY BOOK MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        # 1. Add Book
        case 1:
            bookId = int(input("Enter Book ID: "))

            exists = False
            for book in books:
                if book["bookId"] == bookId:
                    exists = True
                    break

            if exists:
                print("Book ID Already Exists!")
            else:
                bookTitle = input("Enter Book Title: ")
                bookAuthor = input("Enter Author Name: ")
                bookCategory = input("Enter Book Category: ")
                bookPrice = float(input("Enter Book Price: "))
                bookQty = int(input("Enter Quantity Available: "))

                book = {
                    "bookId": bookId,
                    "bookTitle": bookTitle,
                    "bookAuthor": bookAuthor,
                    "bookCategory": bookCategory,
                    "bookPrice": bookPrice,
                    "bookQty": bookQty
                }

                books.append(book)

                print("Book Added Successfully!")

        # 2. Display All Books
        case 2:
            if len(books) == 0:
                print("No Books Found!")
            else:
                for book in books:
                    print("\nBook ID:", book["bookId"])
                    print("Book Title:", book["bookTitle"])
                    print("Author:", book["bookAuthor"])
                    print("Category:", book["bookCategory"])
                    print("Price:", book["bookPrice"])
                    print("Quantity:", book["bookQty"])

        # 3. Search Book
        case 3:
            searchId = int(input("Enter Book ID to Search: "))

            found = False

            for book in books:
                if book["bookId"] == searchId:
                    print("\nBook Found!")
                    print(book)
                    found = True
                    break

            if found == False:
                print("Book Not Found!")

        # 4. Update Book
        case 4:
            updateId = int(input("Enter Book ID to Update: "))

            found = False

            for book in books:
                if book["bookId"] == updateId:

                    print("Enter New Book Details")

                    book["bookTitle"] = input("Enter New Title: ")
                    book["bookAuthor"] = input("Enter New Author: ")
                    book["bookCategory"] = input("Enter New Category: ")
                    book["bookPrice"] = float(input("Enter New Price: "))
                    book["bookQty"] = int(input("Enter New Quantity: "))

                    print("Book Updated Successfully!")
                    found = True
                    break

            if found == False:
                print("Book Not Found!")

        # 5. Delete Book
        case 5:
            deleteId = int(input("Enter Book ID to Delete: "))

            found = False

            for book in books:
                if book["bookId"] == deleteId:
                    books.remove(book)
                    print("Book Deleted Successfully!")
                    found = True
                    break

            if found == False:
                print("Book Not Found!")

        # 6. Exit
        case 6:
            print("Thank You! Application Closed.")
            break

        case _:
            print("Invalid Choice! Please Try Again.")