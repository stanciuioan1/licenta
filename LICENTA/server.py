from flask import Flask, request
import compiler
import base64

app = Flask(__name__)
  
@app.route('/')
def hello_world():
    request_data = request.get_json()
    code = request_data['code']
    problem_no = request_data['problem_no']
    decoded = base64.b64decode(code).decode('utf-8')
    print(decoded)
    print(problem_no)
    tests = compiler.compile(decoded, int(problem_no))
    return tests
  
# main driver function
if __name__ == '__main__':
  
    app.run()