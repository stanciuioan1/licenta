import service.problem_details as problem_details

from __init__ import *



#---------problem_details------------------------

@app.route('/enunt/<problem_no>')
def get_enunt(problem_no):
    return problem_details.get_enunt(problem_no)


@app.route('/date_intrare/<problem_no>')
def get_date_intrare(problem_no):
    return problem_details.get_date_intrare(problem_no)


@app.route('/date_iesire/<problem_no>')
def get_date_iesire(problem_no):
    return problem_details.get_date_iesire(problem_no)

@app.route('/exemplu/<problem_no>')
def get_exemplu(problem_no):
    return problem_details.get_exemplu(problem_no)

@app.route('/tags/<problem_no>')
def get_tags(problem_no):
    return problem_details.get_tags(problem_no)
