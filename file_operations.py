import os
from logger_setup import log_info, log_error

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"]
}

# Organize files
def organize_files(directory):

    try:

        for file in os.listdir(directory):

            file_path = os.path.join(directory, file)

            if os.path.isfile(file_path):

                extension = os.path.splitext(file)[1].lower()

                folder_name = "Others"

                for category, extensions in FILE_TYPES.items():

                    if extension in extensions:
                        folder_name = category
                        break

                target_folder = os.path.join(directory, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                new_path = os.path.join(target_folder, file)

                os.rename(file_path, new_path)

                log_info(f"Moved {file} to {folder_name}")

        print("✅ Files organized successfully!")

    except Exception as e:
        log_error(f"Error organizing files: {e}")
        print("❌ Error occurred while organizing files")


# Rename files
def rename_files(directory, prefix):

    try:

        count = 1

        for file in os.listdir(directory):

            file_path = os.path.join(directory, file)

            if os.path.isfile(file_path):

                extension = os.path.splitext(file)[1]

                new_name = f"{prefix}_{count}{extension}"

                new_path = os.path.join(directory, new_name)

                os.rename(file_path, new_path)

                log_info(f"Renamed {file} to {new_name}")

                count += 1

        print("✅ Files renamed successfully!")

    except Exception as e:
        log_error(f"Error renaming files: {e}")
        print("❌ Error occurred while renaming files")


# Delete empty files
def delete_empty_files(directory):

    try:

        for file in os.listdir(directory):

            file_path = os.path.join(directory, file)

            if os.path.isfile(file_path):

                if os.path.getsize(file_path) == 0:

                    os.remove(file_path)

                    log_info(f"Deleted empty file: {file}")

        print("✅ Empty files deleted!")

    except Exception as e:
        log_error(f"Error deleting empty files: {e}")
        print("❌ Error occurred while deleting empty files")