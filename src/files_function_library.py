# Import standard modules
import shutil
import filecmp

# Load libraries
from pathlib import Path
from datetime import datetime
from log_record_functions import write_log_file as write_log_file


def check_folder (user_dest_path):
    # user_dest_path is the destination path selected by the user
    folder_path = Path(user_dest_path)                     
    # Set returning control variables to default value
    exist = False
    # Check if the user selected folder path exists
    if folder_path.is_dir():
        exist = True
    # Return control variable
    return exist


def check_file (file_dest_path):
    #check if file exist to avoid overwrite and give the user the option to do it manualy
    file_path = Path(file_dest_path)
    exist = False
    if file_path.is_file():
        exist = True
    return exist


def check_create_folder (user_dest_path):
    # user_dest_path is the destination path selected by the user
    folder_path = Path(user_dest_path)                     
    # Set returning control variables to default value
    exist = False
    created = False
    # Check if the user selected folder path exists
    if folder_path.is_dir():
        exist = True
    # Else then create the folder
    else:                                                  
        Path(user_dest_path).mkdir(parents=True, exist_ok=True)
        created = True
    # Return control variables
    return exist, created                                   


def check_list_files (user_orig_path):
    # user_orig_path is the origin path selected by the user
    files = [f.name for f in Path(user_orig_path).iterdir() if f.is_file()]
    # Return file list
    return files


def get_date_file (file_path):
    # Get stats object
    file = Path(file_path)
    stats = file.stat()
    # Convert timestamp to readable
    mod_time = datetime.fromtimestamp(stats.st_mtime)
    # Get year and month from the information if the file creation date
    year = mod_time.year
    month = mod_time.month
    # Give format to the information to return
    formatedyear = f"{year:04d}"
    formatedmonth = f"{month:02d}"
    return  formatedyear, formatedmonth


def copy_files_directory_error (source, destination):
    try:
        # shutil.copy2 copies the file and its metadata
        error = False
        shutil.copy2(source, destination)
        text = ("File copied successfully source: " + str(source) + " to: " + str(destination))
        write_log_file(text)
    except FileNotFoundError:
        error = True
        write_log_file("Error: The source file was not found.")
    except PermissionError:
        error = True
        write_log_file("Error: Permission denied at the source or destination.")
    except shutil.SameFileError:
        error = True
        write_log_file("Error: Source and destination are the same file.")
    except Exception as e:
        error = True
        write_log_file(f"An unexpected error occurred: {e}")
    return error


def get_match_files(source_file, destination_file, copy):
    match = filecmp.cmp(source_file, destination_file, shallow=False)
    #this variable is just for log record text construction 
    if copy:
        text = "Checking before copying "
    else:
        text = "Checking before erasing "
    if match:
        text = text + ("Files match Origin: " + source_file + " Destination: " + destination_file)
    else:
        text = text + ("Files differ Origin: " + source_file + " Destination: " + destination_file)
    write_log_file(text)
    return match


def erase_file (file_orig_path):
    file_path = Path(file_orig_path)
    deleted = False
    # Attempt to delete the file
    try:
        file_path.unlink()
        write_log_file(f"File '{file_path}' has been deleted.")
        deleted = True
    except FileNotFoundError:
        write_log_file(f"Error: The file '{file_path}' does not exist.")
    return deleted




