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
            text label


    screen invevrything_four_modsettings tag smallscreen2:
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
                    textbutton _("Enable all") action [Play("audio", "se/sounds/open.ogg"), MTSSetPersistent("invevrything_four_chapter2_limit",True), MTSSetPersistent("invevrything_four_chapter3_limit",True), MTSSetPersistent("invevrything_four_chapter4_limit",True), MTSSetPersistent("invevrything_four_police_archive_limit",True)] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
                    textbutton _("Disable all") action [Play("audio", "se/sounds/open.ogg"), MTSSetPersistent("invevrything_four_chapter2_limit",False), MTSSetPersistent("invevrything_four_chapter3_limit",False), MTSSetPersistent("invevrything_four_chapter4_limit",False), MTSSetPersistent("invevrything_four_police_archive_limit",False)] hovered Play("audio", "se/sounds/select.ogg") style "menubutton"
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


label invevrything_four_c3arcques_complete:
    stop music fadeout 2.0
    $ renpy.pause (0.5)
    show black with dissolvemed
    $ renpy.pause (0.5)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    jump c3sections