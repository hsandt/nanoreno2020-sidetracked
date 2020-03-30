label s3_4:

label .shot1:
    pause 2.0
    show mc regular at character_left with dissolve

    "Back at the register, I realize I’ve lost my place in the queue so I need to do it again."
    # for v2.2: Call Scene F: Kill time
    "After ten more minutes, I show the tool again, together with the permit."
    show screen screen_item("purchase_permit", "right")
    pause 1.0
    hide screen screen_item
    pause 0.5
    show screen screen_item("screw_loose", "right")
    pause 1.0
    # if you have 2 different transforms, show both at the same time
    cashier "Six euros ninety-nine."
    hide screen screen_item

    mc "OK."
    show screen screen_item("screw_loose", "right") with dissolve
    play sound coins_drop
    pause 0.5
    hide screen screen_item with dissolve
    pause 0.5

    cashier "Thank you."
    mc "Goodbye! {i}(Finally.){/i}"
    $ quick_menu = False
    show overlay black with dissolve
    stop music fadeout 2.0
    $ quick_menu = True

    jump s4a_1
