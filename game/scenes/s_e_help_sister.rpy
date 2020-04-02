# call, not jump to this label, so you can come back
label s_e:

# Check
label .shot1:
    show screen smartphone("message") with dissolve

    if sister_request_phase == 1:
        "I check my sister's message:"
        "\"hey sis could you translate that for me? Thx\" followed by a short, ambiguous Japanese sentence."
        # for me: the sentence is これ以上わかっても知らないよ
        # seems hard to read for the player, so keeping it for me for now:
        # It could mean "if he learns more about this, it's not my problem" or "if she understands, I won't take care of this anymore" or "I have no idea even if I know more about this"
        "Another random request..."
        "Where does it come from, anyway? I could translate it blindly, but a bit more context would help. My clients always provide me with it, I wish she could do the same."
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
        "I translate what I can.":
            $ store.sister_request_reply = "quick translation"
            "I come up with a vague translation and send it to her."
        "I give a fake translation to remind her I'm busy." if not has_given_fake_translation:
            $ store.has_given_fake_translation = True
            $ store.sister_request_reply = "fake translation"
            "I tell her the sentence means something like \"She shouldn't ask random stuff around to people.\""
        "I don't." if not has_given_silence:
            $ store.has_given_silence = True
            $ store.sister_request_reply = "silence"
            "I just ignore the message."
        "I still don't." if has_given_silence:
            $ store.sister_request_reply = "silence2"
            "I ignore the message, again."

    $ store.sister_request_phase = 2
    return

# Second message
label .shot3:
    "I check my sister's new message."
    if sister_request_reply == "ask context":
        "I remember, I asked her for more context. She says:
        {p}\"it's about a man hired to prevent a detective from investigating on embezzlement\""
        "Okay, that doesn't make things too clear but at least she made the effort to explain."
        "I try to come up with a better translation and send it to her. Replies come pretty quick this time, she thanks me."
        $ store.sister_request_phase = 3  # end of request
        return
    if sister_request_reply == "quick translation":
        "She just says: \"Thanks!\""
        "Looks like she was satisfied with my translation... Maybe going simple is the good choice, sometimes. If you don't mind dropping the details..."
        $ store.sister_request_phase = 3  # end of request
        return
    if sister_request_reply == "fake translation":
        "I wonder how she reacted to my joke translation... Ah, here it is:
        {p}\"ahaha... no seriously what does that mean??\""
        "Hmpf."
        call .shot2 from _call_s_e_shot2_1
    if sister_request_reply == "silence":
        "I didn't answer last time, but it looks like she's not giving up:
        {p}\"I know you've read my msg it's showing on the app!\""
        "Urg..."
        call .shot2 from _call_s_e_shot2_2
    if sister_request_reply == "silence2":
        "This time she's more understanding, I guess:
        {p}\"ok maybe you're busy but answer me before the end of the day!\""
        "I'll try."
        $ store.sister_request_phase = 3  # end of request
        return

    return
