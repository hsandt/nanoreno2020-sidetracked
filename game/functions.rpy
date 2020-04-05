# snippet from Andykl to define random statement
# https://github.com/renpy/renpy/issues/1786
python early:
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
