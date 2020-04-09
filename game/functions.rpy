python early:
    from math import ceil

    # Register random statement
    # snippet from Andykl (inspired by jsfehler) to define random statement
    # https://github.com/renpy/renpy/issues/1786
    def parse_random(lexer):
        lexer = lexer.subblock_lexer()
        choices = []
        while lexer.advance():
            with lexer.catch_error():
                stmt = lexer.renpy_statement()
                choices.append(stmt)
        return choices

    def next_random(choices):
        return renpy.random.choice(choices)

    renpy.register_statement(
        name="random", block=True,
        parse=parse_random,
        next=next_random,
    )

    def minutes_to_clock_time(minutes):
        """
        Return readable time string in format HH:mm
        from minutes total from midnight

        """
        hour, minutes_remainder = minutes // 60, minutes % 60
        return "%02d:%02d" % (hour, minutes_remainder)

    def get_clock_time():
        return minutes_to_clock_time(store.currentTime)

    def get_next_bus_time(time_minutes):
        """
        Return time of next bus, in minutes total.
        If there is a bus exactly this minute, return current time.

        """
        # bus arrives every 30 minutes, from midnight
        # (Python 2 requires the "." for float division)
        # keep integer to avoid floating number display in dialogues
        return int(ceil(time_minutes / 30.) * 30)

    readable_numbers_en = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight"
        # should be enough as game is not so long
    }

    def get_half_hour_approx_duration(duration_minutes):
        """
        Return duration approximated to closest half hour
        as a readable string

        """
        # approx per slice of half hour (Python 2 requires the "." for float division)
        half_hours = int(round(duration_minutes / 30.))
        hour, half_remaining = half_hours // 2, half_hours % 2

        if hour == 0:
            # probably impossible
            return "Half an hour"
        elif hour == 1:
            readable_time = "One hour"
        else:
            readable_time = "%s hours" % readable_numbers_en[hour]

        if half_remaining == 1:
            readable_time += " and a half"

        return readable_time


init -1 python:
    def clear_captcha():
        store.captcha_rubber1 = False
        store.captcha_rubber2 = False
        store.captcha_other1 = False
        store.captcha_other2 = False
        store.captcha_other3 = False
        store.captcha_other4 = False
        store.invalid_captcha = False

    def return_verify_captcha_action():
        if store.captcha_rubber1 and store.captcha_rubber2 and not store.captcha_other1 and not store.captcha_other2 and not store.captcha_other3 and not store.captcha_other4:
            # correct answer, disable safe mode and return to Preferences
            # it seems that on "show" Function() statement doesn't work consistently on screen_captcha
            # so we prefer clearing captcha variables on success (for next time) rather than on show
            return [Function(clear_captcha), SetField(persistent, "safe_mode", False), ShowMenu("preferences")]
        else:
            # wrong answer
            return SetVariable("invalid_captcha", "True")

    def has_outstanding_notifications():
        return not store.has_updated_apps or not store.has_freed_space or \
            store.sister_request_phase >= 1 and store.sister_request_phase <= 2

    def change_free_space(delta):
        store.free_space += delta
        store.has_seen_space_left_since_last_change = False  # "dirty" free space

    def on_show_tasktree():
        if store.indicator_newTask:
            store.indicator_newTask = False
            store.new_task_clear_count += 1

    def is_character_sprite_displayed():
        return store.wrapping_scene in ["broken_chair", "bus_stop", "store", "light_bulb"]
