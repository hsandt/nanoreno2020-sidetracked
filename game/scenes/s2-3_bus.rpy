label s2_3:

# Get on bus
label .shot1:
    $ store.currentTime = 15*60 + 00
    $ store.wrapping_scene = "bus"

    $ play_sfx("store_door_open")
    scene bus_stop with CropMove(1.5, "wiperight")
    pause 1.0
    $ play_sfx("store_door_close")
    pause 0.5
    play music "<loop 19.287>audio/bgm/ambient_street.ogg"

    show mc outside regular at character_left with dissolve
    pause 0.5

    window show
    "There, I wait for the next bus while tasting some viennoiseries."
    window hide None

    scene bus_outside with dissolve

    show mc outside regular at character_left with dissolve

    $ play_sfx("bus_stop_and_open")

    "When the bus arrives, I get on and buy a return ticket."

    show screen screen_item("coins", "center") with dissolve
    $ play_sfx("coins_drop")
    pause 0.5
    hide screen screen_item with dissolve
    pause 0.5

    $ CompleteTask(task_Ticket)

    $ play_sfx("smartphone_notification")

    "While I'm paying, my phone vibrates and notifies me of a new message. I'll check this later."

    # Sister has sent request, it will affect Scene F: Kill time > Scene A: Notifications
    $ sister_request_phase = 1

# Inside bus
label .shot2:
    $ play_sfx("bus_close")

    scene bus_inside with dissolve
    pause 0.5

    "The inside surprisingly looks Japanese."
    "I sit in the back, where I usually feel better to do my stuff without people looking."
    $ play_sfx("step_on_chair")
    pause 1.0

    $ StartTask(task_PushClosestStop)

    "I pull out my phone, see what I can do until I arrive."
    call s_f from _call_s_f_1  # Kill time

    "As the bus approaches the store, I push the stop button on my left. It does nothing, though. Probably broken."
    $ FailTask(task_PushClosestStop)

    pause 0.5

    "Another hurdle... Another problem I will solve."
    "I can try another button, or let somebody else do it for me."
    "Oh, there’s also that new app, “Stop, Please!” that allow people to send a “stop” signal to the bus they are in."
    "If I scan the QR code on the ad stuck in the bus, I should be able to install it."

    $ has_stood_up = False
    $ has_installed_app = False
    $ has_asked_passenger = False
    $ wait_count = 0

    menu stop_button:
        "What do I do?"
        "Stand up and push the next closest stop button" if not has_stood_up:
            jump s2_3.shot3a
        "Stand up and try again!" if has_stood_up:
            jump s2_3.shot3b
        "Install “Stop, Please!”" if not has_installed_app:
            jump s2_3.shot4
        "Ask another passenger to push a working button" if not has_asked_passenger:
            jump s2_3.shot5
        "Wait for someone else to push the stop button" if wait_count == 0:
            jump s2_3.shot6
        "Wait a bit more" if wait_count == 1:
            jump s2_3.shot7

# Stand up
label .shot3a:
    $ has_stood_up = True

    $ StartTask(task_StandUp)
    "I stand up and walk toward another stop button in the central alley."

    # SFX reuse for another purpose
    queue sound [inspect_chair, step_on_chair]
    # custom SFX accessibility notification since it's a queue of 2 sounds
    # with a unique description
    python:
         if preferences.audio_cues:
             renpy.notify("SFX: Katell loses balance and falls back on seat")

    "The bus suddenly shakes and I lose my balance. Right, they like cobblestones in this city."
    "I fall back to my seat without having been able to reach the button."
    jump stop_button

# Stand up 2nd time
label .shot3b:
    "I stand up once more, this time clinging to bars, seats, whatever."
    "This bothers the other passengers, but I don't care anymore."
    "After an epic march, I reach the damn thing and press it."

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    "It's working."
    $ CompleteTask(task_StandUp)
    jump .shot8

# App
label .shot4:
    $ has_installed_app = True

    $ StartTask(task_InstallStopApp)
    "I scan the QR code on the sticker, and wait for the app to install. We'll arrive at the store in a few minutes, so I hope it will work in time."
    "I launch the app and follow the instructions. Apparently, I must connect to the bus first."
    "I follow a convoluted process to sync my phone with the bus. Cry out with joy as you witness the magic of the {i}Internet of Things{/i}!"
    "...{w=1.0} In just a moment..."
    $ change_free_space(-50)

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    "In the meantime, another passenger pressed the stop button. Fine, the app will be useful next time..."
    $ CompleteTask(task_InstallStopApp)
    $ CompleteTask(task_WaitStop)
    jump .shot8

# Ask
label .shot5:
    $ has_asked_passenger = True

    $ StartTask(task_AskPassenger)
    "I call the passenger sitting in front of me, but he doesn't answer."
    "He's wearing headphones, so maybe they are just too good at insulating sound. I think I need the same, but for notifications."
    $ FailTask(task_AskPassenger)
    jump stop_button

# Wait 1
label .shot6:
    $ wait_count += 1

    $ StartTask(task_WaitStop)
    "I wait, hoping somebody else will push a working stop button."
    "It doesn't happen."
    "We're getting closer to the store."
    jump stop_button

# Wait 2
label .shot7:
    $ wait_count += 1

    "I continue waiting, but nothing happens. Am I gonna miss the stop?"
    "As I'm expecting the worst, I nervously tap my foot."

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    "Somebody finally calls for the stop."
    $ CompleteTask(task_WaitStop)
    jump .shot8

# Get off
label .shot8:
    pause 0.8

    $ play_sfx("bus_stop_and_open")

    window show None
    "The bus stops near the DIY store, I get off and walk in."
    window hide

    $ CompleteTask(task_Stop)
    $ CompleteTask(task_Bus)
    $ CompleteTask(task_Store)

    stop music fadeout 1.0

    jump s3_1
