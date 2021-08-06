import pandas
import random

adverbs = pandas.read_csv('adverbs.csv',header=0)
adjectives = pandas.read_csv('adjectives.csv',header=0)
animals = pandas.read_csv('animals.csv',header=0)
specials = pandas.read_csv('special.csv',header=0)

adverbCount = adverbs.count(0).values[0]
adjectiveCount = adjectives.count(0).values[0]
animalCount = animals.count(0).values[0]
specialCount = specials.count(0).values[0]

selectAdverb = random.randint(0,adverbCount-1)
selectAdjective = random.randint(0,adjectiveCount-1)
selectAnimal = random.randint(0,animalCount-1)
selectSpecial = random.randint(0,specialCount-1)

adverb = adverbs.iloc[selectAdverb].values[0]
adjective = adjectives.iloc[selectAdjective].values[0]
animal = animals.iloc[selectAnimal].values[0]
number = random.randint(0,9)
special = specials.iloc[selectSpecial].values[0]

password = adverb + adjective + animal + str(number) + special

print(password)