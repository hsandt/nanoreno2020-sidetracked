label s3_2:

label .shot1:
    show mc regular at character_left with dissolve
    mc "Hi."
    show item hex_key at item_right with dissolve
    "I show the hex key to the cashier. She scans it, then stop for a moment."
    hide item with dissolve
    
    cashier "Thank you. Can I see your purchase permit?"
    mc "Sorry?"
    cashier "You need a purchase permit to buy a tool of category C. You can print one on the machine over there."
    "The cashier points at a huge device in the corner. Four people are queuing in front of it."
    mc "I see."

    hide mc with dissolve

    jump s3_3
