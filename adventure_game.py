import time
import random

dest1 = ()
term = ()
replay = ()


def print_pause(string, time_sleep):
    print(string)
    time.sleep(time_sleep)


def replay_q():
    replay = input("Would you like to play again?\n\n")
    if "yes" in replay:
        primary_plot()
    elif "no" in replay:
        print_pause("Thanks for playing,\n\n", 10)
    else:
        print("Sorry, Try again...\n\n")
        replay_q()


def primary_plot():
    print_pause("You’re a telecommunications technician "
                "and you are arriving at "
                "a customers home for an install.\n", 1)
    print_pause("You are in a bad part of town and"
                "you have not been able to "
                "reach the customer over the phone.\n", 1)
    print_pause("It is late and the sun is going down.\n", 2)
    print_pause("You look at your notes and you see"
                " the serving terminal is two"
                " houses away in the back yards of the neighbors.\n", 2)
    print_pause("You grab your meter and your iPad."
                " You can go to the terminal "
                "first and get it over with, or you can go to"
                " the customers door and greet them. \n", 1)
    primary_question()


def customer1():
    print_pause("You walk to the front door and knock. \n", 3)
    print_pause("The customer takes a very long time"
                " to come to the door. \n", 4)
    print_pause("When they get to the door you hear"
                " them unlock about 6 different locks "
                "on the door before the door slowly creeks "
                "open and you catch your first glimpse "
                "of the customer.\n", 4)
    print_pause("They ask you what you want\n", 3)
    print_pause("You tell them you’re there for an "
                "installation and that you tried to "
                "reach them over the phone but they didn’t "
                "answer.\n", 4)
    print_pause("The person at the door tells you "
                "they didn’t order anything and demand "
                "you leave at once. \n", 4)
    print_pause("The neighbor comes outside and "
                "begins to accuse you of wiretapping on "
                "behalf of the government. \n", 3)
    print_pause("You swiftly get into your vehicle "
                "and leave without incident. \n", 4)
    print_pause("You get to go home to your family "
                "tonight and start over tomorrow. \n", 4)
    replay_q()


def customer2():
    print_pause("You walk to the front door and "
                "knock. \n", 3)
    print_pause("The customer takes a very long "
                "time to come to the door. \n", 4)
    print_pause("When they get to the door you "
                "hear them unlock about 6 different locks on "
                "the door before the door slowly creeks "
                "open and you catch your first "
                "glimpse of the customer.\n", 4)
    print_pause("They ask you what you want\n", 3)
    print_pause("You tell them you’re there for "
                "an installation and that you tried to reach "
                "them over the phone but they didn’t "
                "answer.\n", 4)
    print_pause("They apologize and tell you "
                "that their phone was dead. \n", 3)
    print_pause("They invite you in but you "
                "decline and tell them you’re going "
                "to begin your "
                "outside work\n", 4)
    print_pause("You go back to the van and gather "
                "your supplies so you can go to the terminal\n", 4)
    terminal()


def primary_question():
    print_pause("1. Terminal\n", 0)
    print_pause("2. Greet the customer\n", 2)
    dest1 = input("Where do you want to go first? "
                  "Please chose only 1 or 2: \n")

    customerpick = ("1", "2")
    cstselection = ()
    if "1" in dest1:
        terminal()
    elif "2" in dest1:
        cstselection = random.choice(customerpick)
        if "1" in cstselection:
            customer1()
        else:
            customer2()
    else:
        print("Sorry, Try again...\n\n")
        primary_question()


def terminal():
    print_pause("You make a quick mental note of "
                "all what you need to bring with you to the terminal "
                ", you decide to bring the meter, iPad, "
                "and your jumper wire.\n", 2)
    print_pause("You will have to jump a fence "
                "at night\n", 1)
    print_pause("You can take\n", 0)
    print("1. Flashlight, Dog Spray, Safety Vest")
    print("2. Flashlight, Hard Hat, Ladder")
    term = input("What else do you chose to bring "
                 "with you? Please only select 1 or 2.")
    if "1" in term:
        terminal_1()
    elif "2" in term:
        terminal_2()
    else:
        print("Sorry, Try again...\n\n")
        terminal()


def terminal_1():
    print_pause("You gather your supplies and you "
                "walk over to the neighbors house where the terminal "
                "is located,\n", 3)
    print_pause("You decide not to knock on the door "
                "because it appears no one is home.\n", 3)
    print_pause("You look over their fence to find the "
                "serving terminal. You spot it in a far corner "
                "of the lot, surrounded by trash and rotting "
                "wood.\n", 3)
    print_pause("You scan for evidence of a dog and you "
                "spot a food and water bowl. You also notice a "
                "dog chain. You don’t see a dog. You rattle the "
                "fence hoping to see if a dog comes out but "
                "nothing happens. \n", 4)
    print_pause("You jump the fence.\n\n", 1)
    print_pause("Once your feet land on the ground you "
                "immediately grab your dog spray from your belt "
                "and make your way swiftly to the serving terminal. \n", 3)
    print_pause("You are wearing your reflective vest so "
                "its obvious that you’re a communications "
                "worker performing some work.\n", 3)
    print_pause("The homeowner who you didn’t know was "
                "home emerges from a dark room. They begin "
                "yelling obscenities to you and demand that you "
                "exit the property at once.\n\n", 3)
    print_pause("The release a large and very vicious "
                "dog who sprints toward you like you were a "
                "large delicious steak. \n", 3)
    print_pause("The dog leaps into the air as he lunges "
                "for your throat but you remember you’re "
                "armed with dog spray.\n", 3)
    print_pause("You spray the dog in the eyes and in "
                "his throat.\n", 2)
    print_pause("The dog falls to the ground whimpering-\n", 2)
    print_pause("You’ve eliminated that threat.\n\n", 2)
    print_pause("Now the homeowner runs toward you and "
                "appears to have a large firearm in "
                "their hand. \n", 2)
    print_pause("They get within six feet of you and "
                "raise a shiny 1911 to your face, you "
                "see down the barrel and notice there isn’t "
                "a round chambered. \n", 5)
    print_pause("The homeowner pulls the trigger and "
                "you hear an audible click but nothing "
                "happens.\n", 4)
    print_pause("Dismayed, the homeowner inspects "
                "their weapon. \n", 4)
    print_pause("You deploy your dog spray into "
                "the eyes of the homeowner and you flee for "
                "your van.\n\n", 3)
    print_pause("You jump the fence and swiftly "
                "get into your vehicle and leave without "
                "incident. "
                "You get to go home to your family tonight "
                "and start over tomorrow.  \n\n", 3)
    print_pause("Dispatch calls you and asks if "
                "you'll be able to get to another install that "
                "is on your list. You tell them to shove "
                "the job where the sun doesn't shine. "
                "You hang up and drive home.", 3)
    replay_q()


def terminal_2():
    print_pause("You gather your supplies and you "
                "walk over to the neighbors house where "
                "the terminal is located, \n", 4)
    print_pause("You decide not to knock on the "
                "door because it appears no one is home.\n", 4)
    print_pause("You look over their fence to "
                "find the serving terminal. You spot it in "
                "a far corner of the lot, surrounded by "
                "trash and rotting wood. \n", 4)
    print_pause("You scan for evidence of a dog "
                "and you spot a food and water bowl. "
                "You also notice a dog chain.\n", 4)
    print_pause("You don’t see a dog.\n", 4)
    print_pause("You rattle the fence hoping to "
                "see if a dog comes out but nothing happens.\n", 4)
    print_pause("You prop your ladder up on the "
                "fence, climb over then jump to the ground. \n", 4)
    print_pause("As soon as your feet hit the "
                "ground you hear the sound of a sliding "
                "glass door on the patio of the home. \n", 4)
    print_pause("You begin to panic and you try "
                "to get back over the fence because "
                "you just noticed that there is a large "
                "and seemingly very aggressive dog "
                "in pursuit of you.\n", 4)
    print_pause("You hear a southern scratchy "
                "voice yell out “get ‘em killer!” \n", 4)
    print_pause("You’re positive that you just "
                "defecated yourself but you have bigger "
                "issues to worry about right now. \n", 4)
    print_pause("You attempt to grab the ladder "
                "from over the fence with all of your "
                "strength but it is too late. \n", 4)
    print_pause("‘Killer’ just grabbed onto your "
                "boot and is about to live up to his name\n", 4)
    print_pause("You grab your hardhat off of your "
                "head and throw it at the dog but "
                "that only angers him more.\n", 4)
    print_pause("He leaps up and chomps down on "
                "your upper back,\n", 4)
    print_pause("the owner comes outside with a "
                "glass of iced tea and grabs a seat "
                "in a lawn chair. \n", 4)
    print_pause("The dog starts to pull you back "
                "into the yard and now has you on "
                "the ground.\n", 4)
    print_pause("You yell out for help but it "
                "is too late. \n", 4)
    print_pause("The dog grabs your neck between "
                "his large and very powerful jaws "
                ", you’re dead.\n", 4)
    print_pause("Later in the next few months "
                "the dog is put down, the homeowner is "
                "arrested but charges are dropped because "
                "you didn't identify yourself as "
                "a telecommunications employee. They "
                "were within their rights to defend "
                "their property.\n", 4)
    print_pause("The Telephone company declines "
                "to pay your family your death benefit "
                "because you didn't have your dog spray "
                "per company policy, and you weren't "
                "wearing your vest while in a utility "
                "easement. \n", 4)
    replay_q()


primary_plot()
