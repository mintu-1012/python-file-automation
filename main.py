import os
from file_operations import organize_files, rename_files, delete_empty_files
from logger_setup import setup_logger

def main():

    setup_logger()

    print("\n====== PYTHON FILE AUTOMATION ======")

    directory = input("Enter folder path: ")

    if not os.path.exists(directory):
        print("❌ Invalid folder path")
        return

    print("\nChoose Operation")
    print("1. Organize Files")
    print("2. Rename Files")
    print("3. Delete Empty Files")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        organize_files(directory)

    elif choice == "2":

        prefix = input("Enter filename prefix: ")

        rename_files(directory, prefix)

    elif choice == "3":
        delete_empty_files(directory)

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()