label s1_1:
    $ store.has_wifi = True
    $ store.currentTime = "17:00"
    $ store.wrapping_scene = "broken_chair"

label .shot1:
    show overlay black
    pause 1.0
    # the show/hide at the beginning of each scene is only to show textbox with quick dissolve
    # then hide it when no text is shown (without having to manually "window hide" every time)
    window show
    "They say I'm easily distracted."
    "That's not true."
    "I'm not jumping from topic to topic without reason. It's just that problems keep popping up in my face."
    window hide None # no transition except on scene start/end
    pause 0.5

    "Like that one time."

label .shot2:
    scene bg apartment
    show mc casual regular left at character_right
    with Dissolve(1.0)
    play music apartment
    # Call to start Lightbulb task so it shows up in the task tree
    $ StartTask(task_LightBulb)
    mc "This chair is not stable at all!"
    # Call to start Chair task
    $ StartTask(task_Chair)
    pause 0.5

    "I crouch and inspect the chair to see where the issue comes from."
    hide mc with dissolve
    play sound inspect_chair
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: inspect chair")
    pause 1.5
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show screen screen_item("screw_loose", "left")
    mc "..."
    show mc casual regular left at character_right
    with dissolve
    mc "Looks like that screw is a bit loose."
    mc "Hex type, uh? Let’s see if I got a matching screwdriver."
    $ StartTask(task_HexKeyApartment)

    hide screen screen_item
    hide mc with dissolve
    play sound searching_drawer
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: searching drawer")
    pause 4.0
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show mc casual regular left at character_right with dissolve
    mc "Nope. No such thing."
    $ FailTask(task_HexKeyApartment)

    mc "Guess I need to go to the DIY store to get one. Screwdriver or key."
    $ StartTask(task_HexKeyStore)

    pause 0.5

    mc "I should take a measurement of the screw hole before I leave."
    $ StartTask(task_ScrewSize)
    $ RevealTask(task_Store)
    $ RevealTask(task_FindHexKey)
    $ RevealTask(task_BuyHexKey)

    menu:
        "Take a photo of the screw with a scale reference":
            jump .shot3a
        "Measure screw with a meter and write result in notepad":
            jump .shot3b

label .shot3a:
    $ store.screw_measurement_method = "photo"
    $ StartTask(task_ScrewPhoto)

    "I draw my smartphone and take a picture of the screw. I put my finger on it as a scale reference."
    show screen screen_item("screw_loose", "left")
    play sound smartphone_camera
    pause 1.0
    hide screen screen_item with dissolve
    "As I’m checking that the photo is good enough, I notice a few notifications on the phone."
    call s_a from _call_s_a_2
    $ CompleteTask(task_ScrewPhoto)

    "OK, I’d better hurry now and go to the store while it’s open."
    jump .shot4

label .shot3b:
    $ store.screw_measurement_method = "meter"
    $ StartTask(task_ScrewMeter)

    "I grab a meter, measure the screw external diameter, internal diameter and write them on my notepad."
    $ CompleteTask(task_ScrewMeter)

    mc "OK, let’s go!"
    jump .shot4

label .shot4:
    $ CompleteTask(task_ScrewSize)
    
    $ StartTask(task_Store)
    $ RevealTask(task_FindHexKey)
    $ RevealTask(task_BuyHexKey)

    # the window show None / hide at the end of each scene is just to have a clean
    # textbox dissolve at the end
    window show None
    "The store is not too far, I should be back in no time."
    window hide
    $ quick_menu = False
    show overlay black with dissolve
    stop music fadeout 2.0
    pause 1.0
    play sound door_open_close
    pause 2.0

    # No Wi-Fi outside
    $ store.has_wifi = False
    $ quick_menu = True
    jump s2_1
