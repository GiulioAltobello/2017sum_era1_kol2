#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class matrix:
    def __init__(self, a):
        self.a=a
        
    def __str__(self):
        s=''
        for x in range(len(self.a)):
            for y in range(len(self.a[0])):
                s+= str(self.a[x][y]) +' '
            s+= '\n'
        return s
        

def sum(m1,m2):
    return (m1.a+m2.a)

def prodotto(m1,m2):
    s=0
    m3=matrix([[0 for i in range(len(m2.a[0]))]for j in range(len(m1.a))])
    for i in range(len(m1.a)):
        for j in range(len(m2.a[i])):
            for h in range(len(m1.a[i])):
                s+=m1.a[i][h]*m2.a[h][j]
            m3.a[i][j]=s
            s=0
    return m3

m1 = matrix([[0,1,3],[6,1,9],[3,1,6]])
m2 = matrix([[6,1,9],[0,1,3],[5,1,8]])

m3=prodotto(m1,m2)
print m1
print m2
print m3

m3=sum(m1,m2)
print m3
    
