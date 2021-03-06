# From Ren'Py Accessibility Add-On
# https://minute.itch.io/renpy-accessibility
# Only kept parameters actually used, and that are not already in the new Renpy Accessibility feature

init python:
    def changeColor(newColor):
        return SetField(preferences, "pref_text_color", newColor)

    ### Audio Cues
    # These are used in place of "play music" and "play sound". In your script:
    # $ play_sfx("door_close")
    # will play the door close sound effect.
    # $ play_music(lamentoso, 10)
    # will play "lamentoso" with a 10 second fadein.

    def play_sfx(sound_name, **kwargs):
        # slightly modified to allow passing a string, so you can reuse the same SFX
        # with different meanings, hence different notification texts (currently not used,
        # since only queued sounds with custom notification reuse sounds; but more flexible anyway)
        # also removed "{i}{/i}" which for some reason shows at "[i][/i]"
        renpy.sound.play(sfx_to_assets[sound_name], **kwargs)
        notify_sfx(sound_name)

    def notify_sfx(sound_name):
        if preferences.audio_cues:
            renpy.notify("SFX: " + sfx_dictionary[sound_name])

    def play_music(music_name, **kwargs):
        # same modification as in SFX
        renpy.music.play(music_to_assets[music_name], **kwargs)
        if preferences.audio_cues:
            renpy.notify("Now Playing: " + music_dictionary[music_name])
