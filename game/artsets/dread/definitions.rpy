# lcrop is usually at ~55% height. 100% scale
# scrop is usually at ~70% height. 66% scale
# For distant sprites, 90% anchor and 70% (of small) seems appropriate.
init -12 python:
#Ebby dread normal
    autoComposite('dread ebby',
    basename='', base="artsets/dread/EBOLA/EbbySkullBlood.png",
    bases={
    'noskull':"artsets/dread/EBOLA/EbbyBlood.png",
    },
    dict={
    'normal':"",
    'wink':"artsets/dread/EBOLA/EbbyWink.png",
    'concerned':"artsets/dread/EBOLA/EbbyConcerned.png",
    'excited':"artsets/dread/EBOLA/EbbyExcited.png",
    'sad':"artsets/dread/EBOLA/EbbySad.png",
    'rape':"artsets/dread/EBOLA/EbbyRape.png",
    'joy':"artsets/dread/EBOLA/EbbyJoy.png",
    }, wimg=808, himg=1929, 
    xcomp=297, ycomp=188, wcomp=259, hcomp=268,
    lcrop=1060, scrop=1350,
    sscale=0.62)
#Ebby dread toast
    autoComposite('dread ebby',
    base="artsets/EBOLA/EbbyBlood.png",
    bases={
    'skull':"artsets/EBOLA/EbbySkullBlood.png",
    },
    dict={
    'toastdead':"artsets/dread/EBOLA/EbbyToastDead.png",
    'toastsad':"artsets/dread/EBOLA/EbbyToastSad.png",
    'toastjoy':"artsets/dread/EBOLA/EbbyToastJoy.png",
    }, wimg=808, himg=1929, 
    xcomp=297, ycomp=188, wcomp=259, hcomp=334,
    lcrop=1060, scrop=1350,
    sscale=0.62)
#Sars dread
    autoComposite('dread sars',
    basename='', base="artsets/dread/SARS/SarsNormal.png",
    bases={
    'point':"artsets/dread/SARS/SarsPoint.png"
    },
    dict={
    'normal':"",
    'concerned':"artsets/dread/SARS/SarsConcerned.png",
    'grin':"artsets/dread/SARS/SarsGrin.png",
    'sad':"artsets/dread/SARS/SarsSad.png",
    'stars':"artsets/dread/SARS/SarsStars.png",
    'angry':"artsets/dread/SARS/SarsAngry.png",
    'blush':"artsets/dread/SARS/SarsRed.png",
    }, wimg=751, himg=1790, 
    xcomp=241, ycomp=129, wcomp=307, hcomp=284,
    lcrop=984, scrop=1200,
    sscale=0.64)
#Llov dread
    autoComposite('dread llov',
    basename='', base="artsets/dread/LLOV/normal.png",
    dict={
    'normal':"",
    'shifty':"artsets/dread/LLOV/shifty.png",
    }, wimg=755, himg=1577, 
    xcomp=214, ycomp=132, wcomp=253, hcomp=275,
    lcrop=980, scrop=1070)
    
    autoComposite('dread llov',
    base="artsets/dread/LLOV/normal2.png",
    dict={
    'happy':"",
    }, wimg=755, himg=1577, 
    xcomp=214, ycomp=132, wcomp=253, hcomp=275,
    lcrop=980, scrop=1070)
    
    autoComposite('dread llov',
    basename='shock', base="artsets/dread/LLOV/shock.png",
    dict={
    'cry':"artsets/dread/LLOV/cry.png",
    }, wimg=656, himg=1551, 
    xcomp=185, ycomp=95, wcomp=265, hcomp=308,
    lcrop=980, scrop=1070)
    
    autoComposite('dread llov',
    basename='inquisitive', base="artsets/dread/LLOV/inquisitive.png",
    dict={
    'romance':"artsets/dread/LLOV/romance.png",
    }, wimg=656, himg=1551, 
    xcomp=185, ycomp=95, wcomp=265, hcomp=308,
    lcrop=980, scrop=1070)
    
    autoComposite('dread llov',
    basename='kiss', base="artsets/dread/LLOV/kiss.png",
    wimg=656, himg=1551,
    lcrop=980, scrop=1070)
#HIV dread
    autoComposite('dread hiv',
    basename='', base="artsets/dread/HIV/normal.png",
    dict={
    'normal':"",
    }, wimg=755, himg=1850, 
    lcrop=1000, scrop=1290)
#AIDS dread
    autoComposite('dread aids',
    basename='', base="artsets/dread/AIDS/normal.png",
    dict={
    'normal':"",
    }, wimg=795, himg=1828, 
    lcrop=1000, scrop=1280)
#MALARIA dread
    autoComposite('dread mal',
    basename='', base="artsets/dread/MOLLY/normal.png",
    dict={
    'normal':"",
    }, wimg=799, himg=2058, 
    lcrop=1172, scrop=1436)
#RABIES dread
    autoComposite('dread rab',
    basename='', base="artsets/dread/RAB/normal.png",
    dict={
    'normal':"",
    }, wimg=815, himg=1846, 
    lcrop=1000, scrop=1280,
    sscale=0.7)
#JOKI dread
    autoComposite('dread joki',
    basename='', base="artsets/dread/JOKI/normal.png",
    dict={
    'normal':"",
    }, wimg=716, himg=1892, 
    lcrop=1000, scrop=1280)