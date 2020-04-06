# call, not jump to this label, so you can come back
label s_c:
    # are we freeing space to get ID or just like that? show sub-tree / separate tree accordingly
    $ task_suffix = make_task_suffix(free_space_context)
    $ StartTask(task_FreeSpace + task_suffix)

    if not has_deleted_small_apps:
        $ change_free_space(+40)
        $ store.has_deleted_small_apps = True

        "I start fiddling with my phone, trying to find which apps I can safely delete. I delete a few small apps and games, but I only free 40 MB. I now have [free_space] MB..."
        "I check the bigger apps I could get rid of."
    else:
        "I've already deleted small apps, so I immediately check the big ones left."

    if not has_tried_dict:
        "There is a Japanese dictionary app I've barely touched. I'd like to test it first, see if it's worth keeping."

    if not has_deleted_game:
        if has_tried_game_count == 0:
            "There is a mobile game that takes quite a lot of memory, and I've never tried it. I should before I delete it."
        else:
            "There is that mobile game I was playing earlier. I could delete it and re-download it later, or try it one more time first."

    # allow trying once more

    menu try_choice:
        "What do I try or delete?"
        "Try the dictionary app" if not has_tried_dict:
            call s_c.shot2 from _call_s_c_shot2
        "Try the game" if has_tried_game_count == 0:
            call s_c.try_game from _call_s_c_try_game
        "Try the game once more" if has_tried_game_count > 0 and not has_deleted_game:
            call s_c.try_game from _call_s_c_try_game_1
        "Delete the game" if has_tried_game_count > 0 and not has_deleted_game:
            call s_c.shot3 from _call_s_c_shot3_1

    return

label .try_game:
    $ task_suffix = make_task_suffix(free_space_context)
    $ StartTask(task_DeleteGame + task_suffix)
    $ StartTask(task_PlayGame + task_suffix)

    $ store.play_context = "free space"
    call s_d from _call_s_d  # Play game

    $ CompleteTask(task_PlayGame + task_suffix)

    $ store.play_context = None
    call s_c.shot3 from _call_s_c_shot3
    return

# Dictionary app
label .shot2:
    show screen smartphone("dictionary") with dissolve

    $ task_suffix = make_task_suffix(free_space_context)
    $ StartTask(task_DeleteDict + task_suffix)

    "I open the dictionary app and try a few words. Example sentences are incredible."
    "I already have 4 dictionaries for Japanese, but good examples are a killer feature, so I'll keep this one as well."

    $ FailTask(task_DeleteDict + task_suffix)

    $ store.has_tried_dict = True

    $ store.currentTime += 9

    show screen smartphone("notifications") with dissolve

    "What else can I do?"
    call try_choice from _call_try_choice
    return

# Delete game
label .shot3:
    # complete either Free Space sub-tree under Get ID node, or separate tree depending on context
    $ task_suffix = make_task_suffix(free_space_context)

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
    if free_space <= 340:
        show screen smartphone("notifications") with dissolve
        $ store.is_showing_smartphone = True

        if not has_navigated_very_slowly:
            $ store.has_navigated_very_slowly = True
            # has_updated_apps should be True at this point, hence the thought
            "I navigate through my files, but it’s very slow. Probably because I only have [free_space] MB left."
            "I guess updating all my apps while running out of storage space was not a good idea."
            $ store.currentTime += 8

            # the first time (for photo), you can push through one more time without freeing space
            menu:
                "Should I free space now or go on like that?"
                "Free space":
                    call .free_space_to_check(file_name) from _call_check_file_free_space_to_check
                "Go on":
                    "I take on myself and spend a few minutes browsing files very slowly."
                    $ store.currentTime += 8
        else:
            "Navigating among files is still very slow. This time it won't cut, I need to free some space!"
            $ store.currentTime += 6
            call .free_space_to_check(file_name) from _call_check_file_free_space_to_check_1

        hide screen smartphone with dissolve
        $ store.is_showing_smartphone = False

        return
    elif free_space <= 400:
        if not has_navigated_slowly:
            "I navigate through my files, but it's a bit slow. Maybe freeing some space would help. It's not critical though, so I go on."
            $ store.has_navigated_slowly = True
        else:
            "I navigate through my files, but it's a bit slow again."
        $ store.currentTime += 5
        return
    else:
        $ store.currentTime += 2
        return

label .free_space_to_check(file_name):
    $ free_space_context = "check " + file_name
    call s_c from _call_s_c
    $ free_space_context = None

    pause 0.5

    if file_name == "health no":
        call increase_queuer_dissatisfaction from _call_increase_queuer_dissatisfaction_1

    "With space being freed, I resume searching for the file I want. It's much faster!"
    return
