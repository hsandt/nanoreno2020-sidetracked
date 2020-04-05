label s3_3:

label .shot1:
    $ store.currentTime = "17:00"

    pause 1.0

    show mc regular at character_left with dissolve
    "After 20 minutes in the queue, I finally reach the permit printer. It’s a kind of Frankenstein’s monster assembled from a scanner, a camera, a speaker and a printer."
    "I select Purchase permit C on the touch screen."
    printer "Please show a proof of age: ID card or passport."

    $ StartTask(task_ID)

    "I search for my ID card and realize I left it at home. But there’s no way I come back empty-handed."
    "Fortunately, I got a scan of my ID card on my smartphone. This would never work on an airport-gateway-level device, but on this one it should."
    "I draw my smartphone to open the picture of the scan."

    $ has_notifications = has_outstanding_notifications()
    if has_notifications:
        "But I can't help peeking at the notifications."
        menu:
            "Should I check them out?"
            "Yes, check notifications":
                "Let's have a look."
                $ notifications_context = "id"
                call s_a from _call_s_a_4
                $ notifications_context = None
                "So, what was it? Right, the ID."
            "No, ignore them":
                "People are waiting behind me, I should focus on getting that permit printed."

    call check_file("id")

    # fallthrough to .shot2

label .shot2:
    "I find the scan of my ID card, and show it to the scanner. Hopefully it doesn’t care about watermarks or whatever."
    printer "...{w=1.0} ...{w=1.0} ...{w=1.0} Thank you."

    $ CompleteTask(task_ID)

    printer "Please face the camera and remove your glasses."
    "I follow the instructions."
    printer " ...{w=1.0} ...{w=1.0} Error. Face does not match photograph on proof of age."
    "I move the lock of hair hiding my eye."
    printer "...{w=1.0} Identification complete. Your permit will be issued in a moment."

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
