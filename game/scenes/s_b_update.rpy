# call, not jump to this label, so you can come back
label s_b:
    "I see 14 updates pending. I carefully select which apps to update based on how much I use them."
    if has_wifi:
        "Hopefully, that will help download faster and save some space."
    else:
        "Since I'm on 4G, I'd better be careful with my data usage."
    pause 1.0
    "After the fourth manual update, I get impatient and just touch “Update all”. I know, I know."

    $ store.has_updated_apps = True
    $ change_free_space(-100)

    if has_wifi:
        "There are around 100 MB of updates. Fortunately, it downloads pretty fast on Wi-Fi."
        if not has_freed_space:
            "It takes a lot of space though. I now have only [free_space] MB left."
        $ store.currentTime += 7
    else:
        "There are around 100 MB of updates. Actually, my phone plan should be able to handle that."
        pause 0.5
        if update_context == "play game":
            "It's very slow, but I take on myself and wait until I can play the game."
            $ store.currentTime += 17
        else:
            "It's very slow... I'll let that happen in the background."
            $ store.currentTime += 8

    pause 0.5
    if wrapping_scene == "bus_stop" and currentTime > next_bus_time:
        # can only happen when freeing space and trying dict before game
        # clamp time
        $ store.currentTime = store.next_bus_time
        "But it doesn't even end before I see the bus coming, so I let the rest update in the background."

    return
