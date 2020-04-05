label s2_2:

# MC enters bakery and buys everything
label .shot1:
    $ store.currentTime = "14:30"
    $ store.wrapping_scene = "bakery"

    play sound store_door_open
    scene bakery with CropMove(1.5, "wipeleft")
    play music store fadeout 1.0
    pause 1.0

    play sound store_door_close
    pause 0.5

    window show
    "My eyes agree with my nose, only problem is I don’t know what to choose."
    "The shining buttery croissant has a decent volume, but there is a chance it's empty inside."
    "The pain au chocolat would ensure a substantial snack, but so would the cream puff."
    window hide None

    menu:
        "Hmm… What do I take?"
        "Croissant":
            pass
        "Pain au chocolat":
            pass
        "Cream puff":
            pass

    "I check the items' prices, and all are quite cheap. I'm sure I could get a few with a single bill and still have coins left for the bus."
    mc "One croissant, one pain au chocolat and one cream puff, please."

    show screen screen_item("coins", "center") with dissolve
    play sound coins_drop
    pause 0.5
    hide screen screen_item with dissolve
    pause 0.5

    window show None
    "I get the food and the coins from the difference, then go back to the bus stop."
    window hide

    $ CompleteTask(task_BuyFood)
    $ CompleteTask(task_Coins)

    pause 0.5
    stop music fadeout 2.0

    jump s2_3
