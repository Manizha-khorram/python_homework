
import traceback


def diary():
    try:
        with open('diary.txt', '+a') as file:
          first_time = True
          while True:
              if first_time:
                user_input = input('What happened today?  (Type "done for now" if you want to exit!) \n')
                first_time = False
              else:
                user_input = input('What else?  (Type "done for now" if you want to exit!) \n')

              if user_input.lower() == "done for now":
                  print('Yout diary saved, Exiting...')
                  break

              file.write(user_input+ '\n')
             

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

print(diary())
