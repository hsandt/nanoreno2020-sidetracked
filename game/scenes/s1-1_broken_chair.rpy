label s1_1:
    $ store.has_wifi = True
    $ store.currentTime = 13*60 + 57  # game starts at ~14h, then events will increment time
    $ store.wrapping_scene = "broken_chair"

    # Renpy needs to be told to stop Main Menu BGM (Title Theme)
    stop music fadeout 2.0

label .shot1:
    scene overlay black
    pause 1.0

    show mc casual regular silhouette left at character_center with dissolve

    # the show/hide at the beginning of each scene is only to show textbox with quick dissolve
    # then hide it when no text is shown (without having to manually "window hide" every time)
    window show
    "Some say I'm easily distracted.{w} That's not true."
    "I'm not randomly jumping from a topic to another. Rather, problems keep popping up, and I have to solve them."
    window hide None # no transition except on scene start/end
    pause 0.5

    "Exactly what happened today."

    hide mc with dissolve
    pause 0.5

label .shot2:
    scene bg apartment day
    show mc casual regular left at character_center
    with Dissolve(1.0)
    $ play_music("apartment")

    # Call to start HaveLunch task so it shows up in the task tree
    # Don't notify this one though; it's unnatural for MC to write that now!
    $ StartTask(task_HaveLunch)

    mc "Hmm!\nNothing like the smell of roasted vegetables — that are not burnt."

    show mc at character_chair_sit_down
    pause 0.5
    $ play_sfx("step_on_chair")
    $ store.is_character_sitting = True

    "I sit down to enjoy the carefully crafted lunch.\nMy palate is ready — my bottom disagrees."

    pause 0.2
    show mc at character_chair_sit_shake
    pause 1.0

    mc "This chair is not stable at all!"

    show mc at character_move_chair_x(0.2)
    pause 1.0

    # Call to start Chair task
    $ StartTask(task_Chair)

    "I crouch and inspect the chair."

    show mc at character_move_behind_chair_x(0.5)

    $ play_sfx("inspect_chair")
    pause 1.5
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show screen screen_item("screw_loose", "bottom_left") with dissolve
    pause 0.5

    mc "Looks like that screw is a bit loose."
    mc "Hexagonal type, uh? Let’s see if I got a matching screwdriver."

    hide screen screen_item

    show mc at character_stand_up
    pause 0.5
    show mc casual regular at character_move_right(1.0)
    pause 1.0

    $ store.is_character_sitting = False

    $ StartTask(task_HexKeyApartment)

    $ play_sfx("searching_drawer")
    pause 4.0
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    mc "Nope. Nothing such."
    show mc casual regular left at character_move_behind_chair_x(1.0)
    pause 0.2
    $ FailTask(task_HexKeyApartment)

    "I need to find a way to fix this.\nIt's not my style to leave things unsorted."

    pause 0.6
    # `at` is just to warp character and avoid moonwalk if player clicks to skip anim
    show mc casual regular at character_move_behind_chair_x(0.0)
    pause 0.2
    "I know, the pile of dishes.\nBut look how they are perfectly stacked!"

    pause 0.7
    show mc casual regular left
    pause 0.3

    "Anyway, I guess I need to go to the DIY store to get some hexagonal screwdriver or key."

    $ store.unlocked_tasktree = True
    $ StartTask(task_HexKeyStore, notify=True)
    "Very organized as always, I write this on my TODO list."
    "I'll check it later by clicking on the notepad icon at the bottom-right, or by pressing the T key."

    show mc casual regular at character_move_right_farther(0.5)
    pause 1.0
    # `at` is just to warp character and avoid moonwalk if player clicks to skip anim
    show mc casual regular left at character_move_right_farther(0.0)
    pause 0.5

    mc "Oh, I should take the diameter of the screw hole before I leave."
    "I'll need that to buy the correct tool model.\nI don't want it to end like last time —"
    "I picked the wrong batteries, and the store wouldn't take them back because the package was opened."
    show mc at character_move_behind_chair_x(4.0)
    "How was I supposed to know they were not compatible without opening the package?"
    pause 0.8
    "Okay, enough digressing. The diameter."

    # MC should be at the right position with normal reading speed, but if player
    # was skipping text, go quickly to target position now
    show mc at character_move_behind_chair_x(0.5)

    $ StartTask(task_ScrewSize)
    $ RevealTask(task_Store)
    $ RevealTask(task_FindHexKey)
    $ RevealTask(task_BuyHexKey)

    # hide just to avoid displaying choices on the MC's face
    hide mc with Dissolve(0.3)
    pause 0.2

    menu:
        "How should I get the diameter of the screw hole?"
        "Take a photo":
            jump .shot3a
        "Measure it with a meter":
            jump .shot3b

label .shot3a:
    $ store.screw_measurement_method = "photo"
    $ StartTask(task_ScrewPhoto)

    pause 0.2
    # must show again at correct position after hiding for menu
    show mc casual regular left at character_stand_behind_chair_x with Dissolve(0.3)
    pause 0.3
    show mc at character_sit_down
    $ store.is_character_sitting = True

    "I pick my smartphone and take a picture of the screw. I put my finger besides as a scale reference."
    show screen screen_item("screw_loose", "left")
    $ play_sfx("smartphone_camera")
    pause 1.0
    hide screen screen_item with dissolve

    show mc at character_stand_up
    $ store.is_character_sitting = False

    "As I check the photo, I notice a few notifications on the phone."

    # hide just to avoid displaying choices on the MC's face
    hide mc with Dissolve(0.3)
    pause 0.2

    menu:
        "Should I check them out?"
        "Yes, check notifications":
            "We never know when something important will show up."
            $ notifications_context = "photo"
            call s_a from _call_s_a
            $ notifications_context = None
            # must show again at correct position after hiding for menu
            show mc casual regular left at character_stand_behind_chair_x with Dissolve(0.3)
            pause 0.3
            "So, what was I doing? Ah, right, I got a picture of the screw."
        "No, ignore them":
            # must show again at correct position after hiding for menu
            show mc casual regular left at character_stand_behind_chair_x with Dissolve(0.3)
            pause 0.3
            "I have what I need already."

    $ CompleteTask(task_ScrewPhoto)

    "I’d better go to the store now."
    jump .shot4

label .shot3b:
    $ store.screw_measurement_method = "meter"
    $ StartTask(task_ScrewMeter)

    pause 0.2
    # must show again at correct position after hiding for menu
    show mc casual regular left at character_stand_behind_chair_x with Dissolve(0.3)
    pause 0.3
    show mc at character_sit_down
    $ store.is_character_sitting = True

    queue sound ["<silence 1.5>", write_on_paper]
    $ notify_sfx("write_on_paper")

    "I grab a meter, measure the internal diameter of the screw and write it on my notepad."
    "Nothing as reliable as good old paper. Plus, I don't trust batteries."
    $ CompleteTask(task_ScrewMeter)

    show mc at character_stand_up
    $ store.is_character_sitting = False
    pause 0.5

    mc "Time to go."
    jump .shot4

# Sister call
label .shot4:
    $ CompleteTask(task_ScrewSize)

    $ StartTask(task_Store)
    $ RevealTask(task_FindHexKey)
    $ RevealTask(task_BuyHexKey)

    pause 0.2
    show mc casual regular at character_move_right(0.8)
    pause 0.3

    # to avoid spamming notification in loop, add a pause (silence) between each
    play sound [smartphone_call, "<silence 1.0>"] loop
    $ notify_sfx("smartphone_call")

    "My phone rings just before I leave. It's my sister, Tifenn."
    pause 1.0
    "I make sure to let the phone ring a few more times, then answer."
    stop sound fadeout 0.1  # very short, just to avoid pop
    pause 0.5
    mc "Hi. I'm busy right now."
    pause 0.5
    sister "...
    {p=1.0}Hey, Kat, how are you? Can I ask you something?"
    pause 0.5
    "Wait, did she ignore what I've just said on purpose?"
    mc "I said I'm busy."
    sister "Busy doing... what you're totally supposed to do, as always?"

    # comical turning back thinking
    pause 1.1
    show mc casual regular left
    pause 0.5

    mc "Yes."

    pause 1.0

    sister "Fine. I'll send you a message later."
    mc "Please don't."
    sister "Thanks, I knew I could count on you. Bye!"

    "She hangs up."
    pause 0.5
    "Where was I again? Oh, yeah. The store."

label .shot5:
    # the window show None / hide at the end of each scene is just to have a clean
    # textbox dissolve at the end
    window show None
    "I just get there, pick a screwdriver, come back, and I'm done."
    window hide

    pause 1.2

    # No Wi-Fi outside
    $ store.has_wifi = False

    jump s2_1
