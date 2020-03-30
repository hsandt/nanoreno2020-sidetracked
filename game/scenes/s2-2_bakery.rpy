label s2_2:

# MC enters bakery and buys everything
label .shot1:
    "My sense of smell finds a bakery nearby, so I walk in. My eyes agree with my nose, only problem is I don’t know what to choose."

    "The shining buttery croissant has a decent volume, but some are really empty inside."
    "The pain au chocolat would ensure a substantial snack, but so would the cream puff."

    menu:
        "Hmm… What do I take?"
        "Croissant":
            pass
        "Pain au chocolat":
            pass
        "Cream puff":
            pass

    "I check the item’s price, but realize my bill will cover much more than that. Even with one bus return ticket, I would have many coins left."
    mc "One croissant, one pain au chocolat and one cream puff, please."
    "I get the items and go back to the bus stop."

    jump s2_3
