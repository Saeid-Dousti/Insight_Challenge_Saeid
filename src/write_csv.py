'''
This file writes the output and error lists into their respective CSV files
'''

import os

def write_report_func(final_list):
    output_folder_path = os.path.abspath("./output")
    output_file = os.path.join(output_folder_path, 'report.csv')
    with open(output_file,'w') as f:
        f.write('\n'.join(','.join(row) for row in final_list))

def write_error_func(error_list):
    output_folder_path = os.path.abspath("./output")
    output_file = os.path.join(output_folder_path, 'error_log.csv')
    with open(output_file,'w') as f:
        f.write('\n'.join(row for row in error_list))
