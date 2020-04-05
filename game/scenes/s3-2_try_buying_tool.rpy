label s3_2:

label .shot1:
    $ store.currentTime = "16:30"
    $ store.wrapping_scene = "store"

    $ StartTask(task_BuyHexKey)

    show mc regular at character_left with dissolve
    mc "Hi."
    show screen screen_item("hex_key", "right") with dissolve
    "I show the hex key to the cashier. She scans it, then stop for a moment."
    hide screen screen_item with dissolve

    cashier "Thank you. Can I see your purchase permit?"
    mc "Sorry?"
    cashier "You need a purchase permit to buy a tool of category C. You can print one on the machine over there."
    "The cashier points at a huge device in the corner. Four people are queuing in front of it."
    mc "I see."

    pause 0.2
    $ StartTask(task_Permit, notify=True)
    pause 0.5

    hide mc with dissolve

    jump s3_3
