import os
import shutil

folder = input("Enter the folder path to organize: ").strip().strip('"')

if not os.path.isdir(folder):
    print("Error: Folder not found!")
else:
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".doc"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv"],
    }

    for category in categories:
        os.makedirs(os.path.join(folder, category), exist_ok=True)

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if not os.path.isfile(path) or filename == os.path.basename(__file__):
            continue

        extension = os.path.splitext(filename)[1].lower()

        for category, extensions in categories.items():
            if extension in extensions:
                destination = os.path.join(folder, category, filename)

                if not os.path.exists(destination):
                    shutil.move(path, destination)
                    print(f"Moved {filename} to {category}")
                break

    print("File organization complete!")
