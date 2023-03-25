import random


def madlib1():
    Number = input('Type a Number: ')
    Measure_of_time = input('Type a Measure of time: ')
    Mode_of_transportation = input('Type a Mode of Transportation: ')
    Adjective = input('Type  Adjective: ')
    Adjective2 = input('Type  Adjective2: ')
    noun = input('Type a noun: ')
    Color = input('Type a color: ')
    Part_of_the_body = input('Type a part of the body: ')
    verb = input('Type a Verb: ')
    Number2 = input('Type a Number: ')
    Noun2 = input('Type a Noun: ')
    Noun3 = input('Type a Noun: ')
    Part_of_the_body2 = input('Type a Part of the body: ')
    Verb = input('Type a verb: ')
    Noun4 = input('Type a Noun: ')
    Adjective3 = input('Type  Adjective: ')
    Silly_word = input('Type a Silly word: ')
    Noun = input('Type a Noun: ')

    print(f''' 
           It was about {Number} {Measure_of_time} ago when i arrived at the hospital in a {Mode_of_transportation}.
           The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {noun} here. There are nurses here
           who have {Color} {Part_of_the_body}. If someone wants to come into my room i told them that they have to 
           {verb} first. I've decorated my room with {Number2} {Noun2}. Today i talked to a doctor and they were 
           wearing a {Noun3} on their {Part_of_the_body2}. I heard that all doctors {Verb} {Noun4} every day for 
           breakfast. The most {Adjective3} thing about being in the hospital is the {Silly_word} {Noun}! ''')


def madlib2():
    Proper_Noun = input('Type a proper noun: ')
    Person_Name = input('Type a person name: ')
    Noun = input('Type a Noun: ')
    Adjective_feeling = input('Type  adjective (feeling): ')
    Verb = input('Type a verb: ')
    Adjective_feeling2 = input('Type adjective (feeling): ')
    animal = input('Type a Animal: ')
    Verb2 = input('Type a verb: ')
    color = input('Type a color: ')
    Verb_ing = input('Type a verb ending in ing: ')
    Adverb_ly = input('Type Adverb ending in ly: ')
    number = input('Type a Number: ')
    Measure_of_time = input('Type a measure of time: ')
    Color = input('Type a color: ')
    Animal = input('Type a Animal: ')
    Number = input('Type a number: ')
    Silly_word = input('Type a silly word: ')
    Noun2 = input('Type a noun: ')

    print(f'''
          This weekend i am going camping with {Proper_Noun} {Person_Name}. I packed my lantern, sleeping bag,
          and {Noun}. I am so {Adjective_feeling} to {Verb} in a tent. I am {Adjective_feeling2} we might see a(n)
          {animal}. I hear they they're kind of dangerous. While we're camping, we are going to hike, fish, and {Verb2}.
          I have heard that the {color} lake is great for {Verb_ing}. Then we will {Adverb_ly} hike trough the forest
          for {number} {Measure_of_time}. If i see a {Color} {Animal} while hiking, i am going to bring it home as a 
          pet! At night we will tell {Number} {Silly_word} stories and roast {Noun2} around the campfire!! ''')


def madlib3():
    Proper_Noun = input('Type a proper noun: ')
    Person_Name = input('Type a person name: ')
    Adjective = input('Type Adjective: ')
    Color = input('Type a color: ')
    Animal = input('Type animal: ')
    Place = input('Type a place: ')
    Adjective2 = input('Type Adjective: ')
    Magical_creature_plural = input('Type  magical creature plural:  ')
    Adjective3 = input('Type Adjective: ')
    Magical_creature_plural2 = input('Type magical creature plural: ')
    Room_in_a_house = input('Type a room in a House: ')
    Noun = input('Type a noun: ')
    Noun2 = input('Type a noun: ')
    Noun_plural3 = input('Type a Noun plural: ')
    Adjective4 = input('Type Adjective: ')
    Noun_plural4 = input('Type a Noun plural: ')
    Number = input('Type a Number: ')
    Measure_of_time = input('Type a Measure of time: ')
    Verb_ing = input('Type a verb ending in ing: ')
    Adjective5 = input('Type Adjective: ')
    Noun5 = input('Type a Noun: ')

    print(f''' 
          Dear {Proper_Noun} {Person_Name}. I am writing to you from a {Adjective} castle in an enchanted forest.
          I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. There are {Adjective2}
          {Magical_creature_plural} and {Adjective3} {Magical_creature_plural2} here! In the {Room_in_a_house} there is 
          a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun_plural3} and dream of {Adjective4} 
          {Noun_plural4}. It feels as though i have lived here for {Number} {Measure_of_time}. I hope one day you can 
          visit, although the only way to get here now is {Verb_ing} on a {Adjective5} {Noun5}!! ''')


result = random.choice([madlib1, madlib2, madlib3()])
result()
