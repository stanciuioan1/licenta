import os
import filecmp


codes = {200: 'success', 404: 'file_name not found',
         400: 'error', 408: 'timeout'}

file_name = "pb.cpp"
bin_file = "pb"
inp_file = "pb.in"
out_file = "pb.out"
expectedOut = "pb_exp.out"
timeout = '2'  # secs


class program:
    def __init__(self, inp, timeout, exp_out=""):
        self.file_name = file_name  # Full name of the program
        self.lang = None  # Language
        self.name = bin_file  # Name without extension
        self.inp_file = inp  # Input file
        self.expectedout = exp_out  # Correct output file
        self.actualout = out_file  # Actual output file
        self.timeout = timeout  # Timeout set for execution


    def compile(self):
        os.system('g++ -o ' + self.name + ' ' + self.file_name)
        if (os.path.isfile(self.name)):
            return 200     
        else:
            return 400


    def run(self):
        cmd = './' + self.name
        r = os.system('timeout ' + timeout + ' ' +
                      cmd + ' < ' + self.inp_file + ' > ' + self.actualout)
        if r == 0:
            return 200
        elif r == 31744:
            os.remove(self.actualout)
            return 408
        else:
            os.remove(self.actualout)
            return 400

    def match(self):
        if os.path.isfile(self.actualout) and os.path.isfile(self.expectedout):
            b = filecmp.cmp(self.actualout, self.expectedout)
            return b
        else:
            return 404





problem_nr = 1
problem_text = '''#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("pb.in");

int main()
{
    int a,b;
  fin>>a>>b;
  cout << a+b;
    return 0;
}'''

lang = 'cpp'

def clean_up():
    files_to_delete = [file_name, inp_file, expectedOut, bin_file, out_file]
    for i in files_to_delete:
        if os.path.exists(i):
            os.remove(i)


def compile(text_problem, problem_no):
    tests={
        "1":"",
        "2":"",
        "3":"",
        "4":"",
    }
    
    code_file = open(file_name, "w")
    code_file.write(text_problem)
    code_file.close()

    new_program = program(inp_file, timeout, expectedOut)

    result = new_program.compile()
    print ('Compilation: ', (result))
    print(result)
    if result != 200:
        tests["1"] = 'ec'
        tests["2"] = 'ec'
        tests["3"] = 'ec'
        tests["4"] = 'ec'
        return tests


    os.chdir('problems')
    folder_files = os.listdir()
    if str(problem_no)  in folder_files:
        os.chdir(str(problem_no)) #entering the problem 


        for i in range(1,5):
            os.chdir("in")
            input_file = open(str(i)+".in", "r")
            input_text = input_file.read()
            os.chdir("../out")
            output_file = open(str(i)+".out", "r")
            output_text = output_file.read()
           
            os.chdir("../../..")
            create_input_file = open(inp_file, "w")
            create_input_file.write(input_text) #ramane
            create_output_file = open(expectedOut, "w")
            create_output_file.write(output_text) # ramane
            create_input_file.close() # ramane
            create_output_file.close() #ramane

 

            print("TEST NR "+ str(i))
            result = new_program.run()
            print ('Running: ' + str(result))
            if result==408:
                tests[str(i)] = result
            else:
                print ('Result: ', new_program.match())
                print("--------------------------\n\n")
                tests[str(i)]=new_program.match()

            os.chdir("problems/"+ str(problem_no))

    os.chdir("../../")
    clean_up()
    return tests

    

if __name__ == '__main__':
    compile()


        

    