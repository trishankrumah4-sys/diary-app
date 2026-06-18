import datetime

def write_entry():
    date = datetime.date.today()
    print(f"\n📖 Diary Entry - {date}")
    entry = input("What's on your mind today? \n> ")
    
    with open("diary.txt", "a") as f:
        f.write(f"\n--- {date} ---\n")
        f.write(entry + "\n")
    
    print("✅ Entry saved!")

def read_entries():
    try:
        with open("diary.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No entries yet!")

while True:
    print("\n1. Write entry\n2. Read entries\n3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        break