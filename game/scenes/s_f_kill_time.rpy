# call, not jump to this label, so you can come back
label s_f:
    $ idle_choice_index = renpy.random.randint(0, 2)
    $ picked_idle_choice = False

    menu:
        "To kill the time, I..."
        "play that mobile game I've never tried." if has_tried_game_count == 0:
            $ store.play_context = "kill time"
            call s_d from _call_s_d_1
            $ store.play_context = None
        "continue playing the mobile game from earlier." if has_tried_game_count > 0 and not has_deleted_game:
            $ store.play_context = "kill time"
            call s_d from _call_s_d_2
            $ store.play_context = None
        "check my notifications.":
            "I check my notifications."
            $ notifications_context = "kill time"
            call s_a from _call_s_a_3
            $ notifications_context = None
        "twiddle my thumbs." if idle_choice_index == 0:
            $ picked_idle_choice = True
        "hum a tune." if idle_choice_index == 1:
            $ picked_idle_choice = True
        "look around." if idle_choice_index == 2:
            $ picked_idle_choice = True

    if picked_idle_choice:
        if is_character_sprite_displayed():
            show mc at character_leg_beat
        $ renpy.call("s_f.idle_choice%d" % idle_choice_index)
        if is_character_sprite_displayed():
            show mc at character_stand_up
        $ store.currentTime += 8

    return

label .idle_choice0:
    "I wait, doing nothing special."
    return

label .idle_choice1:
    "I start humming a theme I've heard in a series, but I don't remember which one."
    "Wasn't it that bird-themed Super Sentai from the nineties? For some reason the French opening is stuck in my head."
    return

label .idle_choice2:
    "For a few minutes, I look around me and appreciate the aesthetics of my surroundings."
    return
