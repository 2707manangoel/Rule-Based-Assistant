def personal_assistant():
    print("=====================================================")
    print("           Welcome to My AI Assistant")
    print("=====================================================")
    print("Hello! I am your personal assistant.")

    while True:
        print("\n What would you like me tto do?")
        print("1. Say hello")
        print("2. Tell a joke")
        print("3. Give motivation")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print("Hello! Nice to meet you.")

        elif choice =="2":
            print("Why do programmers prefer dark mode?")
            print("Because light attracts bugs!")

        elif choice =="3":
            print("Keep learning,keep building, and never give up!")

        elif choice =="4":
            print("Goodbye! Have a great day.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


personal_assistant()
