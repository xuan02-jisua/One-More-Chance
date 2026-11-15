# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stressed Student")
define pov = Character("[povname]")

default loop_count = 0
default student_route = False

transform half_size:
    zoom 0.7

#init python:
    #style.default.font = "CheeseFoamOolongSong-Bold.ttf"
    #style.default.language = "eastasian"

label start:
    scene heaven at truecenter with fade:
        zoom 3.5
    "Welcome, Angel. "

    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Angel"
    pov "I'm [povname]."

    "[povname], you are now assigned with a new mission. "
    "Sadly, as of just now, a poor soul chose to end his life at the brink of despair . "
    "His life is full of struggles, obstacles and sadness."
    "I hereby assign you to guide him towards hope."

    pov "But how? "

    "You will have to discover for yourself."
    "But remember, not every choice leads to a happy ending......"
    "If you fail, time will rewind and you will be stucked in a time loop. "
    "You will remember everything, even when the world forgets. "
    "Good luck. "

    pov "Okay, I will do my best!"

    jump mission

label mission: 
    scene time loop at truecenter with fade:
        zoom 3.5
    show press:
        zoom 0.85
        xanchor 0.5
        yanchor 0.5
        xpos 0.63
        ypos 0.7
    call screen startmission
    centered "MISSION START"
    jump student

screen startmission:
        imagebutton:
            at half_size
            xanchor 0.5
            yanchor 0.5
            xpos 0.4
            ypos 0.3
            idle "startlogo.png"
            action Jump("student")


label timeloop:
    scene time loop at truecenter with fade:
        zoom 3.5
    $ loop_count += 1
    "TIME LOOP [loop_count]"
    show die happily at truecenter
    "Ohno, I have failed my task....."
    "But it's okay, I have learned from my mistake. "
    "I am ready to start over again. "
    jump mission

label student:
    scene classroom at truecenter with fade:
        zoom 3.5
    
    "In the classroom"
    "The school bell rings for the third time. "
    "Class has dismissed an hour ago. "
    show angry at truecenter
    "A student sits alone looking at the table. "
    "His examination papers are scattered all over the table. "
    "He stares at the marks disappointedly as his eyes slowly watered. "
    s "I am so sick of trying."
    s "I will never pass my exams no matter how hard I try."
    s "HOW AM I GOING TO SIT FOR THE SPM? "

    pov "Ohno, I should help him. "
    pov "What should I say? "
    menu: 
        "Hey, why are you not going back home! ":
            s "Mind your own business!"
            hide angry
            show girl despair at truecenter
            "The student runs out of the classroom. "
            "As you follow him, you see him running towards the third floor corridor."
            "Before you could pull him, he jumps off the third floor. "
            jump ending

        "Hey, let's take a deep breath. ":
            s "Who are you? "
            menu: 
                "It's not important. ":
                    s "I don't talk to strangers. "
                    hide angry
                    show girl despair at truecenter
                    "The student leaves the classroom hastily. "
                    "The next day, a distressed news of a student commiting suicide is broadcasted online. "
                    jump ending

                "I am an angel and I am here to help you. ":
                    s "I am a failure. I can't live like this. "
                    s "My parents will be so disappointed in me."
                    pov "Hey, relax. I know you have done your best. "
                    s "How do you know? "
                    pov "Judging by how you are so concerned about your results, "
                    pov "I trust that you must have put a lot of effort. "
                    s "Finally, someone that understands me! "
                    s "What should I do? "

                    menu: 
                        "Consult your teacher. ":
                            s "My teachers don't believe in me. "
                            s "Now you're calling me to find the ones that questioned me at the start? "
                            hide angry
                            show cry at truecenter
                            "The student leaves the classroom hastily. "
                            "The next day, a distressed news of a student commiting suicide is broadcasted online. "
                            jump ending

                        "Discuss with your parents. ":
                            hide angry
                            show cry at truecenter
                            "The student leaves the classroom feeling discouraged. "
                            "When his parents finds out about his results, he is punished badly. "
                            "The next day, a distressed news of a student commiting suicide is broadcasted online. "
                            jump ending 

                        "Change your study method. ":
                            s "But how? "
                            menu: 
                                "Find someone you trust to ask for advice. ":
                                    pov "They will surely be glad to help you. "
                                    hide angry
                                    show hopeful at truecenter
                                    s "I'll try. "
                                    $ student_route = True
                                    jump ending

                                "Find your classmates to ask for advice. ":
                                    s "The student leaves the classroom."
                                    hide angry
                                    show cry at truecenter
                                    "The next day, the student is laughed by his classmates. "
                                    "Out of shame, he jumps off the window of the classroom. "
                                    jump ending

        "Have you studied before the exam? ":
            s "Why is everyone questioning me?"
            hide angry
            show girl despair at truecenter
            "The student runs out of the classroom. "
            "As you follow him, you see him running towards the third floor corridor."
            "Before you could pull him, he jumps off the third floor. "
            
            jump ending


label ending:
    if student_route == True:
        jump happy_ending
        
    else: 
        jump bad_ending

label happy_ending:
    scene good ending at truecenter with fade:
        zoom 3.5
    show correct at truecenter
    "Congrats! "
    "Mission accomplished. "
    hide correct
    show happy at truecenter
    "HAPPY ENDING"
    return

label bad_ending:
    scene black
    show wrong at truecenter
    "BAD ENDING"
    jump timeloop

return
