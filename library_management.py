books = []

while True:
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Book name: ")
        books.append(book)
        print("Book added!")

    elif choice == "2":
        print("\nBooks:")
        for book in books:
            print(book)

    elif choice == "3":
        search = input("Enter book name: ")
        if search in books:
            print("Book found!")
        else:
            print("Book not found!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")