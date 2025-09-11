
# I B H W S S
#I PROJECT IDEA
#B BUILDING
#H HOW PROGRAMMING WORK
# W CONCEPT
#S  sODO CODE
#S starting



#FAKE NEWS HEADLINE GENERATOR
#EXAMPLE "shah_ruk khan SPOTTED RIDING A BUFFALO NEAR INDIA GATE"
#WHAT BUILD = FAKE AND FUNNY  LIST OF WORDS
#HOW
#SUBJECTS(WHO,WHAT)
#ACTIONS(DECLARE WAR)
#PLACES OR OBJECTS = WHERE, WHAT

# i am going to start the new project and its name is fake news
#import the random mobile
import random

Subjects=[
    " khan",
    "sal_man khan",
    "A mumbai cat",
    "auto_ricksha from delhi",
    "mumbai"
]

Actions=[
    "going to delhi ",
    "cancel the service",
    "orders",
    "celebrations",
    "dances with.....",
    "playing games "
]

places_or_objects=[
    " masjid in delhi",
    "red fort ",
    "lotus temple",
    "zoo in delhi",
    "metro station",
    "india gate"
]

# #start the headline generator

while True:
    subjects = random.choice(Subjects)
    actions = random.choice(Actions)
    places_or_objects = random.choice(places_or_objects)
    

    headline =f"BREAKING NEWS{Subjects} {Actions} {places_or_objects} "
    print(headline)
    

    user_input = input ( "DO YOU WANT ANOTHER HEADLINE (YES/NO).script()")

    if user_input =="no":
    

        print("thanks for using the fake news headline generator")
        print("have a good day byy")
        break






















