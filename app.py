from flask import Flask
from flask import Flask, render_template
import pandas
import random

app = Flask(__name__)
path = "./wordFiles/"

def get_word(type = 'noun'):
    """Get a random word of the requested type
    
    Keyword Arguments:
        type {string} -- The part of speech you want to return. Options = word, noun, adverb, adjective, animal, special, verb, prepostion, special
    
    Returns:
        [string] -- word of the requested type
    """

    words = pandas.read_csv(path+type+'.csv',header=0)
    wordCount = words.count(0).values[0]
    word = words.iloc[random.randint(0,wordCount-1)].values[0]

    return word

@app.route("/")
def main():
    adverb = get_word(type='adverb')
    adjective = get_word(type='adjective')
    animal = get_word(type='animal')
    number = random.randint(0,9)
    special = get_word(type='special')
    password = adverb + adjective + animal + str(number) + special

    return render_template(
        'index.html', **locals()
        )

@app.route('/words/')
def nouns():
    i = 1
    password = ''
    while i < 5:
        password = password + get_word(type='word').capitalize()
        i += 1
    
    return render_template(
        'index.html', **locals()
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)