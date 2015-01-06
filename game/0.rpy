label initialize_calendar:
    #Ensures renpy properly tracks the calendar object for saving and rollback.
    $ calendar = icalendar
    return

python early:
#calendar
    # using a single dictionary instead of a list of dictionaries for maximum flexibility
    ## Syntax for calendar keys: "day,name"
    icalendar = dict()
    day = 0
#points
    def set_points(name="",points=0.0,day=None):
        if day==None: day = globals()["day"] #default is current day
        if points==None: points=0
        if name==None: name=""
        key = str(day)+","+name
        # If key doesn't exist, add it.
        if key not in calendar:
            calendar[key] = 0.0
        calendar[key] += float(points)
        
    def points(name="",day=None):
        if day==None: day = globals()["day"] #default is current day
        #calculate points
        p = 0.0
        for d in xrange(day+1):
            key = str(d)+","+name
            if key in calendar:
                f = 365 #points fade completely after this many days
                i = 1 - ((day - d) / float(f))
                p += calendar[key] * ((abs(i) + i) / 2)
        return p

    def m_change_parse(lex):
        name = lex.word()
        point = lex.float()
        day = lex.integer()
        return (name, point, day)
    
    def m_change_exec(o):
        name, point, day = o
        set_points(name,point,day)
    
    renpy.register_statement("points", parse = m_change_parse, execute = m_change_exec)
    