# call, not jump to this label, so you can come back
label s_d:

# Start
label .shot1:
    if not has_updated_apps:
        "As soon as I launch the game, an update pop-up requests me to download the latest patch."
        if play_context == "free space":
            "That's 100 MB. So I must lose space in order to free space? Neat."
        "Anyway, I can't do that from the game though, so I go to the application store."
        $ update_context = "play game"
        call s_b from _call_s_b  # Update
        $ update_context = None
    else:
         "I've already updated all the apps earlier, so I can play the latest patch of the game."

    if not has_tried_game:
        "I'm welcomed by a login window, which asks me to create an account, with password and all. I guess it's because it's fundamentally an online game."
        "Fortunately, I can also sign up with a Google or Twitter account. Ah, but maybe I should avoid linking my stuff to big companies and SNS..."

        menu:
            "How do I sign up?"
            "Create a linked account":
                call .shot2 from _call_s_d_shot2
            "Be a rebel and create an account from scratch":
                call .shot3 from _call_s_d_shot3

    call .shot4 from _call_s_d_shot4
    return

# Link account
label .shot2:
    "I use the easy sign up and start playing."
    return

# From scratch
label .shot3:
    "I go to the form to create an account from scratch."
    "I need to find a cool username and a tricky password."

    "In general, I build my passwords from funny sentences that are easy to remember, that I turn into a series of related words or emojis."

    menu:
        "What should I use this time?"
        "Capharnaum in the square marketplace":
            "\"Capharnaum in the square marketplace\""
        "OK, so that will make... \"K-far# >x< ZA \[_\]$<->$\""
        "Sixty-six zebras ate a watermelon salad":
            "\"Sixty-six zebras ate a watermelon salad\""
            "Fine, that should turn into... \"6T6//// *nom*nom* 1~~~mLnsLd\""
        "The principal broke into the hair salon riding a motorbike":
            "\"The principal broke into the hair salon riding a motorbike\""
            "I can change it for... \"Ma1n NO$->//II\\\\ >8 o<o\""

    "Hey, it's not too complicated this time. I even kept it under 30 characters."
    "I create my account using that password, and start playing."
    return

label .shot4:
    $ has_tried_dict = True

    if play_context == free_space:
        "The game is... okay. There is a lot to do, so it's hard for me to tell if it's worth going on or not."
        "But if it's so long, I might as well take my time and play it later (if some competitor hasn't showed up in the meantime). So I think I can safely delete it for now."
    elif not has_tried_game:
        "The game is... okay. There is a lot to do, so I guess I can continue playing a bit later."
    else:
        "I resume my session where I left it, and go over a few missions. Is it normal that I'm at level 3 and I'm dealing, like, 6,187 damage every attack?"
        "Well, I guess that's just a number, but it's a bit hard for me to understand how really strong it is so early in the game."
    return