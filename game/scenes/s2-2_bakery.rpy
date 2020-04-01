label s2_2:

# MC enters bakery and buys everything
label .shot1:
    $ store.time = "17:30"

    "My sense of smell finds a bakery nearby, so I walk in."

    play music store fadeout 1.0
    pause 1.0
    scene bakery with wipeup

    "My eyes agree with my nose, only problem is I don’t know what to choose."
    "The shining buttery croissant has a decent volume, but there is a chance it's empty inside."
    "The pain au chocolat would ensure a substantial snack, but so would the cream puff."

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
    "I get the items and go back to the bus stop."

    pause 0.5
    stop music fadeout 2.0

    jump s2_3
