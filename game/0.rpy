python early:
    calendar = list() #calendar[day no.][character name]
    calendar.append(dict())
    day = 0
    
    ###############"nextday" statement##################################################
    
    def m_nextday_parse(lex):
        rest = lex.rest()
        if rest:
            renpy.error("Arguments given to intransitive statement: 'nextday " + rest + "'.")
    
    def m_nextday_exec(o):
        day += 1
        calendar.append(dict())
    
    def m_nextday_lint(o):
        pass
    
    renpy.register_statement("nextday", parse = m_nextday_parse, execute = m_nextday_exec, lint = m_nextday_lint)
    
    ################"change" statement##################################################
    
    def m_change_parse(lex):
        name = lex.word()
        point = lex.integer()
        day = lex.integer()
        return (name, point, day)
    
    def m_change_exec(o):
        name, point, day = o
        calendar[day][name] = point
    
    def m_change_lint(o):
        name, point, day = o
        if not (isinstance(name, basestring) or (isinstance(point, (int, long)) and (-100 <= point <= 100)) or (isinstance(day, (int, long)) and day >= 0)):
            renpy.error("Type mismatch: 'change " + name + " " + point + " " + day + "'.")
    
    renpy.register_statement("change", parse = m_change_parse, execute = m_change_exec, lint = m_change_lint)
    
    #####################################################################################
    
    def points(day, name):
        p = 0.0
        dd = day + 1
        for d in xrange(dd):
            i = 1 - ((day - d) / 365)
            p += calendar[d][name] * ((abs(i) + i) / 2)
        return p / (dd)
    