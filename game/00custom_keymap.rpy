# Based on 00keymap.rpy in Ren'py SDK and:
# https://www.reddit.com/r/vndevs/comments/fi3jrt/renpy_custom_keymap_just_thought_id_share_in_case/
# https://pastebin.com/t51iumWx

init -160 python:
    custom_keymap = dict(
        preferences = [ 'o', 'p' ],
        task_tree = ['t']
    )

init -150 python:
    def open_task_tree_if_in_game():
        if not main_menu:
            renpy.run(ShowMenu("tasktree"))

init -130 python:
    ## Only affects modified keybindings, does not remove others.
    config.keymap.update(custom_keymap)

    # The default keymap. We might also want to put some of this into
    # the launcher.
    _custom_keymap = renpy.Keymap(
        preferences = ShowMenu("preferences"),
        task_tree = open_task_tree_if_in_game
    )

    config.underlay.append(_custom_keymap)
