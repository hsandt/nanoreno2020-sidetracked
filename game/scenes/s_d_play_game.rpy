# call, not jump to this label, so you can come back
label s_d:

# Start
label .shot1:
    show screen smartphone("notifications") with dissolve
    $ store.is_showing_smartphone = True

    if not has_updated_apps:
        "As soon as I launch the game, an update pop-up requests me to download the latest patch."
        if play_context == "free space":
            "That's 100 MB. So I must lose space in order to free space? Neat."
        "Anyway, I can't do that from the game though, so I go to the application store."
        $ store.update_context = "play game"
        call s_b from _call_s_b  # Update
        $ store.update_context = None
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
    "I go to the form to create an account from scratch. I need to find a cool username and a tricky password."

    "Username is no problem, but passwords are a bit more complex."
    "In general, I build them from funny sentences that are easy to remember, that I turn into a series of related words or emojis."

    menu:
        "What should I use this time?"
        "Capharnaum in the square marketplace":
            "\"Capharnaum in the square marketplace\"
            {p=1.0}OK, so that will make... \"K-far# >x< ZA \[_\]$<->$\""
        "Sixty-six zebras ate a watermelon salad":
            "\"Sixty-six zebras ate a watermelon salad\"
            {p=1.0}Fine, that should turn into... \"6T6//// *nom*nom* 1~~~mLnsLd\""
        "The principal broke into the hair salon riding a motorbike":
            "\"The principal broke into the hair salon riding a motorbike\"
            {p=1.0}I can change it for... \"Ma1n NO$->//II\\\\ >8 o<o\""

    "Hey, it's not too complicated this time. I even kept it under 30 characters."
    "I create my account using that password, and start playing."
    return

label .shot4:
    show screen smartphone("game") with dissolve
    $ store.is_showing_smartphone = True

    play music game fadein 0.5
    pause 2.0

    if play_context == "free space":
        "The game is... actually quite interesting. But there is a lot to do, so it's hard for me to tell if it's worth going on or not."
        "If I try to see more of it, I may never be able to delete it. Maybe I should delete it now, and re-install it later."
        "My account should preserve my save until next time I play..."
        "Assuming that in the meantime, servers are not shut down, with some competitor making all of it obsolete -_-'"
        stop music fadeout 1.5
        "After a few more minutes, I end my session."
        show screen smartphone("notifications") with dissolve
    elif not has_tried_game:
        "The game is... actually quite interesting. Placing your characters the right way helps you finish the fights much more quickly."
        "But I don't feel in danger enough, so I don't feel the need to improve. Even after many mistakes I still have plenty of health."
        "Also, numbers are a bit mind blowing. Is it normal that I'm still at level 3 and yet dealing 6,187 damage in one attack?"
        "Well, I guess it's all relative..."
        pause 1.0
        stop music fadeout 1.5
        "After a few more fights, I end my session."
        hide screen smartphone with dissolve
        $ store.is_showing_smartphone = False
    else:
        "I resume my session where I left it, and go over a few missions."
        "Hmm... There are really, many, many characters. I'm glad I don't have to name every of them."
        pause 2.0
        stop music fadeout 1.5
        "After a few missions, I end my session."
        hide screen smartphone with dissolve
        $ store.is_showing_smartphone = False

    $ store.has_tried_game = True

    call .restore_bgm

    return

label .restore_bgm:
    if wrapping_scene == "broken_chair":
        play music apartment
    elif wrapping_scene == "bus_stop":
        play music "<loop 19.287>audio/bgm/ambient_street.ogg"
    elif wrapping_scene == "bakery":
        play music store
    elif wrapping_scene == "bus":
        play music "<loop 19.287>audio/bgm/ambient_street.ogg"
    elif wrapping_scene == "store":
        play music store
    elif wrapping_scene == "light_bulb":
        pass
