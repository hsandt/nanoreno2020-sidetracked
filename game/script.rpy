init:
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define mc = Character("Katell", color="#BD8CBE")
    define sister = Character("Tifenn", what_font=gui.jp_text_font, color="#b97d91")
    define driver = Character("Bus driver", color="#b87639")
    define cashier = Character("Cashier", color="#49b976")
    define printer = Character("Printer", color="#CCCCCC")

    # Story event flags
    define has_wifi = False
    define has_seen_base_notifications = False
    define has_seen_space_left_since_last_change = False
    define has_seen_sister_request = False
    define has_given_fake_translation = False
    define has_given_silence = False
    define has_installed_bus_stop_app = False
    define has_updated_apps = False
    define has_deleted_small_apps = False
    define has_tried_dict = False
    define has_tried_game_count = 0
    define has_deleted_game = False
    define has_freed_space = False
    define has_invented_pwd = False
    define has_navigated_slowly = False
    define has_navigated_very_slowly = False
    define has_explored_screwdrivers = False
    define has_explored_power_screwdrivers = False
    define free_space = 400
    define sister_request_phase = 0
    define sister_request_reply = None
    define queuer_dissatisfaction = 0  # how much customers behind you are impatient in Permit scene
    define wrapping_scene = None  # high context scene, used to restore correct BGM
    define notifications_context = None
    define update_context = None
    define free_space_context = None
    define play_context = None

    define task_list = None
    define active_tasks_stack = None

    # UI variables
    define is_character_sitting = False
    define is_showing_smartphone = False
    # Current time in minutes. Convert to readable time with minutes_to_clock_time
    define currentTime = 0
    # New Task Indicator
    define indicator_newTask = False
    define new_task_clear_count = 0  # how many times the player checked for a new task

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
    if not persistent.unlocked:
        "\"Sidetracked\" is an application downloaded from the Internet, and has been made by unrecognized author \"komehara\"."
        "It cannot be started unless Safe mode is disabled in the options."
        return

    $ from copy import deepcopy
    $ store.task_list = deepcopy(initial_task_list)
    $ store.active_tasks_stack = []  # will be cleared by ResetAllTasks, but need to initialize
    # Reset all tasks to Not Started so they dont show up
    # Comment out to check GUI appearance
    $ ResetAllTasks()


label lbl_realstart:
    jump s1_1

# Restore BGM from context. Useful after using smartphone.
label restore_bgm:
    if wrapping_scene == "broken_chair":
        $ play_music("apartment")
    elif wrapping_scene == "bus_stop":
        $ play_music("street")
    elif wrapping_scene == "bakery":
        $ play_music("store")
    elif wrapping_scene == "bus":
        $ play_music("street")
    elif wrapping_scene == "store":
        $ play_music("store")
    elif wrapping_scene == "light_bulb":
        pass
