
#backgrounds, images, and character definitions have been moved to definitions.rpy

# The game starts here.
label start:
    stop music
    scene bg black
    menu:
        "Demo":
            jump final
        "Skeleton":
            jump actI
    return

init:
    if persistent.first is None:
        $ persistent.first = True
    if persistent.ecchi is None:
        $ persistent.ecchi = False
label splashscreen:
    if persistent.first:
        scene bg root
        $renpy.transition(dissolve)
        call screen eula
        $renpy.transition(fade)
        call screen h_toggle
        scene black with dissolve
        $ persistent.ecchi = _return
        $ persistent.first = False
    return


