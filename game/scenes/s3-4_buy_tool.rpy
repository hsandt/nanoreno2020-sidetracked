label s3_4:

label .shot1:
    pause 2.0
    "I’ve also been standing in the queue for 15 minutes now, so I’m nervously tapping my leg with the tool’s package."
    mc "Good afternoon."
    show item hex_key at item_right with dissolve
    mc "This one, please."
    cashier "That’ll be six euros ninety-nine."
    mc "OK."
    show item coins at item_right with dissolve
    play sound coins_drop
    pause 0.5
    hide item with dissolve
    pause 0.5

    cashier "Thank you."
    mc "Goodbye! {i}(Finally.){/i}"
    show overlay black with dissolve
    stop music fadeout 2.0

    jump s4a_1
