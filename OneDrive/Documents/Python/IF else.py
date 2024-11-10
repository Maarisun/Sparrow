Score=int(input("Mark:"))
if(Score<35):
   print("Poor Student")
elif(Score>35 and Score<70):
   print("Average Student")
elif(Score>70 and Score==100):
   print("Good student")
else:
    print("Invalid Score")
