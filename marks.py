import csv
import sys

f=sys.argv[1]
marks_list=[]
with open(f, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        marks_list.append(row)

marks_list.pop(0)
total=[]
for i in marks_list:
    i[1]=int(i[1])
    i[2]=int(i[2])
    i[3]=int(i[3])
    i[4]=int(i[4])
    i[5]=int(i[5])
    i[6]=int(i[6])
    total.append([i[0],sum(i[1:])])

marks_list.sort(key=lambda x: x[1],reverse=True)
print("Topper in Maths is",marks_list[0][0])
marks_list.sort(key=lambda x: x[2],reverse=True)
print("Topper in Biology is",marks_list[0][0])
marks_list.sort(key=lambda x: x[3],reverse=True)
print("Topper in English is",marks_list[0][0])
marks_list.sort(key=lambda x: x[4],reverse=True)
print("Topper in Physics is",marks_list[0][0])
marks_list.sort(key=lambda x: x[5],reverse=True)
print("Topper in Chemistry is",marks_list[0][0])
marks_list.sort(key=lambda x: x[6],reverse=True)
print("Topper in Hindi is",marks_list[0][0])
total.sort(key= lambda x: x[1], reverse=True)
print("\nBest Students in the class are")
print(total[0][0], "first rank")
print(total[1][0], "second rank")
print(total[2][0], "third rank")
