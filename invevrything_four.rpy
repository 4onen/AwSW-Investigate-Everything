init:
    # Settings menu
    screen invevrything_four_checkbox(label, id):
        hbox:
            spacing 10
            imagebutton:
                xcenter 0.5
                ycenter 0.5
                idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                action [MTSTogglePersistentBool(id),
                        Play("audio", "se/sounds/yes.wav")]
                hovered Play("audio", "se/sounds/select.ogg")
                focus_mask None
            text "[label]"

    python:
        @renpy.pure
        class invevrything_four_SetManyPersistent(Action, FieldEquality):
            identity_fields = ['value']
            equality_fields = ['fields']

            def __init__(self, fields, value):
                self.fields = fields
                self.value = value

            def __call__(self):
                for field in self.fields:
                    setattr(persistent, field, self.value)
                renpy.save_persistent()
                renpy.restart_interaction()

            def get_selected(self):
                for field in self.fields:
                    if not (getattr(persistent, field) == self.value):
                        return False
                return True

    define invevrything_four_modsettings_enable_all = [Play("audio", "se/sounds/open.ogg"), invevrything_four_SetManyPersistent(("invevrything_four_chapter2_limit","invevrything_four_chapter3_limit","invevrything_four_chapter4_limit","invevrything_four_police_archive_limit"),True)]
    define invevrything_four_modsettings_disable_all = [Play("audio", "se/sounds/open.ogg"), invevrything_four_SetManyPersistent(("invevrything_four_chapter2_limit","invevrything_four_chapter3_limit","invevrything_four_chapter4_limit","invevrything_four_police_archive_limit"),False)]

    screen invevrything_four_modsettings():
        tag smallscreen2
        modal True
        window id "invevrything_four_modsettings" at popup2:
            style "smallwindow"
            vbox:
                align(0.5,0.5)
                spacing 20
                text "Re-enable investigation limits:" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 40
                    textbutton _("Enable all") action invevrything_four_modsettings_enable_all hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
                    textbutton _("Disable all") action invevrything_four_modsettings_disable_all hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
                grid 3 2:
                    align (0.5, 0.5)
                    transpose True
                    spacing 10
                    use invevrything_four_checkbox("Chapter 2 limit", "invevrything_four_chapter2_limit")
                    null
                    use invevrything_four_checkbox("Chapter 3 limit", "invevrything_four_chapter3_limit")
                    use invevrything_four_checkbox("Police Archive limit", "invevrything_four_police_archive_limit")
                    use invevrything_four_checkbox("Chapter 4 limit", "invevrything_four_chapter4_limit")
                    null
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button




label invevrything_four_c1skip:
    $ renpy.pause (0.0)
    stop music fadeout 1.0
    Br brow b "..."

    play sound "fx/sheet.wav"

    scene black with dissolve
    $ renpy.pause (0.5)
    scene deadbody at Pan ((0, 1080), (0, 350), 10) with dissolveslow
    $ renpy.pause (10.0)

    play sound "fx/unroll.ogg"
    show invest with wiperightquick

    play sound "fx/unroll.ogg"
    show start with wipeleftquick

    $ renpy.pause (0.5)
    play music "mx/investigation.ogg"
    $ renpy.pause (0.5)

    hide invest
    hide start
    with dissolvemed

    $ renpy.pause (0.5)

    m "Two wings, two legs, just like the waitress in the café. About as big as a human, length-wise, if not slightly taller. The wingspan would certainly look impressive at that size."

    show deadbody at Position(xpos = 0, xanchor=0, ypos=-1000, yanchor=0) with ease

    show deadbodywounds at Pan ((0, 1000), (0, 1000), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    show deadbodywounds at Pan ((0, 1000), (0, 1000), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick

    show deadbody at Position(xpos = 0, xanchor=0, ypos=-350, yanchor=0) with ease

    $ renpy.pause (1.0)

    show deadbodywounds at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    show deadbodywounds at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodywounds with dissolvequick
    $ answers = 0
    c "Those wounds were inflicted with a sharp instrument, not claws."
    $ answers = 1
    c "That means someone with hands wielded something like a knife against the victim."
    $ answers = 2
    c "This is a populated area. If it was Reza, he wouldn't use the gun instead because he doesn't want to make noise and attract attention."
    $ answers = 3
    
    show deadbodyblood at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyblood with dissolvequick
    show deadbodyblood at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyblood with dissolvequick

    c "The blood pool came from the neck. Undisturbed. The victim likely died from lack of air before their blood flowed out from gravity."
    $ answers = 4
    c "They died here, too, or we'd see drag marks and there wouldn't be nearly so much blood pooled."
    $ answers = 5
    
    show deadbodyteeth at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyteeth with dissolvequick
    show deadbodyteeth at Pan ((0, 350), (0, 350), 0) with dissolvequick
    $ renpy.pause (0.5)
    hide deadbodyteeth with dissolvequick

    c "If the victim died of suffocation, then, before the major blood loss, they wouldn't have that much in their mouth."
    c "That could be the attacker's blood."
    $ answers = 6

    Br "I expect forensics already took a sample of it, so it might actually help us determine who the perpetrator is."
    Br "Wow. I think that's about everything."

    jump invevrything_four_c1skip_end



label invevrything_four_c3arcques_complete:
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    show black with dissolvemed
    $ renpy.pause (0.5)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    jump c3sections