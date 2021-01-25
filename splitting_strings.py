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
# .FIND( )
#this enables us to find index values for strings 
#With .find( ) we can pass in a string and check to see if that string is in the list and return the index position of that string

print('smooth'.find('t'))
#>>4

#we can use it to find starting index of longer strings
print('smooth'.find('oo'))
#>>2

#example
god_wills_it_line_one = "The very earth will disown you"

disown_placement= god_wills_it_line_one.find('disown')
print(disown_placement)
#note that to count the index vales we put a line behinf the 'T' and call that zero then 
#move forward counting the spaces also as index value

##########################################################################
#.format()
#define fn
def fave_song(song, artist, year):
  #return a string with 3 format placeholders. Reads as .format a string that has 3 arguments to insert into a string 
  return "My fave song is {} by {} in the year {}.".format(song, artist, year)
  #print result of calling fn with 3 arguments

print(fave_song("relax", "frankie", "1995"))

#example 2
#define fn
def poem_title_card(title, poet):
  #in this example I have used \ to include some "" otherwise it would not work
  return("The poem \"{}\" is written by {}.".format(title, poet))
print(poem_title_card("enigma", "pablo"))

#.format() continued...
#we can use keywords to avoid any confusion. More helpful and easier to read
def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
 #example// define fn with three parameter
def poem_description(publishing_date, author, title, original_work):
     #create var that holds string with some placeholders that formats with keywords
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  #return var poem_desc for further use
  return poem_desc
  #call function and pass in keyword values
my_beard_description = (poem_description(author = "Shel Silverstein",title = "My Beard",original_work = "Where the Sidewalk Ends",publishing_date = "1974"))
print(my_beard_description)  

#challenge
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

#create a new list from the string at the comma splits
highlighted_poems_list = highlighted_poems.split(",")

print(highlighted_poems_list)

#remove whitespace from new list by creating a for loop
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  #strip the whitespace from between each poem
  highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)

highlighted_poems_details = []
#we created a new list and then below added each poem element index value to make a list of lists
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.strip())
print(highlighted_poems_details)

#create three new lists to put in the title, poets and dates so that we can then create a new list of lists
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  #I can use index values within each element of highlighted_poems_details to split and append to the new lists
  #in the list are 3 values so I have 0,1,2
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
#for each index in range of highlighted_poems_details, pass each value into string
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))



###########################################################################################
#SUMMARY
#.upper(), .title(), and .lower() adjust the casing of your string.
#.split() takes a string and creates a list of substrings.
#.join() takes a list of strings and creates a string.
#.strip() cleans off whitespace, or other noise from the beginning and end of a string.
#.replace() replaces all instances of a character/string in a string with another character/string.
#.find() searches a string for a character/string and returns the index value that character/string is found at.
#.format() allows you to interpolate a string with va
#######################################################################
#SECTION CHALLENGE
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

#------------------------------------------------
# Start coding below!
#i can replace all the current transaction seperators with a new one so that i can work work with comma sep values
daily_sales_replaced = daily_sales.replace(";,;", "|")
#print(daily_sales_replaced)
#i now have all daily transactions divided by | so i can split into a new list below
daily_transactions = daily_sales_replaced.split(",")
#print(daily_transactions)

daily_transactions_split = []
#i can create a new list to store a list of each daily transaction
#Can do this by looping through each daily transaction sub list in overall daily transaction
for daily in daily_transactions:
  #then split at end of daily transactions . I marked with | char
  #note daily is individual strings within list
  #then append that to my new list
 daily_transactions_split.append(daily.split("|"))
#print(daily_transactions_split)

#create new list
transactions_clean = []
#wipe out white space using a loop and split() and append to new list
for transaction in daily_transactions_split:
  transaction_clean = []
  for data_point in transaction:
    transaction_clean.append(data_point.replace("\n","").strip(" "))
  transactions_clean.append(transaction_clean) 
#print(transactions_clean)

customers = []
sale = []
thread_sold = []

#now we have a clean list containing inner lists of [customer, sale, threadsold, date]
#we can itereate over these and append to seperate lists we just created

for x in transactions_clean:
  #we append to new list customers the values at index [0] from transaction_clean
  customers.append(x[0])
  sale.append(x[1])
  thread_sold.append(x[2])

#print(customers)
#print(sale)
#print(thread_sold)


total_sales = 0
#having started total_sales at zero, i can iterate through the total sales list and add each value to the sum of the previus
#basically keeping a running tally of sales as I iterate through. Also strip off the $ and set as a float rather than string value

for x in sale:
  total_sales +=  float(x.strip("$"))
print(total_sales)
 



  






