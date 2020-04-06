label s3_3:

label .shot1:
    $ store.currentTime = "17:00"

    pause 1.0

    show mc regular at character_left with dissolve
    "After spending 20 minutes in the queue, I finally reach the permit printing machine."
    "It has a touch screen where you can select various types of documents. I touch \"Purchase Permit: Category C\"."
    printer "Please enter your date of birth."
    "Entered."
    printer "Please provide your Health Insurance Number."

    $ StartTask(task_HealthNumber)
    pause 1.0

    show mc at character_check_wallet

    "I search for my Health Insurance card, and realize I left it at home. But there’s no way I come back empty-handed."
    "Fortunately, I have my Health Number somewhere on my phone. I grab it, trying to remember in which file it's written."

    $ has_notifications = has_outstanding_notifications()
    if has_notifications:
        "But I can't help peeking at the notifications."
        menu:
            "Should I check them out?"
            "Yes, check notifications":
                "Let's have a look."
                $ notifications_context = "health no"
                call s_a from _call_s_a_4
                $ notifications_context = None
                "So, what was it? Right, the ID."
            "No, ignore them":
                "People are waiting behind me, I should focus on getting that permit printed."

    call check_file("health no") from _call_check_file_1

    # fallthrough to .shot2

label .shot2:
    "I find the Health Insurance Number, and enter it in the machine."
    printer "...{w=1.0} Thank you. Your permit will be issued in a moment."

    $ CompleteTask(task_HealthNumber)

    play sound printer
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: printer")
    pause 3.0

    show screen screen_item("purchase_permit", "right") with dissolve
    pause 1.0

    "I pick the permit, and go back to the register."
    $ CompleteTask(task_Permit)

    stop sound
    hide screen screen_item with dissolve

    hide mc with dissolve

    jump s3_4

label increase_queuer_dissatisfaction:
    pause 0.5

    $ store.queuer_dissatisfaction += 1
    if queuer_dissatisfaction == 1:
        "I feel growing dissatisfaction in the queue behind me."
        "Aha, sorry. I'm really grateful for your patience, guys."
    else:  # == 2
        "Now customers queuing behind me are really getting impatient."
        "Oops, I think it's time I print that permit."
