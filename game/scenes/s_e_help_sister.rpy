# call, not jump to this label, so you can come back
label s_e:

# Check
label .shot1:
    show screen smartphone("message") with dissolve

    if sister_request_phase == 1:
        "I check my sister's message:"
        sister "hey kat could you translate that for me? Thx"
        sister "これ以上わかっても知らないよ (kore ijou wakatte mo shiranai yo)"
        # for me: the sentence is これ以上わかっても知らないよ
        # seems hard to read for the player, so keeping it for me for now:
        # It could mean "if he learns more about this, it's not my problem" or "if she understands, I won't take care of this anymore" or "I have no idea even if I know more about this"

        $ StartTask(task_TranslateSentence, notify=True)

        "OK, this is pretty much quite a short and ambiguous Japanese sentence."
        "Where does it come from, anyway? I could translate it blindly, but a bit more context would help."
        call .shot2 from _call_s_e_shot2
    else:
        call .shot3 from _call_s_e_shot3

    return

# Reply
label .shot2:
    menu:
        "How do I reply?"
        "I ask for context.":
            $ store.sister_request_reply = "ask context"
            "I ask her for more details about what's going on around that line."
            $ StartTask(task_GetContext)
            $ store.currentTime += 4
        "I translate what I can.":
            $ store.sister_request_reply = "quick translation"
            "I come up with a vague translation and send it to her."
            $ CompleteTask(task_TranslateSentence)
            $ store.currentTime += 8
        "I give a fake translation to remind her I'm busy." if not has_given_fake_translation:
            $ store.has_given_fake_translation = True
            $ store.sister_request_reply = "fake translation"
            "I tell her the sentence means something like \"She shouldn't ask random stuff around to people.\""
            $ store.currentTime += 3
        "I don't." if not has_given_silence:
            $ store.has_given_silence = True
            $ store.sister_request_reply = "silence"
            "I just ignore the message."
            $ store.currentTime += 2
        "I still don't." if has_given_silence:
            $ store.sister_request_reply = "silence2"
            "I ignore the message, again."
            $ store.currentTime += 2

    $ store.sister_request_phase = 2
    return

# Second message
label .shot3:
    "I check my sister's new message."
    if sister_request_reply == "ask context":
        "I remember, I asked her for more context. She says:
        {p}\"it's about a man hired to prevent a detective from investigating on embezzlement\""
        $ CompleteTask(task_GetContext)
        "Okay, that doesn't make things too clear but at least she made the effort to explain."
        "I try to come up with a better translation and send it to her. She thanks me, saying the translation makes all sense."
        $ CompleteTask(task_TranslateSentence)
        "I like jobs done properly."
        $ store.currentTime += 11
        $ store.sister_request_phase = 3  # end of request
    elif sister_request_reply == "quick translation":
        "She just says: \"Thanks!\""
        "Looks like she was satisfied with my translation... Maybe going simple is the good choice, sometimes. Maybe..."
        $ store.currentTime += 2
        $ store.sister_request_phase = 3  # end of request
    elif sister_request_reply == "fake translation":
        "I wonder how she reacted to my joke translation... Ah, here it is:
        {p}\"ahaha... no seriously what does that mean??\""
        "Hmpf."
        $ store.currentTime += 2
        call .shot2 from _call_s_e_shot2_1
    elif sister_request_reply == "silence":
        "I didn't answer last time, but it looks like she's not giving up:
        {p}\"I know you've read my msg it's showing on the app!\""
        "Urg..."
        $ store.currentTime += 2
        call .shot2 from _call_s_e_shot2_2
    elif sister_request_reply == "silence2":
        "This time she's more understanding, I guess:
        {p}\"ok maybe you're busy but answer me before the end of the day!\""
        "I'll try."
        $ store.currentTime += 2
        $ store.sister_request_phase = 3  # end of request
    else:
        "Oops, this should never be entered. Send a bug report to komehara!"

    return
