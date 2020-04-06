# From Ren'Py Accessibility Add-On
# https://minute.itch.io/renpy-accessibility
# Only kept parameters actually used, and that are not already in the new Renpy Accessibility feature
# (which can handle text)

### Initial GUI preferences
# Here, we'll keep all our gui preferences, along with our persistent variables regarding accessibility.

# Audio cues
default persistent.audio_cues = True

## Default alpha of the say window. Append to your say screen.
# Our window already has a slight alpha, no we start at 1.0 opacity
default persistent.say_window_alpha = 1.0

# Default text color
# Replace all instances of gui.text_color with persistent.pref_text_color. Append to your say screen.
# Commented out define since we initialize from a variable, which must be done in init python (below)
# default persistent.pref_text_color = "#333333"

###
# This is all the functions for accessibility.

init python:
    persistent.pref_text_color = gui.text_color

    ###Initial Audio Cues Setup
    # Define every song with an alias

    # sad_song = "filepath.mp3"

    # alias : "Song Title",
    music_dictionary = dict(
        title_theme = "Title Theme - Upbeat Music",
        apartment = "Apartment Theme - Day - Upbeat Music",
        store = "Store - Chill Music",
        game = "Mobile Game - Battle Music",
        street = "Ambient Street Sounds",
        apartment_night = "Apartment Theme - Night - Relaxing Music",
        apartment_night_sad = "Apartment Theme - Night - Sad Music"
    )

    # Define every sound with an alias
    # door_close = "door closing sfx.wav"

    # alias : "Sound description."
    sfx_dictionary = dict(
        coins_drop = "Coins dropped",
        door_open_close = "Door opens and closes",
        inspect_chair = "Inspect chair",
        printer = "Print",
        screw_tighten = "Tighten screw",
        searching_drawer = "Rummage container full of items",
        smartphone_camera = "Take photo",
        smartphone_notification = "Smartphone notification",
        step_on_chair = "Sit down",
        bus_stop_and_open = "Bus stops and door opens with hissing",
        bus_close = "Bus door closes",
        topping_bus_card = "Passengers top up their card",
        bus_stop_button = "Bus stop button pressed",
        store_door_open = "Store automatic door opens with chime",
        store_door_close = "Store automatic door closes",
        write_on_paper = "Write on paper",
        task_update = "Task update notification"
    )

    # Self-voicing (female voices)
    if renpy.windows:
        config.tts_voice = "Hazel"
    elif renpy.macintosh:
        config.tts_voice = "Victoria"
    elif renpy.linux:
        config.tts_voice = "english_rp+f2"
