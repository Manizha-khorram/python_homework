import csv
import traceback


#Task2

def read_employees():

    empl_dict = {}
    empl_list = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)

            first_row = True
            for row in reader:
               if first_row:
                empl_dict['fields'] = row
                first_row = False
               else:
                 empl_list.append(row)
                 
            empl_dict['rows'] = empl_list
            return empl_dict   

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")       


        

employees = read_employees()

print(employees)




# Task 3
def column_index(column_name):

    try:
        if column_name in employees['fields']:
            return employees['fields'].index(column_name)
        else:
            raise ValueError(f"Column '{column_name}' does not exist in fields.")
    except KeyError:
        raise KeyError("The 'fields' key is missing in the employees dictionary.")


employees = read_employees()

employee_id_column = column_index('employee_id')

print(employees)


#Task4

def first_name(row_number):
    try:
        
        empl_first_name_index = column_index('first_name')
        
        row = employees['rows'][row_number - 1]
        
        return row[empl_first_name_index]

    except IndexError:
        print(f"Row {row_number} does not exist")
        return None        


#Task5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    
    return matches

#Task6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


#Task7
def sort_by_last_name():
    last_name_column = column_index('last_name')
    
    employees["rows"].sort(key=lambda row: row[last_name_column])
    
    return employees["rows"]


