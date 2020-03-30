label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop with dissolve
    "Right, I forgot buses only come every 20 minutes on Sunday."
    "Looks like I have some time on my hands. But my smartphone can keep me busy."
    call s_f from _call_s_f

# MC enters bus, but doesn’t have coins
label .shot2:
    # play sound bus_arrives
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: bus arrives")
    pause 1.0

    "I raise my head from the phone as the bus finally arrives."
    "I get on the bus and give a bill to the driver, who makes an apologetic face."
    driver "Sorry, coins only."
    "I search in my wallet, but there are not enough to buy a ticket."
    "I apologize in return, quickly get off and decide to turn my bill into coins in some local store."

    jump s2_2
