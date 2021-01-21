#=================================================================

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
#created a list and a variable

for dog in dog_breeds_available_for_adoption:
    #created a FOR loop that looks at each element
  print(dog)
  #print each element
  if dog == dog_breed_I_want:
      #if element equals dog variable print statement
    print("They have the dog I want!")
    #as we have found element we break out of loop
    break


#=================================================================]
#so i want to create a new class of 6 called students_in_poetry
#if class is under 6 i pop one out of all students into my poetry class
#after popping the end one off i append them into poetry until the class is full (6)
#then i printed my new class poetry list note Loki was first member

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)


#=================================================================

#nested loops

#here is have a lists within a list and a var that is set as 0

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
#first loop looks at three lists we call locations within the big list then print that data
for location in sales_data:
  
    print(location)
    #we looked within the inner list at each element 
    for sales in location:
        #and for each element inside the inner lists we add that element to scoops_sold.
      scoops_sold += sales
      #note that += adds to the last var value and keeps a running total
print(scoops_sold)
#finally i printed the running total which was 96

#================================================================

#List comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
#check each element within the list to see if it is greater than 161
#if it is assign into new list can_ride_coaster
#print new list
# i read this as "for each element within the list if a condtion is met put into new list"

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#we can modify the new list elements
my_upvotes = [192, 34, 22, 175, 75, 101, 97]
#to add 100 to each one by taking each element in upvotes and giving it a var called votes. 
#then i add 100 to the new var and append that new var to new list
updated_values = [votes + 100 for votes in my_upvotes]

#example of a list comprehension
celsius = [0, 10, 15, 32, -5, 27, 3]

# I take each element from celsius
# assign to new var called temp
#perfom some maths on new temp
#rest is telling computer where to find temp 
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)


#created a list ranging from 0 to 9 inclusive
single_digits = list(range(0,10))
#created a new list called square
squares =[]

#created a for loop
for digit in single_digits:
  #created a var to store each element raised to the power 2
  numnber_to_append = digit**2
  #added that result to new list called squares
  squares.append(numnber_to_append)
#printed squares to give [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
#created new list comprehension from original list single_digits
#reads as new list cubes contains an element from single_digits list raised to the power 3 
cubes = [num**3 for num in single_digits]
#print cubes to give [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(cubes)

#popped end off and printed value of pop then printed what was left
cubes_sort = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
print(cubes_sort.pop())
print(cubes_sort)

#================================================================================

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price

average_price = total_price/len(prices)

print("Average Haircut price: ", average_price)

new_prices = [price -5 for price in prices]

print(new_prices)
#set new variable new_prices to 0
#
total_revenue = 0

#create a for loop based on the index range of the length of list.
#any list will do as they are all same length (len)
for i in range(len(hairstyles)):
  #iterate through prices and last_week revs and add the corresponding elements together, then add that and tot up total revenue 
  total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + "$" + str(total_revenue))

average_daily_revenue = total_revenue/7

print("$" + str(average_daily_revenue))

##note what is below can be put into 1 line. 
cuts_under_30 =[
  #expression// further down in loop we get rid of [i] < 30
  hairstyles[i]

  #for statement//create index based on length of any list
  for i in range(len(hairstyles))

  #conditional//get rid of any prices >$30
  if new_prices[i] < 30
  
]
#this creates a new list of all cuts that costs less then $30
print(cuts_under_30)
  
#==========================================================================

#notes on modulus
#it is not /2 it is modulus 2. So 2 % 2 has a remainder of 0 so it breaks at 2
numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)







