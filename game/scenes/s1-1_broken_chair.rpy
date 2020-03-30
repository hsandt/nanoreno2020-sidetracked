label s1_1:
    # hide dialogue box initially so it doesn't stick to the HUD
    # from here on, dialogue box will automatically disappear during pauses between dialogues
    window hide

label .shot1:
    show overlay black
    "They say I'm easily distracted."
    "That's not true."
    "I'm not jumping from topic to topic without reason. It's just that problems keep popping up in my face."
    pause 0.5

    "Like that one time."

label .shot2:
    scene bg apartment
    show mc casual regular left at character_right
    with Dissolve(1.0)
    play music apartment
    mc "This chair is not stable at all!"
    pause 0.5

    "I crouch and inspect the chair to see where the issue comes from."
    hide mc with dissolve
    play sound inspect_chair
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: inspect chair")
    pause 1.5
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show item screw_loose at item_left
    show mc casual regular left at character_right
    with dissolve
    mc "Looks like that screw is a bit loose."
    mc "Hex type, uh? Let’s see if I got a matching screwdriver."
    hide item
    hide mc with dissolve
    play sound searching_drawer
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: searching drawer")
    pause 4.0
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show mc casual regular left at character_right with dissolve
    mc "Nope. No such thing."
    mc "Guess I need to go to the DIY store to get one. Screwdriver or key."
    pause 0.5

    mc "I should take a measurement of the screw hole before I leave."

    menu:
        "Take a photo of the screw with a scale reference":
            jump .shot3a
        "Measure screw with a meter and write result in notepad":
            jump .shot3b

label .shot3a:
    $ screw_measurement_method = "photo"

    "I draw my smartphone and take a picture of the screw. I put my finger on it as a scale reference."
    show item screw_loose at item_left
    play sound smartphone_camera
    pause 1.0
    hide item with dissolve
    "As I’m checking that the photo is good enough, I notice a few notifications on the phone."
    call sa_1

    "OK, I’d better hurry now and go to the store while it’s open."
    jump .shot4

label .shot3b:
    $ screw_measurement_method = "meter"

    "I grab a meter, measure the screw external diameter, internal diameter and write them on my notepad."
    mc "OK, let’s go!"
    jump .shot4

label .shot4:
    "The store is not too far, I should be back in no time."
    show overlay black with dissolve
    stop music fadeout 2.0
    pause 1.0
    play sound door_open_close
    pause 2.0
    jump s2_1
