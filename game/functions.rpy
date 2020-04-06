python early:
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

init -1 python:
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
