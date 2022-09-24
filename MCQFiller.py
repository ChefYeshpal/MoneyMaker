# MCQ  filler is for filling up my google spreadsheet in which ive written stuff like
    #book, test area, page noumber, right, wrong, unattempted, start time, endtime, date
# Created Date 
# Last Updated Date: 2022-09-24 20:12:06
# FileName: MCQFiller.py
# Change History (ctrl + shift + I)
    # 2022-09-24 20:09:19 : as of today prog take input of book name , right wrong unattempted and test area. 
    # 2022-09-24 20:16:15 : 
#To do
    # add entry for start time and end time 
    # add % logic with formula based  (Rx3-W)/(R+W+U)*100  
    # Add Looping mechnism 
    # The output should go into the text file
    #  




################################################################

#for todays input date
from datetime import date

today = date.today()
print("Today's date:", today)

#user Input
bookName = input("Book name: ")
TestArea = input("Test Area: ")
PageNum = input("Page Number: ")


#NoOfQuesAttempt = input("overall number of attempted questions: ")

#create a loop for here
RightQues = int(input("Right: "))
WrongQues = int(input("Wrong: "))
UnattemptQues = int(input("Unattempted: "))
#to here
 


#to check wether the overall no. of ques is ok
sum = int(RightQues+WrongQues+UnattemptQues)



print ("overall questions: " + str(int(sum)))





