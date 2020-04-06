# call, not jump to this label, so you can come back
label s_d:

# Start
label .shot1:
    show screen smartphone("notifications") with dissolve
    $ store.is_showing_smartphone = True

    if not has_updated_apps:
        "As soon as I launch the game, an update pop-up requests me to download the latest patch."

        # only show task tree / sub task tree for UpdateApps if freeing space
        # else, when we really want to free space, just skip any task already done
        if play_context == "free space":
            $ task_suffix = make_task_suffix(free_space_context)
            $ StartTask(task_UpdateApps + task_suffix)

        if play_context == "free space":
            "That's 100 MB. So I must lose space in order to free space? Neat."
        "Anyway, I can't do that from the game though, so let's go to the update screen."
        $ store.update_context = "play game"
        call s_b from _call_s_b  # Update
        $ store.update_context = None

        if play_context == "free space":
            $ CompleteTask(task_UpdateApps + task_suffix)
    elif has_tried_game_count == 0:
        "I've already updated all the apps earlier, so I can play the latest patch of the game."

    if has_tried_game_count == 0:
        "I'm welcomed by a login window, which asks me to create an account, with password and all."
        "I guess it's because it's fundamentally an online game."

        # complete either Free Space sub-tree under Get ID node, or separate tree depending on context
        if play_context == "free space":
            $ task_suffix = make_task_suffix(free_space_context)
            $ StartTask(task_CreateAccount + task_suffix)

        "Fortunately, I can also sign up with a Google or Twitter account. Ah, but maybe I should avoid linking my stuff to big companies..."

        menu:
            "How do I sign up?"
            "Create a linked account":
                call .shot2 from _call_s_d_shot2
            "Be a rebel and create an account from scratch":
                call .shot3 from _call_s_d_shot3

        if play_context == "free space":
            $ CompleteTask(task_CreateAccount + task_suffix)

    call .shot4 from _call_s_d_shot4
    return

# Link account
label .shot2:
    "I use the easy sign up and start playing."
    return

# From scratch
label .shot3:
    "I go to the form to create an account from scratch. I need to find a cool username and a tricky password."

    # complete either Free Space sub-tree under Get ID node, or separate tree depending on context
    if play_context == "free space":
        $ task_suffix = make_task_suffix(free_space_context)
        $ StartTask(task_InventPassword + task_suffix)

    "Username is no problem, but passwords are a bit more complex."
    "In general, I build them from funny sentences that are easy to remember, that I turn into a series of related words or emojis."

    menu:
        "What should I use this time?"
        "Capharnaum in the square marketplace":
            "{i}Capharnaum in the square marketplace{/i}...
            {p=1.0}OK, so that will make...
            {p=1.0}\"K-far# >x< ZA \[_\]$<->$\""
        "Sixty-six zebras ate a watermelon salad":
            "{i}Sixty-six zebras ate a watermelon salad{/i}...
            {p=1.0}Fine, that should turn into...
            {p=1.0}\"6T6//// *nom*nom* 1~~~mLnsLd\""
        "The principal broke into the hair salon riding a motorbike":
            "{i}The principal broke into the hair salon riding a motorbike{/i}...
            {p=1.0}I can change it for...
            {p=1.0}\"Ma1n NO$->//II\\\\ >8 o<o\""

    if play_context == "free space":
        $ CompleteTask(task_InventPassword + task_suffix)

    "Hey, it's not too complicated this time. I even kept it under 30 characters."
    "I create my account using that password, and start playing."

    return

label .shot4:
    show screen smartphone("game") with dissolve
    $ store.is_showing_smartphone = True

    $ play_music("game", fadeout=0.8, fadein=0.8)
    pause 1.5

    if has_tried_game_count > 0:
        "I resume my session where I left it, and go over a few missions."

        if has_tried_game_count == 1:
            "The setting is funny. The remorses of dead people come from the future, shaped as monsters."
            "They attack people in the present to prevent them from the doing the same kind of mistakes."
            "But there are really, many, many characters. I'm glad I don't have to name every of them."
        elif has_tried_game_count == 2:
            "How many times have I played this game today? I almost feel guilty it's a free-to-play."
            "Maybe I should drop some money on it... But I don't have a sense of {i}money versus time{/i} good enough to know what's worth what."
            "Some may say that I don't have a good sense of time, period. But that's not it, I simply do as much as I can in the allocated time."

        if play_context == "free space":
            pause 0.5
            "OK, I think I've played enough to have a good idea of what the game is about."
            "I don't think I'll play much more, so I can delete when I'm done."

        pause 1.5
        stop music fadeout 1.5
        "After a few missions, I end my session."
    elif play_context == "free space":
        "It's a tactical role-playing game, and actually quite interesting. But there is a lot to do, so it's hard for me to tell if it's worth going on or not."
        "I think I can delete it now, and if I change my mind, reinstall it later."
        "My account should preserve my save until next time I play..."
        "Assuming that in the meantime, servers are not shut down, with some competitor making all of it obsolete -_-'"
        stop music fadeout 1.5
        "After a few more minutes, I end my session."
    else:
        "It's a tactical role-playing game, and actually quite interesting. Placing your characters the right way helps you finish the fights much more quickly."
        "But I don't feel in danger enough, so I don't feel the need to improve. Even after many mistakes I still have plenty of health."
        "Also, numbers are a bit mind blowing. Is it normal that I'm still at level 3 and yet dealing 6,187 damage in one attack?"
        "Well, I guess it's all relative..."
        pause 1.0
        stop music fadeout 1.5
        "After a few more fights, I end my session."

    if play_context == "free space":
        # we were just freeing space, so come back to notifications instead of hiding smartphone altogether
        show screen smartphone("notifications") with dissolve
    else:
        hide screen smartphone with dissolve
        $ store.is_showing_smartphone = False

    $ store.has_tried_game_count += 1

    call restore_bgm from _call_s_d_restore_bgm

    return
