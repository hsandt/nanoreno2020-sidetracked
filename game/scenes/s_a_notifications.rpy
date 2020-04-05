# call, not jump to this label, so you can come back
label s_a:
    show screen smartphone("notifications") with dissolve
    $ store.is_showing_smartphone = True

    if not has_seen_base_notifications:
        $ store.has_seen_base_notifications = True
        $ store.has_seen_space_left_since_last_change = True

        "New album released today, professional translators meetup tomorrow..."
        "But my main concern is that bunch of app updates I have been delaying for two weeks."
        "That, and the fact that I'm running out of storage space, with only [free_space] MB left."

        if sister_request_phase == 1:
            $ store.has_seen_sister_request = True
            "Oh, and it looks like my sister sent me a message. I hope it's not one of her shameless requests."
    else:
        $ store.found_interesting_notification = False
        if not has_updated_apps:
            $ store.found_interesting_notification = True
            "I still have a bunch of apps to update."
        if not has_freed_space:
            $ store.found_interesting_notification = True
            if not has_seen_space_left_since_last_change:
                $ store.has_seen_space_left_since_last_change = True
                "I only have [free_space] MB of space left."
            else:
                "I still only have [free_space] MB of space left."
        if sister_request_phase == 1:
            $ store.found_interesting_notification = True
            if not has_seen_sister_request:
                $ store.has_seen_sister_request = True
                "It looks like my sister sent me a message. I hope it's not one of her shameless requests."
            else:
                "I still haven't answered my sister."
        elif sister_request_phase == 2:
            $ store.found_interesting_notification = True
            "My sister has sent me another message."

        if not found_interesting_notification:
            "Nothing in particular catches my attention, so I put my phone back in my pocket."
            call .exit from _call_s_a_exit
            return

    menu:
        "What should I handle?"
        "Update apps" if not has_updated_apps:
            call s_b from _call_s_b_1
        "Free storage space" if not has_freed_space:
            $ free_space_context = "notifications"
            call s_c from _call_s_c_1
            $ free_space_context = None
        "Check sister message" if sister_request_phase == 1:
            call s_e from _call_s_e
        "Check sister reply" if sister_request_phase == 2:
            call s_e from _call_s_e_1
        "Nothing":
            "I don't see anything urgent and put the phone back in my pocket."
            call .exit from _call_s_a_exit_1
            return

    pause 0.5

    # Only one notification max per check
    # Although you can have more if you chain actions (update to play to free space...)
    random:
        "Anyway, let's go on with what we were doing."
        "That's one thing done. Time to get back on my main task."
        "With this done, I put my phone back in my pocket."

    # if checking notifications in the queue, customers behind get more impatient
    if notifications_context == "id":
        call increase_queuer_dissatisfaction

    call .exit
    return

label .exit:
    hide screen smartphone with dissolve
    $ store.is_showing_smartphone = False
    return
