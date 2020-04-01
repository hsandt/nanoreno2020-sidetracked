label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop with dissolve
    play music "<loop 19.287>audio/bgm/ambient_street.ogg"
    $ store.currentTime = "17:15"

    window show
    "Right, I forgot buses only come every 20 minutes on Sunday."
    "Looks like I have some time on my hands. But my smartphone can keep me busy."
    window hide None

    call s_f from _call_s_f

# MC enters bus, but doesn’t have coins
label .shot2:
    # play sound bus_arrives
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: bus arrives")
    pause 1.0

    "I raise my head from the phone as the bus finally arrives, and wave it down."

    scene bus_outside with dissolve

    "I get on the bus and give a bill to the driver, who makes an apologetic face."
    driver "Sorry, coins only."
    "I search in my wallet, but there are not enough to buy a ticket."
    "I apologize in return, quickly get off and decide to turn my bill into coins in some local store."

    window show None
    "My sense of smell finds a bakery nearby, so I walk in."
    window hide

    jump s2_2
