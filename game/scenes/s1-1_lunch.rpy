label s1_1:
    "[Scene 1.1: Lunch]"
    jump .intro

label .intro:
    scene bg woman_apartment
    show woman casual
    # play music routine
    "(Woman wants to have lunch in her apartment, but notices her chair is broken.)"
    menu repair_chair:
        "(repair the chair properly?)"
        "Yes":
            jump repair_chair_properly
        "No, hack around":
            jump repair_chair_hack

label repair_chair_properly:
    "(Woman searches a screwdriver, but finds none)"
    jump s1_2b

label repair_chair_hack:
    "(Woman uses a glue gun to keep the screw stuck into the chair)"
    jump s1_2a
