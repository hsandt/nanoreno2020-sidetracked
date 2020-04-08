label s1_1:
    $ store.has_wifi = True
    $ store.currentTime = 13*60 + 57  # game starts at ~14h, then events will increment time
    $ store.wrapping_scene = "broken_chair"

    # Renpy needs to be told to stop Main Menu BGM (Title Theme)
    stop music fadeout 2.0

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
    scene bg apartment day
    show mc casual regular left at character_right
    with Dissolve(1.0)
    $ play_music("apartment")

    # Call to start HaveLunch task so it shows up in the task tree
    # Don't notify this one though; it's unnatural for MC to write that now!
    $ StartTask(task_HaveLunch)

    mc "Hmm... Nothing like the smell of roasted vegetables.{w} That are not burnt."

    show mc at character_right_sit_down
    pause 0.5
    $ play_sfx("step_on_chair")
    $ store.is_character_sitting = True

    "I sit at my table to taste the carefully crafted lunch. My palate is ready, but my bottom disagrees."

    pause 0.2
    show mc at character_right_sit_shake
    pause 1.0

    mc "This chair is not stable at all!"

    show mc at character_right_sit_down
    pause 1.0

    # Call to start Chair task
    $ StartTask(task_Chair)
    # pause 0.5

    "I crouch and inspect the chair to see where the issue comes from."
    $ play_sfx("inspect_chair")
    pause 1.5
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show screen screen_item("screw_loose", "bottom_left") with dissolve
    pause 0.5

    mc "Looks like that screw is a bit loose."
    mc "Hex type, uh? Let’s see if I got a matching screwdriver."

    hide screen screen_item

    show mc at character_stand_up
    pause 0.5
    show mc casual regular at character_right
    pause 0.5

    $ store.is_character_sitting = False

    $ StartTask(task_HexKeyApartment)

    $ play_sfx("searching_drawer")
    pause 4.0
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show mc casual regular left at character_right
    mc "Nope. No such thing."
    $ FailTask(task_HexKeyApartment)

    mc "Guess I need to go to the DIY store to get one. Screwdriver or key."

    $ StartTask(task_HexKeyStore, notify=True)

    "I write this on my TODO list. I'll check it later by clicking on the notepad icon at the bottom-right, or by pressing the T key."

    show mc casual regular at character_move_right_farther
    pause 1.0
    show mc casual regular left
    pause 0.5

    mc "I should take a measurement of the screw hole before I leave."

    show mc at character_move_right(0.2)
    pause 0.5

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

    pause 0.5
    show mc at character_right_sit_down
    $ store.is_character_sitting = True

    "I draw my smartphone and take a picture of the screw. I put my finger on it as a scale reference."
    show screen screen_item("screw_loose", "left")
    $ play_sfx("smartphone_camera")
    pause 1.0
    hide screen screen_item with dissolve

    show mc at character_stand_up
    $ store.is_character_sitting = False

    "As I’m checking that the photo is good enough, I notice a few notifications on the phone."
    menu:
        "Should I check them out?"
        "Yes, check notifications":
            "We never know if there's not something important."
            $ notifications_context = "photo"
            call s_a from _call_s_a
            $ notifications_context = None
            "So, where was I? Oh yeah, I got the measurement for the screw."
        "No, ignore them":
            "I have what I need already."

    $ CompleteTask(task_ScrewPhoto)

    "I’d better hurry now and go to the store while it’s open."
    jump .shot4

label .shot3b:
    $ store.screw_measurement_method = "meter"
    $ StartTask(task_ScrewMeter)

    pause 0.5
    show mc at character_right_sit_down
    $ store.is_character_sitting = True

    queue sound ["<silence 1.5>", write_on_paper]
    $ notify_sfx("write_on_paper")

    "I grab a meter, measure the screw external diameter, internal diameter and write them on my notepad."
    $ CompleteTask(task_ScrewMeter)

    show mc at character_stand_up
    $ store.is_character_sitting = False

    mc "OK, let’s go!"
    jump .shot4

# Sister call
label .shot4:
    $ CompleteTask(task_ScrewSize)

    $ StartTask(task_Store)
    $ RevealTask(task_FindHexKey)
    $ RevealTask(task_BuyHexKey)

    pause 0.2
    show mc casual regular
    pause 0.2

    # to avoid spamming notification in loop, add a pause (silence) between each
    play sound [smartphone_call, "<silence 1.0>"] loop

    "Just before I leave, my phone rings. It's my sister, Tifenn."
    pause 1.0
    "I make sure I leave the phone ring a few more times, then I answer:"
    stop sound
    mc "I'm busy now."
    sister "...{w=1.0} A such nice intro.{w=1.0} Are you actually busy? Or yet again being sidetracked to something completely unrelated to what you were doing?"

    # comical turningback thinking
    pause 1.2
    show mc casual regular left
    pause 0.5

    mc "No. And it's related."

    pause 1.0

    sister "Fine. I'll send you a message later."
    mc "Please don't."
    sister "Thanks, bye!"

    "She hangs up. Where was I? Oh, yes, the chair."

label .shot5:
    # the window show None / hide at the end of each scene is just to have a clean
    # textbox dissolve at the end
    window show None
    "I just get to the store, pick a screwdriver, come back, and done."
    window hide

    stop music fadeout 2.0
    pause 0.5
    show mc casual regular at character_move_right_exit

    # hide Back, Task tree and Preferences button so they don't show above the overlay
    $ quick_menu = False
    show overlay black with dissolve
    pause 0.5
    $ play_sfx("door_open_close")
    pause 2.0

    # No Wi-Fi outside
    $ store.has_wifi = False
    $ quick_menu = True
    jump s2_1
