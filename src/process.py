'''
- main process of the CSV data to create the output list with desired values
'''
def process_func(main_list):
    py_list = [ii['Product/Year'] for ii in main_list] #list of product/years
    unq_py_list = list(set(py_list))
    unq_py_list.sort() # to make sure the outcome list is sorted alphabetically and numerically
    out_list=[]
    for header in unq_py_list: #iterating through unique list of product/year
        cmpny_py_list = [ii['Company'] for ii in main_list if ii['Product/Year'] == header] #list of companies a complaint about A product/year is filed against
        n_cmplt_cmpny_py = [cmpny_py_list.count(ii) for ii in set(cmpny_py_list)] # list of Number of Complaints against each unique Company about a Product/Year
        max_prct_cmpny = round(100.0*float(max(n_cmplt_cmpny_py))/float(sum(n_cmplt_cmpny_py)))
        out_list.append([header, str(py_list.count(header)), str(len(set(cmpny_py_list))), str(max_prct_cmpny)])

    return out_list
