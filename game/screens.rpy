################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
    font gui.name_text_font
    outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    idle_color "#744675"
    hover_color "#f4cfe5"

style gui_text:
    properties gui.text_properties("interface")
    selected_idle_outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    # The Bold Font makes text with outline a bit dense, so extra kerning helps
    kerning 2

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        background Transform(style.window.background, alpha=preferences.say_window_alpha)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" color preferences.pref_text_color
        if is_showing_smartphone or is_character_sitting:
            yalign 0.05
        else:
            yalign 0.85

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign  # will be overridden in screen say
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    # darker purple than usual so NPC with different name colors do not clash with outline
    outlines [ (absolute(2), "#3b233c", absolute(0), absolute(0)) ]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        if is_showing_smartphone:
            ypos 505
        else:
            ypos 405

        for i in items:
            textbutton i.caption action i.action at choice_transform

transform choice_transform:
    alpha 0.0
    ease 0.5 alpha 1.0

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    # ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        #hbox:
        style_prefix "quick"
        #
        #    xalign 0.5
        #    yalign 1.0
        #
        #    textbutton _("Back") action Rollback()
        #    textbutton _("History") action ShowMenu('history')
        #    textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #    textbutton _("Auto") action Preference("auto-forward", "toggle")
        #    textbutton _("Save") action ShowMenu('save')
        #    textbutton _("Q.Save") action QuickSave()
        #    textbutton _("Q.Load") action QuickLoad()
        #    textbutton _("Prefs") action ShowMenu('preferences')
        imagebutton auto "gui/button/backbutton_%s.png" focus_mask True action Rollback()
        use preferences_button
        use tasktree_button

    key "game_menu" action ShowMenu(preferences.game_menu_screen)

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text
style quick_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

style quick_text:
    color "#ffffff"
    outlines [ (absolute(1), "#0aa248", absolute(0), absolute(0)) ]



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.1

        spacing gui.navigation_spacing

        if main_menu:
            #button:
            #  action Start()
            #  add "gui/button/button_idle.png"
            #  text _("Start") style "navigation_button_text"
            hbox:
                imagebutton auto "gui/button/button_%s.png"  action Start()
                text _("Start") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5

        else:

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action ShowMenu("history")
                text _("History") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
            #textbutton _("History") action ShowMenu("history")

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action ShowMenu("save")
                text _("Save") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
            #textbutton _("Save") action ShowMenu("save")

            #hbox:
            #    imagebutton auto "gui/button/button_%s.png"  action ShowMenu("tasktree")
            #
            #    text _("TODO List") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5

        hbox:
            imagebutton auto "gui/button/button_%s.png"  action ShowMenu("load")
            text _("Load") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
        #textbutton _("Load") action ShowMenu("load")

        #hbox:
            #imagebutton auto "gui/button/optionsbutton_%s.png"  action ShowMenu("preferences")
            #text _("Preferences") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
        #textbutton _("Preferences") action ShowMenu("preferences")

        hbox:
            imagebutton auto "gui/button/button_%s.png"  action ShowMenu("accessibility")

            text _("Accessibility") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5

        if _in_replay:

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action EndReplay(confirm=True)
                text _("End Replay") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
            #textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action MainMenu()
                text _("Main Menu") style "navigation_button_text" color gui.idle_color xpos -124 yalign 0.5 xalign 0.5
            #textbutton _("Main Menu") action MainMenu()

        hbox:
            imagebutton auto "gui/button/button_%s.png"  action ShowMenu("about")

            text _("Credits") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
        #textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action ShowMenu("help")
                text _("Help") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            hbox:
                imagebutton auto "gui/button/button_%s.png"  action Quit(confirm=not main_menu)
                text _("Quit") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5
            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            #textbutton _("Quit") action Quit(confirm=not main_menu)

    use preferences_button
    use tasktree_button

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:
    #
    #    vbox:
    #        text "[config.name!t]":
    #            style "main_menu_title"
    #
    #        text "[config.version]":
    #            style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "bg main_menu_overlay"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    # compared to default template, set accent to False
    # to avoid overriding color with gui.accent_color
    properties gui.text_properties("main_menu", accent=False)
    color gui.title_color

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation
    hbox:
        yalign 0.9
        xalign 0.039
        imagebutton auto "gui/button/button_%s.png"  action Return()
        text _("Return") style "navigation_button_text" color gui.idle_color  xpos -124 yalign 0.5 xalign 0.5

    #textbutton _("Return"):
    #    style "return_button"
    #
    #    action Return()

    label title xalign 0.9

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 145
    top_padding 220

    background "bg game_menu_overlay"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380
    ysize 680

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    hover_outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    outlines [ (absolute(1), "#f4cfe5", absolute(0), absolute(0)) ]


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        null height 5
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # Disabled as used for mobile only, where you can touch left/right to rollback
                # vbox:
                #     style_prefix "radio"
                #     label _("Rollback Side")
                #     null height 5
                #     textbutton _("Disable") action Preference("rollback side", "disable")
                #     textbutton _("Left") action Preference("rollback side", "left")
                #     textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    null height 5
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Default menu")
                    null height 5
                    textbutton _("Preferences") action SetField(preferences, "game_menu_screen", "preferences_screen")
                    textbutton _("Save") action SetField(preferences, "game_menu_screen", "save_screen")

                if main_menu:
                    vbox:
                        # we'll show foreground check icon manually anyway
                        style_prefix "check"

                        label _("Security")

                        null height 5

                        if persistent.safe_mode:
                            # we don't use ToggleField here to avoid changing the field before captcha confirmation,
                            # but in counterpart we change Safe Mode and display the check icon manually
                            textbutton _("Safe Mode"):
                                action ShowMenu("screen_captcha")
                                foreground "gui/button/check_selected_foreground.png"
                        else:
                            textbutton _("Safe Mode") action ToggleField(persistent, "safe_mode")

            null height (2 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    hbox:
                        bar value Preference("text speed")

                        # reset to default value of preferences.text_cps in options.rpy
                        textbutton _("Reset"):
                            action Preference("text speed", 0)

                    null height gui.pref_spacing

                    label _("Auto-Forward Time")

                    hbox:
                        bar value Preference("auto-forward time")

                        # reset to default value of preferences.afm_time in options.rpy
                        textbutton _("Reset"):
                            action Preference("auto-forward time", 15)

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        null height gui.pref_spacing

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        null height gui.pref_spacing

                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 400

style accessibility_hbox:
    box_wrap_spacing gui.pref_spacing

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    outlines [ (absolute(1), "#ffffff00", absolute(0), absolute(0)) ]
    selected_outlines [ (absolute(1), "#744675", absolute(0), absolute(0)) ]
    hover_color "#f4cfe5"
    hover_outlines [ (absolute(1), "#744675", absolute(0), absolute(0)) ]

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    outlines [ (absolute(1), "#ffffff00", absolute(0), absolute(0)) ]
    selected_outlines [ (absolute(1), "#744675", absolute(0), absolute(0)) ]
    hover_color "#f4cfe5"
    hover_outlines [ (absolute(1), "#744675", absolute(0), absolute(0)) ]

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")
    hover_outlines [ (absolute(1), "#f4cfe5", absolute(0), absolute(0)) ]

style slider_vbox:
    xsize 685


## Accessibility screen ##############################################################
##
## Similar to Preferences screen, but only for accessibility options.
## It contains a mix of native Accessibility features from Ren'Py
## (found in the Accessibility panel toggled by A key)
## and functions from the Ren'Py Accessibility Add-On

screen accessibility():

    tag menu

    use game_menu(_("Accessibility"), scroll="viewport"):

        style_prefix "accessibility"

        vbox:
            hbox:
                box_wrap True
                # box_wrap_spacing in accessibility style

                vbox:
                    style_prefix "check"

                    # Copied from renpy SDK: 00accessibility.rpy
                    label _("Font Override")

                    null height 5

                    # almost good, but one caveat compared to Ren'Py Accessibility Add-On's approach of replacing font manually in screen say():
                    # Ren'Py applies the transform globally, which is usefully to override even the name/interface font (The Bold Font),
                    # but also overrides the label below as OpenDyslexic, whereas it should always be displayed with the target font
                    textbutton "{font=[gui.text_font]}" + _("Default") + "{/font} / {font=[gui.interface_text_font]}" + _("Default") + "{/font}":
                        action Preference("font transform", "None")
                        style_suffix "radio_button"

                    textbutton "{font=_OpenDyslexic3-Regular.ttf}" + _("Opendyslexic") + "{/font}":
                        action Preference("font transform", "opendyslexic")
                        style_suffix "radio_button"

                vbox:
                    style_prefix "check"

                    label _("Font Color")

                    null height 5

                    textbutton _("Default (Purple)"):
                        action changeColor(gui.text_color)
                        style_suffix "radio_button"

                    # I wanted to make that text black, but when selected, it adds a purple
                    # outline and it's ugly. Better use a style to mimic default radio text becoming
                    # white instead when selected, but didn't manage to inject specific style here
                    textbutton _("Black"):
                        action changeColor("#000000")
                        style_suffix "radio_button"

                vbox:
                    style_prefix "check"

                    # Copied from renpy SDK: 00accessibility.rpy
                    label _("Self-Voicing")

                    null height 5

                    textbutton _("Off"):
                        action Preference("self voicing", "disable")
                        style_suffix "radio_button"

                    textbutton _("Text-to-speech"):
                        action Preference("self voicing", "enable")
                        style_suffix "radio_button"

                vbox:
                    style_prefix "check"

                    # Copied from Ren'Py Accessibility Add-On: screens replacements.rpy
                    label _("Audio")

                    null height 5

                    # Toggle Audio Cues
                    textbutton _("Audio Cues") action ToggleField(preferences, "audio_cues")

                vbox:
                    style_prefix "check"
                    xsize 950

                    # Copied from Ren'Py Accessibility Add-On: screens replacements.rpy
                    label _("HUD")

                    null height 5

                    # Toggle Quick Menu Key Hints
                    textbutton _("Quick Menu Keys (unselect when using self-voicing)") action ToggleField(preferences, "show_quick_menu_keyboard_hints")

                vbox:
                    style_prefix "slider"

                    # Set Textbox Opacity
                    label _("Window Alpha")

                    null height 5

                    hbox:
                        bar value FieldValue(preferences, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.2)

                        textbutton _("Reset"):
                            action SetField(preferences, "say_window_alpha", 1.0)

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height gui.pref_spacing

            vbox:
                style_prefix "slider"

                label _("Text Size Scaling")

                null height 5

                hbox:
                    bar value Preference("font size")

                    textbutton _("Reset"):
                        action Preference("font size", 1.0)

                null height gui.pref_spacing

                label _("Line Spacing Scaling")

                null height 5

                hbox:
                    bar value Preference("font line spacing")

                    textbutton _("Reset"):
                        action Preference("font line spacing", 1.0)

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("O / P")
        text _("Toggles the Preferences screen.")

    hbox:
        label _("T")
        text _("Toggles the TODO list (in-game only).")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    color "#f4cfe5"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    outlines [ (absolute(1), "#9e649f", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(1), "#f4cfe5", absolute(0), absolute(0)) ]
    idle_color "#f4cfe5"
    hover_color "#9e649f"


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()



style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


## Captcha screen #######################################################
##

screen screen_captcha():
    # useful when showing game menu behind semi-transparent overlay to prevent
    # interactions with other widgets, but currently Captcha is shown alone
    # modal True

    tag menu

    add "gui/captcha/captcha_menu_base.png" xalign 0.5 yalign 0.46

    use captcha_button(834, "Verify", return_verify_captcha_action())
    # as soon as we click on SafeMode, we disable it, so Cancel must re-enable it
    # as we failed to pass the captcha
    use captcha_button(1010, "Cancel", [SetField(persistent, "safe_mode", "False"), Return()])

    text "Select all squares with" xpos 745 ypos 275 color "#ffffff" size 24
    text "{b}RUBBER DUCK{/b}" xpos 745 ypos 312 color "#ffffff" size 26
    text "Click {b}Verify{/b} once they are all selected." xpos 745 ypos 358 color "#ffffff" size 22

    grid 3 2:
        xpos 736
        ypos 412
        xspacing 25
        yspacing 13
        use captcha_image("butterfly", "captcha_other1")
        use captcha_image("mallard", "captcha_other2")
        use captcha_image("rubber_duck_toy", "captcha_rubber1")
        use captcha_image("lamp_post", "captcha_other3")
        use captcha_image("rubber_duck_baker", "captcha_rubber2")
        use captcha_image("swan", "captcha_other4")

    if invalid_captcha:
        text "Selection is invalid." xpos 745 ypos 695 color "#000000" size 24

screen captcha_image(image_name, variable_name):
    fixed:
        xsize 132
        ysize 132
        add "gui/captcha/captcha_item_%s.jpg" % image_name:
            xpos 2
            ypos 2
        # frame imagebutton must be above image to show hover color correctly
        imagebutton:
            auto "gui/captcha/captcha_image_frame_%s.png"
            action ToggleVariable(variable_name, "True")

screen captcha_button(_xpos, _text, _action):
    fixed:
        xpos _xpos
        ypos 727

        imagebutton:
            auto "gui/captcha/captcha_button_%s.png"
            action _action

        text _text:
            xanchor 0.5
            xpos +86
            ypos +7
            size 24
            color "#ffffff"

## Item display screen #######################################################
##

#-----------------------------------------------
init python:
    # [ NAME, DESCRIPTION, IMAGE_PATH ]
    item_unknown = ["unknown", "unknown", "images/item/unknown.png"]
    itemList = [["coins", "Coins", "images/item/coins.png"],
                ["hex_key", "Hex Key", "images/item/hex_key.png"],
                ["purchase_permit", "Purchase Permit", "images/item/purchase_permit.png"],
                ["screw_loose", "Screw", "images/item/screw_loose.png"],
                ["screw_tight", "Screw", "images/item/screw_tight.png"]]

    def GetItemByName(_item):
        Item = item_unknown
        for itm in itemList:
          if (itm[0] == _item):
            Item = itm
        return Item

#-----------------------------------------------
screen screen_item(itemName, displaySide="left"):
    $ newxpos = 0
    $ newypos = 0

    if displaySide == "left":
        $ newxpos = 400
        $ newypos = 200
    elif displaySide == "bottom_left":
        $ newxpos = 400
        $ newypos = 400
    elif displaySide == "right":
        $ newxpos = 1100
        $ newypos = 200
    else:  # center
        $ newxpos = 800
        $ newypos = 200

    $ item = GetItemByName(itemName)

    frame:
        background None
        xpos newxpos
        ypos newypos

        add "gui/ItemBox.png"

        add item[2] xpos 18 ypos 17
        text item[1] xpos 166 style_prefix "item"

style item_text is gui_text:
    xalign 0.5
    yalign 0.345
    color "#000000"
    outlines [ (absolute(0), "#9e649f", absolute(0), absolute(0)) ]

## Phone display screen #######################################################
##

style smartphone_time_text is gui_text:
    xpos 770
    ypos 335
    size 40  # ignored??
    color "#ffffff"
    outlines [ (absolute(0), "#9e649f", absolute(0), absolute(0)) ]

screen smartphone(app_name):
    $ currentTime = get_clock_time()

    # semi-transparent underlay to make scene behind smartphone less noticeable
    add "underlay white_half_alpha"

    if app_name == "notifications":
        add "images/bg/sub/smartphone_home_notifications.png":
            xalign 0.5
            yalign 1.0
        text currentTime style_prefix "smartphone_time"
        if has_wifi:
            add "images/bg/sub/wifi.png" xpos 1050 ypos 338
        else:
            add "images/bg/sub/4g.png" xpos 1032 ypos 341
    elif app_name == "dictionary":
        add "images/bg/sub/smartphone_dict_app.png":
            xalign 0.5
            yalign 1.0
        add "images/bg/sub/smartphone_top_bar.png":
            xalign 0.5
            yalign 1.0
        text currentTime style_prefix "smartphone_time"
    elif app_name == "message":
        add "images/bg/sub/smartphone_message_app.png":
            xalign 0.5
            yalign 1.0
        add "images/bg/sub/smartphone_top_bar.png":
            xalign 0.5
            yalign 1.0
        text currentTime style_prefix "smartphone_time"
    elif app_name == "game":
        add "images/bg/sub/smartphone_game.png":
            xalign 0.5
            yalign 1.0

    add "images/bg/sub/smartphone_body.png":
        xalign 0.5
        yalign 1.0

## Task display screen #######################################################
##

#-----------------------------------------------
init python:

    #Task Status
    status_Hidden = "Hidden"  # you should not see this at all!
    status_NotStarted = "Not Started"
    status_InProgress = "In Progress"
    status_Complete = "Complete"
    status_Failed = "Failed"

    #Task Names
    task_HaveLunch = "Have Lunch"
    task_Chair = "Fix the chair"
    task_HexKeyApartment = "Find hex key in apartment"
    task_HexKeyStore = "Buy new hex key"
    task_ScrewSize = "Get size of hex screw"
    task_ScrewPhoto = "Take photo of screw"
    task_ScrewMeter = "Measure screw"
    task_Store = "Go to DIY store"
    task_Bus = "Take the bus"
    task_Ticket = "Buy ticket and get on"
    task_Coins = "Get coins"
    task_BuyFood = "Buy some food with a bill"
    task_Stop = "Stop near DIY store and get off"
    task_PushClosestStop = "Push nearest stop button"
    task_StandUp = "Stand up and push second nearest stop button"
    task_InstallStopApp = "Install app to send stop signal"
    task_AskPassenger = "Ask another passenger to push stop button"
    task_WaitStop = "Wait for another passenger to push stop button"
    task_FindHexKey = "Find hex key"
    task_CheckScrewdrivers = "In the screwdriver shelves"
    task_CheckOthers = "In other shelves"
    task_BuyHexKey = "Buy hex key"
    task_Permit = "Get purchase permit"
    task_HealthNumber = "Get Health Insurance Number"

    # Free space subtree
    task_FreeSpace = "Free space on smartphone"
    task_DeleteDict = "Delete dictionary app"
    task_DeleteGame = "Delete game"
    task_PlayGame = "Play game"
    task_CreateAccount = "Create account"
    task_InventPassword = "Invent password"
    task_UpdateApps = "Update apps"
    task_LightBulb = "Change the light bulb"
    task_BuyLightBulb = "Buy new light bulb"

    # Sister request tree
    task_TranslateSentence = "Translate sentence for sis"
    task_GetContext = "Get more info on context"

    # to distinguish freeing space to get ID (sub-tree) or just like that,
    # after reading notifications (separate tree)
    def make_task_suffix(free_space_context):
        if free_space_context.startswith("check "):
            checked_file = free_space_context[6:]
            return " (%s)" % checked_file
        else:
            return ""

    check_photo_suffix = make_task_suffix("check photo")           # " (photo)"
    check_health_suffix = make_task_suffix("check health no")  # " (health number)"

    # [ TASKNAME, LEVEL, STATUS]
    task_unknown = ["Unknown", 0, status_InProgress]

    # initial task list has everything not hidden just to test GUI when
    # commenting out the initial ResetAllTasks
    initial_task_list = [
        # light bulb at top just so player can see it immediately near game end
        [task_LightBulb, 0, status_InProgress],
        [task_BuyLightBulb, 1, status_InProgress],
        [task_HaveLunch, 0, status_InProgress],
        [task_Chair, 1, status_InProgress],
        [task_HexKeyApartment, 2, status_InProgress],
        [task_HexKeyStore, 2, status_InProgress],
        [task_ScrewSize, 3, status_InProgress],
        [task_ScrewPhoto, 4, status_InProgress],
        [task_ScrewMeter, 4, status_InProgress],
        [task_Store, 3, status_InProgress],
        [task_Bus, 4, status_InProgress],
        [task_Ticket, 5, status_NotStarted],
        [task_Coins, 6, status_NotStarted],
        [task_BuyFood, 7, status_Complete],
        [task_Stop, 5, status_Complete],
        [task_PushClosestStop, 6, status_Complete],
        [task_StandUp, 6, status_Complete],
        [task_InstallStopApp, 6, status_Complete],
        [task_AskPassenger, 6, status_Complete],
        [task_WaitStop, 6, status_Complete],
        [task_FindHexKey, 3, status_NotStarted],
        [task_CheckScrewdrivers, 4, status_NotStarted],
        [task_CheckOthers, 4, status_InProgress],
        [task_FreeSpace + check_photo_suffix, 5, status_InProgress],
        [task_DeleteDict + check_photo_suffix, 6, status_NotStarted],
        [task_DeleteGame + check_photo_suffix, 6, status_NotStarted],
        [task_PlayGame + check_photo_suffix, 7, status_InProgress],
        [task_UpdateApps + check_photo_suffix, 8, status_NotStarted],
        [task_CreateAccount + check_photo_suffix, 8, status_InProgress],
        [task_InventPassword + check_photo_suffix, 9, status_InProgress],
        [task_BuyHexKey, 3, status_InProgress],
        [task_Permit, 4, status_Failed],
        [task_HealthNumber, 5, status_InProgress],
        [task_FreeSpace + check_health_suffix, 6, status_InProgress],
        [task_DeleteDict + check_health_suffix, 7, status_NotStarted],
        [task_DeleteGame + check_health_suffix, 7, status_NotStarted],
        [task_PlayGame + check_health_suffix, 8, status_InProgress],
        [task_UpdateApps + check_health_suffix, 9, status_NotStarted],
        [task_CreateAccount + check_health_suffix, 9, status_InProgress],
        [task_InventPassword + check_health_suffix, 10, status_InProgress],
        [task_FreeSpace, 0, status_InProgress],
        [task_DeleteDict, 1, status_NotStarted],
        [task_DeleteGame, 1, status_NotStarted],
        [task_PlayGame, 2, status_InProgress],
        [task_UpdateApps, 3, status_NotStarted],
        [task_CreateAccount, 3, status_InProgress],
        [task_InventPassword, 4, status_InProgress],
        [task_TranslateSentence, 0, status_InProgress],
        [task_GetContext, 1, status_InProgress]
    ]

#-----------------------------------------------
    def ResetAllTasks():
        for task in store.task_list:
            task[2] = status_Hidden

        active_tasks_stack.clear()
        return

    def GetTaskStatus(_taskName):
        for task in store.task_list:
            if task[0] == _taskName:
                return task[2]
        return None

    def SetTaskStatus(_taskName, _status):
        for task in store.task_list:
            if task[0] == _taskName:
                task[2] = _status
        return

    def RevealTask(_taskName):
        SetTaskStatus(_taskName, status_NotStarted)
        return

    def StartTask(_taskName, notify=False):
        SetTaskStatus(_taskName, status_InProgress)
        store.indicator_newTask = True

        if notify:
            renpy.notify("Starting new major task: " + _taskName)
            renpy.play(audio.task_update)

        # push to stack, the last task is the active one
        if _taskName not in store.active_tasks_stack:
            store.active_tasks_stack.append(_taskName)
        else:
            print("WARNING in StartTask: %s already added to active_tasks_stack" % _taskName)
        return

    def HasCompletedTask(_taskName):
        return GetTaskStatus(_taskName) == status_Complete

    def CompleteTask(_taskName):
        SetTaskStatus(_taskName, status_Complete)
        RemoveFromActiveTasks(_taskName)
        return

    def FailTask(_taskName):
        SetTaskStatus(_taskName, status_Failed)
        RemoveFromActiveTasks(_taskName)
        return

    def RemoveFromActiveTasks(_taskName):
        for i, active_task_name in enumerate(store.active_tasks_stack):
            if active_task_name == _taskName:
                del store.active_tasks_stack[i]
                return

        print("WARNING in RemoveFromActiveTasks: %s not found in active_tasks_stack" % _taskName)

#-----------------------------------------------
screen tasktree():
    tag menu

    # Reset newTask indicator in callback
    on "show" action Function(on_show_tasktree)

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("TODO List"), scroll="viewport"):

        style_prefix "about"

        # optional safety check (should be init on start)
        # note that "store." is mandatory for task_list to avoid NoneType error,
        # although we are not in Python code
        if store.task_list:
            vbox:
                for task in store.task_list:
                    $taskLevel = task[1]
                    if task[1] == 0:
                        $taskName = "{size=+10}" + str(task[0]) + "{/size}"
                    else:
                        $taskName = "|_ " + str(task[0])
                    if task[2] == status_NotStarted:
                        text taskName + ": {size=-5}" + task[2] + "{/size}" xpos 50*taskLevel color "#3b3b3b"
                    elif task[2] == status_InProgress:
                        # the current task (last of active ones) has a brighter color and "current" hint
                        if len(store.active_tasks_stack) > 0 and task[0] == store.active_tasks_stack[-1]:
                            text taskName + ": {size=-5}" + task[2] + " (Current){/size}" xpos 50*taskLevel color "#cb78e4"
                        else:
                            text taskName + ": {size=-5}" + task[2] + "{/size}" xpos 50*taskLevel
                    elif  task[2] == status_Complete:
                        text taskName + ": {size=-5}" + task[2] + "{/size}" xpos 50*taskLevel color "#3c9c21"
                    elif  task[2] == status_Failed:
                        text taskName + ": {size=-5}" + task[2] + "{/size}" xpos 50*taskLevel color "#d92118"
                    elif  task[2] == status_Hidden:
                        #text taskName + " : " + task[2] xpos 50*taskLevel color "#6b7867"
                        pass #Do not show unstarted tasks

screen preferences_button():
    python:
        button_action = None
        hint_text = None

        is_preferences_screen_open = renpy.get_screen("preferences") is not None
        if is_preferences_screen_open:
            button_action = Return()
            hint_text = "P (close)"
        else:
            button_action = ShowMenu("preferences")
            hint_text = "P"

    imagebutton auto "gui/button/optionsbutton_%s.png" focus_mask True action button_action
    if preferences.show_quick_menu_keyboard_hints:
        text hint_text xpos 1700 ypos 969 style_prefix "quick"
    key "toggle_preferences" action button_action

screen tasktree_button():
    if not main_menu and unlocked_tasktree:
        python:
            button_action = None
            hint_text = None

            is_tasktree_screen_open = renpy.get_screen("tasktree") is not None
            if is_tasktree_screen_open:
                button_action = Return()
                hint_text = "T (close)"
            else:
                button_action = ShowMenu("tasktree")
                hint_text = "T"

        imagebutton auto "gui/button/taskbutton_%s.png" focus_mask True action button_action
        if indicator_newTask:
            add "gui/button/indicator_new.png"
        if preferences.show_quick_menu_keyboard_hints:
            text hint_text xpos 1475 ypos 969 style_prefix "quick"
        key "toggle_tasktree" action button_action
