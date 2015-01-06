#CG
init -12:
    image dread prologue_nets = "artsets/dread/scenes/prologue/nets.png"
    image dread prologue_emma_sad = "artsets/dread/scenes/prologue/emma sad.png"
    
#SCENES
init:
    image dread_tuonen_bg = "artsets/dread/scenes/tuonen/tuonen bg.png"
    image dread_tuonen_waves1 = "artsets/dread/scenes/tuonen/tuonen waves 1.png"
    image dread_tuonen_waves2 = "artsets/dread/scenes/tuonen/tuonen waves 2.png"
    image dread_tuonen_waves3 = "artsets/dread/scenes/tuonen/tuonen waves 3.png"
    image dread_tuonen_boat = "artsets/dread/scenes/tuonen/tuonen boat.png"
    
label dread_prologue_river:
    scene black
    scene dread_tuonen_bg
    play music m_swan
    show dread_tuonen_waves3:
        xpos 0.49 xanchor 0.5 yalign 1.0
        parallel:
            ease 4.0 xpos 0.51
            ease 4.0 xpos 0.49
            repeat
    show dread_tuonen_boat:
        xalign 0.5 yalign 0.45
        rotate 6
        parallel:
            ease 2.0 rotate -6
            ease 2.0 rotate 6
            repeat
        parallel:
            easein 80 zoom 0.2
        parallel:
            easein 80 xalign 0.3
        parallel:
            easein 80 yalign 0.6
    show dread_tuonen_waves2:
        xpos 0.48 ypos 0.98 xanchor 0.5 yanchor 1.0
        parallel:
            ease 4.0 xpos 0.52
            ease 4.0 xpos 0.48
            repeat
        parallel:
            ease 2.0 ypos 0.98
            ease 2.0 ypos 1.02
            repeat
    show dread_tuonen_waves1:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
        alignaround (.5, 1.0)
        parallel:
            linear 2.0 ypos 1.1 clockwise circles 1
            repeat
        parallel:
            ease 2.0 xpos 0.55
            ease 2.0 xpos 0.45
            repeat
    show layer master:
        zoom 1.5 xalign 0.5 yalign 0.5
        ease 60 zoom 1.0
    with Dissolve(5)
    pause 55
    stop music fadeout 5
    scene black with Dissolve(5)
    return
