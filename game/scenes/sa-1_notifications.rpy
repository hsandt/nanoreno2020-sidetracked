# call, not jump to this label, so you can come back
label sa_1:
    if not has_updated_apps:
        "New album released today, professional translators meetup tomorrow... and a few app updates available now."
        "I check the app updates. There are 14 of them, so I carefully select which apps to update based on how much I use them."
        "Hopefully that will help reduce my data usage while also saving some space."
        "After the fourth manual update, I get impatient and just touch “Update all”. Maybe it wasn’t the best idea, though."
        "Shortly after, I get a notification \"Storage space running out\"."
        $ store.has_updated_apps = True
    elif not has_freed_space:
        "I still have the \"Storage space running out\" notification."
    else:
        "There are just a few minor events, though."
        return

    menu:
        "What should I do?"
        "Free space on the smartphone":
            call sa_2 from _call_sa_2
        "Ignore the notification":
            "I can take care of this later."

    return
