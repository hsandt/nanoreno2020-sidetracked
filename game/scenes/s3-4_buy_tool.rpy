label s3_4:

label .shot1:
    "{i}One hour later...{/i}"

    scene bg store with dissolve
    # play music store
    show mc regular at character_left with dissolve
    "Thanks to the store’s efficient sorting system, it took me ages to find the right screwdriver."
    "I’ve also been standing in the queue for 15 minutes now, so I’m nervously tapping my leg with the tool’s package."
    mc "Good afternoon."
    show item hex_key at item_right with dissolve
    mc "This one, please."
    cashier "That’ll be six euros ninety-nine."
    mc "OK."
    play sound coins_drop
    hide item with dissolve
    pause 0.5

    cashier "Thank you."
    mc "Goodbye! {i}(Finally.){/i}"
    show overlay black with dissolve

    jump s4a_1
