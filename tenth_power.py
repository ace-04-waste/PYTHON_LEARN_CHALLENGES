# Write your tenth_power function here:
def tenth_power(num):
  return num **10

# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024
print(tenth_power(999))

#square root
# Write your square_root function here:
def square_root(num):
  return num**0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10
print(square_root(36))

#win percentage
# Write your win_percentage function here:
def win_percentage(wins, losses):
  return (wins/(wins + losses))*100

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
print("correct answer is "+ str(win_percentage(5,5)) + "%")

#average of two numbers
# Write your average function here:
def average(num1, num2):
  return (num1 + num2)/2

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


#Finding the remainder using % operator
# Write your remainder function here:
def remainder(num1,  num2):
  return (num1*2) % (num2/2)

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

#recall remainders are what is left after dividing

#calculating dog years
# Write your dog_years function here:
def dog_years(name, age):
  return name + ", you are " + str(age*7) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

#James Bond
# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " +  first_name + " " + last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Anya", "Doran"))
# should print Angelou, Maya Angelou

#calculate a tip
# Write your tip function here:
def tip(total, percentage):
  tip = (total*percentage)/100
  return tip
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

#first three multiples
# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num*3 

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# Write your lots_of_math function here:
def lots_of_math(a,b,c,d):
  first = a+b
  second = c-d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth
  
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0

#relational operators
x = 20
y = 20

# Write the first if statement here:

if x==y:
  print("These numbers are the same")

credits = 120

# Write the second if statement here:

if credits >= 120:
  print("You have enough credits to graduate!")

#grading system using ELIF//
def grade_converter(gpa):
  grade = "F"

  if gpa >= 4:
    grade = "A"

  elif gpa >= 3:
    grade = "B"
  elif gpa >= 2:
    grade = "C"
  elif gpa >= 1:
    grade = "D"
  elif gpa >= 0:
    grade = "F"
    
  return grade

"""
  #grading project 
  def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3 and ps_score >= 90 and ec_count >= 3:
    return("This applicant should be accepted.")
  
  elif gpa >= 3 and ps_score >= 90 and ec_count < 3:
    return("This applicant should be given an in-person interview.")

  else:
    return("This applicant should be rejected.") """

def first_plus_last(list):
    return list[0] + list[-1]

print(first_plus_last([1,2,3,4,5,6,7,4,8,9,]))