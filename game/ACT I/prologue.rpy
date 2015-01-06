label prologue:
    call prologue_name
    call prologue_0
    call prologue_nets
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

init:
    $ cg_switcher("prologue_nets", "dread")
    $ cg_switcher("prologue_emma_sad", "dread")
    
label prologue_nets:
    scene prologue_nets with fade
    "To my surprise, my bosses found room for her on a supply flight, and she was in my arms before I knew it."
    "To her credit, she remained silent about the rather hostile conditions - the minimal air conditioning, the mosquito netting everywhere, the Army rations, the dust that seeps into everything, and the constant sound of tarpaulins rustling in the wind."
    emma "Is this what you thought it would be? Is it what you really want?"
    prot "Yes, and no, respectively. It's actually a little bit better than I expected, being in the middle of fucking nowhere. As for what I want, that's a little bit irrelevant right now. Duty calls."
    scene prologue_emma_sad with fade
    emma "Is that what they tell you? When does duty stop and life begin? Where do I fit in? When will there be time for us?"
    "I struggle to find answers and reassurances, but I have none. Emma kept quiet for the next few days about the subject, but I could see it in her eyes every time I have to report in for work."
    "The pile of paperwork on my cheap folding table continued to grow. Then, just like that,{nw}"
    scene prologue_emma_sad:
        "black" with Dissolve(1)
    "The pile of paperwork on my cheap folding table continued to grow. Then, just like that,{fast} she was gone again. I half wonder if it really happened at all."
    return
