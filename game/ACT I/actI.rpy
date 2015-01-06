label actI:
    call initialize_calendar
    call prologue
    call actI_title
    call actI_structure
    plh "end of Act I."
    return
    
label actI_title:
    plh "Show act I title card."
    return

label actI_structure:
    # Day structure might become more sophisticated in the future.
    day set 1
label actI_loop:
    # Calls a label for the current day if it exists, else calls a generic day.
    if renpy.has_label("actI_day"+str(day)):
        $renpy.call("actI_day"+str(day))
    else:
        call actI_generic_day
    day end
    if day < 14: # Act I continues for about 2 weeks.
        jump actI_loop
    return
    
#The generic day labels are used when no script for the current day exists. They are place holders.
label actI_generic_day:
    call actI_generic_morning
    call actI_generic_noon
    call actI_generic_afternoon
    call actI_generic_evening
    return
label actI_generic_morning:
    plh "Dawn of day [day]."
    return
label actI_generic_noon:
    plh "If weekday go to class. Else freetime."
    return
label actI_generic_afternoon:
    plh "Freetime."
    return
label actI_generic_evening:
    plh "Go to bed."
    return

label actI_letters:
    plh "Tally the scores"
    plh "Protag receives letters from the girls that like him asking him to attend the dance. If he receives more than one, he must choose only one."
    plh "If he receives no letters, trigger the fallback route."
    return
label actI_futsal:
    plh "A futsal game happens at the very end of act I."
    return
