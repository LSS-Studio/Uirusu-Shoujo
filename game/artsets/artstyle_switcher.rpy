init -13:
    if persistent.artstyle is None:
        $ persistent.artstyle = 'default'
    
init -13 python:
    # Used for declaring images that switch artstyles.
    # Takes a list of image names.
    def artstyle_switcher(artist='', prefix='', list=[], bases=[]):
        artstyle_switcher2(artist,prefix,list)
        for base in bases:
            artstyle_switcher2(artist,prefix,list,base)
        return
    def artstyle_switcher2(artist='', prefix='', list=[], base=''):
        if prefix: prefix = prefix+" "
        if base: base = " "+base
        for item in list:
            for name in[
            prefix+item+base,
            prefix+item+base+" full",
            prefix+item+base+" large",
            prefix+item+base+" large full"
            ]:
                renpy.image(name, DynamicDisplayable(artstyle_dynamic,name=name, artist=artist))
        return
    def artstyle_dynamic(st, at, name='', artist=''):
        if renpy.image_exists(persistent.artstyle+" "+name):
            return persistent.artstyle+" "+name, None
        elif renpy.image_exists(artist+" "+name):
            return artist+" "+name, None
        else:
            return Placeholder('girl'), None
            
    # Used for compositing and declaring many images with little effort.
    # For each item, defines 4 images. Cropped small, cropped large, full small, and full large.
    def autoComposite(prefix='',basename=None, base='', bases={}, dict={}, wimg=800, himg=1600, xcomp=0, ycomp=0, wcomp=200, hcomp=200, lcrop=1000, scrop=900, lscale=1.0, sscale=0.66):
        suffix=''
        if prefix:
            prefix = prefix+" "
        #main base
        autoComposite2(**locals())
        #additional bases
        for key in bases:
            suffix = key
            base = bases[key]
            autoComposite2(**locals())
        return
    def autoComposite2(prefix ,basename, base, suffix, dict, wimg, himg, xcomp, ycomp, wcomp, hcomp, lcrop, scrop, lscale, sscale,**extra):
        if basename or basename=='':
            if basename and suffix:
                basename = basename+" "
            # declare baseimage
            autoComposite3(basename+suffix, base, **locals())
        for key in dict:
            # declare composite images
            if dict[key] and base:
                src=im.Composite((wimg, himg),(0,0),base,(xcomp,ycomp),dict[key])
            elif base:
                src=base
            elif dict[key]:
                src=dict[key]
            if suffix: suffix = " "+suffix
            autoComposite3(key+suffix, **locals())
    def autoComposite3(name, src, prefix, wimg, lcrop, scrop, lscale, sscale,**extra):
        #cropped
        renpy.image(prefix+name, im.FactorScale(im.Crop(src,(0,0,wimg,scrop)),sscale))
        #full image
        renpy.image(prefix+name+" full", im.FactorScale(src,sscale))
        #large cropped
        renpy.image(prefix+name+" large", im.FactorScale(im.Crop(src,(0,0,wimg,lcrop)),lscale))
        #large full
        renpy.image(prefix+name+" large full", im.FactorScale(src,lscale))
        return