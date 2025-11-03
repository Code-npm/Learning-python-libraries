
import numpy as np

S1=int(input("Enter marks of Student1:-"))
S2=int(input("Enter marks of Student2:-"))
S3=int(input("Enter marks of Student3:-"))
S4=int(input("Enter marks of Student4:-"))
S5=int(input("Enter marks of Student5:-"))

marks=np.array([])
marks=np.append(marks, [S1 , S2 ,S3 ,S4 , S5])
print(marks)
print(np.mean(marks))
print(np.min(marks))
print(np.max(marks))
