#Task1
def hello():
    return('Hello!')

print(hello())

#Task2
def greet(name):
    return('Hello,'+" "+ name +'!')

print(greet('Manizha'))

#Task3

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                if b == 0:
                    raise ZeroDivisionError
                return a / b
            case "modulo":
                if b == 0:
                    raise ZeroDivisionError
                return a % b
            case "int_divide":
                if b == 0:
                    raise ZeroDivisionError
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
      
print(calc(2,2, 'devide'))

#Task4
def data_type_conversion(value, type):
    try:
        match type:
            case "str":
                return str(value) 
            case "int":
                return int(value)
            case "float":
                return float(value)
            case _:
                raise ValueError(f"Unsupported type: {type}")
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type}."

print (data_type_conversion(3.4, "int"))


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

#Task9

def hangman(secret, guess):
    correct_guess = ""
    secret = secret.lower()
    guess= guess.lower()
    for letter in secret:
            if letter in guess:
                correct_guess += letter

            else :
                correct_guess +="_"
            
    return correct_guess    

print(hangman("Life is short!", "labscdefor"))


#Task10
def pig_latin(string):
    vowels = "aeiou"
    
    words = string.split()  
    modified_words = [] 
    
    for word in words:
        if word[0].lower() in vowels:
            modified_words.append(word + 'ay')
        
        else:
            vowel_pos = len(word) 
            for i in range(len(word)):
                if i > 0 and word[i-1].lower() == 'q' and word[i].lower() == 'u':
                    continue
                    
                if word[i].lower() in vowels:
                    vowel_pos = i
                    break
            
        
            modified_words.append(word[vowel_pos:] + word[:vowel_pos] + "ay")
    
    return " ".join(modified_words)

print(pig_latin('apple is sweet so I ate it so quickly'))       


