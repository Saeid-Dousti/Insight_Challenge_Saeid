'''
This file is the main file of the Insight Fellowship Challenge
Author: Saeid Dousti
submitted: 03-19-2020
'''
from input_path import input_path_func
from cmp_main_list import cmp_main_list_func
from process import process_func
from write_csv import write_report_func, write_error_func

if __name__ == "__main__":
    input_path = input_path_func()                              # Fetching the input CSV file address
    main_list, error_list = cmp_main_list_func(input_path)      # Reading, and parsing input file to a list of dictionary. Also create a report for the lines it can't parse properly 
    output_list = process_func(main_list)                       # Processing the main list of complaints into the desired output elemets
    write_report_func(output_list)                              # writing the report.csv file
    write_error_func(error_list)                                # writing the error.csv file

    print('Done!')
