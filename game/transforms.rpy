init:
    transform character_left:
        xalign 0.2
        yalign 1.0

    transform character_move_left(duration=1.0):
        ease duration xalign 0.2
        yalign 1.0

    transform character_move_left_exit:
        easeout 0.8 xpos -0.5
        yalign 1.0

    transform character_right:
        xalign 0.8
        yalign 1.0

    transform character_move_right(duration=1.0):
        ease duration xalign 0.8
        yalign 1.0

    transform character_move_right_farther:
        easeout 0.2 xalign 0.85
        yalign 1.0

    transform character_move_right_exit:
        easeout 0.8 xpos 1.5
        yalign 1.0

    transform character_right_sit_down:
        ease 0.2 xalign 0.8
        easein 0.5 ypos 1.2

    transform character_right_sit_shake:
        ease 0.2 xalign 0.79
        ease 0.2 xalign 0.81
        repeat
        ypos 1.2

    transform character_stand_up:
        easein 0.5 yalign 1.0

    transform character_check_wallet:
        pause 0.4
        easein 0.4 yalign 1.1
        pause 0.2
        linear 0.2 yalign 1.0

    transform character_leg_beat(pause_duration=1.0):
        easein 0.5 yalign 1.1
        linear 0.1 yalign 1.0
        pause pause_duration
        repeat

    # not used anymore, we use pixel placement in screen_item
    transform item_left:
        xalign 0.3
        yalign 0.4

    transform item_center:
        xalign 0.5
        yalign 0.4

    transform item_right:
        xalign 0.7
        yalign 0.4
