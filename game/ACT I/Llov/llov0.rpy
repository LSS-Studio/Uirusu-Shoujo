init:
    transform llov_shake:
        ease 0.25 xpos -0.02
        ease 0.5 xpos 0.02
        ease 0.25 xpos 0.0

label llov_morning1:
    $ name_llov = "Little Girl"
    scene black
    pause 1
    scene bg prot_room with vpunch
    # play the sound of a door bursting open.
    "Someone enters my room, slamming the door loudly."
    show llov happy:
        alignaround (.55, 1.6)
        zoom 1.0 xpos 1.0 xanchor 0.0 ypos 1.0 yanchor 0.90
        parallel:
            ease 1.0 xalign .5
            ease 0.5 xalign .55
        parallel:
            time 0.2
            ease 0.7 yanchor 0.88
            ease 0.2 yanchor 0.92
            ease 0.4 yanchor 0.9
    llov "Ebby~!"
    show llov inquisitive
    llov "Huh? Ebby, are you sleeping?"
    show llov normal
    show llov:
        ease 0.5 yanchor 0.6 xalign 0.45 zoom 1.5
    llov "Ebby? Wake up!"
    show layer master at llov_shake
    "She attempts to shake me awake"
    show llov devilish:
        ease 0.5 zoom 1.0 yanchor 0.9 xalign .55
    llov "Ebby, if you won't wake up..."
    show llov:
        ease 0.5 zoom 3.0 yanchor 0.3
    show layer master:
        xalign 0.5 yalign 0.5
        time 0.3
        ease 0.05 rotate 12
        ease 0.1 rotate -12
        ease 0.12 rotate 12
        ease 0.14 rotate -12
        ease 0.1 rotate 0
    "An impact slams into my side, knocking the breath out of my lungs, and forcing me wide awake. I can feel her legs wrapping around my waist."
    llov inquisitive "Eh? Ebby just now had a strange voice. Is Ebby all right?"
    "She attempts to remove the covers, but I've got a tight grip on them. She pulls harder, and harder, until suddenly the blankets slip from my hands."
    show llov shock:
        transform_anchor True
        ease 0.3 yanchor -0.2 zoom 2.55 rotate 45
        transform_anchor False
    pause 0.25
    with vpunch
    #cg?
    "The girl goes tumbling backwards, and hits her head on the foot of my bead."
    "I get a chance to get a good look at the girl. She's short, probably very young. She rubs the back of her head gingerly, before darting her eyes at me."
    show llov shock:
        zoom 1.5 rotate 0
        ease 0.3 yanchor 0.6
    llov "Ahh!! Ebola-chan turned into a mister!"
    "Come to think of it, She's been calling me Ebby all this time hasn't she?"
    prot "Idiot. Ebola-chan is in the next room over."
    show llov confused
    llov "Eh?"
    llov "Ahahaha, Llov got the wrong room again."
    prot "Llov?"
    $ name_llov = "Lloviu"
    llov happy "Ah, it's Llov's name. Lloviu Cuevavirus."
    llov normal "What is mister's name?"
    prot "Er, my name is [name]."
    llov inquisitive "[name]?"
    extend happy " What a funny name!"
    prot "Anyway, Does this happen a lot?"
    llov confused "What?"
    prot "Getting the wrong room. Throwing yourself on top of strangers."
    show llov flustered
    pause 0.3
    show llov confused
    pause 0.3
    llov "L-Llov brought snacks! Mister take some!"
    "She holds out a sponge cake in a plastic wrapper."
    prot "Eh, it's a bit crushed, but..."
    "I reach out to take it, but she quickly pulls it back."
    llov cry "Ehh!? Llov's snack is ruined!!"
    "Tears begin to roll up in her eyes as she stares at the confection, her body beginning to quiver slightly."
    prot "Woah, hey!"
    "I take the snack from her, ripping the plastic open and shoving the bits of sponge cake into my mouth. It's filled with cream."
    prot "It's really good."
    show llov romance
    "She stares at me intently for a moment."
    llov cry "Wah!! Mister is too kind!"
    "She breaks into tears again, throwing her arms around me. I gently stroke her shoulder in an attempt to comfort her."
    show llov shock:
        ease 0.5 zoom 1.1 yanchor 0.8
    llov "Ah!"
    "Suddenly she breaks away from the embrace, hopping back down onto the floor."
    llov "Llov has to go do something!"
    show llov:
        ease 0.5 xanchor 0.0 xpos 1.0
    "She quickly darts out of the room, gone as quickly as she came."
    return

