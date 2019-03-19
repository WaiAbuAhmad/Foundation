### Challenge: How many drinks do you need to buy to throw a great party? 
# you will have a list of your friends, and their favorite drink. 
# you will also know how many drinks of a certain type are drunk per hour
from collections import Counter

#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}


#types of drinks people drink, with lists of examples
cocktails = ['Gin and Tonic', 'Mate Vodka', 'Rum and Coke']

wines = ['Red Wine', 'White Wine']

liquors = ['whiskey', 'gin', 'vokda']

nonalcoholic = ['tea', 'water', 'orange juice']

# number of drinks per hour people drink, depeneding on the type. 
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}
num=[0,0,0,0]
party_duaration = 6
total_drinks = {}

for key, value in favorite_drinks.items():
    if value.lower() in list(map(lambda item:item.lower(), cocktails )) :
        num[0] +=number_of_drinks_per_hour_per_type["cocktails"]
        total_drinks.update({"cocktail":num[0]})
    elif value.lower() in list(map(lambda item:item.lower(), wines )) :
        num[1] +=number_of_drinks_per_hour_per_type["wines"]
        total_drinks.update({"wine":num[1]})
    elif value.lower() in list(map(lambda item:item.lower(), liquors )) :
        num[2] +=number_of_drinks_per_hour_per_type["liquors"]
        total_drinks.update({"liquors":num[2]})
    elif value.lower() in list(map(lambda item:item.lower(), nonalcoholic )) :
        num[3] +=number_of_drinks_per_hour_per_type["nonalcoholic"]
        total_drinks.update({"nonalcoholic":num[3]})
   
print("for {} hours party we need {} drinks".format(party_duaration,(sum(total_drinks.values)*party_duaration)))