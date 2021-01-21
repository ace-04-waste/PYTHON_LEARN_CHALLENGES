#DIVISIBLE BY TEN
#Write your function here
#create a var with parameter which is a list of numbers
def divisible_by_ten(nums):
  #create a count to keep track of how many numbers are divisible by ten and set at zero
  count = 0
  #create a for loop to see if each number in list is divisible using modulus
  for number in nums:
    if (number % 10 == 0):
  #if no remainder then its divisible by ten so add one to count using +=

      count += 1
  return count
  
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#================================================================

#GREETINGS

#defined var with names parameter to pass in
def add_greetings(names):
    #created an empty list to populate
    empty_list =[]
    #create for loop where for each names in  names list I add Hello
    for name in names:
        empty_list.append("Hello, " + name)
        #return empty list so when I call function i can print resulting new list aka empty_list
    return empty_list       

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#================================================================
#DELETE STARTING EVEN NUMBERS

#define function to remove all even numbers from start of lst
def delete_starting_evens(lst):
#Use while loop to check if list has at least one element and element is an even number
    while len(lst) > 0 and lst[0] % 2 ==0 :
#if both conditions are met then take that element off and repeat until we hit an odd number in the loop.      
      lst = lst[1:]
#return lst      
    return lst
      

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#================================================================
#ODD INDICES
#define a variable called odd_indices , so that we can pass in a list
def odd_indices(lst):
  new_list = []
  #so i want to start at an odd INDEX position and jump 2 each time so that I always hit an odd index position , 1/3/5 etc. The determing strp is the len of lst as we only want to iterate through lst
  for index in range(1,len(lst) ,2):
    #so for each index in the range above we now wish to add each element that has an odd index to the new_list
    new_list.append(lst[index])
    #then return new_list 
  return new_list


#call function and pass argumens aka list of numbers
print(odd_indices([4, 3, 7, 10, 11, -2]))

#==================================================================

