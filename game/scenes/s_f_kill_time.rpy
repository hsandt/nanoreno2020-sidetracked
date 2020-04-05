# call, not jump to this label, so you can come back
label s_f:
    $ idle_choice_index = renpy.random.randint(0, 2)

    menu:
        "To kill the time, I..."
        "launch that mobile game I haven't tried yet." if has_tried_game_count == 0:
            call s_d from _call_s_d_1
        "continue playing the mobile game from earlier." if has_tried_game_count > 0 and not has_deleted_game:
            call s_d from _call_s_d_2
        "check my notifications.":
            "I check my notifications."
            $ notifications_context = "kill time"
            call s_a from _call_s_a_3
            $ notifications_context = None
        "twiddle my thumbs." if idle_choice_index == 0:
            "I wait, doing nothing special."
        "hum." if idle_choice_index == 1:
            "To pass the time, I hum a theme I've heard in a series, but I don't remember which one."
        "look around." if idle_choice_index == 2:
            "For a few minutes, I look around me and appreciate the aesthetics of my surroundings."

    return
