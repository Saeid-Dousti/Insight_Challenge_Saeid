import re
'''
- In this functions file, the complaints.csv file read into a list of dictionaries, one dictionary for each line of complaint
- In the line parsing, the proper end of line is distinguished from the others by matching date format of XXXX-XX-XX of the next line
- To parse the complaint lines properly, the commas between quotation marks are replaced with @#$#@
- Finally after creating the main_list, commas are replacing @#$#@
'''
def cmp_main_list_func(in_path):

    with open(in_path, mode='r', encoding= 'utf8', newline='\n') as f:
        alls = ''.join(f.readlines())
        lines = re.split('\n(?=\d{4}.\d{2}.\d{2})', alls)

    keys = lines[0].strip().split(',')

    main_list = []
    Error_list = []
    for ii in range(1, len(lines)):
        try:
            qpattern = re.findall(r',"(.*?)",\s*', lines[ii])
            qpatterntoreplace = [qp.replace(',', '@#$#@') for qp in qpattern]
            for jj in range(0, len(qpattern)):
                lines[ii] = lines[ii].replace(qpattern[jj], qpatterntoreplace[jj])
            list_row = split_w_comma_func(lines[ii], len(keys))

            dict_row = dict()
            for kk, Header in enumerate(keys):
                dict_row[Header] = list_row[kk]
            
            # a new key named "Product/Year" is defined to facilitate the final sorting based on product and year all at once
            dict_row['Product/Year'] = (dict_row['Product'].strip() + ',' + re.findall(r'\d{4}', dict_row['Date received'])[0]).replace('@#$#@',',').lower()  # make the product/Year all lower case

            main_list.append(dict_row)
        except:
            print('Error in reading complaint# '+str(ii))
            Error_list.append('Error in reading complaint# '+str(ii))

    return main_list, Error_list

def split_w_comma_func(line_string,length):
    '''
    - spliting each complaint line by commas
    '''
    list_line = line_string.strip().split(',')
    return list_line

