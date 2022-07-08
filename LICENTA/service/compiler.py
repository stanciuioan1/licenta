import os


file = "pb.cpp"
bin_file = "pb"
file_input = "pb.in"
file_output = "pb.out"
expect = "pb_exp.out"
time_limit = '2' 


def compile_code():
    os.system('g++ -o ' + bin_file + ' ' + file)
    if (os.path.isfile(bin_file)):
        return 0     
    return -1


def run_current_test():
    resp = os.system('timeout ' + time_limit + ' ' +'./' + bin_file + ' < ' + file_input + ' > ' + file_output)
    if resp == 0:
        return 200
    return 408

def compare_actual_wth_expected():
    f1 = open(file_output, "r")
    file1 = f1.read()
    f2 = open(expect, "r")
    file2 = f2.read()

    print(file1)
    print(file2)

    if file1 == file2:
        return True
    return False



def clean_up():
    files_to_delete = [file, file_input, expect, bin_file, file_output]
    for i in files_to_delete:
        if os.path.exists(i):
            os.remove(i)


def execute(text_problem, problem_no):
    tests={
        "1":"",
        "2":"",
        "3":"",
        "4":"",
    }
    
    code_file = open(file, "w")
    code_file.write(text_problem)
    code_file.close()


    result = compile_code()
    print ('Compiled with code: ', (result))
    print(result)
    if result != 0:
        tests["1"] = 'ec'
        tests["2"] = 'ec'
        tests["3"] = 'ec'
        tests["4"] = 'ec'
        return tests


    os.chdir('problems')
    folder_files = os.listdir()
    if str(problem_no)  in folder_files:
        os.chdir(str(problem_no)) 

        for i in range(1,5):
            os.chdir("in")
            input_file = open(str(i)+".in", "r")
            input_text = input_file.read()
            os.chdir("../out")
            output_file = open(str(i)+".out", "r")
            output_text = output_file.read()
           
            os.chdir("../../..")
            create_input_file = open(file_input, "w")
            create_input_file.write(input_text) 
            create_output_file = open(expect, "w")
            create_output_file.write(output_text) 
            create_input_file.close() 
            create_output_file.close()

 

            print("TEST NR "+ str(i))
            result = run_current_test()
            print ('Ruleaza: ' + str(result))
            if result==408:
                tests[str(i)] = result
            else:
                print ('Rez: ', compare_actual_wth_expected())
                print("--------------------------\n\n")
                tests[str(i)]=compare_actual_wth_expected()

            os.chdir("problems/"+ str(problem_no))

    os.chdir("../../")
    clean_up()
    return tests

    



        

    