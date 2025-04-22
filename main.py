str = input ("Please enter a string and then give a character to search for:")
char = input ("Please enter a character to search for:")
count = 0 
i = 0
while (i < len(str)):
   if (str[i] == char):
       count = count + 1
   i = i + 1

print ("The character ", char, " appears ", count, " times in the word", str)