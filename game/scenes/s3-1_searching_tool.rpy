label s3_1:

label .shot1:
    $ store.currentTime = "16:00"
    $ store.wrapping_scene = "store"

    scene bg store with Dissolve(1.0)
    play music store
    show mc regular at character_left with dissolve

    $ StartTask(task_FindHexKey)

    window show
    "As I walk past the aisles, I glance at the signs: \"Hammers & Mallets\", \"Keys & Locks\", \"Painting\"..."
    "Eventually, I see two categories that seem fit: \"Screwdrivers & Nut Drivers\", and \"Power Screwdrivers\". Where should I go first?"
    window hide None

    $ StartTask(task_CheckScrewdrivers)

    menu choose_category:
        "Screwdrivers & Nut Drivers" if not has_explored_screwdrivers:
            jump s3_1.shot2a
        "Power Screwdrivers" if not has_explored_power_screwdrivers:
            jump s3_1.shot2b

# Screwdrivers & Nut Drivers
label .shot2a:
    "I walk along the shelves in the \"Screwdrivers & Nut Drivers\" area. They are full of interesting labels like Slot, Cross, Frearson and Torx... But I see no hex."
    "Except for those drivers that remove hexagonal nuts, but they are not what I need."
    $ store.has_explored_screwdrivers = True

    if has_explored_screwdrivers and has_explored_power_screwdrivers:
        jump .shot3

    "Where should I go next?"
    jump choose_category

# Power Screwdrivers
label .shot2b:
    "The \"Power Screwdrivers\" area is full of electric screwdrivers. And also drills. Curious."
    "I realize those tools may be a bit too much for what I want to do. I’ll let grease elbow do the job this time."
    $ store.has_explored_power_screwdrivers = True

    if has_explored_screwdrivers and has_explored_power_screwdrivers:
        jump .shot3

    "Where should I go next?"
    jump choose_category

label .shot3:
    $ FailTask(task_CheckScrewdrivers)

    "Unable to find the right tool in the most meaningful places, I start wandering around."

    $ StartTask(task_CheckOthers)

    "After some time I reach the \"Keys & Locks\" area, where they put digit padlocks, padlocks with keys... and of course, hex keys. Logical."

    if screw_measurement_method == "photo":
        "I check the photo of the loose screw on my phone to make sure I pick the right key."
        if not has_freed_space:
            "I notice that navigating in my pictures is a bit slow."
            if has_seen_base_notifications:
                "I guess it's because I'm lacking free space."
        "While I'm at it, I glance at the notifications on my phone."
        call s_a from _call_s_a
        "Where was I? Oh yeah, the screw."
    else:
        "I check the loose screw’s dimensions in my notepad to make sure I pick the right key."

    play sound searching_drawer
    pause 1.0

    show screen screen_item("hex_key", "right") with dissolve
    "I find the right key in the middle of the mess."
    hide screen screen_item with dissolve
    hide item

    "I grab it and rush to the cash register."
    $ CompleteTask(task_CheckOthers)
    $ CompleteTask(task_FindHexKey)

    hide mc with dissolve
    pause 1.0

    jump s3_2
