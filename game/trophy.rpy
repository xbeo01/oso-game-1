image makeshift_trophy:
    "items/makeshift_trophy.png"
    xalign 0.5
    yalign 0.5
    zoom 5.0
    rotate 45

label trophy:
    p "oh, i know what to use this for!" # * 280
    show spraypaint
    show scraptrophy
    # TODO: find og coords first before implementing this
    # * 279
    # ! xalign 0.5
    # ! $ flash = Fade(.25, 0, .75, color="#fff")
    # ! xalign 0.5
    hide spraypaint
    hide scraptrophy
    show makeshift_trophy
    "You used the {b}glittery gold spray paint{/b} on the {b}scrap trophy{/b}, making it into a {b}makeshift trophy{/b}!"
    $ item.spraypaint = False
    $ item.scrap_trophy = False
    $ item.makeshift_trophy = True
    hide makeshift_trophy
    return