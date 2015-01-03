label prologue:
    call prologue_name
    call prologue_0
    call prologue_river
    return
label prologue_name:
    $ name = renpy.input("What is the protagonist's name?", "Chungus", pixel_width=310)#Should be about 12 W's
    $ name = name.strip()
    $ if name == '': name = "Chungus"
    menu:
        "Is [name]-kun correct?"
        "Yes":
            pass
        "No":
            jump prologue_name
    return
label prologue_0:
    #play music test tubes
    plh "All the prologue stuff here."
    return
    
label prologue_river:
    $ scene_switcher("prologue_river", "dread")
    return
