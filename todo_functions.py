import csv

def add_todo(file_name):
    print("Add todo")
    # Ask title of todo
    todo_name = input("Enter title of todo: ")
    # open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # Insert Values - title = user entered
                # - completed = False
        writer.writerow([todo_name, "False"])
    

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            # ["todo1", "False"]
            if (row[1] == "True"):
                print(f"Todo {row[0]} is complete")
            else:
                print(f"Todo {row[0]} is not complete")
