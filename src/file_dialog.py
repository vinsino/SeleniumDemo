import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()


    file_path = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=[("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")]
    )

    if file_path:
        print(f"Selected file: {file_path}")
        return file_path

# Call the function to open the file dialog
# open_file_dialog()
