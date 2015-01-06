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
    
    def newday(): #temporary solution because all writers are offline atm
        day += 1
    
    def set_points(name = "", point = 0.0, day = None):
        if not day: day = globals()["day"] #default is current day
        if not isinstance(point, float): points = 0.0
        if not isinstance(name, str): name = ""
        calendar[day, name] = point
        
    def points(name = "", day = None):
        if day==None: day = globals()["day"] #default is current day
        #calculate points
        p = 0.0
        for d in xrange(day + 1):
            key = (d, name)
            if key in calendar:
                f = 365 #points fade completely after this many days
                i = 1 - ((day - d) / f)
                p += calendar[key] * ((abs(i) + i) / 2)
        return p
    
    def shift_points(name = "", point = 0.0, day = None): #shorthand for "set_points(name, points(name, day) + point)"
        if not day: day = globals()["day"]
        if not isinstance(point, float): points = 0.0
        if not isinstance(name, str): name = ""
        calendar[day, name] += point #not using set_points because optimisation
    
    def m_change_parse(lex):
        name = lex.word()
        point = lex.float()
        day = lex.integer()
        return (name, point, day)
    
    def m_change_exec(o):
        name, point, day = o
        calendar[day, name] = point #not using set_points because optimisation
    
    renpy.register_statement("points", parse = m_change_parse, execute = m_change_exec)
    
    def m_day_parse(lex):
        comm = lex.word()
        if comm == "end": return (comm, None)
        val = lex.integer()
        return (comm, val)
    
    def m_day_exec(o):
        comm, val = o
        if comm == "end":
            day += 1
            return
        elif comm = "set":
            day = val
            return
        elif comm = "shift":
            day += val
            return
        return
    
    renpy.register_statement("day", parse = m_day_parse, execute = m_day_exec)
    