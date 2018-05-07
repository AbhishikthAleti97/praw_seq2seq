def clean(data):
    data = data.replace("motherfucking","").replace("Fuck","Dang").replace("motherfucker","idiot")
    data = data.replace("cunt"," idiot").replace("bitch","stupid girl").replace("bitchy","bossy")
    data = data.replace("asshole","idiot").replace("shitting","kidding").replace("masturbation","sleep").replace("masturbating","sleeping").replace(" dick","n idiot").replace("dicks","idiots")
    data = data.replace("bitches "," sensitive little girls ").replace("bitch","pain").replace("slut"," bad company ")
    data = data.replace(" hoe","bad influence ").replace(" fucks ", " bonkers ").replace("fuck","shoot")
    return data



data = open("data","r")
for line in data:
    x = open("cleaned_data","a")
    x.write(clean(line))
    x.close()
