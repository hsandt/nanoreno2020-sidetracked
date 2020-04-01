label s4a_1:
    # probably no smartphone usage at the end of the game, but just in case
    $ store.has_wifi = True

label .shot1:
    $ store.currentTime = "19:10"

    # should be bg apartment_night, but we only have one
    scene bg apartment with dissolve

    show mc regular left at character_right

    window show
    "Back in my apartment, I hastily remove my shoes and open the tool’s package."
    window hide None

    show screen screen_item("hex_key", "left") with dissolve
    mc "OK, let’s try this now."
    hide screen screen_item with dissolve
    show screen screen_item("screw_loose", "left") with dissolve
    "I use the key to tighten the screw on the chair."
    play sound screw_tighten
    pause 0.5
    hide screen screen_item
    show screen screen_item("screw_tight", "left") with dissolve
    pause 0.5
    mc "A-ha! Can I stand on it now?"
    hide screen screen_item
    hide mc
    with Dissolve(0.1)
    play sound step_on_chair
    "I get onto the chair and slowly stand up, as I make sure it won’t make me roll all over the floor."
    mc "Stable."
    mc "Now I can change this light bulb!"
    "That's right, I forgot to mention that if I needed a stable chair, it was to change my broken light bulb."
    "I start removing the dead bulb, but realize I don’t have any replacement."
    "Wait, do I need to go back to the DIY store?"
    play sound step_on_chair
    show mc regular left at character_right with Dissolve(0.1)
    "I step off the chair and I check my watch. 19:30."
    mc "..."

    menu:
        "Should I go back to the store to get a replacement bulb?"
        "Yes":
            jump .shot2a
        "Screw this and go to bed":
            jump .shot2b

label .shot2a:
    mc "I think I still have time to go."
    "The store is not too far, I should be back in no time."
    play sound door_open_close
    $ quick_menu = False
    show overlay black with dissolve
    $ quick_menu = True
    jump ending2

label .shot2b:
    $ quick_menu = False
    show overlay black with dissolve
    $ quick_menu = True
    "After that, I made myself a soup, went in my bed and read a novel for two hours straight before sleeping."
    "I’ll see what I can do for the light tomorrow..."
    jump ending1
