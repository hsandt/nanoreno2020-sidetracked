init:
    #Defining persistent variables

    if persistent.unlocked is None:
      $persistent.unlocked = False
    if persistent.captcha  is None:
      $persistent.captcha = False
      # The script of the game goes in this file.

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    $ captcha_rubber = False
    $ captcha_other1 = False
    $ captcha_other2 = False
    $ captcha_other3 = False
    $ captcha_other4 = False
    $ captcha_other5 = False
    $ invalid_captcha = False

    define e = Character("Eileen")


# The game starts here.

label start:
    if not persistent.unlocked:
        "this game has been made by an unauthorised author \"komehara\" and cannot be started unless safe mode is disabled in the options"
        return

label lbl_realstart:
    jump s1_1
