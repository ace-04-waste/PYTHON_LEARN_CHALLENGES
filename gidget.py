dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie', 'staffy', 'shitsu']
dog_breed_I_want = input("What dog do you want: ")
#created a list and a variable

for dog in dog_breeds_available_for_adoption:
   
  #print each element
    if dog == dog_breed_I_want:
      #if element equals dog variable print statement
    print("They have the dog I want!")
    #as we have found element we break out of loop
    else:
        print("get me the dog I want fatty")