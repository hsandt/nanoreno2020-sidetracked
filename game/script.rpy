init:
    transform character_left:
        xalign 0.2
        yalign 1.0

    transform character_right:
        xalign 0.8
        yalign 1.0

    transform item_left:
        xalign 0.3
        yalign 0.4

    transform item_right:
        xalign 0.7
        yalign 0.4

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define mc = Character("MC", color="#BD8CBE")
    define driver = Character("Driver", color="#b87639")
    define cashier = Character("Cashier", color="#49b976")
    define printer = Character("Printer", color="#CCCCCC")

    # Story event flags
    define has_wifi = False
    define has_seen_base_notifications = False
    define has_seen_space_left_since_last_change = False
    define has_seen_sister_request = False
    define has_given_fake_translation = False
    define has_given_silence = False
    define has_updated_apps = False
    define has_deleted_small_apps = False
    define has_tried_dict = False
    define has_tried_game = False
    define has_deleted_game = False
    define has_freed_space = False
    define has_explored_screwdrivers = False
    define has_explored_power_screwdrivers = False
    define free_space = 400
    define sister_request_phase = 0
    define update_context = None
    define play_context = None

    # UI variables
    define is_showing_smartphone = False
    define currentTime = "17:00"

init:
    # Defining persistent variables

    if persistent.unlocked is None:
      $persistent.unlocked = False
    if persistent.captcha  is None:
      $persistent.captcha = False
      # The script of the game goes in this file.

    # Captcha variables
    $ captcha_rubber = False
    $ captcha_other1 = False
    $ captcha_other2 = False
    $ captcha_other3 = False
    $ captcha_other4 = False
    $ captcha_other5 = False
    $ invalid_captcha = False


# The game starts here.
label start:
    #Reset all tasks to Not Started so they dont show up
    $ResetAllTasks()
    if not persistent.unlocked:
        "\"Sidetracked\" is an application downloaded from the Internet, and has been made by unrecognized author \"komehara\"."
        "It cannot be started unless Safe mode is disabled in the options."
        return

label lbl_realstart:
    jump s1_1
