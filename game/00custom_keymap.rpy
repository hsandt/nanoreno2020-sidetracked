# Based on 00keymap.rpy in Ren'py SDK and this example config to get closer to JP VN UI behavior:
# https://www.reddit.com/r/vndevs/comments/fi3jrt/renpy_custom_keymap_just_thought_id_share_in_case/
# https://pastebin.com/t51iumWx

init -160 python:
    custom_keymap = dict(
        toggle_preferences = [ 'o', 'p' ],
        toggle_tasktree = ['t']
    )

init -130 python:
    ## Only affects modified keybindings, does not remove others.
    config.keymap.update(custom_keymap)

    # don't set config.underlay here; we'll add key-action statements directly
    # in screen definitions
