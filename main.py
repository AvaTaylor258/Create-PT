import csv
import os

def add_menu():
	print("ADDING MENU\n")
	task_name = input("Task Name: ")
	due_date = input("Due Date: ")
	priority = int(input("Priority: "))

	task = [task_name, due_date, priority]

	if not os.path.isfile("tasks.csv"):
		with open("tasks.csv", "a") as f:
			c = csv.writer(f)
			c.writerow(["Task Name", "Due Date", "Priority"])
			c.writerow(task)
	else:
		with open("tasks.csv", "a") as f:
			c = csv.writer(f)
			c.writerow(task)
	f.close()

def display():
	f = open("tasks.csv", "r")
	c = csv.reader(f)

	counter = 0

	for r in c:
		if r[0] == "Task Name":
			pass
		else:
			print(f"[{counter}] {r[0]}")
		counter += 1
	
	f.close()

while True:
	os.system("clear")
	opt = int(input("TO-ULTIMATE-DO\n\n[0] Quit\n[1] Add\n[2] View\n\n> "))
	os.system("clear")
	if opt == 0:
		break
	elif opt == 1:
		add_menu()
	elif opt == 2:
		print("VIEWING MENU\n")
		display()
		input("\nPress enter to continue ")