def main():
    print("To_do list manager!")

    while True:
        print("\nOptions:")
        print("1 - Add a task")
        print("2 - View task")
        print("3 - Mark task as complete")
        print("4 - Delete a task")
        print("5 - Exit")

        choice = input("Choose option: ")

	if choice == '1':
		name = input("Please add a task: ")
		print("name")
            
	elif choice == '2':
		print(View task)
		if no task:
			print('No task')

	elif choice == '3':
		print("Mark task as complete: ")

	elif choice == '4':
		print("Delete a task: ")

	elif choice == '5':
		print("Goodbye!")
			break

	else:
		print("Please choose a valid option.")

if __name__ == "__main__":
    main()
