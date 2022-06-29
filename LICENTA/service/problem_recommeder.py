import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import time

start = time.time()

ratings = pd.read_csv("scores.csv")
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
        scores = ratings[ratings.userId == user_no]
        scores = scores[['problemId', 'score']]
        # print(scores)
        dicti = {}
        for i,j  in scores.iterrows():
            dicti[j.problemId] = j.score


        return dicti


    def total_score_of_user(self, user_no):
        sc = self.GetScores(user_no)
        total = np.zeros(24)
        for i in sc:
            score = sc[i]
            poz = int(i/20)
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
        scores = self.GetScores(user_no)
        print(scores)
        categ = self.get_category_recommandation(user_no, current_problem_no)

        range_start = categ * 20 + 1
        range_stop = range_start + 19
        solved_problems_in_categ = []
        for i in scores:
            if i >= range_start and i<=range_stop and scores[i] > 0:
                solved_problems_in_categ.append(i)
        ret_list = []
        for i in range(range_start, range_stop+1):
            if i not in solved_problems_in_categ:
                ret_list.append(problem_titles[i])


        return ret_list












class Collaborative_Filtering:
    X = 0
    user_mapper = 0
    problem_mapper = []
    user_inv_mapper = []
    problem_inv_mapper = []

    def create_matrix(self, df):
        N = len(df['userId'].unique())
        M = len(df['problemId'].unique())

        # Map Ids to indices
        self.user_mapper = dict(zip(np.unique(df["userId"]), list(range(N))))
        self.problem_mapper = dict(zip(np.unique(df["problemId"]), list(range(M))))
        # Map indices to IDs
        self.user_inv_mapper = dict(zip(list(range(N)), np.unique(df["userId"])))
        self.problem_inv_mapper = dict(zip(list(range(M)), np.unique(df["problemId"])))

        user_index = [self.user_mapper[i] for i in df['userId']]
        problem_index = [self.problem_mapper[i] for i in df['problemId']]

        val = csr_matrix((df["score"], (problem_index, user_index)), shape=(M, N))

        return val, self.user_mapper, self.problem_mapper, self.user_inv_mapper, self.problem_inv_mapper

    def find_similar_problems(self, problem_id, X, k, metric='cosine', show_distance=False):
        neighbour_ids = []

        problem_ind = self.problem_mapper[problem_id]
        problem_vec = X[problem_ind]
        k += 1
        # kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
        kNN = NearestNeighbors(n_neighbors=k, algorithm="auto", metric=metric)

        kNN.fit(X)
        problem_vec = problem_vec.reshape(1, -1)
        neighbour = kNN.kneighbors(problem_vec, return_distance=show_distance)
        for i in range(0, k):
            n = neighbour.item(i)
            neighbour_ids.append(self.problem_inv_mapper[n])
        neighbour_ids.pop(0)
        return neighbour_ids

    def collaborative_filtering(self, problem):
        self.X, self.user_mapper, self.problem_mapper, self.user_inv_mapper, self.problem_inv_mapper = self.create_matrix(
            ratings)
        problem_titles = dict(zip(problems['problemId'], problems['title']))

        problem_id = problem

        similar_ids = self.find_similar_problems(problem_id, self.X, k=10)
        problem_title = problem_titles[problem_id]


        ret = []
        print(f"Since you solved {problem_title}, we recommend: ")
        for i in similar_ids:
            ret.append(problem_titles[i])

        return ret


