label s2_2:

# MC enters bakery and buys everything
label .shot1:
    $ store.wrapping_scene = "bakery"

    $ play_sfx("store_door_open")
    scene bakery with CropMove(1.5, "wipeleft")
    $ play_music("store", fadeout=1.0)
    pause 1.0

    $ play_sfx("store_door_close")
    pause 0.5

    window show
    "My eyes agree with my nose, only problem is to decide what to choose."
    "The buttery croissant (pleonasm) has a decent volume, but there is a also slight chance it's just empty."
    "In this regard, the pain au chocolat seems a safer option..."
    "Wait, what about the profiterole? It looks pretty substantial. But I run the risk of spilling pastry cream on the street...{w} Big deal."
    window hide None

    menu:
        "Hmm... What should I take?"
        "Croissant":
            pass
        "Pain au chocolat":
            pass
        "Profiterole":
            pass

    "Bah, let's just take all of them. The bill will cover it."
    mc "One croissant, one pain au chocolat and one profiterole, please."
    "I give the bill."
    baker "Here you go."

    show screen screen_item("coins", "center") with dissolve
    $ play_sfx("coins_drop")
    pause 0.5
    hide screen screen_item with dissolve
    pause 0.5

    window show None
    "I pick the food and the coins, and go back to the bus stop."
    window hide

    $ CompleteTask(task_BuyFood)
    $ CompleteTask(task_Coins)

    pause 0.5
    stop music fadeout 2.0

    jump s2_3
