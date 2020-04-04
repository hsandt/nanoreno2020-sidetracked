   
label credits:
    $ quick_menu = False
    play music apartment fadeout 1.0 

    image splash = "gui/Sidetracked_intrologo.png" 
    image thanks eng = Text("{color=#f4cfe5}{size=80}Thanks for Playing!{/color}", text_align=0.5, drop_shadow = (3, 3), drop_shadow_color = "#000000")
    $ credits_speed = 55 #scrolling speed in seconds
    scene bg menuoverlay  #replace this with a fancy background
    
    image cred_eng = Text(gui.about, text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    show cred_eng at Move((0.5, 3.7), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")      
    with dissolve
    with Pause(credits_speed)
    
    show splash
    with dissolve
    with Pause(4)
    hide splash
    with dissolve
    with Pause(1)
    show thanks eng:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with Pause(2)
    with dissolve
    return
