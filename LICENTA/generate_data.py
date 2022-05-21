import csv
import random

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
        n = random.randint(1, 150)  # nr de probleme
        for i in range(1,n):
            x = (i ** 3 -214354) % 480
            score = random.randint(1, 4)
            score *= 25
            data = [user, x, score]
            writer.writerow(data)

    f.close()
