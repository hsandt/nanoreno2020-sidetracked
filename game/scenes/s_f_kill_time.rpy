# call, not jump to this label, so you can come back
label s_f:
    menu:
        "To kill the time, I..."
        "launch that mobile game I haven't tried yet." if has_tried_game_count == 0:
            call s_d from _call_s_d_1
        "continue playing the mobile game from earlier." if has_tried_game_count > 0 and not has_deleted_game:
            call s_d from _call_s_d_2
        "check my notifications.":
            "I check my notifications."
            call s_a from _call_s_a_3

    return
