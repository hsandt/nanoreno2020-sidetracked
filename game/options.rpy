## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Sidetracked")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "3.4"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
This game was developed for {a=https://itch.io/jam/nanoreno-2020}NaNoRenO 2020{/a}.


{u}Credits{/u}

- Writing, Programming: komehara

- UI Programming: Marionette

- Background Art: JW Jones

- Character Sprites: Maxenau

- Item Sprites: komehara

- BGM: Fabian Fabro (FirahFabe)

- Ambient BGM: komehara

- Sound Effects: Fabian Fabro (FirahFabe), komehara


{u}License{/u}

Original backgrounds: copyright JW Jones 2020

Other backgrounds:

- Bus stop (bus_stop.jpg) adapted from `bus stop noon.jpg` by Uncle Mugen, distributed for free usage on {a=https://lemmasoft.renai.us/forums/viewtopic.php?p=226871}this thread{/a})

- Bus outside (bus_outside.jpg) adapted from {a=https://commons.wikimedia.org/wiki/File:Rennes_-_Bluebus_20180316-02.jpg}Rennes_-_Bluebus_20180316-02.jpg{/a} by Pymouss under CC-BY-4.0 on Wikimedia Commons

- Bus inside (bus_inside.jpg) adapted from {a=http://unyokan2.ninja-web.net/haikei2/bass/bass007.jpg}bass007.jpg{/a} distributed by Unyo@ on {a=http://unyokan.ojaru.jp/framepage2.html}this page{/a} under custom license (allows free use with optional crediting)

- Bakery (bakery.jpg) adapted from {a=https://commons.wikimedia.org/wiki/File:Typical_French_bakery_pastries.jpg}Typical_French_bakery_pastries.jpg{/a} by Andre.o.mob under CC-BY-SA-4.0 on Wikimedia Commons

- Store (store.jpg) adapted from {a=https://commons.wikimedia.org/wiki/File:Tokyu_Hands_in_Taipei_Breeze_Centre_201608.JPG}Tokyu_Hands_in_Taipei_Breeze_Centre_201608{/a} by Wpcpey under CC-BY-SA-4.0 on Wikimedia Commons

Free UI sprites: {a=https://loudeyes.itch.io/dating-sim-ui-pack}Dating Sim UI Pack{/a} by Lynda Mc Donald, distributed under custom license (allows free usage with appropriate credit)

Fonts: The Bold Font by {a=http://svenpels.com}Sven Pels{/a}, distributed for free usage on {a=https://www.dafont.com/the-bold-font.font}dafont.com{/a}

Character sprites: copyright Maxenau 2020

Item sprites: {a=https://creativecommons.org/licenses/by-sa/4.0/}CC BY-SA 4.0{/a} komehara

BGM: copyright Fabian Fabro 2020

Ambient BGM:

- ambient_street.ogg: {a=https://creativecommons.org/licenses/by-sa/4.0/}CC BY-SA 4.0{/a} komehara

Free BGM:

- Yawarakana Uso by {a=http://musmus.main.jp}MusMus{/a} under {a=http://musmus.main.jp/info.html}custom license{/a} (allows free usage as BGM with appropriate credit)

- Game BGM (bgm_maoudamashii_fantasy03_short.ogg) cropped from Fantasy 03 by {a=https://maoudamashii.jokersounds.com}Maoudamashii{/a} distributed on {a=https://maoudamashii.jokersounds.com/list/bgm10.html}this page{/a} under {a=https://maoudamashii.jokersounds.com/music_rule.html}custom license{/a} (allows free usage with appropriate credit whenever possible)

Original SFX: inspect_chair.ogg is {a=https://creativecommons.org/licenses/by-sa/4.0/}CC BY-SA 4.0{/a} komehara, everything else is copyright Fabian Fabro 2020

Free SFX:

- smartphone notification {a=https://notificationsounds.com/notification-sounds/unconvinced-569}notification_unconvinced.ogg{/a} by {a=https://notificationsounds.com}Notification Sounds{/a} under CC BY 4.0

[Ren'Py Accessibility Add-On](https://minute.itch.io/renpy-accessibility) under MIT license

Source code available on the {a=https://github.com/hsandt/nanoreno2020-sidetracked}GitHub repository{/a}
""")

define gui.credits = _("""
{size=+10}{b}Team{/b}{/size}


{b}Writing & Programming{/b}

komehara


{b}UI Programming{/b}

Marionette


{b}Background Art{/b}

JW Jones


{b}Item Art{/b}

komehara


{b}Character Art{/b}

Maxenau


{b}Music{/b}

Fabian Fabro


{b}Sound Design{/b}

Fabian Fabro
komehara



{size=+10}{b}Free assets{/b}{/size}

{b}Backgrounds{/b}

Uncle Mugen
Pymouss
Unyokan
Andre.o.mob
Wpcpey


{b}Dating Sim UI Pack{/b}

Lynda Mc Donald


{b}The Bold Font{/b}

Sven Pels


{b}BGM{/b}

MusMus
Maoudamashii


{b}SFX{/b}

Notification Sounds



{size=+10}{b}Code snippets / Add-Ons{/b}{/size}

jsfehler, Andykl (random statement)
minute (Ren'Py Accessibility Add-On)



{size=+10}{b}Playtesters{/b}{/size}

♡Nagisa♡



{size=+10}{b}Special Thanks{/b}{/size}

cephalo



Developed for NaNoRenO 2020 with Ren'Py
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Sidetracked"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = audio.title_theme


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
define config.enter_transition = Dissolve(0.2)
define config.exit_transition = Dissolve(0.2)

## Between screens of the game menu.
define config.intra_transition = Dissolve(0.2)

# Used when returning to the main menu from the game.
define config.game_main_transition = Dissolve(0.2)

## A transition that is used after a game has been loaded.
define config.after_load_transition = Dissolve(0.5)

# Used when entering the main menu from the splashscreen.
define config.end_splash_transition = Dissolve(0.5)

## Used when entering the main menu after the game has ended.
define config.end_game_transition = Dissolve(0.5)


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Sidetracked-1583110243"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
