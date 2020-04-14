label s2_1:

# MC receives notification
label .shot1:
    scene bus_stop
    $ play_music("street")
    $ store.currentTime += 26  # if doing nothing on smartphone: ~14h30
    $ store.wrapping_scene = "bus_stop"

    show mc outside regular left at character_right

    pause 1.5

    window show
    "Now, I remember. Buses come every 30 minutes on Sunday."
    window hide None

    # depending on actions in the first scene, MC may arrive closer or farther to the next bus
    # in addition, the next bus will "lock" the currentTime when it arrives
    # same thing for the "real" bus Katell will take after the bakery
    python:
        store.next_bus_time = get_next_bus_time(store.currentTime)
        # cheat: if MC is too close to next bus, go back in time slightly so she has enough time
        # to use smartphone (although we'll shorten time for very long activity anyway)
        store.currentTime = min(store.next_bus_time - 18, store.currentTime)
        time_before_next_bus = store.next_bus_time - store.currentTime
        next_bus_clock_time = minutes_to_clock_time(store.next_bus_time)
    if time_before_next_bus > 10:
        "And I've just missed the previous one..."
        if has_freed_space:
            "Maybe I shouldn't have spent too much time on my phone."

    show mc at character_leg_beat

    pause 0.5

    $ StartTask(task_Bus, notify=True)
    $ RevealTask(task_Ticket)
    $ RevealTask(task_Stop)

    "A few other people are waiting at the bus stop with me."
    "The street is rather quiet, with few cars passing by."

    pause 1.0

    show mc at character_right

    "Next bus will be at [next_bus_clock_time], that's in [time_before_next_bus] minutes..."
    "Looks like I have some time on my hands."

    call s_f from _call_s_f

    pause 0.5

    # Normally, long activities are now clamped in the smartphone scenes to make sure the player
    # never sees a time "in the future" (after bus arrives) on smartphone, but we kept this
    # for safety
    $ store.currentTime = store.next_bus_time

    "I see the bus coming and wave it down, pretending not to see the two other people doing exactly the same."
    "I'd rather avoid relying on others if I can."
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
    "I don't have one, so I naively try to buy a ticket."
    "I give a bill to the driver, who replies with a stoic face."
    driver "Sorry, coins only."
    $ StartTask(task_Coins)

    show mc at character_check_wallet

    "I search for coins in my wallet, but there aren't enough to buy a ticket."
    "Passenger candidates waiting behind me put an invisible pressure on my back. I don't like stress, so I apologize and quickly get off."

    $ play_sfx("bus_close")

    show mc outside regular left

    pause 0.5

    "Granted, things are not going as smooth as I expected. But there is nothing to worry about — yet."
    "I can just turn my bill into coins at some local store."
    $ StartTask(task_BuyFood)

    show mc at character_smell

    window show None
    "My sense of smell finds a bakery nearby, so I'm heading there."
    $ clock_time = get_clock_time()
    "[clock_time]? Maybe it's not the right time, but I left my lunch at home, so that will make up for it."
    window hide

    pause 0.5
    show mc at character_move_left_exit

    jump s2_2
