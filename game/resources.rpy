# Images

## Overlay

image overlay black = Solid("#000000")
image overlay smartphone_backlayer = Solid("#ffffff80")

## Backgrounds (1080p)

image bg apartment = "images/bg/apartment.jpg"
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
image mc outside regular = "images/char/mc_out_reg.png"
image mc regular = "images/char/mc_reg.png"
image mc regular left = im.Flip("images/char/mc_reg.png", horizontal=True)


# Audio

## BGM

# define audio.title_screen = "audio/bgm/title_screen.ogg"
define audio.apartment = "audio/bgm/apartment_theme.ogg"
define audio.store = "audio/bgm/MusMus-BGM-102.mp3"
define audio.game = "audio/bgm/bgm_maoudamashii_fantasy03_loop_only.ogg"
# for memo, but never used directly as we must loop with full file path
# define audio.street = "audio/bgm/ambient_street.ogg"
# define audio.apartment_night = "audio/bgm/apartment_theme_night.ogg"
# define audio.apartment_night_sad = "audio/bgm/apartment_theme_night_sad.ogg"

## SFX
define audio.coins_drop = "audio/sfx/coins_drop.ogg"
define audio.door_open_close = "audio/sfx/door_open_close.ogg"
define audio.inspect_chair = "audio/sfx/inspect_chair.ogg"
define audio.printer = "audio/sfx/printer.ogg"
define audio.screw_tighten = "audio/sfx/screw_tighten.ogg"
define audio.searching_drawer = "audio/sfx/searching_drawer.ogg"
define audio.smartphone_camera = "audio/sfx/smartphone_camera.ogg"
define audio.smartphone_notification = "audio/sfx/notification_unconvinced.ogg"
define audio.step_on_chair = "audio/sfx/step_on_chair.ogg"
