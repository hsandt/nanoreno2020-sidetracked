label s3_1:

label .shot1:
    $ store.currentTime = "16:00"
    $ store.wrapping_scene = "store"

    scene overlay black with Dissolve(1.0)

    play sound store_door_open
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: automatic door opens")

    pause 1.0

    scene bg store with Dissolve(1.0)
    play music store
    show mc regular at character_left with dissolve

    play sound store_door_close
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: automatic door closes")

    window show
    "I start searching for a hexagonal key or screwdriver."
    window hide None

    $ StartTask(task_FindHexKey, notify=True)

    "As I walk past the aisles, I glance at the signs: \"Hammers & Mallets\", \"Keys & Locks\", \"Painting\"..."
    "Eventually, I see two categories that seem fit: \"Screwdrivers & Nut Drivers\", and \"Power Screwdrivers\". Where should I go first?"

    $ StartTask(task_CheckScrewdrivers)

    menu choose_category:
        "Screwdrivers & Nut Drivers" if not has_explored_screwdrivers:
            jump s3_1.shot2a
        "Power Screwdrivers" if not has_explored_power_screwdrivers:
            jump s3_1.shot2b

# Screwdrivers & Nut Drivers
label .shot2a:
    "I walk along the shelves in the \"Screwdrivers & Nut Drivers\" area. They are full of interesting labels like Slot, Cross, Frearson and Torx... But I see no hex."
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
        call check_file("photo")
        "Once I find it, I search the matching key on the shelf using my finger as reference scale."
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
