# Important: To fix the "Couldn't find file 'gui/'" error,
# ensure that the 'gui' directory is present in the 'game' folder of your Ren'Py project.
# This directory contains necessary GUI assets and is required for Ren'Py to load the default graphical user interface.
# If it's missing, create a new Ren'Py project using the Ren'Py launcher and copy the 'gui' directory from there into your project's 'game' folder.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen") # Note: This character is unused but harmless

# Character Definitions
define t = Character("Tomoya", image="tomoya")
define n = Character("Nagisa", image="nagisa")
define k = Character("Kyou", image="kyou")
define r = Character("Ryou", image="ryou")
define ko = Character("Kotomi", image="kotomi")
define to = Character("Tomoyo", image="tomoyo")
define f = Character("Fuko", image="fuko")

# Image Definitions (from images/ folder)
image tomoya normal = "images/tomoya_normal.png"
image tomoya sad = "images/tomoya_sad.png"
image nagisa smile = "images/nagisa_smile.png"
image nagisa shy = "images/nagisa_shy.png"
image kyou angry = "images/kyou_angry.png"
image ryou smile = "images/ryou_smile.png"
image kotomi happy = "images/kotomi_happy.png"
image tomoyo serious = "images/tomoyo_serious.png"
image fuko star = "images/fuko_star.png"

# Backgrounds (from images/ folder)
image bg school = "images/school_bg.png"
image bg classroom = "images/classroom_bg.png"
image bg library = "images/library_bg.png"
image bg park = "images/park_bg.png"
image bg home = "images/home_bg.png"

# Variables for Game Mechanics
default nagisa_affection = 0
default kyou_affection = 0
default ryou_affection = 0
default kotomi_affection = 0
default tomoyo_affection = 0
default fuko_affection = 0
default drama_club_progress = 0

# Define audio files and music control screen in an init block
init:
    define audio.opening_theme = "fire/music/opening_theme.mp3"
    define audio.school_theme = "fire/music/school_theme.mp3"
    define audio.hopeful_theme = "fire/music/hopeful_theme.mp3"
    define audio.festival_theme = "fire/music/festival_theme.mp3"
    define audio.nagisa_ending = "fire/music/nagisa_ending.mp3"
    define audio.door_open = "fire/sfx/door_open.wav"

    # Define a simple screen to control music (optional)
    screen music_control():
        vbox:
            text "Music Control"
            textbutton "Play Music" action Play("music", audio.opening_theme, loop=True)
            textbutton "Stop Music" action Stop("music")
            textbutton "Close" action Hide("music_control")

# The game starts here.
label start:
    play music audio.opening_theme fadein 1.0
    scene bg school with fade
    # Optional: Uncomment the line below to show the music control screen at start
    # show screen music_control
    "Welcome to the Clannad Visual Novel!"
    "In this game, you’ll follow Tomoya Okazaki’s journey through high school."
    "You’ll make choices that affect your relationships and the story’s outcome."
    "Your decisions will increase affection points with characters, unlocking different paths."
    "Let’s begin!"
    jump introduction

# Introduction Scene
label introduction:
    scene bg school with fade
    play music audio.school_theme fadein 1.0
    "It’s the start of a new school year at Hikarizaka High School."
    show tomoya normal at center with dissolve
    t "Another year, same old routine. I’m just going through the motions."
    "The cherry blossoms are in bloom, but they don’t mean much to me."
    "As I walk up the hill to school, I notice a girl standing alone."
    show nagisa shy at right with moveinright
    n "Um... excuse me..."
    t "Huh? Are you talking to me?"
    n "Yes. I’m Nagisa Furukawa. I think we’re in the same class."
    t "Oh, right. Tomoya Okazaki. Nice to meet you."
    n "Nice to meet you too, Okazaki-san."
    menu:
        "What should I say?"
        "Ask about the cherry blossoms":
            t "You seem interested in the cherry blossoms."
            n "Yes, they’re beautiful. They make me feel like something new is starting."
            $ nagisa_affection += 1
        "Comment on the weather":
            t "Nice weather today, huh?"
            n "Yes, it’s a perfect day for the first day of school."
    "We chat for a bit before heading to class."
    jump classroom

# Classroom Scene
label classroom:
    scene bg classroom with fade
    play sound audio.door_open
    show tomoya normal at left with dissolve
    "The classroom is noisy as usual. I take my seat near the back."
    show kyou angry at right with moveinright
    k "Hey, Okazaki! Did you do the summer homework?"
    t "Nope. Did you?"
    k "Of course I didn’t! Who has time for that?"
    show ryou smile at center with dissolve
    r "Um, Kyou-nee, we really should have done it..."
    k "Relax, Ryou. We’ll figure it out."
    menu:
        "How should I respond?"
        "Offer to help Ryou":
            t "I could help you out, Ryou, if you’re stuck."
            r "Really? Thank you, Okazaki-kun!"
            $ ryou_affection += 1
        "Tease Kyou":
            t "Sounds like you’re in trouble, Kyou."
            k "Shut it, Okazaki!"
            $ kyou_affection += 1 # Kyou likes the banter
    "The day drags on, but something feels different."
    jump nagisa_drama

# Nagisa Drama Scene
label nagisa_drama:
    scene bg classroom with fade
    show nagisa smile at center with dissolve
    n "Okazaki-san, I’ve been thinking about starting the drama club again."
    t "Drama club? Why?"
    n "I love theater. It’s been my dream since I was little."
    t "Sounds like a lot of work."
    menu:
        "What should I do?"
        "Offer to help":
            t "Alright, I’ll help you out."
            n "Really? Thank you so much!"
            $ nagisa_affection += 2
            $ drama_club_progress += 1
            jump drama_club_start
        "Decline":
            t "Sorry, not my thing."
            n "Oh... I understand."
            jump fuko_meeting

# Drama Club Start Scene
label drama_club_start:
    "We spend days recruiting members and fixing up the clubroom."
    play music audio.hopeful_theme
    "Nagisa’s determination starts to rub off on me."
    jump fuko_meeting

# Fuko Meeting Scene
label fuko_meeting:
    scene bg school with fade
    show fuko star at center with dissolve
    f "Hi! Want a starfish?"
    t "A what?"
    f "A starfish! I carved it myself."
    show nagisa smile at right
    n "She’s Fuko Ibuki. She’s a little... unique."
    menu:
        "Accept the starfish?"
        "Take it":
            t "Sure, why not?"
            f "Yay! You’re my friend now!"
            $ fuko_affection += 2
        "Refuse":
            t "No thanks."
            f "Aw... okay."
    "Fuko’s strange behavior sticks with me."
    jump kotomi_meeting

# Kotomi Meeting Scene
label kotomi_meeting:
    scene bg library with fade
    show kotomi happy at center with dissolve
    "I find a quiet girl reading in the library."
    t "Hey, what’s your name?"
    ko "Kotomi. Kotomi Ichinose."
    t "I’m Tomoya. What are you reading?"
    ko "A book on quantum mechanics."
    menu:
        "Talk to her?"
        "Ask about the book":
            t "Quantum mechanics? That’s intense."
            ko "Yes, it’s fascinating!"
            $ kotomi_affection += 1
            "Kotomi seems lonely. Maybe I’ll check on her later."
        "Leave her alone":
            t "I’ll let you read."
    jump tomoyo_meeting

# Tomoyo Meeting Scene
label tomoyo_meeting:
    scene bg school with fade
    show tomoyo serious at center with dissolve
    to "You’re Okazaki, right?"
    t "Yeah. And you are?"
    to "Tomoyo Sakagami. I’m running for student council."
    t "Good luck with that."
    menu:
        "Support her?"
        "Encourage her":
            t "You’d make a great president."
            to "Thanks. I appreciate it."
            $ tomoyo_affection += 1
            "Tomoyo’s got a strong presence."
        "Stay neutral":
            t "Cool, I guess."
    jump festival_prep

# Festival Preparation Scene
label festival_prep:
    scene bg classroom with fade
    play music audio.festival_theme
    show nagisa smile at center
    n "The festival is tomorrow! We’re almost ready."
    t "You’ve worked hard, Nagisa."
    n "It’s all thanks to you, Okazaki-san."
    if drama_club_progress > 0:
        "The play is a success, and Nagisa shines on stage."
        $ nagisa_affection += 3
    else:
        "Without enough help, the play struggles."
    jump ending

# Ending Scene
label ending:
    scene bg school with fade
    stop music fadeout 1.0
    if nagisa_affection >= 5:
        play music audio.nagisa_ending
        show nagisa smile at center
        n "Okazaki-san, I couldn’t have done this without you."
        t "You’re stronger than you think, Nagisa."
        "Nagisa and I grow closer, starting a new chapter together."
    elif kyou_affection >= 3:
        show kyou angry at center
        k "You’re not so bad, Okazaki."
        t "You either, Kyou."
        "Kyou and I find a strange sort of friendship."
    elif fuko_affection >= 3:
        show fuko star at center
        f "Friends forever, right?"
        t "Yeah, Fuko. Forever."
        "Fuko’s quirky spirit stays with me."
    else:
        t "The year ends quietly. Maybe next time will be different."
    "The end."
    return