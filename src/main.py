# main.py

# Import functions from another Python file
import file_dialog
import excel_handler
from selenium_nlsc_script import SeleniumNLSC
import nlsc_regex_processing

# Call a function from the imported module
# file_path = "./input/123.xlsx"

file_path = file_dialog.open_file_dialog()
column_data = excel_handler.read_excel(file_path)
print(column_data)
seleniumNlsc = SeleniumNLSC()
seleniumNlsc.close_notification()
# nlsc_collection = seleniumNlsc.get_nlsc_data_new(column_data)
nlsc_collection = seleniumNlsc.get_nlsc_data(column_data)
seleniumNlsc.close_browser()
processed_collection = nlsc_regex_processing.regex_process(nlsc_collection)
excel_handler.write_excel(file_path, processed_collection)
print(processed_collection)

# print(column_data)