label ending1:
    pause 1.0
    window show None
    "Sidetracked{w=1.4} - END{w=1.7} - Deserved rest"
    window hide
    jump end

label ending2:
    pause 1.0
    window show None
    "Sidetracked{w=1.4} - END{w=1.7} - Just one more time"
    window hide
    jump end

label end:
    pause 0.5
    $ quick_menu = False
    show overlay black with dissolve
    pause 1.0
    jump credits
