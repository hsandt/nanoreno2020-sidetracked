label s3_4:

label .shot1:
    $ store.currentTime = "17:45"

    pause 2.0
    show mc regular at character_left with dissolve

    "Back at the register, I realize I’ve lost my place in the queue so I need to do it again."
    "Once more, I pull out my smartphone as I've got nothing to do. Actually, maybe I should stop doing that."
    "Nah, it's not like I'm gonna lose myself while queuing in a shop or anything."
    call s_f from _call_s_f_2
    "As I finish my business with the phone, I realize I've reached the register."
    "This time, I show the tool together with the permit."
    show screen screen_item("purchase_permit", "right")
    pause 1.0
    hide screen screen_item
    pause 0.5
    show screen screen_item("hex_key", "right")
    pause 1.0
    # if you have 2 different transforms, show both at the same time
    cashier "Six euros ninety-nine."
    hide screen screen_item

    mc "OK."
    play sound coins_drop
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: coins dropped on counter")
    pause 0.5

    cashier "Thank you."
    $ CompleteTask(task_BuyHexKey)
    $ CompleteTask(task_HexKeyStore)

    pause 0.5

    show mc regular left
    "Ha! I knew I could make it! And it took me only...{w=1.0} Four hours."

    pause 0.2
    show mc regular
    pause 0.5

    window show None
    "Time to go home."
    window hide

    show mc regular left at character_move_left_exit

    $ quick_menu = False

    show overlay black with Dissolve(1.0)
    stop music fadeout 2.0

    play sound store_door_open
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: automatic door opens")

    pause 3.0

    jump s4_1
