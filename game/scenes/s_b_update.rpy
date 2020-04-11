# call, not jump to this label, so you can come back
label s_b:
    "I see 14 updates pending."
    "I carefully select which apps to update based on how much I use them."
    if has_wifi:
        "Hopefully that will help download faster while also saving some space."
    else:
        "Hopefully that will help reduce my data usage while also saving some space."
    "After the fourth manual update, I get impatient and just touch “Update all”."

    $ store.has_updated_apps = True
    $ change_free_space(-100)

    if has_wifi:
        "Fortunately, it downloads pretty fast on Wi-Fi."
        if not has_freed_space:
            "It takes a lot of space though. I now have only [free_space] MB left."
        $ store.currentTime += 7
    else:
        "I'm on 4G, so I hope it won't blow up my data consumption. Apparently, there are around 100 MB of updates."
        if update_context == "play game":
            "It's very slow, but I take on myself and wait."
            $ store.currentTime += 17
        else:
            "It's very slow... I'll let that happen in the background."
            $ store.currentTime += 8

    if wrapping_scene == "bus_stop" and currentTime > next_bus_time:
        # can only happen when freeing space and trying dict before game
        # clamp time
        $ store.currentTime = store.next_bus_time
        "But it doesn't even end before I see the bus coming, so I let the rest update in the background."

    return
