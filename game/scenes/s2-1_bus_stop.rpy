label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop with dissolve
    $ play_music("street")
    $ store.currentTime = "14:00"
    $ store.wrapping_scene = "bus_stop"

    show mc outside regular at character_left with dissolve
    show mc at character_leg_beat

    window show
    "The bus is the most convenient way to go to the DIY store, so I wait at the stop with a few other people."
    $ StartTask(task_Bus, notify=True)
    $ RevealTask(task_Ticket)
    $ RevealTask(task_Stop)
    "The street is rather quiet, as few cars are passing by."
    window hide None

    pause 1.0

    show mc at character_left

    "Right, I forgot buses only come every 20 minutes on Sunday."
    "Looks like I have some time on my hands. But my smartphone can keep me busy."

    call s_f from _call_s_f

# MC enters bus, but doesn’t have coins
label .shot2:
    pause 0.5

    "I raise my head from the phone as the bus finally arrives, and wave it down."
    pause 0.3

    $ StartTask(task_Ticket)

    scene bus_outside with dissolve

    show mc outside regular at character_left with dissolve

    $ play_sfx("bus_stop_and_open")
    pause 2.5

    queue sound ["<silence 0.8>", topping_bus_card, "<silence 1.8>", topping_bus_card, "<silence 1.5>", topping_bus_card]
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: " + sfx_dictionary["topping_bus_card"])

    "The passengers before me top up their smart cards as they get on the bus."
    "I don't have one, so I try to buy a ticket."
    "I give a bill to the driver, who says with a stoic face:"
    driver "Sorry, coins only."
    $ StartTask(task_Coins)

    show mc at character_check_wallet

    "I search in my wallet, but there are not enough to buy a ticket."

    $ play_sfx("bus_close")

    "I apologize and quickly get off."

    show mc outside regular left

    pause 0.5

    "Granted, things are not going as smooth as I expected, but there is nothing to worry about yet."
    "I can just turn my bill into coins in some local store."
    $ StartTask(task_BuyFood)

    window show None
    "My sense of smell finds a bakery nearby, so I'm heading toward it."
    "Maybe it's not the right time, but I left my lunch at home anyway, so that will cover up."
    window hide

    pause 0.5
    show mc at character_move_left_exit

    jump s2_2
