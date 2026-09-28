import os
from tkinter import Tk, filedialog, messagebox


def select_file_from_explorer():
    """Opens file explorer and forces it to the front of the screen."""
    root = Tk()
    root.withdraw()

    # Force the file dialog to open on top of other windows
    root.attributes("-topmost", True)

    file_path = filedialog.askopenfilename(
        title="Select any file",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("Python Files", "*.py"),
        ],
    )

    root.destroy()  # Clean up the tkinter instance
    return file_path


def handle_file(file_path):
    if not file_path:
        print("❌ No file was selected or the window was closed.")
        return

    print(f"\n📂 Selected File: {file_path}")
    print("-" * 40)
    print("1. Read File")
    print("2. Write File (Overwrite)")
    print("3. Append File (Add to end)")
    print("4. Delete File")
    print("-" * 40)

    choice = input("Choose an action (1-4): ").strip()

    try:
        if choice == "1":
            # Try UTF-8 first, fallback to 'latin-1' if it has weird symbols
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, "r", encoding="latin-1") as f:
                    content = f.read()

            print("\n--- File Content ---")
            print(content)
            print("--------------------")

        elif choice == "2":
            content = input("Enter the text to write: ")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content + "\n")
            print("📝 File overwritten successfully!")

        elif choice == "3":
            content = input("Enter the text to append: ")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(content + "\n")
            print("➕ Content added successfully!")

        elif choice == "4":
            confirm = (
                input("Are you sure you want to delete this? (y/n): ")
                .strip()
                .lower()
            )
            if confirm == "y":
                os.remove(file_path)
                print("🗑️ File deleted!")

    except PermissionError:
        messagebox.showerror(
            "Permission Error",
            "Python doesn't have permission to open this file.\nTry a file in your Documents or Desktop folder.",
        )
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file:\n{str(e)}")


if __name__ == "__main__":
    print("🔄 Opening File Explorer window...")
    selected_path = select_file_from_explorer()
    handle_file(selected_path)