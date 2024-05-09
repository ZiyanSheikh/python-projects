question1 = "1.Which programming language used for the ai(artificial intelligence):_","i.python","ii.javascript","iii.php","iv.none of these"
question2 = "2.Which one of the following is a programming language","i.C++","ii.Java script","iii.Python" ,"iv.Both i and iii"
question3 = "3.Comments in programming languages can be execute or not","i.Yes","ii.Not"

prizes = [1000,2000,3000,4000,5000,10000]

for questions in question1:
    print(questions)

info = input("Write the correct option:")

if info == "i":
    print("Congratulations! you have won and you got", prizes[0])

else:
    print("Try again please!")

for questions1 in question2:
    print(questions1)

info1 = input("Write the correct option:")

if info1 == "iv":
    print("Really you are going well and got",prizes[1])

else:
    print("Opps you are going wrong just one try left")

for questions2 in question3:
    print(questions2)

info2 = input("Write the correct option:")

if info2 == "ii":
     print("Really you are going well and got", prizes[2],"You have totally got the:",prizes[0:3])

else:
    print("Ops!")













