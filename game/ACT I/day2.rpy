label actI_day2:
    plh "Saturday"
    plh "Awaken, hungry. Go to the cafeteria."
    show sars normal at Position(xalign=0.0, yanchor=0.66)
    show rab normal at Position(xalign=0.23, yanchor=0.66)
    show hiv normal at Position(xalign=0.6, yanchor=0.66)
    show aids normal at Position(xalign=0.8, yanchor=0.66)
    show mal normal at Position(xalign=1.0, yanchor=0.66)
    show llov normal at Position(xalign=0.4, yanchor=0.66)
    plh "Meet more characters. Testing some sprites"
    plh "The protagonist is free to do what he wants. There will probably be a choice point leading to different scenes now."
    call actI_generic_evening
    return