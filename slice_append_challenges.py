#Write your function here
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#below i appended the lenght of a list to the list
#Write your function here
#here is my thinking. I define fn and set parameter of lst to pass in
#then i say in this var, lst, append the length of the list
# then return the new list, lst 
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here
#here i wanted to add the sum of the last two lst items three times
#then return the updated lst
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Write your function here
#I wanted to create a fn that checks and compares length of list and returns an value

def larger_list(lst1, lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  if len(lst1) == len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]


#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5, 7], [-10, 2, 5, 10]))

#Write your function here
#i wanted to check if there are more items than n and return a boolean
def more_than_n(lst, item, n):
  #count number of items in lst
  is_item = lst.count(item)
  if is_item > n:
    return True
  else:
    return False


#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#I can combine lists, sort them and return the sorted list then
#call the function with two lists as below
#Write your function here#Write your function here
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sorted_list = sorted(unsorted)
  return sorted_list


print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


#Write a function that lists every 3rd number between start and 100
def every_three_nums(start):
  return list(range(start,100,3))

print(every_three_nums(91))

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  if lst.count(item1) < lst.count(item2):
    return item2
  if lst.count(item1) == lst.count(item2):
    return item1



#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#note that the parameters make more sense if you think about what you want to pass in as args

#finds an index and doubles it then adds the start and end of lst back on
def double_index(lst, index):
  if index >= len(lst):
    return lst

  else:
    new_lst = lst[0:index]
  new_lst.append(lst[index]*2)
  new_lst = new_lst + lst[index+1:]
  return new_lst


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))