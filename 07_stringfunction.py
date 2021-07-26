# String Functions
story = "my name is Aditya Santosh Dhuri studying in BE EXTC is"

# 1) To Find Length
print(len("story")) # way1 this will only print the lenth of story 

print(len(story)) # way2 this will print the no of words inside story
print(story.capitalize())

# 2) Ends with
print(story.endswith("Dhuri"))
print(story.endswith("is"))
print(story.endswith("EXTC"))

# 3) Count
print(story.count('a'))

# 4) Capitalize
print(story.capitalize()) #Capitalize the first letter and decapitalize remaining

# 5) Find
print(story.find("is")) # it gives the position of that word that occured at the start if occured again does not count 
print(story.find("black")) # -1 is shown if the word is not present

# 6) Replace
print(story.replace("is", "Good")) # replaces all the old word with new word
