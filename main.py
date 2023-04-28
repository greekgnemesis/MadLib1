import random

def madlib1():
    prompts = [
        "Type a Number: ",
        "Type a Measure of time: ",
        "Type a Mode of Transportation: ",
        "Type  Adjective: ",
        "Type  Adjective2: ",
        "Type a noun: ",
        "Type a color: ",
        "Type a part of the body: ",
        "Type a Verb: ",
        "Type a Number: ",
        "Type a Noun: ",
        "Type a Noun: ",
        "Type a Part of the body: ",
        "Type a verb: ",
        "Type a Noun: ",
        "Type  Adjective: ",
        "Type a Silly word: ",
        "Type a Noun: ",
    ]
    answers = []
    for prompt in prompts:
        answers.append(input(prompt))
    print(f''' 
           It was about {answers[0]} {answers[1]} ago when i arrived at the hospital in a {answers[2]}.
           The hospital is a/an {answers[3]} place, there are a lot of {answers[4]} {answers[5]} here. There are nurses here
           who have {answers[6]} {answers[7]}. If someone wants to come into my room i told them that they have to 
           {answers[8]} first. I've decorated my room with {answers[9]} {answers[10]}. Today i talked to a doctor and they were 
           wearing a {answers[11]} on their {answers[12]}. I heard that all doctors {answers[13]} {answers[14]} every day for 
           breakfast. The most {answers[15]} thing about being in the hospital is the {answers[16]} {answers[17]}! ''')

def madlib2():
    prompts = [
        "Type a proper noun: ",
        "Type a person name: ",
        "Type a Noun: ",
        "Type   adjective (feeling): ",
        "Type a verb: ",
        "Type   adjective (feeling): ",
        "Type a Animal: ",
        "Type a verb: ",
        "Type a color: ",
        "Type a verb ending in ing: ",
        "Type Adverb ending in ly: ",
        "Type a Number: ",
        "Type a measure of time: ",
        "Type a color: ",
        "Type a Animal: ",
        "Type a number: ",
        "Type a silly word: ",
        "Type a noun: ",
    ]
    answers =[]
    for prompt in prompts:
        answers.append(input(prompt))

    print(f'''
          This weekend i am going camping with {answers[0]} {answers[1]}. I packed my lantern, sleeping bag,
          and {answers[2]}. I am so {answers[3]} to {answers[4]} in a tent. I am {answers[5]} we might see a(n)
          {answers[6]}. I hear they they're kind of dangerous. While we're camping, we are going to hike, fish, and {answers[7]}.
          I have heard that the {answers[8]} lake is great for {answers[9]}. Then we will {answers[10]} hike trough the forest
          for {answers[11]} {answers[12]}. If i see a {answers[13]} {answers[14]} while hiking, i am going to bring it home as a 
          pet! At night we will tell {answers[15]} {answers[16]} stories and roast {answers[17]} around the campfire}! ''')


def madlib3():
    prompts = [
        "Type a proper noun: ",
        "Type a person name: ",
        "Type Adjective: ",
        "Type a color: ",
        "Type animal: ",
        "Type a place: ",
        "Type Adjective: ",
        "Type  magical creature plural:  ",
        "Type Adjective: ",
        "Type magical creature plural: ",
        "Type a room in a House: ",
        "Type a noun: ",
        "Type a noun: :,
        "Type a Noun plural: ",
        "Type Adjective: ",
        "Type a Noun plural: ",
        "Type a Number: ",
        "Type a Measure of time: ",
        "Type a verb ending in ing: ",
        "Type Adjective: ",
        "Type a Noun: ",

    print(f''' 
          Dear {answers[0]} {answers[1]}. I am writing to you from a {answers[2]} castle in an enchanted forest.
          I found myself here one day after going for a ride on a {answers[3]} {answers[4]} in {answers[5]}. There are {answers[6]}
          {answers[7]} and {answers[8]} {answers[9]} here! In the {answers[10]} there is 
          a pool full of {answers[11]}. I fall asleep each night on a {answers[12]} of {answers[13]} and dream of {answers[14]} 
          {answers[15]}. It feels as though i have lived here for {answers[16]} {answers[17]}. I hope one day you can 
          visit, although the only way to get here now is {answers[18]} on a {answers[19]} {answers[20]}!! ''')


result = random.choice([madlib1, madlib2, madlib3()])
result()
