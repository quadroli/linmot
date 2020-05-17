x = 1
import math
print ("Hello user")
print ()
name = input ("What is your name: ")
print()
print ("Nice to meet you " + str(name))
print()
ans = input ("Do you wish to use linear motion calculator[y/n]: ")
while x == 1:
 if ans == "y":
  print ("What do you wish to calculate?")   
  print ("->(1)Final velocity\n->(2)Initial velocity\n->(3)Accelaration\n->(4)Time\n->(5)Displacement")
  opt = ["1","2","3","4","5"]
  ans1 = input("Enter your answer: ")
  if ans1 ==  (opt[0]):
   print ("Given what data: ")
   print(" (a)initial velocity, accelaration and time\n (b)displacement, time and initial velocity\n (c)initial velocity, accelarartion and displacement") 
   ans2 = input ("Enter your answer: ")
   opt1 = ["a","b","c"]
   if ans2 == (opt1[0]):
    n1au = input ("Enter value for initial velocity: ")
    n1aa = input ("Enter value for accelaration: ")
    n1at = input ("Enter value for time: ")
    res1a = (float(n1aa) * float(n1at)) + float(n1au)
    print("Your answer is = " + str(res1a) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1 
   elif  ans2 == (opt1[1]):
    n1bs = input("Enter value for displacement: ")
    n1bt = input("Enter value for time: ")
    n1bu = input("Enter value for initial velocity: ")   
    res1b = (((float(n1bs) * 2) / float(n1bt)) - float(n1bu)) 
    print("Your answer is = " + str(res1b) ) 
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt1[2]):
    n1cu = input("Enter value for the initial velocity: ")
    n1ca = input("Enter value for accelaration: ")
    n1cs = input("Enter value for displacement: ")    
    res1c = math.sqrt(((float(n1cu)**2) + ((float(n1ca) * float(n1cs)) * 2)))
    print("Your answer is = " + str(res1c) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
  elif ans1 == (opt[1]):
   print ("Given what data: ")
   print("(a)final velocity, accelaration and time\n(b)displacement, time and final velocity\n(c)final velocity, accelaration and displacement\n(d)displacement, time and accelaration")     
   opt2 = ["a","b","c","d"]
   ans2 = input ("Enter your answer: ")
   if ans2 == (opt2[0]):
    n2av = input("Enter value for the final velocity: ")
    n2aa = input("Enter value for accelaration: ")
    n2at = input ("Enter value for time: ")   
    res2a = float(n2av) - (float(n2aa) * float(n2at))
    print("Your answer is = " + str(res2a) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt2[1]):
    n2bs = input("Enter value for displacement: ")
    n2bt = input("Enter value for time: ")
    n2bv = input("Enter value for final velocity: ")  
    res2b = (((float(n2bs) * 2)/float(n2bt)) - float(n2bv))
    print("Your answer is = " + str(res2b) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1 
   elif ans2 == (opt2[2]):
    n2cv = input ("Enter value for final velocity: ") 
    n2ca = input("Enter value for accelaration: ")
    n2cs = input ("Enter value for displacement: ")   
    res2c = math.sqrt(((float(n2cv)**2) - ((float(n2ca) * float(n2cs)) * 2)))   
    print("Your answer is = " + str(res2c) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed") 
     x = x + 1    
   elif ans2 == (opt2[3]):
    n2ds = input("Enter value of displacement: ")
    n2dt = input("Enter value of time: ")
    n2da = input("Enter value for accelaration: ")      
    res2d = (float(n2ds) / float(n2dt)) - ((float(n2da) * float(n2dt))/ 2)
    print("Your answer is = " + str(res2d) ) 
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
  elif ans1 == (opt[2]):
   print ("Given what data?")
   print("(a)initial velocity, final velocity and time\n(b)final velocity, initial velocity and displacement\n(c)displacement, time and initial velocity")    
   opt3 = ["a","b","c"]
   ans2 = input ("Enter your answer: ")
   if ans2 == (opt3[0]):
    n3au = input("Enter value for initial velocity: ")
    n3av = input("Enter value for final velocity: ")
    n3at = input("Enter value for time: ")
    res3a = ((float(n3av) - float(n3au))/float(n3at))
    print("Your answer is = " + str(res3a) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt3[1]):
    n3bv = input("Enter your value for final velocity: ")
    n3bu = input("Enter your value for initial velocity: ")
    n3bs = input("Enter your value for displacement: ") 
    res3b = ((float(n3bv)**2 - float(n3bu)**2)/(float(n3bs) * 2))
    print("Your answer is = " + str(res3b) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt3[2]):
    n3cs = input("Enter your value for displacement: ")
    n3ct = input("Enter your value for time: ")
    n3cu = input("Enter your value for initial velocity: ")    
    res3c = (((float(n3cs) * 2)/(float(n3ct)**2)) - ((float(n3cu) * 2)/float(n3ct)))  
    print("Your answer is = " + str(res3c) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
  elif ans1 == (opt[3]):
   print("Given what data?")
   print("(a)accelaration, initial velocity and final velocity\n(b)displacement, initial velocity and final velocity")   
   opt4 = ["a","b"]
   ans2 = input("Enter your answer: ")
   if ans2 == (opt4[0]):
    n4aa = input("Enter your value for accelaration: ")
    n4au = input("Enter your value for initial velocity: ")
    n4av = input("Enter your value for final velocity: ")
    res4a = (float(n4av) - float(n4au))/float(n4aa)
    print("Your answer is = " + str(res4a) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt4[1]):
    n4bs = input("Enter your value for displacement: ")
    n4bu = input("Enter your value for initial velocity: ")
    n4bv = input("Enter your value for final velocity: ")   
    res4b = (((float(n4bv) + float(n4bu))/(float(n4bs) * 2))**-1)
    print("Your answer is = " + str(res4b) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
  elif ans1 == (opt[4]):
   print("Given what data?")
   print("(a)time, initial velocity and final velocity\n(b)final velocity, initial velocity and acceleration\n(c)initial velocity, time and accelaration") 
   opt5 = ["a","b","c"]
   ans2 = input("Enter your answer: ")
   if ans2 == (opt5[0]):
    n5at = input("Enter your value for time: ")
    n5au = input("Enter your value for initial velocity: ")
    n5av = input("Enter your value for final velocity: ")
    res5a = (((float(n5au) + float(n5av)) * float(n5at))/2) 
    print("Your answer is = " + str(res5a) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt5[1]):
    n5bv = input("Enter your value for final velocity: ")
    n5bu = input("Enter your value for initial velocity: ")
    n5ba = input("Enter your value for accelaration: ")
    res5b = ((float(n5bv)**2 - float(n5bu)**2)/(float(n5ba) * 2)) 
    print("Your answer is = " + str(res5b) ) 
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
   elif ans2 == (opt5[2]):
    n5cu = input("Enter your value for initial velocity: ")
    n5ct = input("Enter your value for time: ")
    n5ca = input("Enter your value for accelaration: ")
    res5c = (float(n5cu) * float(n5ct)) + (float(n5ca) * (float(n5ct) ** 2)/2) 
    print("Your answer is = " + str(res5c) )
    print()
    print("Do you want to go back to menu?")
    rez = input("Enter your answer[y/n]: ")
    if rez == ("n"):
     print("Goodbye " + str(name))
     print("Program closed")
     x = x + 1
 elif ans == "n":
  print("Goodbye " + str(name))
  print("program closed")
  x = x + 1
#First time i've ever used a comment, ahhhh, feels good, i just wanted to make the lines of code even, Thank you for reading also Thankyou KC.