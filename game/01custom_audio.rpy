init -120 python:
    renpy.music.register_channel("mission_a", mixer="music")
    renpy.music.register_channel("mission_b", mixer="music")

    # use this when playing mission (full track) on music
    def set_mission_full_volume(volume, delay=0):
        renpy.audio.music.set_volume(volume, delay, channel="music")

    def set_mission_a_volume(volume, delay=0):
        renpy.audio.music.set_volume(volume, delay, channel="mission_a")

    def set_mission_b_volume(volume, delay=0):
        renpy.audio.music.set_volume(volume, delay, channel="mission_b")

    def solo_mission_full(delay=0):
        set_mission_full_volume(1.0, delay=delay)
        set_mission_a_volume(0.0, delay=delay)
        set_mission_b_volume(0.0, delay=delay)

    def solo_mission_a(delay=0):
        set_mission_full_volume(0.0, delay=delay)
        set_mission_a_volume(1.0, delay=delay)
        set_mission_b_volume(0.0, delay=delay)

    def solo_mission_b(delay=0):
        set_mission_full_volume(0.0, delay=delay)
        set_mission_a_volume(0.0, delay=delay)
        set_mission_b_volume(1.0, delay=delay)

    def duo_mission_ab(delay=0):
        set_mission_full_volume(0.0, delay=delay)
        set_mission_a_volume(1.0, delay=delay)
        set_mission_b_volume(1.0, delay=delay)
