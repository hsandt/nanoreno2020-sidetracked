# Images

## Overlay

image overlay black = Solid("#000000")
image overlay smartphone_backlayer = Solid("#ffffff80")

## Backgrounds (1080p)

image bg apartment day = "images/bg/apartment_day.jpg"
image bg apartment night = "images/bg/apartment_night.jpg"
image bg bus_stop = "images/bg/bus_stop.jpg"
image bg bus_outside = "images/bg/bus_outside.jpg"
image bg bus_inside = "images/bg/bus_inside.jpg"
image bg bakery = "images/bg/bus_outside.jpg"
image bg store = "images/bg/store.jpg"
image bg menuoverlay = "gui/overlay/game_menu.png"

## Sub-backgrounds (smartphone)

image sub smartphone = "images/bg/sub/smartphone_body.png"

## Items

# for memo, but never used directly as we use the screen_item with item identifier
image item hex_key = "images/item/hex_key.png"
image item screw_loose = "images/item/screw_loose.png"
image item screw_tight = "images/item/screw_tight.png"
image item coins = "images/item/coins.png"
image item purchase_permit = "images/item/purchase_permit.png"

## Characters

image mc casual regular = "images/char/mc_cas_reg.png"
image mc casual regular left = im.Flip("images/char/mc_cas_reg.png", horizontal=True)
image mc casual regular night = "images/char/mc_cas_reg_night.png"
image mc casual regular night left = im.Flip("images/char/mc_cas_reg_night.png", horizontal=True)
image mc outside regular = "images/char/mc_out_reg.png"
image mc outside regular left = im.Flip("images/char/mc_out_reg.png", horizontal=True)
image mc regular = "images/char/mc_reg.png"
image mc regular left = im.Flip("images/char/mc_reg.png", horizontal=True)


# Audio

# -1 so it's done just before music_dictionary definition in accessibility_setup.rpy
init -1:
    ## BGM assets
    define audio.title_theme = "<to 19.2>audio/bgm/title_theme.ogg"
    define audio.apartment = "audio/bgm/apartment_theme.ogg"
    define audio.street = "<loop 19.287>audio/bgm/ambient_street.ogg"
    define audio.store = "<from 0.240 to 199.92>audio/bgm/MusMus-BGM-102_normalized.ogg"
    define audio.apartment_night = "<loop 21.333>audio/bgm/apartment_theme_night.ogg"
    define audio.apartment_night_sad = "<loop 21.333>audio/bgm/apartment_theme_night_sad.ogg"  # unused
    define audio.game = "audio/bgm/bgm_maoudamashii_fantasy03_loop_only.ogg"

    ## BGM mapping (so accessibility feature can get BGM notification text from core name
    ## instead of filepath, which contains the <loop> pattern and is not very convenient)
    define music_to_assets = dict(
        title_theme = audio.title_theme,
        apartment = audio.apartment,
        street = audio.street,
        store = audio.store,
        apartment_night = audio.apartment_night,
        apartment_night_sad = audio.apartment_night_sad,
        game = audio.game
    )

    ## SFX assets
    define audio.coins_drop = "audio/sfx/coins_drop.ogg"
    define audio.door_open_close = "audio/sfx/door_open_close.ogg"
    define audio.inspect_chair = "audio/sfx/inspect_chair.ogg"
    define audio.printer = "audio/sfx/printer.ogg"
    define audio.screw_tighten = "audio/sfx/screw_tighten.ogg"
    define audio.searching_drawer = "audio/sfx/searching_drawer.ogg"
    define audio.smartphone_camera = "audio/sfx/smartphone_camera.ogg"
    define audio.smartphone_call = "audio/sfx/ringtone_notification_1.ogg"
    define audio.smartphone_notification = "audio/sfx/ringtone_notification_2.ogg"
    define audio.step_on_chair = "audio/sfx/step_on_chair.ogg"
    define audio.bus_stop_and_open = "audio/sfx/bus_stop_and_open.ogg"
    define audio.bus_close = "audio/sfx/bus_close.ogg"
    define audio.topping_bus_card = "audio/sfx/topping_bus_card.ogg"
    define audio.bus_stop_button = "audio/sfx/bus_stop_button.ogg"
    define audio.store_door_open = "audio/sfx/store_door_open.ogg"
    define audio.store_door_close = "audio/sfx/store_door_close.ogg"
    define audio.write_on_paper = "audio/sfx/write_on_paper.ogg"
    define audio.task_update = "audio/sfx/notification_unconvinced.ogg"

    ## SFX mapping (to allow to reuse audio assets for actions with different meanings,
    ## and also so accessibility feature can use short name as dict key rather than filepath)
    define sfx_to_assets = dict(
        coins_drop = audio.coins_drop,
        door_open_close = audio.door_open_close,
        inspect_chair = audio.inspect_chair,
        printer = audio.printer,
        screw_tighten = audio.screw_tighten,
        searching_drawer = audio.searching_drawer,
        smartphone_camera = audio.smartphone_camera,
        smartphone_notification = audio.smartphone_notification,
        step_on_chair = audio.step_on_chair,
        bus_stop_and_open = audio.bus_stop_and_open,
        bus_close = audio.bus_close,
        topping_bus_card = audio.topping_bus_card,
        bus_stop_button = audio.bus_stop_button,
        store_door_open = audio.store_door_open,
        store_door_close = audio.store_door_close,
        write_on_paper = audio.write_on_paper,
        task_update = audio.task_update
    )
