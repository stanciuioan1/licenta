import os


def get_enunt(problem_no):
    print(os.listdir())
    os.chdir('problems')
    folder_files = os.listdir()
    if not (str(problem_no)  in folder_files):
        return 500
    
    os.chdir(str(problem_no)) 
    input_file = open("enunt", "r")
    input_text = input_file.read()
    input_file.close()
    os.chdir("../../")
    return input_text



def get_date_intrare(problem_no):
    os.chdir('problems')
    folder_files = os.listdir()
    if not (str(problem_no)  in folder_files):
        return 500
    
    os.chdir(str(problem_no))
    input_file = open("date_intrare", "r")
    input_text = input_file.read()
    input_file.close()
    os.chdir("../../")
    return input_text



def get_date_iesire(problem_no):
    os.chdir('problems')
    folder_files = os.listdir()
    if not (str(problem_no)  in folder_files):
        return 500
    
    os.chdir(str(problem_no)) #entering the problem 
    input_file = open("date_iesire", "r")
    input_text = input_file.read()
    input_file.close()
    
    os.chdir("../../")
    return input_text

def get_exemplu(problem_no):
    os.chdir('problems')
    folder_files = os.listdir()
    if not (str(problem_no)  in folder_files):
        return 500
    
    os.chdir(str(problem_no)) #entering the problem 
    input_file = open("exemplu", "r")
    input_text = input_file.read()
    input_file.close()
    os.chdir("../../")
    return input_text

def get_tags(problem_no):
    os.chdir('problems')
    folder_files = os.listdir()
    if not (str(problem_no)  in folder_files):
        return 500
    
    os.chdir(str(problem_no)) #entering the problem 
    input_file = open("tags", "r")
    input_file.close()
    input_text = input_file.read()
    os.chdir("../../")
    return input_text

