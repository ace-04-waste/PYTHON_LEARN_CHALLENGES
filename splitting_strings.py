authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

#we can pass our .split() an argument to split at certain chars
fave = "plumpudding"
print(fave.split("m"))

author_names = authors.split(",")
print (author_names)

#create a new empty list
author_last_names = []
#create a for loop to look at each element which is a whole name
for name in author_names:
  #split each whole name into two and return the end value which is surname. append to new list
  author_last_names.append(name.split()[-1])
print(author_last_names)

##############################################################################
#SPLITTING STRINGS 3
# we can split strings using using escape sequences
#basically we tell computer that we want to split by something other than a char
#two types:
#1. \n Newline - split by each new line(end of line)
#2. \t Horizontal Tab - split by tabs
#usesul as lots of datasets have tab and space break formats

#example
smooth_chorus =  \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_line = smooth_chorus.split('\n')
print(chorus_line)

###################################################################
#JOINING STRINGS
#we can split strings and put them back together again using .join()
#again we can pass a delimiter
#'delimiter'.join(list_you_want_to_join)
#so the argument has become the list

#example join our list with the delimiter ' ' aka space to give a sentence
my_words = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_words))
#note what happens if we don't have a space below
my_words = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(''.join(my_words))

#example 2
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = (' '.join(reapers_line_one_words))
print(reapers_line_one)

##########################################################################
#JOINING STRINGS 2
#we can use an string as the delimiter to join with other strings such as commas 
#so we can join csv files as these are comma seperated
songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
songs_csv = ','.join(songs)
print(songs_csv)

#example 2
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full  = '\n'.join(winter_trees_lines)
print(winter_trees_full)

##################################################################################
#stripping strings
#useful for cleaning data of whitespace, tabs and linebreaks
#.strip() will take out whitespace from begining and end of a string
#syntax is var.strip()
#example
featuring = "          paul is great coder                    "
print(featuring.strip())
#note the result has all the whitespace at the ends removed but keeps the space in the middle

#we can use strip with an argument such as .strip('!') but it only strips the ! char
featuring = "!!!paul is a great coder                         !!!"
print(featuring.strip('!'))

#example using strip and join
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
#create a new empty list
love_maybe_lines_stripped = []
#for each value in the list
for line in love_maybe_lines:
  #read and write this backwards// strip each line of white space. then add it to new empty list
  love_maybe_lines_stripped.append(line.strip())
  #we now have rid of all white space
  #repeat again with new list but join back together at newlines
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

#####################################################
#REPLACE
#Takes two arguments and replaces all instances of first argument with second

# syntax // var.replace(replaced_string, with_this_string)

with_spaces = "You got the kind of loving that can be so smooth"
#here we can replace spaces with underscores
with_underscores = with_spaces.replace(' ','_')
print(with_underscores)

#in this example there is a spelling mistake and we can use .replace to fix it
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer','Toomer')
print(toomer_bio_fixed)

#######################################################################
