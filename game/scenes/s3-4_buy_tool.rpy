label s3_4:

label .shot1:
    pause 2.0
    show mc regular at character_left with dissolve

    "Back at the register, I realize I’ve lost my place in the queue so I need to do it again."
    # for v2.2: Call Scene F: Kill time
    "After ten more minutes, I show the tool again, together with the permit."
    show item purchase_permit at item_right
    pause 1.0
    hide item
    pause 0.5
    show item hex_key at item_right
    pause 1.0
    # if you have 2 different transforms, show both at the same time
    cashier "Six euros ninety-nine."
    hide item

    mc "OK."
    show item coins at item_right with dissolve
    play sound coins_drop
    pause 0.5
    hide item with dissolve
    pause 0.5

    cashier "Thank you."
    mc "Goodbye! {i}(Finally.){/i}"
    $ quick_menu = False
    show overlay black with dissolve
    stop music fadeout 2.0
    $ quick_menu = True

    jump s4a_1
