import sys
import tasklist
def main():
    def menu():
        print("********************")
        print("DoIt! Main Menu")
        #time.sleep(1)
        print("********************")

        print("A: View All Incomplete Tasks")
        print("B: Add a New Task")
        print("C: Complete a Task")
        print("D: View All Completed Tasks")
        print("Q: Quit/Log Out")
        print("********************")
        choice = input("Please enter your choice: ")

        if choice == "A" or choice =="a":
            print(tasklist.get_incomplete_tasks())
            menu()
        elif choice == "B" or choice =="b":
            tasklist.addTask()
            menu()
        elif choice == "C" or choice =="c":
            tasklist.markComplete()
            menu()
        elif choice == "D" or choice =="d":
            print(tasklist.get_completed_tasks())
            menu()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("Pick an option, dude!")
            print("Please try again")
            menu()
    menu()
main()
