label s3_3:

label .shot1:
    pause 1.0

    show mc regular at character_left with dissolve
    "After 20 minutes in the queue, I finally reach the permit printer. It’s a kind of Frankenstein’s monster assembled from a scanner, a camera, a speaker and a printer."
    "I select Purchase permit C on the touch screen."
    printer "Please show a proof of age: ID card or passport."
    "I search for my ID card and realize I left it at home. But there’s no way I come back empty-handed."
    "Fortunately, I got a scan of my ID card on my smartphone. This would never work on an airport-gateway-level device, but on this one it should."
    "I draw my smartphone to open the picture of the scan."

    if not has_freed_space:
        menu:
            "But the phone notifies me that there is very little space left."
            "Free space now":
                call sa_2 from _call_sa_2_1
                "With space being freed, I resume searching for my ID scan."
                jump .shot3
            "Ignore":
                jump .shot2
    else:
        jump .shot3

label .shot2:
    "I try to navigate to the file I need, but it’s very slow. I guess I really need to free space now."
    call sa_2 from _call_sa_2_2
    "That should be enough. I search the scan picture again."

label .shot3:
    "I find the scan of my ID card, and show it to the scanner. Hopefully it doesn’t care about watermark or whatever."
    printer "...{w=1.0} ...{w=1.0} ...{w=1.0} Thank you."
    printer "Please face the camera and remove your glasses."
    "I follow the instructions."
    printer " ...{w=1.0} ...{w=1.0} Error. Face does not match photograph on proof of age."
    "I move the lock of hair hiding my eye."
    printer "...{w=1.0} Identification complete. Your permit will be issued in a moment."

    play sound printer
    # SFX accessibility (inspired by Renpy Accessibility Add-On)
    $ renpy.notify("SFX: printer")
    pause 3.0

    show item purchase_permit at item_right with dissolve
    pause 1.0

    "I pick the permit, and go back to the register."
    stop sound
    hide item with dissolve

    hide mc with dissolve

    jump s3_4
