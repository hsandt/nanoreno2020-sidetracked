label s4_1:
    # probably no smartphone usage at the end of the game, but just in case
    $ store.has_wifi = True

label .shot1:
    $ store.currentTime = "19:00"
    $ store.wrapping_scene = "light_bulb"

    # should be bg apartment_night, but we only have one
    scene bg apartment with dissolve

    show mc regular left at character_right

    window show
    "By the time I get back in my apartment, night has already fallen. I hastily remove my shoes and open the tool’s package."
    window hide None

    show screen screen_item("hex_key", "left") with dissolve
    mc "OK, let’s try this now."
    hide screen screen_item with dissolve
    show screen screen_item("screw_loose", "left") with dissolve
    "I use the key to tighten the screw on the chair in the living room."
    play sound screw_tighten
    pause 0.5
    show screen screen_item("screw_tight", "left") with dissolve
    pause 0.5
    mc "A-ha! Is it stable now?"
    hide screen screen_item

    show mc at character_right_sit_down
    pause 0.5
    play sound step_on_chair
    $ store.is_character_sitting = True

    "I sit down. The seat is not moving anymore."

    $ CompleteTask(task_Chair)

    mc "Time for lunch!"
    "I take a mouthful of zucchini. It's cold."
    "I look around me and realize it's pretty dark. I glance at my watch, which shows 7pm."
    "Looks like my lunch has turned into a dinner. A cold dinner."

    play sound step_on_chair
    show mc at character_stand_up
    $ store.is_character_sitting = False
    pause 0.5

    "Eating cold food in the dark makes me look like a vampire. I push the light switch, but nothing happens."
    "I inspect the light bulb and notice it's broken. Another thing I must fix, I guess."

    $ StartTask(task_LightBulb)

    # TODO Animation: MC searches for light bulb as in first scene with screwdriver

    "I start removing the dead bulb, but realize I don’t have any replacement."
    "Wait, do I need to go back to the DIY store?"

    $ RevealTask(task_BuyLightBulb)

    "I check my watch. [currentTime]."
    mc "..."

    menu:
        "Should I go back to the store to get a replacement bulb?"
        "Yes":
            jump .shot2a
        "Screw this and go to bed":
            jump .shot2b

label .shot2a:
    $ StartTask(task_BuyLightBulb)

    mc "I think I can go there once more before it closes, but I need to go now."
    # TODO ANIM: MC turns back to look at meal
    "The meal is cold already, it cannot get colder."
    # TODO ANIM: MC turns back toward door (right) again
    pause 1.0
    "And the store is not too far, I should be back in no time."
    play sound door_open_close
    $ quick_menu = False
    show overlay black with dissolve
    $ quick_menu = True
    jump ending2

label .shot2b:
    "No, I don't want to."

    $ FailTask(task_BuyLightBulb)
    $ FailTask(task_LightBulb)
    $ CompleteTask(task_HaveLunch)

    $ quick_menu = False
    show overlay black with dissolve
    $ quick_menu = True
    "After that, I finished my cold meal, went in my bed and read a novel for two hours straight before sleeping."
    "I’ll see what I can do for the light tomorrow..."
    jump ending1
