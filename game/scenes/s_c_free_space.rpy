# call, not jump to this label, so you can come back
label s_c:
    # are we freeing space to get ID or just like that? show sub-tree / separate tree accordingly
    $ task_suffix = make_task_suffix(free_space_context) if free_space_context.startswith("check ") else ""
    $ StartTask(task_FreeSpace + task_suffix)

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
            $ task_suffix = make_task_suffix(free_space_context) if free_space_context.startswith("check ") else ""
            $ StartTask(task_DeleteGame + task_suffix)
            $ StartTask(task_PlayGame + task_suffix)

            $ store.play_context = "free space"
            call s_d from _call_s_d  # Play game

            $ CompleteTask(task_PlayGame + task_suffix)

            $ store.play_context = None
            call s_c.shot3 from _call_s_c_shot3
        "Delete the game" if has_tried_game and not has_deleted_game:
            call s_c.shot3 from _call_s_c_shot3_1

    return

# Dictionary app
label .shot2:
    show screen smartphone("dictionary") with dissolve

    $ task_suffix = make_task_suffix(free_space_context) if free_space_context.startswith("check ") else ""
    $ StartTask(task_DeleteDict + task_suffix)

    "I open the dictionary app and try a few words. Example sentences are incredible."
    "I already have 4 dictionary apps, but good examples are a killer feature, so I'll keep this one as well."

    $ FailTask(task_DeleteDict + task_suffix)

    $ store.has_tried_dict = True

    "What else can I do?"
    call try_choice from _call_try_choice
    return

# Delete game
label .shot3:
    # complete either Free Space sub-tree under Get ID node, or separate tree depending on context
    $ task_suffix = make_task_suffix(free_space_context) if free_space_context.startswith("check ") else ""

    "I delete the game, which gives me 1.5 GB extra space. Wow, that should be enough!"

    $ CompleteTask(task_DeleteGame + task_suffix)
    $ CompleteTask(task_FreeSpace + task_suffix)

    $ change_free_space(+1500)
    $ store.has_deleted_game = True
    $ store.has_freed_space = True  # actually a synonym for has_deleted_game in this case, but clearer

    return

# a wrapper for the free space scene, that will only trigger free space if smartphone is too slow
# if a bit slow, it will only mention it
label check_file(file_name):
    if free_space <= 300:
        show screen smartphone("notifications") with dissolve
        $ store.is_showing_smartphone = True

        # has_updated_apps should be True at this point, hence the thought
        "I navigate through my files, but it’s very slow. Probably because I only have [free_space] MB left."
        "I guess updating all my apps while running out of storage space was not a good idea. I need to free some now."

        $ free_space_context = "check " + file_name
        call s_c
        $ free_space_context = None

        "With space being freed, I resume searching for the file I want."

        hide screen smartphone with dissolve
        $ store.is_showing_smartphone = False

        return
    elif free_space <= 400:
        "I navigate through my files, but it's a bit slow. Maybe freeing some space would help. It's not critical though, so I go on."
        return
    else:
        return
