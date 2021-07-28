a = {
    "Fast": "Quick Silver",
    "Thor": "Lightning",
    "RDJ": [1, 2, 3],
    "b": {
        "Hulk": "Bruce",
        "Tom": "jerry" 
        }
}

#print keys and (type is dict_keys) convert to list and print values also item
print(a.keys())
print(list(a.keys()))
print(a.values()) #prints keys of dictionary
print(a.items()) #prints keys and values (All)

#update dictionary
c = {
    "bana": "baby"
}
a.update(c)
a.update({"bana": "bocha"}) #updates the existing also
print(a.keys())
print(a)

#get function
print(a.get("Thor")) #shows the value of the key
print(a.get("Mango")) #does not show error it gives value none if print(a["Mango"]) gives error bcoz both shows keys but get does not give error
