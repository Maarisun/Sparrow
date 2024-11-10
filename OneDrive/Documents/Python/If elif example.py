
Tamil=int(input("Tamil:"))
English=int(input("English:"))
Maths=int(input("Maths:"))
Science=int(input("Science:"))
SocialScience=int(input("Social Science:"))
Total=Tamil+English+Maths+Science+SocialScience
print("Total:",Total)
Average=Total/5
print("Average:",Average)
if(Average<=35):
    print("Special Class required")
else:
    print("You're good to go")
