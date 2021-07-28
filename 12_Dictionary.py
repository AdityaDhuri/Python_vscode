# Create and Print a Dictionary

a = {
    "Fast": "Quick Silver",
    "Thor": "Lightning",
    "RDJ": "Iron Man"
}
print(a['Thor'])

#Create nested dictionary ( A dictionary inside dictionary)

a = {
    "Fast": "Quick Silver",
    "Thor": "Lightning",
    "RDJ": [1, 2, 3],
    "b": {
        "Hulk": "Bruce",
        "Tom": "jerry" 
        }
}
a['Thor'] = "Groot" #values can be changed
print(a['Thor'])
a['b']['Tom'] = [1, 2] #whant to change in inside dictionary put the second dictionary name also
print(a['b']['Tom']) 