label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop with dissolve
    "Right, I forgot buses only come every 20 minutes on Sunday."
    "...{p}I might as well check my phone."
    "I pull out my phone and swipes through notifications."
    call sa_1 from _call_sa_1_1

# MC enters bus, but doesn’t have coins
label .shot2:
    "The phone keeps me busy until the bus arrives."
    # play sound bus_arrives
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: bus arrives")
    "I get on the bus and give a bill to the driver, who makes an apologetic face."
    driver "Sorry, coins only."
    "I search in my wallet, but there are not enough to buy a ticket."
    "The last remnants of my momentum lost, I get off and decide to turn my bill into coins in some local store."

    jump s2_2
