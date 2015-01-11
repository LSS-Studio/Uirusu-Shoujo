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
    
init:
    $cg_switcher("prologue_vitruvian", "poneh")
    $cg_switcher("prologue_coffee", "poneh")
    $ cg_switcher("prologue_nets", "dread")
    $ cg_switcher("prologue_emma_sad", "dread")
    image prologue_hazmat = Placeholder("bg")
    image prologue_flashbulb = Solid((255, 255, 255, 255))
    
label prologue_0:
    #MUSIC: Test Tubes
    scene black:
        "prologue_vitruvian" with Dissolve(3.0)
    "I am [name], one of the most notable young virologists of the modern era. I led a ground-breaking research team that won a Nobel prize for its work with Polio. Though I was not provided an individual share of the Prize, this earned me a comfortable position at an acclaimed university in East Baltimore, doing what I love best."
    scene prologue_coffee with fade
    "In my off-hours, I met Emma Duncan, a student earning her Masters' degree in sociology. We hit it off immediately. University regulations forbid cohabitation, so we took a small apartment off-campus together, bought matching Vespas, got matching furniture, and did all the other things couples are supposed to do."
    scene prologue_work with fade
    "Long hours in the lab kept us apart, but Emma was wrapped up in completing her own studies as well. While this was hardly an ideal start to a relationship, it seemed the best either of us could do at the moment."
    scene prologue_map with fade
    "However, when Ebola broke containment in West Africa, the Cooperative Health Action Network needed help, fast – and my name was near the top of the list. Two highly official-looking men in sharp black suits were dispatched to meet with me."
    scene prologue_apartment
    show mib2 at Position(xalign=.25)
    show mib1 at Position(xalign=.75)
    with fade
    "Two men in black greet me at my doorway."
    mib1 "Doctor [name], I presume?"
    prot "You presume correctly. And to what do I owe..."
    "I cough and wave at the smoke drifting in my direction, which earns the henchman a sharp snap of the lead agent’s fingers. He promptly crushes out his cigarette on the tile immediately outside the door."
    prot "To what do I owe the pleasure of your company?"
    mib1 "I assure you, the pleasure is all mine. I have come to ask but one question."
    mib1 "What is it you seek most in life? Fame and fortune, or the chance to do great things, while possibly remaining an unsung hero for all eternity?"
    "I remember the Nobel ceremony, where my name came up exactly once. I wasn’t even allowed to hold one of the medals, and my nominal superiors, who did none of the work, did all of the talking."
    menu:
        "What is it I seek most in life?"
        "Fame and fortune":
            $choice_desire = 'fame and fortune'
        "To do great things":
            $choice_desire = 'to do great things'
    scene black with dissolve
    "I give them their answer, and they leave."
    scene prologue_apartment
    show mib2 at Position(xalign=.25)
    show mib1 at Position(xalign=.75)
    with dissolve
    "The next day, I open my door to find them waiting for me inside my apartment. They must have broken in somehow."
    mib1 "We're here to make you an offer."
    prot "Here's your offer. You have ten seconds to get the fuck out of my apartment before I call..."
    mib2 "Who, him?"
    plh "Background pans to show tied up security guard."
    mib2 "The only difference between you and him is that people would notice if you went missing.\nThat's why we've taken the liberty of arranging an indefinite sabbatical for you."
    mib1 "You said you wanted [choice_desire]. We’re here to make that happen. You need us, and CHAN needs you. Your country needs you. The world needs you."
    scene black with dissolve
    "As soon as assured them I was willing to talk, the agents released the hapless security guard they strong-armed into giving them access to my apartment. Over the course of about an hour, they lay out the plan: I was to travel to West Africa, Ground Zero in the fight against Ebola, to study it directly as it appears."
    scene prologue_apartment
    show mib2 at Position(xalign=.25)
    show mib1 at Position(xalign=.75)
    with dissolve
    prot "This sounds like a cause I am willing to fight for, but I have to run this by Emma."
    "The agents exchange knowing glances."
    mib2 "Of course. She should be here any minute now... just like you texted her."
    prot "Except I..."
    mib1 "You, him, what difference does it make?"
    show emma normal
    "On cue, the door opens behind me. Emma drops her bags and runs to embrace me."
    emma "[name]! Don’t you ever scare me like that again! You made it sound like something bad had happened!"
    prot "I suppose it has, in a way. I've been drafted by our country to go abroad and fight this dreadful Ebola. I don't know how long I will be gone - months, possibly a year or more."
    emma crying "Will I at least be able to come see you?"
    mib1 "That can certainly be arranged, although all trips into a hot zone must be cleared in advance."
    mib2 "So, it’s settled? You’ll work with CHAN?"
    prot "Did I really ever have a choice?"
    scene prologue_airport with fade
    "Upon reaching the field office, the plan mutated faster than the flu, and my job description was revised. I am not to seek a cure for Ebola; others are working on that. Instead, I am to induce it to mutate – the justification being that nature is going to do it anyhow, and it’s best that CHAN be a step ahead."
    "I was only surprised for a moment. I always knew the job was not going to be what it appeared on the surface, and really, this could have been worse – much worse. At least this is well within my capacity."
    scene prologue_phone with fade
    emma "Are you sure? Have you asked? They can’t give you any sort of estimate when you might come home?"
    prot "Darling, I've been here less than a month, and the situation hasn't changed in any meaningful way. We're still stopping isolated outbreaks, one at a time. You know why I'm here."
    "I decide this is a good a time as any to break my change of job description - but only to a degree."
    prot "Things are moving so fast that we're not even hoping for a cure any more, not from this end. We're just trying to stay one step ahead of the virus, so that we can put out hotspots wherever they may arise. Once we can get those under control, we'll work on curing the odd case that still works its way into the light."
    emma "Maybe I can come out and see you then. It will be Spring Break soon, and..."
    "Shit. I completely forgot about University schedules."
    prot "If my superiors will approve it, I'm sure that would be just fine. Don't expect a luxury hotel when you get here, though."
    scene prologue_nets with fade
    "To my surprise, my bosses found room for her on a supply flight, and she was in my arms before I knew it."
    "To her credit, she remained silent about the rather hostile conditions - the minimal air conditioning, the mosquito netting everywhere, the Army rations, the dust that seeps into everything, and the constant sound of tarpaulins rustling in the wind."
    emma "Is this what you thought it would be? Is it what you really want?"
    prot "Yes, and no, respectively. It's actually a little bit better than I expected, being in the middle of fucking nowhere. As for what I want, that's a little bit irrelevant right now. Duty calls."
    scene prologue_emma_sad with fade
    emma "Is that what they tell you? When does duty stop and life begin? Where do I fit in? When will there be time for us?"
    "I struggle to find answers and reassurances, but I have none. Emma kept quiet for the next few days about the subject, but I could see it in her eyes every time I have to report in for work."
    "The pile of paperwork on my cheap folding table continues to grow. Then, just like that,{nw}"
    scene prologue_emma_sad:
        "black" with Dissolve(1)
    "The pile of paperwork on my cheap folding table continues to grow. Then, just like that,{fast} she was gone again. I half wonder if it really happened at all."
    scene prologue_hazmat with dissolve
    "I spent several weeks getting caught up after Emma's brief visit, but it was a simple matter for a man of my intellect to accelerate what nature does on its own. Destined for greatness, I am in God's seat now, manipulating forces that could destroy civilizations."
    "It comes as quite a thrill when, without warning, the virus alters its physical structure into something the world has never seen before:{nw}"
    scene prologue_hazmat:
        "prologue_flashbulb" with dissolve
        time 0.5
        "prologue_hazmat" with dissolve
    extend" an airborne strain!"
    "I reach for my data sheet, but through some terrible twist of fate, I reach left instead of right. My hand bangs into a cage holding one of the monkeys used to test an earlier version of my work. The monkey launches forward and bites down as hard as it can."
    scene prologue_bite with dissolve
    "Yanking my hand free, I check for puncture marks. There is quite a dent in the gloves, and my index finger burns like crazy from the pinching, but no breaches in the suit are visible. Holy shit, those little monsters can bite! I'd better go show myself to the medical examiner and get cleared. Otherwise I'll never leave."
    scene prologue_isolation with fade
    "I never do leave, either. I am immediately quarantined, and within just a couple days the symptoms begin to surface one by one: nausea, headache, fever, vomiting, diarrhea... and then the bleeding. Tears of blood, blood coughed up into the sink and expelled from the bowels into the toilet, blood spilling from the ears and trickling down the neck."
    "I know the game is over. Back home, in a hospital, I might have had a fighting chance... but not here. I beg and plead with the Men In Black."
    prot "Please... Emma... I need to see Emma."
    "There is a nod and a gesture of the hand from the Smoking Man, and just like that, Emma is there. When she sees me slumped on my cot, looking like death warmed over, she throws herself against the plastic sheeting of my isolation unit and pounds at it. The Men In Black allow it, and motion to a Hazmat-suited worker to retrieve my files."
    prot "Emma, dear, at least I've fulfilled my purpose. If I hadn’t created this, nature would have anyhow, and many more people would die from it than just me."
    "I cough up more bloody gobbets onto the dirt floor as Emma screams."
    emma "What?!"
    "The revelation is too much for her, everything turns upside down. She stands up and turns her back on me."
    prot "In order to defeat the enemy, we have to know it, inside and out. That includes what it is likely to do in the future. I developed a new strain of Ebola..."
    emma "WHAT?! You've—you caused this? WHY?"
    call prologue_1
    scene black with fade
    return

label prologue_1:
    prot "I knew you would never understand, which is why I couldn't tell you. We just weren't meant to be. I still love you, Emma, but even if I survive this, we cannot be together."
    "Throwing herself against the plastic once again, Emma persists."
    emma "You've destroyed yourself, for what? You think you've saved the world? Who are you, [name]? What happened to you? You left me for weeks, for months... for this? I should have known. The evidence was here all along!"
    "I wave a hand with the last of my strength. The Men In Black pull her away as she continues to rant at top volume."
    emma "CHAN ruins happiness again!"
    return
    
label prologue_2:
    prot "Emma, I’m so sorry. I didn’t want it to end like this. I’m sure we will meet again..."
    "I have to stop to catch my breath, followed by more coughing and more blood."
    "...in the next life."
    "Emma collapses at the base of the plastic between you, sobbing uncontrollably. I wave a hand with the last of my strength, and the Men In Black pull her away as I collapse onto my death bed."
    emma "CHAN ruins happiness again!"
    return

label prologue_3:
    prot "Where is your mind, Emma? You're a graduate student, I'm a researcher. You knew this when you signed on. Did you think I was..."
    "I have to stop to catch my breath, followed by more coughing and more blood."
    prot "...was magically going to become a nine-to-five drone and settle down to an idyllic suburban life? What black-and-white TV sitcom did you grow up in? Believe it or not, Emma, CHAN is not all about you."
    "Throwing herself against the plastic once again, Emma persists, her voice heavy with bitterness."
    emma "I see. I should have known better than to get mixed up with a man who is already married to his job."
    "I have no reply, and she turns her back once again, this time walking out of the outer isolation tent entirely and into the sunlight beyond. The Men In Black follow her as I collapse and start to blank out."
    return

label prologue_river:
    #the sound of rain
    $ name_joki = "Female Voice"
    $ name_pest = "Male Voice"
    joki "This is him, right? I just wanted to make sure I got the right guy."
    pest "Don't worry, he's the right guy. Ebby left him in pretty bad shape, but we can rebuild him. We have the technology. It'll take us a couple of hours, though, so you might not want to wait around."
    joki "All righty then, just making sure. If I screw up, Death will be pissed. Perkele."
    $ scene_switcher("prologue_river", "dread")
    return
