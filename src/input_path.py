'''
    This function retrieves the path of the input file from the repository
    :return: the input file absolute path
'''
import os

def input_path_func():
    
    input_folder_path = os.path.abspath('./input')
    return os.path.join(input_folder_path,'complaints.csv')
