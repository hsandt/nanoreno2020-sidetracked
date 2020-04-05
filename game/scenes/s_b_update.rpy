# call, not jump to this label, so you can come back
label s_b:
    "I see 14 updates pending."
    "I carefully select which apps to update based on how much I use them."
    if has_wifi:
        "Hopefully that will help download faster while also saving some space."
    else:
        "Hopefully that will help reduce my data usage while also saving some space."
    "After the fourth manual update, I get impatient and just touch \"Update all\"."

    $ store.has_updated_apps = True
    $ change_free_space(-100)

    if has_wifi:
        "Fortunately, it downloads pretty fast on Wi-Fi."
        if not has_freed_space:
            "It takes a lot of space though. I now have only [free_space] MB left."
    else:
        "I'm on 4G, so I hope it won't blow up my data consumption. Apparently, there are around 100 MB of updates."
        if update_context == "play game":
            "It's very slow, but I take on myself and wait. When the update is over, I finally run the game again."
        else:
            "It's very slow… I'll let that happen in the background."

    return
