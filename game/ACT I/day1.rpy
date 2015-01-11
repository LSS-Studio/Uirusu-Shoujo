label actI_day1:
    scene black
    show ebby normal at Position(xalign=0.0, yanchor=0.66)
    show bp normal at Position(xalign=0.25)
    show marb normal
    show pol normal at Position(xalign=0.75)
    show atsuo normal at right
    plh "Friday Evening"
    plh "Wake up on examination table. meet a few major characters."
    show joki full normal behind ebby with None:
        xanchor 0.0 xpos 1.0 yanchor 0.9 ypos 1.0 zoom 0.7
    show atsuo at Position(xalign=1.05)
    show pol at Position(xalign=0.7)
    show joki:
        xalign 0.85
    with ease
    plh "Enter Joki."
    scene black
    show ebby joy:
        xalign 0.5 ypos 1.0 yanchor 0.55 zoom 1.5
    plh "Left in the care of Ebola-chan"
    scene bg prot_room
    plh "Protagonist's room"
    plh "Play sleeping animation."
    return