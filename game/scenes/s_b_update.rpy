# call, not jump to this label, so you can come back
label s_b:
    "I check the app updates. There are 14 of them."
    "I carefully select which apps to update based on how much I use them."
    "Hopefully that will help reduce my data usage while also saving some space."
    "After the fourth manual update, I get impatient and just touch \"Update all\"."

    if has_wifi:
        "Fortunately, it downloads pretty fast on Wi-Fi."
        if not has_freed_space:
            "It takes a lot of space though. I now have only [free_space] MB left."
    else:
        "I download on 4G, hoping it won't blow up my data consumption."
        if update_context == "play game":
            "It's very slow, but I take on myself and wait. When the update is over, I finally run the game again."
        else:
            "It's very slow… I'll let that happen in the background."

    $ has_updated_apps = True
    $ free_space -= 100

    if update_context == "play game":
        return

    "I check if there are any other notifications left."
    call s_a from _call_s_a_1
    return