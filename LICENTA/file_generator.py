import csv
import random
from __init__ import *
import hashlib



header = ['userId', 'problemId', 'score']
data = ['Afghanistan', 652090, 'AF', 'AFG']

header2 = ['problemId', 'title']
with open('problems.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header2)
    names = ['tree', 'graph', 'stack', 'queue', 'dynamic_programming', 'geometry', 'hash', 'backtracking']
    names_extended =[]
    for i in names:
        names_extended.append(i + '_easy')
        names_extended.append(i + '_medium')
        names_extended.append(i + '_hard')

    for i in range(24):
        for k in range(1,21):
            name = names_extended[i] + str(k)
            data = [i*20 + k, name]
            writer.writerow(data)

    #for i in range(1, 480):
    #    name = 'grafuri' + str(i)
    #    data = [i, name]
    #    writer.writerow(data)

    f.close()

with open('scores.csv', 'w') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    # writer.writerow(data)
    for user in range(1,1000):
        new_user = {}
        new_user["username"] = "user" + str(user)

        new_user["password"] = hashlib.sha256("test".encode("utf-8")).hexdigest() 
        new_user["problems"] = {}
        
        n = random.randint(1, 150)  # nr de probleme
        for i in range(1,n):
            x = (i ** 3 -214354) % 480
            score1 = (random.randint(0, 1) == 1)
            score2 = (random.randint(0, 1) == 1)
            score3 = (random.randint(0, 1) == 1)
            score4 = (random.randint(0, 1) == 1)
            score  = score1 + score2+score3+score4
            tests={}
            tests[str(1)]=str(score1)
            tests[str(2)]=str(score2)
            tests[str(3)]=str(score3)
            tests[str(4)]=str(score4)
            problems = new_user["problems"]
            problems[str(x)] = tests

            #users_collection.update_one({"username": ("user" + str(user))}, {"$set": { "problems": problems }})
            data = ["user" + str(user), x, score]
            writer.writerow(data)
        #print(new_user)
        #break
        users_collection.insert_one(new_user)

    f.close()
