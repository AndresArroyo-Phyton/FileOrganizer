import os

from datetime import datetime


def get_year_month ():
    curr_date = datetime.now() 
    # get the year
    year = curr_date.year
    # get the month (as an integer 1-12)
    month = curr_date.month
    # get the day (as an integer 1-12)
    day = curr_date.day
    # format the time as a string "HH:MM:SS" (24-hour format)
    current_time_string = curr_date.strftime("%H:%M:%S")
    # format year and month
    formated_year = f"{year:04d}"
    formated_month = f"{month:02d}"
    formated_day = f"{day:02d}"    
    return current_time_string, formated_year, formated_month, formated_day 


def write_log_file (new_text_line):
    # get current time
    current_time, year, month, day = get_year_month()
    # get current directory
    current_directory = os.getcwd()
    # creates the path
    file_path =  current_directory + "\\" + year + "_" + month + "_" + 'file_organizer.txt'
    # creates the content to write
    content = year + "-" + month + "-" + day +" " + current_time + "> " + new_text_line

    # open the file in append mode ('a')
    with open(file_path, 'a') as f:     
        # write the new line of content
        # the '\n' ensures the text is on its own line
        f.write(content + '\n')
    return



write_log_file ("this is a test 3")




