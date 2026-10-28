from datetime import datetime

def show_data_time():
    now = datetime.now()
    print("Current date and time:" , now.strftime("%d-%m-%Y %I:%M %p"))

def personal_assistant():
    print("=" * 45)
    print("         MY PERSONAL ASSIISTANT  ")
    print("=" * 45)

    name = input("What is your name? ")
    print(f"\n Hello,{name}! Welcome to your assistant. ")

    while True:
        print("\n What would you like me to do?")
        print("1. Say hello")
        print("2. Tell a joke")
        print("3. Give motivation")
        print("4. Show date and time")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print(f"Hello, {name}! Nice to meet you.")
        elif choice =="2":
            print("Why do programmers prefer dark mode?")
            print("Because light attracts bugs!")

        elif choice =="3":
            print("Keep learning, keep building, and never give up!")

        elif choice =="4":
            show_data_time()
        elif choice =="5":
            print(f"Goodbye, {name}! Have a great day.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    personal_assistant()

