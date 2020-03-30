# call, not jump to this label, so you can come back
label s_c:
    if not has_deleted_small_apps:
        $ change_free_space(+60)
        $ store.has_deleted_small_apps = True

        "I start fiddling with my phone, trying to find which apps I can safely delete. I delete a few small apps and games, but I only free 60 MB. I now have [free_space] MB…"
        "I check the bigger apps I could get rid of."
    else:
        "I've already deleted small apps, so I immediately check the big ones left."

    if not has_tried_dict:
        "There is a dictionary app I've barely touched. I'd like to test it first, see if it's worth keeping."

    if not has_deleted_game:
        if not has_tried_game:
            "There is a game that takes quite a lot of memory, and I've never tried it. I should before I delete it."
        else:
            "There is that game I was playing earlier. It takes quite a lot of memory, so even if I didn't go far, I think it's worth deleting."
            "I can always redownload it and take my time to play it later (if some competitor hasn't showed up in the meantime)."

    menu try_choice:
        "What do I try or delete?"
        "Try the dictionary app" if not has_tried_dict:
            call s_c.shot2 from _call_s_c_shot2
        "Try the game" if not has_tried_game:
            $ store.play_context = "free space"
            call s_d from _call_s_d  # Play game
            $ store.play_context = None
            call s_c.shot3 from _call_s_c_shot3
        "Delete the game" if has_tried_game and not has_deleted_game:
            call s_c.shot3 from _call_s_c_shot3_1

    return

# Dictionary app
label .shot2:
    "I open the dictionary app and try a few words. Example sentences are incredible."
    "I already have 4 dictionary apps, but good examples are killer feature, so I'll keep this one as well."

    $ store.has_tried_dict = True

    "What else can I do?"
    call try_choice from _call_try_choice
    return

# Delete game
label .shot3:
    "I delete the game, and gain 1.5 GB. Wow, that should be enough!"

    $ change_free_space(+1500)
    $ store.has_deleted_game = True
    $ store.has_freed_space = True  # actually a synonym for has_deleted_game in this case, but clearer

    "I check if there are any other notifications left."
    call s_a

    return
