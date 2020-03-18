label s1_1:
    "[Scene 1.1: Broken Chair]"

label .shot1:
    show overlay black
    "They say I'm easily distracted."
    "That's not true."
    "I'm not jumping from topic to topic without reason. It's just that problems keep popping up in my face."
    pause 0.5

    "Like that one time."

label .shot2:
    scene bg apartment
    show mc casual regular left at right
    with Dissolve(1.0)
    mc "This chair is not stable at all!"
    pause 0.5

    "I crouch and inspect the chair to see where the issue comes from."
    # play sound inspect_chair
    pause 0.5

    # show item loose_screw
    mc "Looks like that screw is a bit loose."
    mc "Hex type, uh? Let’s see if I got a matching screwdriver."
    # hide item
    hide mc with dissolve
    # play sound rummage_drawer
    pause 1.0

    show mc casual regular left at right with dissolve
    mc "Nope. No such thing."
    mc "Guess I need to go to the DIY store."
    pause 0.5

    mc "I should take a measurement of the screw hole before I leave."

    menu:
        "Take a photo of the screw with a scale reference":
            jump .shot3a
        "Measure screw with a meter and write result in notepad":
            jump .shot3b

label .shot3a:
    "(MC takes photo of the screw, but notices she has no space left on the smartphone)"
    "(after a long series of sub-tasks, she gets back on track)"
    jump .shot4

label .shot3b:
    "(MC measures screw and write the diameter on a notepad)"
    jump .shot4

label .shot4:
    mc "OK, let’s go now."
    "The store is not too far, I should be back in no time."
    show overlay black with dissolve
    
    jump s3_4
