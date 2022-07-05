import numpy as np
import pandas as pd
import time
from __init__ import *
import math
import numpy

start = time.time()
problems = pd.read_csv("problems.csv")
problem_titles = dict(zip(problems['problemId'], problems['title']))

elems = []

for i in range(24):
    elems.append([j for j in range(20*i + 1, 20*i + 21)])

#problems = {}

#problems['tree'] = [elems[0], elems[1], elems[2]]
#problems['graph'] = [elems[3], elems[4], elems[5]]
#problems['stack'] = [elems[6], elems[7], elems[8]]
#problems['queue'] = [elems[9], elems[10], elems[11]]
#problems['dynamic_programming'] = [elems[12], elems[13], elems[14]]
#problems['geometry'] = [elems[15], elems[16], elems[17]]
#problems['hash'] = [elems[18], elems[19], elems[20]]
#problems['backtracking'] = [elems[21], elems[22], elems[23]]





class Content_Based_Filtering:
    def GetScores(self, user_no):
        user_from_db = users_collection.find_one({'username': user_no}) 
        print(user_from_db["problems"])
        problems = user_from_db["problems"]

        dicti = {}
        for i in problems:
            current_score = 0
            if problems[i]['1'] == 'True':
                current_score += 1
            if problems[i]['2'] == 'True':
                current_score += 1
            if problems[i]['3'] == 'True':
                current_score += 1
            if problems[i]['4'] == 'True':
                current_score += 1

            dicti[i] = current_score * 25
        return dicti


    def total_score_of_user(self, user_no):
        sc = self.GetScores(user_no)
        print(sc)
        total = np.zeros(24)
        for i in sc:
            score = sc[i]
            poz = int(int(i)/20)
            total[poz] += score

        for i in range(24):
            total[i] /= 20

        return total

    def get_category_recommandation(self, user_no, current_problem_no):
        scores = self.total_score_of_user(user_no)
        category_of_current = int(int(current_problem_no) / 20)
        recc = category_of_current
        while scores[recc] > 50:
            recc = (recc + 1)%24
            if recc == category_of_current:
                while scores[recc] < 100:
                    recc = (recc + 1) % 24
                    if recc == category_of_current:
                        return 'Full solve'

        return recc
    
    def get_available_problems(self, user_no, current_problem_no):
        print("Utilizatorul este" + user_no)
        scores = self.GetScores(user_no)
        print(scores)
        categ = self.get_category_recommandation(user_no, current_problem_no)

        range_start = categ * 20 + 1
        range_stop = range_start + 19
        solved_problems_in_categ = []
        for i in scores:
            if int(i) >= range_start and int(i)<=range_stop and scores[i] > 0:
                solved_problems_in_categ.append(i)
        ret_list = []
        for i in range(range_start, range_stop+1):
            if i not in solved_problems_in_categ:
                ret_list.append(problem_titles[i])


        return ret_list[:5]





class My_Collaborative_Filtering:
    def cosine_similarity(self,a,b):

        prod_a=0
        prod_b=0
        prod_a_b=0
        length = len(a)
        for i in range(length):
            prod_a += a[i] * a[i]
            prod_b += b[i] * b[i]
            prod_a_b += a[i] * b[i]

        if prod_a == 0 or prod_b == 0:
            return -2
        else:
            return (prod_a_b / math.sqrt(prod_a)) / math.sqrt(prod_b)


    def generate_matrix(self):
        problems1 = []

        no_users=0
        for _ in users_collection.find():
            no_users = no_users + 1

        for i in range(480):
            users = [0 for _ in range(no_users)]
            problems1.append(users)

        user_no = 0
        cursor = users_collection.find()
        for i in cursor:
            for j in i["problems"]:

                problems1[int(j)][user_no] = 1
                if i["problems"][j]['1'] == 'True':
                    problems1[int(j)][user_no] += 1
                if i["problems"][j]['2'] == 'True':
                    problems1[int(j)][user_no] += 1
                if i["problems"][j]['3'] == 'True':
                    problems1[int(j)][user_no] += 1
                if i["problems"][j]['4'] == 'True':
                    problems1[int(j)][user_no] += 1

            user_no +=1

        return problems1


    def compute_knn(self,problem_nr):
        similarities = []
        problems1 = self.generate_matrix()
        for i in problems1:
            similarity = self.cosine_similarity(i, problems1[int(problem_nr)])
            similarities.append(similarity)
    

        rez = numpy.argsort(similarities)
        rez3 = rez[-5:][::-1]    #alegerea ultimelor 5, apoi inversarea
        probs = [problem_titles[i] for i in rez3]
        return probs







