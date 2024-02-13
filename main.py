import csv
import os

def add_menu():
	print("ADDING MENU")
	task_name = input("Task Name: ")
	due_date = input("Due Date: ")
	priority = int(input("Priority: "))

	task = [task_name, due_date, priority]

	if not os.path.isfile("tasks.csv"):
		with open("tasks.csv", "a") as f:
			write = csv.writer(f)
			write.writerow(["Task Name", "Due Date", "Priority"])
			write.writerow(task)
	else:
		with open("tasks.csv", "a") as f:
			write = csv.writer(f)
			write.writerow(task)
	f.close()

def view_menu():
	print("VIEWING MENU")
	f = open("tasks.csv", "r")
	c = csv.reader(f)

	print()
	for r in c:
		if r[0] == "Task Name":
			pass
		else:
			print(f"\t{r[0]}")
	print()
	input("Press enter to continue ")
	
	f.close()

while True:
	os.system("clear")
	opt = int(input("Welcome to To-Ultimate-Do\nWhat would you like to do?\n[0] Quit\n[1] Add\n[2] View\n> "))
	os.system("clear")
	if opt == 0:
		break
	elif opt == 1:
		add_menu()
	elif opt == 2:
		view_menu()