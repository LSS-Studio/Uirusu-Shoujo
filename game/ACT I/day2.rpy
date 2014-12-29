label actI_day2:
    plh "Awaken, hungry. Go to the cafeteria."
    show sars normal at left
    show rab normal at Position(xalign=0.23)
    show hiv normal at Position(xalign=0.6)
    show aids normal at Position(xalign=0.8)
    show mal normal at right
    show llov normal at Position(xalign=0.4)
    plh "Meet more characters. Testing some sprites"
    plh "The protagonist is free to do what he wants. There will probably be a choice point leading to different scenes now."
    call actI_generic_evening
    return