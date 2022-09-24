

#create a loop for here
from asyncore import loop


RightQues = str(input("Right: "))

#RightQues = str(input("put Something here: "))

for val in RightQues:
    if RightQues.isnumeric():
     break
else:
    print(str(input("Put a number: ")))
    



WrongQues = int(input("Wrong: "))
UnattemptQues = int(input("Unattempted: "))
#to here


'''
RightQuesTypo = str(input("put Something here: "))

if RightQuesTypo.isnumeric():
    print(str(input("Put a number: ")))
else:
    print ("ok")
'''

#no Touchy
sum = RightQues+WrongQues+UnattemptQues

print ("overall questions: " + str(int(sum)))
