label s2_3:

# Get on bus
label .shot1:
    # if added BG for bakery, revert to BG for bus stop here
    "There, I wait for the next bus while tasting some viennoiseries."

    # play sound bus_arrives
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: bus arrives")

    "When the bus arrives, I get on and buy a return ticket."
    "While I'm paying, I sense a vibration in my pocket. I'll check this later."
    # play sound smartphone_vibration
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: smartphone vibration")

    # Sister has sent request, it will affect Scene F: Kill time > Scene A: Notifications
    $ sister_request_phase = 1

# Inside bus
label .shot2:
    # TODO: scene bus with dissolve (need bus BG)
    "I sit in the back, where I usually feel better to do my stuff without people looking."
    play sound step_on_chair  # SFX reuse
    pause 1.0

    "I pull out my phone, see what I can do until I arrive."
    call s_f from _call_s_f_1

    "As the bus approaches the store, I push the stop button on my left. It does nothing, though. Probably broken."
    "I guess I’ll have to use another one, or let somebody else do it for me."
    "Oh, there’s also that new app, “Stop, Please!” that allow people to send a “stop” signal to the bus they are in."
    "If I scan the QR code on the ad stuck in the bus, I should be able to install it."

    $ has_stood_up = False
    $ has_installed_app = False
    $ has_asked_passenger = False
    $ wait_count = 0

    menu stop_button:
        "What do I do?"
        "Stand up and push the next closest stop button" if not has_stood_up:
            jump s2_3.shot3
        "Install “Stop, Please!”" if not has_installed_app:
            jump s2_3.shot4
        "Ask another passenger to push a working button" if not has_asked_passenger:
            jump s2_3.shot5
        "Wait for someone else to push the stop button" if wait_count == 0:
            jump s2_3.shot6
        "Wait a bit more" if wait_count == 1:
            jump s2_3.shot7

# Stand up
label .shot3:
    $ has_stood_up = True

    "I stand up and walk toward another stop button in the central alley."
    "The bus suddenly shakes and I lose my balance. Right, they like cobblestones in this city."
    "I fall back to my seat, unwilling to try again."
    jump stop_button

# App
label .shot4:
    $ has_installed_app = True

    "I scan the QR code on the sticker, and wait for the app to install. We'll arrive at the store in a few minutes, so I hope it will work in time."
    "I launch the app and follow the instructions. Apparently, I must connect to the bus first."
    "To do so, I scan another QR code on another sticker. It takes a moment..."
    $ change_free_space(-50)

    # play sound stop_button
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: stop button")

    "In the meantime, another passenger pressed the stop button. Fine, the app will be useful next time..."
    jump .shot8

# Ask
label .shot5:
    $ has_asked_passenger = True

    "I call the passenger sitting in front of me, but he doesn't answer."
    "He's wearing headphones, so maybe they are just too good at insulating sound. I think I need the same, but for notifications."
    jump stop_button

# Wait 1
label .shot6:
    $ wait_count += 1

    "I wait, hoping somebody else will push a working stop button."
    "It doesn't happen."
    "We're getting closer to the store."
    jump stop_button

# Wait 2
label .shot7:
    $ wait_count += 1

    "I continue waiting, but nothing happens. Am I gonna miss the stop?"
    "As I'm expecting the worst, I nervously tap my foot."

    # play sound stop_button
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: stop button")

    "Somebody finally calls for the stop."
    jump .shot8

# Get off
label .shot8:
    "The bus stops near the DIY store, I get off and walk in."
    # play sound automatic_door_open_close
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: automatic door opens and closes")

    jump s3_1
