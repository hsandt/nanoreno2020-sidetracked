label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop with dissolve
    $ play_music("street")
    $ store.currentTime += 26  # if doing nothing on smartphone: ~14h30
    $ store.wrapping_scene = "bus_stop"

    show mc outside regular at character_left with dissolve
    show mc at character_leg_beat

    window show
    "The bus is the most convenient way to go to the DIY store, so I go to the closest stop, where a few other people are waiting."
    $ StartTask(task_Bus, notify=True)
    $ RevealTask(task_Ticket)
    $ RevealTask(task_Stop)
    "The street is rather quiet, as few cars are passing by."
    window hide None

    pause 1.0

    # depending on actions in the first scene, MC may arrive closer or farther to the next bus
    # in addition, the next bus will "lock" the currentTime when it arrives
    # same thing for the "real" bus Katell will take after the bakery
    $ next_bus_time = get_next_bus_time(store.currentTime)
    $ time_before_next_bus = next_bus_time - store.currentTime
    $ next_bus_clock_time = minutes_to_clock_time(next_bus_time)
    if time_before_next_bus < 5:
        "I arrive just in time for the bus of [next_bus_clock_time]."
        $ store.currentTime = next_bus_time
        jump .shot2
    else:
        # we cheat here: 15mn is not enough for *any* smartphone activity,
        # but we assume that if a bus is coming, Katell will just play,
        # or do whatever she was doing, faster to finish her task.
        # This is simpler that implementing an interruption mechanic and having
        # uncomplete tasks.
        show mc at character_left

        if time_before_next_bus > 25:
            "I just miss the bus who leaves without me."
            if has_freed_space:
                "Maybe I shouldn't have spend too much time on my phone."

        "I just remember that buses only come every 30 minutes on Sunday. Next one will be in [time_before_next_bus] minutes..."
        if time_before_next_bus > 9:
            "Looks like I have some time on my hands. But my smartphone can keep me busy."
        else:
            "That's just enough time to do something on my phone."

        call s_f from _call_s_f

        pause 0.5

        # this is where we cheat and potentially, we are going back in time after a long activity
        # this works because the player cannot see the smartphone until the bus after the bakery
        # this way we don't have to clamp time after time update due to long activity when wrapping
        # scene is bus_stop
        $ store.currentTime = next_bus_time

        "I raise my head from the phone as the bus finally arrives, and wave it down."
        # fallthrough .shot2

label .shot2:
    pause 0.3

    $ StartTask(task_Ticket)

    scene bus_outside with dissolve

    show mc outside regular at character_left with dissolve

    $ play_sfx("bus_stop_and_open")
    pause 2.5

    queue sound ["<silence 0.8>", topping_bus_card, "<silence 1.8>", topping_bus_card, "<silence 1.5>", topping_bus_card]
    $ notify_sfx("topping_bus_card")

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
