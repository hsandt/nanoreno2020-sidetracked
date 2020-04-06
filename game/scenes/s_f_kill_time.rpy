# call, not jump to this label, so you can come back
label s_f:
    $ idle_choices = [
        "I wait, doing nothing special.",
        "To pass the time, I hum a theme I've heard in a series, although I don't remember which one.",
        "For a few minutes, I look around me and appreciate the aesthetics of my surroundings."
    ]
    $ idle_choice_index = renpy.random.randint(0, 2)
    $ picked_idle_choice = False

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
            $ picked_idle_choice = True
        "hum." if idle_choice_index == 1:
            $ picked_idle_choice = True
        "look around." if idle_choice_index == 2:
            $ picked_idle_choice = True

    if picked_idle_choice:
        $ idle_choice = idle_choices[idle_choice_index]
        if is_character_sprite_displayed():
            show mc at character_leg_beat
        $ renpy.say(adv, idle_choice)
        if is_character_sprite_displayed():
            show mc at character_stand_up
        $ store.currentTime += 8

    return
