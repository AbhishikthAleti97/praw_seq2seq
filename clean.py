def clean(data):
    data = data.replace("shitting","kidding") #add more filters here
    #take in a dictionary, the next time with a key and a value when using OOPS.
    return data



data = open("data","r")
for line in data:
    x = open("cleaned_data","a")
    x.write(clean(line))
    x.close()
