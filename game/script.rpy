init:
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define mc = Character("Katell", color="#BD8CBE")
    define sister = Character("Tifenn", what_font=gui.jp_text_font, color="#b97d91")
    define driver = Character("Bus driver", color="#b87639")
    define cashier = Character("Cashier", color="#49b976")
    define printer = Character("Printer", color="#CCCCCC")

    # Story event flags
    default has_wifi = False
    default has_seen_base_notifications = False
    default has_seen_space_left_since_last_change = False
    default has_seen_sister_request = False
    default has_given_fake_translation = False
    default has_given_silence = False
    default has_installed_bus_stop_app = False
    default has_updated_apps = False
    default has_deleted_small_apps = False
    default has_tried_dict = False
    default has_tried_game_count = 0
    default has_deleted_game = False
    default has_freed_space = False
    default has_invented_pwd = False
    default has_navigated_slowly = False
    default has_navigated_very_slowly = False
    default has_explored_screwdrivers = False
    default has_explored_power_screwdrivers = False
    default free_space = 400
    default sister_request_phase = 0
    default sister_request_reply = None
    default queuer_dissatisfaction = 0  # how much customers behind you are impatient in Permit scene
    default wrapping_scene = None  # high context scene, used to restore correct BGM
    default notifications_context = None
    default update_context = None
    default free_space_context = None
    default play_context = None

    default task_list = None
    default active_tasks_stack = None

    # UI variables
    default is_character_sitting = False
    default is_showing_smartphone = False
    # Current time in minutes. Convert to readable time with minutes_to_clock_time
    default currentTime = 0
    # New Task Indicator
    default indicator_newTask = False
    default new_task_clear_count = 0  # how many times the player checked for a new task

    # Defining persistent variables
    default persistent.safe_mode = True

    # Captcha variables
    $ captcha_rubber1 = False
    $ captcha_rubber2 = False
    $ captcha_other1 = False
    $ captcha_other2 = False
    $ captcha_other3 = False
    $ captcha_other4 = False
    $ invalid_captcha = False


# The game starts here.
label start:
    $ quick_menu = False

    if persistent.safe_mode:
        "\"Sidetracked\" is an application downloaded from the Internet, and has been made by unrecognized author \"komehara\"."
        "It cannot be started unless Safe mode is disabled in the Preferences."
        return

    $ quick_menu = True

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
