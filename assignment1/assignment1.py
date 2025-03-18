#Task1
def HelloFunc():
    return('Hello!')

print(HelloFunc())

#Task2
def GreetFun(name):
    return('Hello'+" "+ name +'!')

print(GreetFun('Manizha'))

#Task3

def CalcFunc(a , b, opration = None):
   
   if isinstance(a, str) or isinstance(b, str):
        return "Cannot perform operations on strings"
   
   match opration:
       case None:
          return a*b 
       case "+":
          return a+b
       case "-":
          return a-b
       case "/":
          return a/b if b != 0 else "Cannot divide by zero"
       case "%":
          return a%b if b != 0 else "Cannot divide by zero"
       case "//":
          return a // b
       case "**":
          return a**b
        
print(CalcFunc(2,0, '/'))

#Task4
def data_type_conversion(value, type):

   match type:
        case "str":
            return str(value) 
        case "int":
            return int(value)
        case "float":
            return float(value) if isinstance(value , int) else f"You can't convert {value} into a {type}"
        case _:
            raise ValueError(f"Unsupported type: {type}")

print (data_type_conversion("hello", "float"))


#Task5
def grade(*args):
    try:
        if not args: 
            return "Invalid data was provided."

    
        scores = [float(score) for score in args]  

        average = sum(scores) / len(scores)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except (ValueError, TypeError): 
        return "Invalid data was provided."


print(grade(85, 90, 78)) 

#Task6

def repeat(string, count):
      
    result = ""
    for n in range(count):
       result += string
    return result

print(repeat('hello',2))

#Task7
def student_scores(mode, **kwargs):

    if not kwargs: 
            return "No scores provided."
    
    if mode == "best":
        max_score = -1 
        best_student = None
        for student, score in kwargs.items():
            if score > max_score:
                max_score = score
                best_student = student
        return best_student

    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)


print(student_scores("mean", Marry=90, Ahmad=40, Harry=80))

#Task8

def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.lower().split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("Code the dream is the best."))
        
