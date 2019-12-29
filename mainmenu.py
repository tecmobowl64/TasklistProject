import sys
import tasklist
def main():
    def menu():
        print("********************")
        print("DoIt! Main Menu")
        #time.sleep(1)
        print("********************")
        msg = "A: View All Incomplete Tasks\n"
        msg += "B: Add a New Task\n"
        msg += "C: Complete a Task\n"
        msg += "D: View all Completed Tasks\n"
        msg += "Q: Quit/Log Out\n"
        print(msg)
        print("********************")
        choice = input("Please enter your choice: ")

        if choice == "A" or choice =="a":
            tasklist.get_incomplete_tasks()
            menu()
        elif choice == "B" or choice =="b":
            tasklist.addTask()
            menu()
        elif choice == "C" or choice =="c":
            tasklist.markComplete()
            menu()
        elif choice == "D" or choice =="d":
            tasklist.get_completed_tasks()
            menu()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("Pick an option, dude!")
            print("Please try again")
            menu()
    menu()
main()
