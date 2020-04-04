
label credits:
    $ quick_menu = False
    play music apartment noloop
    pause 0.2

    image splash = "gui/Sidetracked_intrologo.png"
    image thanks eng = Text("{color=[gui.idle_color]}{size=80}Thanks for Playing!{/color}", text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    $ credits_duration = 55 # credits duration in seconds
    scene bg menuoverlay with Dissolve(1.0)  #replace this with a fancy background

    image cred_eng = Text(gui.credits, text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    show cred_eng at Move((0.5, 3.7), (0.5, 0.0), credits_duration, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    # wait for Credits to end, and do not allow user click (can still exit via pause menu)
    $ renpy.pause(credits_duration, hard=True)

    show splash
    with dissolve
    with Pause(2)
    hide splash
    with dissolve
    with Pause(1)
    show thanks eng:
        yalign 0.55
        xalign 0.6
    with dissolve
    with Pause(2)
    hide thanks
    with dissolve
    with Pause(2)

    return
