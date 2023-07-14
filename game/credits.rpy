
label credits:
    # The code below works, but I found a bug where if you rollback or load,
    # config gets stuck as it's not part of store, preventing skipping during the game.
    # It's easy to add $ config.allow_skipping = True in previous scenes to fix the issue
    # in case of rollback, but for general loading I don't see how.
    # So for now, we count on player not trying to skip the dialogues just before
    # the credits.

    # Should we allow skipping at all? (credits roll itself cannot be skipped,
    # but if user is holding Skip button or has toggled skip in previous seen,
    # they may accidentally skip the whole credits)
    # $ config.allow_skipping = False
    # Clear any remaining skipping, or the "Skipping" notification will get stuck
    # until you toggle it again
    # $ config.skipping = False

    $ quick_menu = False
    $ play_music("apartment", loop=False)
    $ renpy.pause(0.2, hard=True)

    image splash = "gui/Sidetracked_intrologo.png"
    image thanks eng = Text("{color=[gui.idle_color]}{size=80}Thanks for Playing!{/size}{/color}", text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    $ credits_duration = 55 # credits duration in seconds
    scene bg game_menu_overlay with Dissolve(1.0)  #replace this with a fancy background

    image cred_eng = Text(gui.credits, text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    show cred_eng at Move((0.5, 4.5), (0.5, 0.0), credits_duration, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    # wait for Credits to end, and do not allow user click (can still exit via pause menu)
    $ renpy.pause(credits_duration, hard=True)

    show splash with dissolve
    $ renpy.pause(2.0, hard=True)
    hide splash with dissolve
    $ renpy.pause(1.0, hard=True)
    show thanks eng:
        yalign 0.55
        xalign 0.55
    with dissolve
    $ renpy.pause(2.0, hard=True)
    hide thanks with dissolve
    $ renpy.pause(1.0, hard=True)

    show overlay black with dissolve

    # normally, we computed everything so music has stopped at this point,
    # but just in case we fadeout here
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)

    # See comments at the top
    # $ config.allow_skipping = True

    return
