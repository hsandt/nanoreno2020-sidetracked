label s4_1:
    # probably no smartphone usage at the end of the game, but just in case
    $ store.has_wifi = True

label .shot1:
    # assume Katell has taken the next bus since last scene,
    # that she took 15mn buying the tool in last scene,
    # that bus takes ~30mn to transit, and that buses arrive at the same time
    # in both directions. Plus some time to come back home from bus stop.
    $ store.currentTime = get_next_bus_time(store.currentTime + 48) + 17
    # if doing nothing on smartphone: ~19h00
    $ store.wrapping_scene = "light_bulb"

    pause 2.0
    $ play_sfx("door_open_close")
    pause 1.0

    $ quick_menu = True

    scene bg apartment night with Dissolve(1.0)
    $ play_music("apartment_night")

    show mc casual regular night left at character_right with dissolve

    window show
    "By the time I get back in my apartment, it's already the evening. Exhausted, I remove my shoes and open the tool’s package."
    window hide None

    show screen screen_item("screwdriver", "left") with dissolve
    mc "OK, let’s try this now."
    hide screen screen_item with dissolve
    show screen screen_item("screw_loose", "left") with dissolve
    "I use the key to tighten the screw on the chair in the living room."
    $ play_sfx("screw_tighten")
    pause 0.5
    show screen screen_item("screw_tight", "left") with dissolve
    pause 0.5
    mc "So... Is it stable now?"
    hide screen screen_item

    show mc casual regular night left at character_right_sit_down
    pause 0.5
    $ play_sfx("step_on_chair")
    $ store.is_character_sitting = True

    "I sit down. The seat is not moving anymore."

    $ CompleteTask(task_Chair)

    "I decide to finally enjoy my lunch, or rather, what turned into dinner."
    "I take a mouthful of zucchini. It's cold.{w=1.0} Obviously."

    pause 0.5
    mc "..."
    pause 0.5

    "Thinking about it, maybe I could have just taken lunch on that other chair other there."
    "...{w=1.0} No, there is no need to regret."
    "I was not randomly jumping from a topic to another. Problems just kept popping up, and I had to solve them."
    "Because I decided to take over all these issues, my day was pretty fun."
    "I have even been able to improve many things that will make my daily life easier in the future. For instance..."

    # this is mandatory, so doesn't count as extra
    "I tasted some nice viennoiseries."

    $ extra_actions_count = 0

    if has_installed_bus_stop_app:
        "I installed an app that can do what buttons normally do, but smarter."
        $ extra_actions_count += 1

    if has_updated_apps:
        "I've finally updated my mobile apps."
        $ extra_actions_count += 1

    if has_freed_space:
        "I released a bunch of space on my phone."
        $ extra_actions_count += 1

    if has_tried_dict:
        "I could try that nice Japanese dictionary application."
        $ extra_actions_count += 1

    if has_invented_pwd:
        "I created an account to play that tactical RPG, and devised an elegant password for it."
        $ extra_actions_count += 1

    if has_tried_game_count == 1:
        if not has_invented_pwd:
            "I played that tactical RPG."
        $ extra_actions_count += 1
        if has_deleted_game:
            "... Although I had to delete the app."
    elif has_tried_game_count == 2:
        if not has_invented_pwd:
            "I played that tactical RPG. Twice. But eh, it was fun."
        else:
            "I even tried it twice."
        $ extra_actions_count += 1.5
        if has_deleted_game:
            "Too bad I had to delete it, I guess."
    elif has_tried_game_count > 2:
        if not has_invented_pwd:
            "I played that tactical RPG. Too many times for a single day, maybe."
            if has_deleted_game:
                "Good thing for my health I deleted it, I guess."
        else:
            "Then I played it several times. That made the account worth it!"
            if has_deleted_game:
                "... Except I had to delete the app in the end."
        $ extra_actions_count += 2

    if queuer_dissatisfaction == 1:
        "I annoyed a few ladies and gentlemen diligently filling administrative needs, like me."
        $ extra_actions_count += 1
    if queuer_dissatisfaction > 1:
        "I massively annoyed a row of ladies and gentlemen diligently filling administrative needs, like me."
        $ extra_actions_count += 1.5

    if sister_request_reply == "ask context":
        if sister_request_phase == 2:
            "I helped my sister... Er... Actually, I asked her for more context but didn't read her reply. I'll check that tomorrow."
        else:
            "I helped my sister with a translation. Well, I did all the job, actually. And properly, with context and all."
            $ extra_actions_count += 1.5
    elif sister_request_reply == "quick translation":
        "I translated a sentence for my sister. Barebone, but did the job."
        $ extra_actions_count += 1
    elif sister_request_reply == "fake translation":
        "I translated, er... I enlightened my sister with deep principles."
    elif sister_request_reply == "silence":
        "I... turned a deaf ear to my sister's plea."
    elif sister_request_reply == "silence2":
        "I... turned a deaf ear to my sister's pleas. Twice."
    else:
        "And my sister, er... Oh, right. I didn't check her message at all."

    # Max of 7 unique extra actions, but 11 if you get bonus points by doing things properly / multiple times (including inventing password)
    if extra_actions_count == 0:
        "...{w=1.0} And that's it...{w=1.0} I didn't do much besides fixing the chair. But! It's an investment in real estate, isn't it?"
    elif extra_actions_count < 4:
        "And, er...{w=1.0} That's all. But that's a lot done in the middle of a lunch. Aha..."
    elif extra_actions_count < 8:
        "That's quite a record. For good or bad..."
    else:
        "That's incredible! Especially in four hours flat."

    if extra_actions_count >= 4:
        # Max of ~25 clearing notifications (checking task tree after start task notification, including minor ones)
        if new_task_clear_count == 0:
            "And all of this without checking my TODO list a single time! I know what I must do, right?"
        elif new_task_clear_count < 6:
            "And I barely checked my TODO list. It was all pretty straightforward, I think."
        elif new_task_clear_count < 13:
            "By the way, the TODO list was quite useful. I didn't think things would go that far with that chair!"
        elif new_task_clear_count < 18:
            "By the way, the TODO list was very useful. It's incredible how things went complicated."
        else:
            "I regularly checked my TODO list! Otherwise, I would have been lost!"

    pause 2.0

    "Anyway, that room is pretty dark."

    $ play_sfx("step_on_chair")
    show mc casual regular night left at character_stand_up
    $ store.is_character_sitting = False
    pause 0.5

    "Eating cold food in the dark makes me look like a vampire. It's cool, but I push the light switch nevertheless."
    "Nothing happens."

    show mc casual regular night left at character_move_left(0.5)
    pause 0.5

    "I inspect the light bulb and notice it's broken. Another thing I must fix, I guess."

    $ StartTask(task_LightBulb)

    show mc casual regular night at character_move_right
    pause 1.0

    $ play_sfx("searching_drawer")
    pause 4.0
    # in case player skips sound, stop it now to avoid sound leaking
    stop sound

    show mc casual regular night left at character_right
    mc "Of course. No light bulb to replace with."

    pause 0.5

    "Wait, do I need to go back to the DIY store?"
    mc "..."

    $ RevealTask(task_BuyLightBulb)

    # just to represent time spent since thinking about all of this
    # if not doing anything, around 18h00
    $ store.currentTime += 23 + extra_actions_count * 1
    $ clock_time = get_clock_time()
    "I check my watch. [clock_time]."

    menu:
        "Should I go back to the store to get a replacement bulb?"
        "Yes":
            jump .shot2a
        "Screw this and go to bed":
            jump .shot2b

label .shot2a:
    $ StartTask(task_BuyLightBulb)

    mc "...{w=1.0} Yes, logically I should be able to go there once more before it closes.{w=1.0} But I need to go now."

    show mc casual regular night at character_move_right_farther
    pause 1.0
    show mc casual regular night left
    pause 0.5

    "... Nah, it's fine. The meal is cold already, it cannot get colder."

    show mc casual regular night
    pause 0.5

    window show None
    "I just get to the store, pick a light bulb, come back, and I'm done."
    window hide

    show mc casual regular night at character_move_right_exit
    pause 0.2

    stop music fadeout 2.0

    $ quick_menu = False
    show overlay black with dissolve
    pause 0.3

    $ play_sfx("door_open_close")
    pause 2.4

    jump credits

label .shot2b:
    window show None
    "...{w=1.0} No way, I'm not going back.{w=1.0} I had my fix of problems for today. For the month, actually."
    window hide

    $ FailTask(task_BuyLightBulb)
    $ FailTask(task_LightBulb)
    $ CompleteTask(task_HaveLunch)

    scene overlay black with dissolve
    pause 0.5

    window show
    "After that, I finished my cold roasted vegetables, went in my bed and read a novel for two hours or so, before sleeping."
    "Not too bad to procrastinate once in a while."
    window hide

    stop music fadeout 2.0

    pause 0.5
    $ quick_menu = False
    show overlay black with dissolve
    pause 1.3

    jump credits
