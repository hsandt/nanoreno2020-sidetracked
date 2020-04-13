label s2_3:

# Get on bus
label .shot1:
    # next bus exactly, so +30
    $ store.currentTime += 30  # if doing nothing on smartphone: ~15h30
    $ store.wrapping_scene = "bus"

    $ play_sfx("store_door_open")
    scene bus_stop with CropMove(1.5, "wiperight")
    pause 1.0
    $ play_sfx("store_door_close")
    pause 0.5
    play music street

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
    # we have entered the bus, so from here lock the arrival time
    # whatever we do on the smartphone, it won't change
    # of course, choose a time that broadly covers the longest smartphone
    # activity so it doesn't feel like we are going back in time
    $ bus_arrival_time = store.currentTime + 29

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

    # technically, there is a margin during which the MC finishes the activity
    # just before the stop, does not miss the stop,
    # but doesn't do the stop button challenge either since another passenger would
    # have pressed the button in the meantime... but for simplicity and providing
    # more events to the player, we ignore that
    $ missed_bus_stop = currentTime > bus_arrival_time
    if missed_bus_stop:
        "As I emerge from my phone, I realize I missed the stop for the store."
        "Urg, I need to get off and walk back to the store now. To avoid making things worse, I push the stop button immediately."
    else:
        "As the bus approaches the store, I push the stop button on my left."

    "It does nothing, though. Probably broken."
    $ FailTask(task_PushClosestStop)

    stop music fadeout 1.0
    pause 1.0

    # start synchronized tracks for dynamic music
    $ renpy.audio.music.play(audio.mission, synchro_start=True)
    $ renpy.audio.music.play(audio.mission_a, channel="mission_a", synchro_start=True)
    $ renpy.audio.music.play(audio.mission_b, channel="mission_b", synchro_start=True)
    $ solo_mission_full()

    "Another hurdle... Another problem I will solve."
    "I can try another button, or let somebody else do it for me."
    "Oh, there’s also that new app, “Stop, Please!” that allow people to send a “stop” signal to the bus they are in."
    "If I scan the QR code on the ad stuck in the bus, I should be able to install it."
    $ solo_mission_a(delay=1.0)

    $ has_stood_up = False
    $ store.has_installed_bus_stop_app = False
    $ has_asked_passenger = False
    $ wait_count = 0

    menu stop_button:
        "What do I do?"
        "Stand up and push the next closest stop button" if not has_stood_up:
            jump s2_3.shot3a
        "Stand up and try again!" if has_stood_up:
            jump s2_3.shot3b
        "Install “Stop, Please!”" if not has_installed_bus_stop_app:
            jump s2_3.shot4
        "Ask another passenger to push a working button" if not has_asked_passenger:
            jump s2_3.shot5
        "Wait for someone else to push the stop button" if wait_count == 0:
            jump s2_3.shot6
        "Wait a bit more" if wait_count == 1:
            jump s2_3.shot7

# Stand up
label .shot3a:
    $ solo_mission_full(delay=1.0)

    $ has_stood_up = True
    $ StartTask(task_StandUp)
    "I stand up and walk toward another stop button in the central alley."
    "The bus suddenly shakes and I lose my balance. Right, they like cobblestones in this city."
    "I fall back to my seat without having been able to reach the button."

    $ solo_mission_a(delay=1.0)

    jump stop_button

# Stand up 2nd time
label .shot3b:
    $ solo_mission_full(delay=1.0)

    "I stand up once more, this time clinging to bars, seats, whatever."
    "This bothers the other passengers, but I don't care anymore."
    "After an epic march, I reach the damn thing and press it."

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    pause 1.0

    "It's working."

    stop music fadeout 1.5
    stop mission_a
    stop mission_b
    pause 1.0

    $ CompleteTask(task_StandUp)
    jump .shot8

# App
label .shot4:
    $ store.has_installed_bus_stop_app = True
    $ duo_mission_ab(delay=1.0)

    $ StartTask(task_InstallStopApp)
    "I scan the QR code on the sticker, and wait for the app to install. We'll arrive at the store in a few minutes, so I hope it will work in time."
    "I launch the app and follow the instructions. Apparently, I must connect to the bus first."
    "I follow a convoluted process to sync my phone with the bus. Hopefully this will provide extra awareness to the app and let it do smarter things."

    $ solo_mission_b(delay=1.0)

    "...{w=2.0} In just a moment..."
    $ change_free_space(-50)

    pause 1.0

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    pause 0.5
    stop music
    stop mission_a
    stop mission_b

    "In the meantime, another passenger pressed the stop button. Fine, the app will be useful next time..."
    $ CompleteTask(task_InstallStopApp)
    $ CompleteTask(task_WaitStop)
    jump .shot8

# Ask
label .shot5:
    $ has_asked_passenger = True
    $ solo_mission_full(delay=1.0)

    $ StartTask(task_AskPassenger)
    "I call the passenger sitting in front of me, but he doesn't answer. As I said, don't rely on others too much."
    "He's wearing headphones, so maybe they are just too good at insulating sound. I think I need the same, but for notifications."
    $ FailTask(task_AskPassenger)

    $ solo_mission_a(delay=1.0)

    jump stop_button

# Wait 1
label .shot6:
    $ wait_count += 1
    $ solo_mission_b(delay=1.0)

    $ StartTask(task_WaitStop)
    "I wait, hoping somebody else will push a working stop button."
    "It doesn't happen. I knew it, I shouldn't rely on others like that."
    "We're getting closer to the store."

    $ solo_mission_a(delay=1.0)

    jump stop_button

# Wait 2
label .shot7:
    $ wait_count += 1
    $ solo_mission_b(delay=1.0)

    "I continue waiting, but nothing happens. Am I gonna miss the stop?"
    "As I'm expecting the worst, I nervously tap my foot."

    pause 0.5

    queue sound ["<silence 0.5>", bus_stop_button]
    $ notify_sfx("bus_stop_button")

    pause 0.5
    stop music
    stop mission_a
    stop mission_b

    "Somebody finally calls for the stop."
    "I guess sometimes other people actually do the job."
    $ CompleteTask(task_WaitStop)
    jump .shot8

# Get off
label .shot8:
    # reset all channel volumes, esp. the music which will be used from now on
    $ renpy.audio.music.set_volume(1.0, delay=0, channel="music")
    $ renpy.audio.music.set_volume(1.0, delay=0, channel="mission_a")
    $ renpy.audio.music.set_volume(1.0, delay=0, channel="mission_b")

    pause 0.8

    play music street
    $ play_sfx("bus_stop_and_open")

    window show None
    if missed_bus_stop:
        "The bus stops a few yards from the store. But I don't want to wait for the next returning bus, so I just walk back to the store."
        "It takes me an extra quarter hour."
        # instead of computing the time to the exact next stop + coming back,
        # we just add the average time of coming back from one of the stops ahead
        # this way, even if MC spent far too much time and misses two stops,
        # we still have a meaningful time based on the current time + some extra to stop and come back
        # and it's always higher than bus_arrival_time
        $ store.currentTime += 16
    else:
        "The bus stops near the DIY store, I get off and walk in."
        # now apply the locked arrival time
        $ store.currentTime = bus_arrival_time
    window hide

    $ CompleteTask(task_Stop)
    $ CompleteTask(task_Bus)
    $ CompleteTask(task_Store)

    stop music fadeout 1.0

    jump s3_1
