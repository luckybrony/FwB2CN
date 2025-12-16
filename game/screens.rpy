screen vnui():
    zorder 100
    if replay == 0:
        if uiicons == "On":
            image "map icons[weather]"
            text "$ [money]":
                pos (270, 7)
            text "Day [day]":
                pos (75, 7)
        imagebutton:
            idle "vnui.png"
            hover "vnuih.png"
            xpos 1800
            action (Play("sound2", "audio/phonestart.ogg"), Hide("vnui"), SetField(persistent,"quick_menu", False), Call("phone"))
    else:
        imagebutton:
            idle "vnuireplay.png"
            hover "vnuireplayh.png"
            xpos 1730 ypos 10
            action (Play("sound2", "audio/phonestart.ogg"), SetVariable("replay", 0), Jump("replay"))

    if unread >= 1:
        image "notification":
            xpos 1800
        if unread < 10:
            text "[unread]":
                xpos 1883
        else:
            text "[unread]":
                xpos 1875

label replay:
    return
label phone: 
    call screen phone_screen with dissolve
    return

screen phone_screen():
    zorder 94
    if worldmap >= 1:
        image "map[weather][lastlocation]"
    if worldmap == 2:
        image "bg crystalkingdom"
    image "phonebg"
    image "phonebg[phonebg]"
    imagemap:
        ground "phonemenu.png"
        hover "phonemenuh.png"
        if phoneenabled == 1:
            hotspot (613, 146, 191, 181) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("msgs"))
            hotspot (857, 150, 187, 176) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("todo"))
            hotspot (1095, 151, 185, 202) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("gallery"))
            hotspot (620, 385, 189, 238) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("socials"))
            hotspot (861, 392, 186, 229) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("shop1"))
            hotspot (1089, 395, 188, 229) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("shop2"))
            hotspot (624, 627, 180, 204) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("music"))
            hotspot (859, 625, 186, 209) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("cheats"))
            hotspot (1092, 625, 193, 216) action (Play("sound2", "audio/click1.ogg"), Function(renpy.transition, dissolve), Jump("settings"))
            ## Close
            hotspot (834, 988, 240, 84) action (Play("sound2", "audio/click1.ogg"), Show("vnui"), SetField(persistent,"quick_menu", True), Function(renpy.transition, dissolve), Return())
    #notifications
    if unread > 0:
        image "notification":
            pos (700, 145)
    if feedupdate > 0:
        image "notification":
            pos (700, 380)
    text "[completionpercent:.0f]%":
            pos (940, 185)
    if phoneenabled == 0:
        image "black":
            alpha 0.75

label msgs:
    $ phoneenabled = 0
    #if worldmap == 0:
    #    show screen phone_screen
    menu msgmenu:
        "Unread: [unread]\nRead: [read]"
        "[hon] ([unreadhon])" if farmroute1 == 1:
            menu msgmenuhon:
                "Messages from [hon]"
                "Thinking about you" if honmsg1 == 1:
                    $ honmsg1 = 2
                    $ unread -= 1
                    $ unreadhon -= 1
                    $ read += 1
                    label honmsg1:
                        hon "Howdy stud! Got a little something for you... (Open Attachment)"
                        layeredimage honmsg1:
                            always:
                                "honmsg 1 [honb]"
                        show honmsg1 onlayer screens zorder 95
                        $ textbox = 2
                        with d
                        ""
                        hon "I admit i {i}may{/i} be sipping on some of that milk to make masturbating feel even better haha!"
                        hon "Wish you were here~"
                        "{i}She's trying more of that milk? Judging by how wet she is, it's clearly working.{/i}"
                        hide honmsg1 onlayer screens
                        $ textbox = 1
                        with d
                    jump msgmenuhon  
                "{i}Thinking about you (Read){/i}" if honmsg1 == 2:
                    jump honmsg1  
                "Back":
                    jump msgmenu
        "[blo] ([unreadblo])" if farmroute1 == 1:
            menu msgmenublo:
                "Messages from [blo]"
                "i did it!" if blomsg1 == 1:
                    $ blomsg1 = 2
                    $ unread -= 1
                    $ unreadblo -= 1
                    $ read += 1
                    label blomsg1:
                        blo "hi i sent your letter to anna. and i have something for you too. (Open Attachment)"
                        layeredimage blomsg1:
                            always:
                                "blossommsg1 [blob]"
                            group text:
                                attribute text:
                                    "blossommsg1 text"
                        show blomsg1 text onlayer screens zorder 95
                        $ textbox = 2
                        with d
                        ""
                        show blomsg1 -text onlayer screens zorder 95 with d
                        "{i}Sheesh! The last person I was expecting to get such a raunchy picture from was [blo]!{/i}"
                        "{i}I guess she's someone that's more confident over text than in person. This has me excited to see what she has in store the next time we see each other.{/i}"
                        "{i}Let me just save this picture for later...{/i}"
                        hide blomsg1 onlayer screens
                        $ textbox = 1
                        with d
                    jump msgmenublo  
                "{i}i did it! (Read){/i}" if blomsg1 == 2:
                    jump blomsg1  
                "Back":
                    jump msgmenu
        "[mel] ([unreadmel])" if brothelroute1 == 1:
            menu msgmenumel:
                "Messages from [mel]"
                "You did this~!" if melmsg2 == 1:
                    $ melmsg2 = 2
                    $ unread -= 1
                    $ unreadmel -= 1
                    $ read += 1
                    label melmsg2:
                        show melmsg2 with d
                        mel "Enjoying a beautiful spa day vacation! It was [rub]'s idea, but she got it from you."
                        mel "Thank you... (ur still gross tho) Maybe next time I won't trick you, eh? Hehe."
                        $ textbox = 2
                        "Look at her, pushing out her breasts and butt like that. She knows exactly what she's doing, and always has."
                        "Oh wait, there're some more messages coming in now."
                        $ textbox = 1
                        mel "You getting hard looking at my tits, pervy boy?"
                        mel "Gonna jerk it to this pic? Imagine what it's like in my pussy? Shame you can only imagine XD"
                        mel "What a loser! Maybe I should just find some hot stud here instead. Who knows how long my virginity might last~?"
                        "I quickly type up a reply..."
                        mc "You're going to find a 'hot stud' at the... beauty spa?"
                        mel "... Good point. I'll see you soon >;)"
                        $ textbox = 2
                        "(Click to finish appreciating)"
                        $ textbox = 1
                        hide melmsg2 with d
                    jump msgmenumel
                "{i}You did this~! (Read)" if melmsg2 == 2:
                    jump melmsg2
                "Thanks" if melmsg1 == 1:
                    $ melmsg1 = 2
                    $ unread -= 1
                    $ unreadmel -= 1
                    $ read += 1
                    label melmsg1:
                        mel "It was nice talking to someone that feels sane for once. Let's see if I can't win you back from my sister, hm?"
                        if melnerd == 1:
                            mel "Also, you're the nerd."
                    jump msgmenumel
                "{i}Thanks (Read){/i}" if melmsg1 == 2:
                    jump melmsg1  
                "Back":
                    jump msgmenu
        "[rub] ([unreadrub])" if brothelroute1 == 1:
            menu msgmenurub:
                "Messages from [rub]"
                "Took your advice" if rubmsg1 == 1:
                    $ rubmsg1 = 2
                    $ unread -= 1
                    $ unreadrub -= 1
                    $ read += 1
                    label rubmsg1:
                        layeredimage rubmsg1:
                            always:
                                "rubmsg1 [rubb]"
                        show rubmsg1 with d
                        rub "A day away at a spa with [mel]. I {i}really{/i} needed this. I can't remember the last time I had a day to myself."
                        rub "[mel] keeps asking about running the brothel with me, but I refuse to talk business until our break is over! xxx"
                        $ textbox = 2
                        "Good lord, this lady doesn't send nudes, she sends whole-ass poster-worthy pinups."
                        "(Click to finish appreciating)"
                        $ textbox = 1
                        hide rubmsg1 with d
                    jump msgmenurub
                "{i}You did this~! (Read)" if rubmsg1 == 2:
                    jump rubmsg1
                "Back":
                    jump msgmenu
        "[rik] ([unreadrik])" if barroute2 == 1:
            menu msgmenurik:
                "Messages from [rik]"
                "Bar 2nite?" if rikmsg1 == 1:
                    $ rikmsg1 = 2
                    $ unread -= 1
                    $ unreadrik -= 1
                    $ read += 1
                    label rikmsg1:
                        show rik3a with d
                        rik "Hey, if ur going 2 the bar, why don't you come 2 my place first? ;)"
                        $ textbox = 2
                        "Nice... I should follow up on this."
                        $ textbox = 1
                        "(You can now visit the Bar to begin Bar 4)"
                        hide rik3a with d
                    jump msgmenurik
                "{i}Bar 2nite? (Read)" if rikmsg1 == 2:
                    jump rikmsg1
                "Back":
                    jump msgmenu
        "[sky] ([unreadsky])" if barroute1 == 1:
            menu msgmenusky:
                "Messages from [sky]"
                "The Big Night!" if skymsg1 == 1:
                    $ skymsg1 = 2
                    $ unread -= 1
                    $ unreadsky -= 1
                    $ read += 1
                    label skymsg1:
                        show skymsg1
                        $ textbox = 2
                        with d
                        sky "Me and the girls are going to finally get back together. You should be there!"
                        "Looks like this picture was taken recently. Whoever took it knows [sky]'s good angle!"
                        $ textbox = 1
                        "(You can now visit the Brothel to begin Brothel 4)"
                        hide skymsg1 with d
                    jump msgmenusky
                "{i}The Big Night! (Read)" if skymsg1 == 2:
                    jump skymsg1
                "Back":
                    jump msgmenu
        "[but] ([unreadbut])" if forestroute1 == 1:
            menu msgmenubut:
                "Messages from [but]"
                "i need you bad" if butmsg1 == 1:
                    $ butmsg1 = 2
                    $ unread -= 1
                    $ unreadbut -= 1
                    $ read += 1
                    label butmsg1:
                        show butmsg1 with d
                        but "I want you to cum inside me, over, and over, and over... Don't you dare keep me waiting."
                        $ textbox = 2
                        "She's absolutely soaked!"
                        "Does this mean the potion worked? I guess there's only one way to find out."
                        $ textbox = 1
                        hide butmsg1 with d
                    jump msgmenubut
                "{i}i need you bad (Read)" if butmsg1 == 2:
                    jump butmsg1
                "Back":
                    jump msgmenu
        "[lil] ([unreadlil])" if magicroute1 == 1:
            menu msgmenulil:
                "Messages from [lil]"
                "xxx" if lilmsg1 == 1:
                    $ lilmsg1 = 2
                    $ unread -= 1
                    $ unreadlil -= 1
                    $ read += 1
                    label lilmsg1:
                        lil2 "[lil] 1.0 can't keep me around forever, since it's a big strain on her magic. But before I'm gone, I wanted to share one last picture to commemorate our life together~"
                        layeredimage lilmsg1:
                            always:
                                "lilytext1 [lilb]"
                        show lilmsg1:
                            xalign 0.5 ypos 0
                            linear 1 ypos 0
                            linear 4 ypos -1000
                        with dissolve
                        $ textbox = 2
                        "Woah! What a sexy pic!"
                        "Wasn't the language she was using a little dramatic, though?"
                        menu lilmsg1m:
                            "Zoom Out":
                                show lilmsg1:
                                    xalign 0.5 ypos -500 zpos -1000
                                "(Click to continue)"
                                jump lilmsg1m
                            "Scroll Up":
                                show lilmsg1:
                                    xalign 0.5 ypos 0 zpos 0
                                "(Click to continue)"
                                jump lilmsg1m
                            "Scroll Down":
                                show lilmsg1:
                                    xalign 0.5 ypos -1000 zpos 0 
                                "(Click to continue)"
                                jump lilmsg1m
                            "(Finish Appreciating)":
                                hide lilmsg1 with d
                                $ textbox = 1
                                jump msgmenulil
                "Onsen Invite" if lilmsg2 == 1:
                    $ lilmsg2 = 2
                    $ unread -= 1
                    $ unreadlil -= 1
                    $ read += 1
                    label lilmsg2:
                        lil "The onsen at the castle is currently undergoing reconstruction. When it's done, I'd like to formally invite everyone to break it in!"
                        lil "Come to the castle during the evening if you'd like to check it out."
                    jump msgmenulil
                "{i}xxx (Read){/i}" if lilmsg1 == 2:
                    jump lilmsg1  
                "{i}Onsen Invite (Read){/i}" if lilmsg2 == 2:
                    jump lilmsg2  
                "Back":
                    jump msgmenu
        "[pen] ([unreadpen])":
            menu msgmenupen:
                "Messages from [pen]"
                "Break out the wine!" if penmsg2 == 1:
                    $ penmsg2 = 2
                    $ unread -= 1
                    $ unreadpen -= 1
                    $ read += 1
                    label penmsg2:
                        pen "Hey, man! I was wondering if [mox] and yourself would be interested in coming on over and sharing a bottle of wine with me?"
                        pen "And if that's not enough to sell you, how about this?"
                        layeredimage penmsg2:
                            always:
                                "penmsg2 [penb]"
                        show penmsg2
                        $ textbox = 2
                        with d
                        "Oohhh, niiice! Another picture for the collection. {i}Saves{/i}"
                        "Hmm... Are pictures like this the equivalent of dick pics from my first universe? It's not like I can complain, I love mare pussy."
                        "I'll definitely take [pen] up on her offer if it means I can slide in there. I should visit when I get the chance."
                        "(Click to finish admiring)"
                        $ textbox = 1
                        hide penmsg2 with d
                        jump msgmenupen
                "{i}Break out the wine! (Read){/i}" if penmsg2 == 2:
                    jump penmsg2
                "Threesome?" if penmsg1 == 1:
                    $ penmsg1 = 2
                    $ unread -= 1
                    $ unreadpen -= 1
                    $ read += 1
                    label penmsg1:
                        pen "Good evening! I was wondering if you wanted to give that threesome with [mox] and I another try? I'm free tonight, let me know if you're interested."
                        menu:
                            "Currently Busy" if worldmap == 0:
                                "I'm too busy right now. I should wait until I have some free time. (You can only accept [pen]'s proposition from the world map.)"
                            "Accept" if worldmap >= 1:
                                $ moxpen2 = 1
                                "I send [pen] a reply saying yes, and within the hour, [mox] and I are in the treehouse with her."
                                show bg peneloperoom
                                show pen laughing:
                                    xalign 0.25
                                show mox happy:
                                    xalign 0.75
                                with d
                                pen "I'm so glad you could join us! Allow me to show you to my room."
                                $ replay = 1
                                call moxpen2 from _call_moxpen2_1
                                scene black with d
                                "Some cleaning up later, and we're back home."
                                jump worldmap
                            "Decline" if worldmap >= 1:
                                jump msgmenupen
                "{i}Threesome? (Read){/i}" if penmsg1 == 2:
                    jump penmsg1
                "Back":
                    jump msgmenu
        "[mox] ([unreadmox])":
            menu msgmenumox:
                "Messages from [mox]"
                "hope u slept well" if moxmsg2 == 1:
                    $ moxmsg2 = 2
                    $ unread -= 1
                    $ unreadmox -= 1
                    $ read += 1
                    label moxmsg2:
                        mox "Sorry to leave you alone in bed! I trust you not to trash the apartment while im gone ;) \nIll be back later tonight good luck on your big quest! xx"
                    jump msgmenumox
                "{i}hope u slept well (Read){/i}" if moxmsg2 == 2:
                    jump moxmsg2  
                "Hiya!" if moxmsg1 == 1:
                    $ moxmsg1 = 2
                    $ unread -= 1
                    $ unreadmox -= 1
                    $ read += 1
                    label moxmsg1:
                        mox "I popped ur msg cherry! :) \nMaybe u can pop mine later too? xd"
                    jump msgmenumox
                "{i}Hiya! (Read){/i}" if moxmsg1 == 2:
                    jump moxmsg1  
                "Back":
                    jump msgmenu
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve
            return
label todo:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    call completionpercentcalc from _call_completionpercentcalc_1
    menu todomenu:
        "Game Completion: [completionpercent:.0f]%%\nSuggestion: [todosuggestion]"
        "Treehouse ([magiccompletion]/3)":
            menu:
                "First Visit ([magicroute1]/1)":
                    pass
                "Second Visit ([magicroute2]/1)":
                    pass
                "Third Visit ([magicroute3]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Brothel ([brothelcompletion]/4)":
            menu:
                "First Visit ([brothelroute1]/1)":
                    pass
                "Second Visit ([brothelroute2]/1)":
                    pass
                "Third Visit ([brothelroute3]/1)":
                    pass
                "Fourth Visit ([brothelroute4]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Farm ([farmcompletion]/4)":
            menu:
                "First Visit ([farmroute1]/1)":
                    pass
                "Second Visit ([farmroute2]/1)":
                    pass
                "Third Visit ([farmroute3]/1)":
                    pass
                "Fourth Visit ([farmroute4]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Bakery ([bakerycompletion]/2)":
            menu:
                "First Visit ([bakeryroute1]/1)":
                    pass
                "Second Visit ([bakeryroute1]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Forest ([forestcompletion]/2)":
            menu:
                "First Visit ([forestroute1]/1)":
                    pass
                "Second Visit ([forestroute2]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Bar ([barcompletion]/4)":
            menu:
                "First Visit ([barroute1]/1)":
                    pass
                "Second Visit ([barroute2]/1)":
                    pass
                "Third Visit ([barroute3]/1)":
                    pass
                "Fourth Visit ([barroute4]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Castle ([castlecompletion]/3)":
            menu:
                "First Visit ([castleroute1]/1)":
                    pass
                "Second Visit ([castleroute2]/1)":
                    pass
                "Third Visit ([castleroute3]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Act 2 ([act2completion]/8)" if castleroute3 == 1:
            menu:
                "Arrival ([dawnroute1]/1)":
                    pass
                "[rik] and [hon] Training ([crystal1a]/1)":
                    pass
                "[rub] and [bla] Training ([crystal1b]/1)":
                    pass
                "Cadia Falls ([crystal2]/1)":
                    pass
                "[pen]'s Findings ([crystal3]/1)":
                    pass
                "[but]'s Findings ([crystal4]/1)":
                    pass
                "[daw] and [bla]'s Idea ([crystal5]/1)":
                    pass
                "Return to Arcadia ([crystal6]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Extra ([extracompletion]/3)":
            menu:
                "[mox]'s Concert ([moxieroute1]/1)":
                    pass
                "Eidolon Spire ([morriganroute1]/1)":
                    pass
                "Finale ([finale]/1)":
                    pass
                "Back":
                    pass
            jump todomenu
        "Secrets ([secretcompletion]/[totalsecrets])" if secretcompletion > 0 or finale == 1:
            $ bigmenu = 1
            menu:
                "Walk at Twilight ([lilysecret]/1)" if steamcontent == 1:
                    pass
                "Country Gals ([honeycrispsecret]/1)" if steamcontent == 1:
                    pass
                "Sonic Boom! ([rikusecret]/1)":
                    pass
                "Nevermore Shrine ([butpensecret]/1)" if steamcontent == 1:
                    pass
                "The Fun has been Doubled! ([selenesecret]/1)":
                    pass
                "Another [daw], Another Day ([dawnsecret]/1)":
                    pass
                "Open Marriage ([augustasecret]/1)" if steamcontent == 1:
                    pass
                "DLC ([blackcurrantsecret]/1)" if steamcontent == 1:
                    pass
                "A Succubi's Secrets ([butterssecret]/1)" if steamcontent == 1:
                    pass
                "Bad Ending ([morrigansecret]/1)" if steamcontent == 1:
                    pass
                "The People's Princess ([moxiesecret]/1)" if steamcontent == 1:
                    pass
                "Memories of a Boutique ([rubysecret]/1)" if steamcontent == 1:
                    pass
                "Back":
                    pass
            $ bigmenu = 0
            jump todomenu
        "Back":
            pass
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return
label gallery:
    $ phoneenabled = 0
    $ gallery = 1
    show black:
        alpha 1
    $ textbox = 2
    call genreset from _call_genreset_58
    menu gallerymenu:
        "This is a CG gallery, to replay entire scenes, you can visit characters at their homes."
        "Intro":
            menu galleryintromenu:
                "[mox] & [pen] Double Blowjob":
                    show moxpen1a 1 with d
                    ""
                    show moxpen1a 2 with d
                    ""
                    show moxpen1b 1 with d
                    ""
                    show moxpen1b 2 with d
                    ""
                    play sound2 cum
                    show moxpen1b cum with c
                    ""
                    play sound2 cum
                    hide moxpen1b
                    show moxpen1a 2 cum1
                    with c
                    ""
                    show moxpen1a 1 cum2 with c
                    ""
                    hide moxpen1a with d
                "[lil] Buttjob":
                    show lily1a 1 with d
                    ""
                    show lily1a hands with d
                    ""
                    show lily1a -hands with d
                    show lily1a buttjob1 with d
                    ""
                    show lily1a buttjob2 cum with c
                    ""
                    show lily1a -buttjob2 with d
                    ""
                    hide lily1a with d
                "[mox] & [pen] Threesome":
                    show moxpen2a 1 with d
                    ""
                    show moxpen2a 2 with d
                    ""
                    show moxpen2b e1 with d
                    ""
                    show moxpen2b e2 sex1 with d
                    ""
                    show moxpen2b sex2 with d
                    ""
                    show moxpen2b e3 sex3 with c
                    ""
                    show moxpen2b e3 sex4 with d
                    ""
                    show moxpen2c m1 p1 with d
                    ""
                    show moxpen2c m2 p2 cum with c
                    ""
                    hide moxpen2a
                    hide moxpen2b
                    hide moxpen2c
                    with d
                "[mox]'s First Time Marathon" if intro2 == 1:
                    show moxie1a e1 with d
                    ""
                    show moxie1a e2 v1 with d
                    ""
                    show moxie1a e3 v2 cum with c
                    ""
                    show moxie1a -v2  with d
                    ""
                    show moxie1b e1 with d
                    ""
                    show moxie1b e2 v1 with d
                    ""
                    show moxie1b e3 v2 cum with c
                    ""
                    show moxie1b e3 -v2 with d
                    ""
                    hide moxie1a
                    hide moxie1b 
                    with d
                "Back":
                    jump gallerymenu
            jump galleryintromenu
        "Treehouse" if magicroute1 == 1:
            menu gallerytreehousemenu:
                "[lil] Clone Handjob":
                    show lil2a l2e1 with d
                    ""
                    show lil2a hj1 l2e2 with d
                    ""
                    show lil2a lily1 l1e1 with d
                    ""
                    show lil2a l1e2 l2e2 cum hj1cum with c
                    ""
                    hide lil2a with d
                "[lil] Clone Threesome":
                    show lil2b e1 with d
                    ""
                    show lil2b e2 with d
                    show handjob at flip with d:
                        xalign 0.05 yalign 0.9
                    ""
                    show lil2c e2b 
                    hide lil2b
                    hide handjob 
                    with d
                    ""
                    show lil2c v1a e2a with d
                    ""
                    show lil2c v2a with c
                    ""
                    show lil2c e3 cum2 -v2a with d
                    ""
                    hide lil2c with d
                "[lil] 2.0 Message":
                    show lilmsg1 with d:
                        xalign 0.5 zpos -1000 ypos -450
                    ""
                    hide lilmsg1 with d
                "[lil] Sideways Leg-Up Sex" if magicroute2 == 1:
                    show lily3a e1 with d
                    ""
                    show lily3a e2 v1 with d
                    ""
                    show lily3a cum v2 with d
                    ""
                    show lily3a e3 -v1 -v2 with d
                    ""
                    hide lily3a
                "[lil] Sideways Leg-Down Sex" if magicroute2 == 1:
                    show lily3b e1 with d
                    ""
                    show lily3b e2 v1 with d
                    ""
                    show lily3b v2 with d
                    ""
                    show lily3b -v2 -v1 with d
                    ""
                    hide lily3b with d
                "[pen] Pet-Play Paizuri":
                    show pen1a e1 collar with d
                    ""
                    show pen1a cum e2 with d
                    ""
                    hide pen1a with d
                "[pen] Tied From Behind":
                    show pen1b e1 rope with d
                    ""
                    show pen1b v1 e2 with d
                    ""
                    show pen1b v2 cum e2 with c
                    "" 
                    show pen1b -v2 -v1 e3 with d
                    ""
                    hide pen1b with d
                "[pen] and [mox] Butt Sandwich" if magicroute3 == 1:
                    show pen2a always me1 pe1 with d
                    ""
                    hide pen2a with d
                "[pen] and [mox] Doggystyle" if magicroute3 == 1:
                    show pen2b always me1 pe1 with d
                    ""
                    show pen2b v1 me2 pe2 with d
                    ""
                    show pen2b cum v2 with c
                    ""
                    show pen2b -v1 -v2 me3 pe3 with d
                    ""
                    hide pen2b with d
                "[pen] and [mox] 69"  if magicroute3 == 1:
                    show pen2c always e1 c1 with d
                    ""
                    show pen2c v1 with d
                    ""
                    show pen2c c2 v2 e1 with c
                    ""
                    hide pen2c
                "[pen], [mox], and [lil] Finale"  if magicroute3 == 1:
                    show pen2d always l1 m1 p1 c1 with d
                    ""
                    show pen2d s1 l2 m2 p2 with d
                    ""
                    show pen2d s2 c2 with c
                    ""
                    show pen2d s3 l3 m3 p3 with d
                    ""
                    show pen2d s4 c3 l2 with c
                    ""
                    show pen2d p2 with c
                    ""
                    hide pen2d
                "Back":
                    jump gallerymenu
            jump gallerytreehousemenu
        "Brothel" if brothelroute1 == 1:
            menu gallerybrothelmenu:
                "[mel] Footjob":
                    show mel1a e1 with d
                    ""
                    show mel1a e2 with d
                    ""
                    show mel1a cum e3
                    with c
                    ""
                    hide mel1a
                "[mel] Blowjob":
                    show mel1b e1 with d
                    ""
                    show mel1b e2 with d
                    ""
                    show mel1b cum
                    with c
                    ""
                    hide mel1b
                "[mel] Handjob" if brothelroute2 == 1:
                    show melody2a e1 hj goth with d
                    ""
                    show melody2a e2 with d
                    ""
                    show melody2a hj2 cum e3 with c
                    ""
                    hide melody2a with d
                "[mel] Cowgirl and Reverse Cowgirl" if brothelroute2 == 1:
                    show melody2b c1 e1 with d
                    ""
                    show melody2b a1 e2 with d
                    ""
                    show melody2b c2 with d
                    ""
                    show melody2b e2 cum a2 with c
                    ""
                    show melody2b e3 with d
                    ""
                    hide melody2b
                    show melody2c e1 c1 
                    with d
                    ""
                    show melody2c a1 e2 with d
                    ""
                    show melody2c a2 cum with c
                    ""
                    show melody2c -a1 -a2 e1 with d
                    ""
                    hide melody2c
                "[mel] From Behind" if brothelroute3 == 1:
                    show mel3a e1 with d
                    ""
                    show mel3a v1 e2 with d
                    ""
                    show mel3a cum v2 with c
                    ""
                    show mel3a -v1 -v2 e3 with d
                    ""
                    hide mel3a with d
                "[mel] Legs Up" if brothelroute3 == 1:
                    show mel3b e1 with d
                    ""
                    
                    show mel3b v1 e2 with d
                    ""
                    show mel3b v2 cum with d
                    ""
                    show mel3b -v1 -v2 e3 with d
                    "" 
                    hide mel3b with d
                "[mel], [sky], [blo] Threesome" if brothelroute4 == 1:
                    show cru1 with d
                    ""
                    show cru1 cum with d
                    ""
                    show cru2 es1 em1 eb1 with d
                    ""
                    show cru2 s1 eb2 with d
                    ""
                    show cru2 s2 eb1 em2 with d
                    ""
                    show cru2 s3 em1 es2 with d
                    ""
                    show cru2 cum -s3 eb2 em2 with d
                    ""
                    show cru2 es1 em1 eb1 with d
                    ""
                    hide cru1
                    hide cru2
                    with d
                "[rub] Bathrobe":
                    show ruby1a e1 with d
                    ""
                    show ruby1a e2 with d
                    "" 
                    show ruby1a e3 with d
                    ""
                    hide ruby1a with d
                "[rub] Couch Missionary":
                    show ruby1b e1 with d
                    ""
                    show ruby1b e2 v1 with d
                    ""
                    show ruby1b e3 v2 cum with c
                    ""
                    show ruby1b -v2 with d
                    ""
                    hide ruby1b with d
                "[rub] From Behind" if brothelroute2 == 1:
                    show rub2a e1a lingerie2 plug with d
                    ""
                    show rub2a e2a v1 with d
                    ""
                    show rub2a v2 e2a cum with c
                    ""
                    show rub2a -v2 e3 with d
                    ""
                    hide rub2a with d
                "[rub] Legs Up" if brothelroute2 == 1:
                    show rub2b e1 lingerie plug with d
                    ""
                    show rub2b v1 e2 with d
                    ""
                    show rub2b v2 cum with c
                    ""
                    show rub2b -v1 -v2 -a1 -a2 e3 -plug with d 
                    ""
                    show rub2b a1 e2 with d
                    ""
                    show rub2b a2 e2 with d
                    ""
                    show rub2b -v1 -v2 -a1 -a2 e3 with d 
                    ""
                    hide rub2b with d
                "Back":
                    jump gallerymenu
            jump gallerybrothelmenu
        "Farm" if farmroute1 == 1:
            $ bigmenu = 1
            menu galleryfarmmenu:
                "Note: You can scroll and drag large menus"
                "Back":
                    $ bigmenu = 0
                    jump gallerymenu
                "[blo] Butt from Below":
                    show blossom1a e1 with d
                    ""
                    show blossom1a e2 with d
                    ""
                    hide blossom1a with d
                "[blo] Butt from the Side":
                    show blossom1b with d
                    ""
                    show blossom1b hand with d
                    ""
                    show blossom1b -hand b1 with d
                    ""
                    show blossom1b b1 b2 cum with d
                    ""
                    show blossom1b -b1 -b2 cum with d
                    ""
                    hide blossom1b with d
                "[blo] Butt from a MSG":
                    show blomsg1 text with d
                    ""
                    show blomsg1 -text with d
                    ""
                    hide blomsg1 with d
                "[blo] Pussy from Below" if farmroute2 == 1:
                    show blo2a with d
                    ""
                    hide blo2a with d
                "[blo] Blowjob" if farmroute2 == 1:
                    show blo2b e1 with d
                    ""
                    show blo2b e2 with d
                    ""
                    show blo2b cum with c
                    ""
                    show blo2b e3 with d
                    ""
                    hide blo2b with d
                "[blo] Doggystyle" if farmroute2 == 1:
                    show blo2c e1 with d
                    ""
                    show blo2c v1 e2 with d
                    "" 
                    show blo2c cum v2 with c
                    ""
                    show blo2c -v2 e3 with d
                    ""
                    hide blo2c with d
                "[blo] and [mel]" if farmroute4 == 1:
                    show blomel1 e1 with d
                    ""
                    show blomel1 e2 with d
                    ""
                    show blomel1 a1 with d
                    "" 
                    show blomel1 a2 cum e3 with d
                    ""
                    show blomel1 -a1 -a2 with d
                    ""
                    hide blomel1 with d
                "[hon] Shower":
                    show honeycrisp1a with d
                    ""
                    hide honeycrisp1a with d
                "[hon] Thighjob":
                    show honeycrisp1b e1 with d
                    ""
                    show honeycrisp1b e2 tj1 with d
                    ""
                    show honeycrisp1b e3 tj2 with d
                    "" 
                    show honeycrisp1b e2 -tj2 cum with d
                    ""
                    hide honeycrisp1b with d
                "[hon] Butt Tease":
                    show honeycrisp1c with d
                    ""
                    hide honeycrisp1c with d
                "[hon] Doggystyle" if farmroute2 == 1:
                    show hon2a e1 with d
                    ""
                    show hon2a v1 e2 with d
                    ""
                    show hon2a cum v2 with c
                    ""
                    show hon2a e3 -v2 with d
                    "" 
                    hide hon2a with d
                "[hon] Cowgirl" if farmroute2 == 1:
                    show hon2b e1 with d
                    ""
                    show hon2b pp1 e2 with d
                    "" 
                    show hon2b pp2 e3 with d
                    ""
                    show hon2b cum2 cum with d 
                    ""
                    show hon2b pp1 cum1 e4 with d
                    "" 
                    hide hon2b with d
                "[hon] Milking" if farmroute3 == 1:
                    show hon3a e1 with d
                    ""
                    show hon3a anna e2 with d
                    ""
                    show hon3a larger with d
                    ""
                    show hon3a -anna milk e3 with d
                    ""
                    show hon3a mm2 e4 with d
                    ""
                    hide hon3a with d
                "[hon] and Anna Threesome" if farmroute3 == 1:
                    show hon3b e1 with d
                    ""
                    show hon3b e2 s1 with d
                    ""
                    show hon3b c1 s2 with d
                    ""
                    show hon3b e1 -s1 -s2 with d
                    ""
                    show hon3b s3 e3 with d
                    ""
                    show hon3b s4 c2 with d
                    ""
                    show hon3b -s3 -s4 e1 with d
                    ""
                    hide hon3b with d
                "Back":
                    $ bigmenu = 0
                    jump gallerymenu
            jump galleryfarmmenu
        "Bakery" if bakeryroute1 == 1:
            menu gallerybakerymenu:
                "[bla] Paizuri":
                    show bla1a e1 with d
                    ""
                    show bla1a e2 with d
                    ""
                    show bla1a e3 cum1 with c
                    ""
                    hide bla1a with d
                "[bla] Doggystyle":
                    show bla1b e1 with d
                    ""
                    show bla1b v1 e2 with d
                    ""
                    show bla1b v2 cum with c
                    ""
                    show bla1b -v1 -v2 e1 with d
                    ""
                    hide bla1b with d
                "[bla] Blowjob with [cre]" if bakeryroute2 == 1:
                    show bla2a e1 with d
                    ""
                    show bla2a cum e2 with d
                    ""
                    hide bla2a with d
                "[bla] Sex with [cre]" if bakeryroute2 == 1:
                    show bla2b e1 sex1 with d
                    "" 
                    show bla2b sex2 e2 with d
                    ""
                    show bla2b sex3 cum with c
                    ""
                    show bla2b sex1 e3 with d
                    ""
                    hide bla2b with d
                "Back":
                    jump gallerymenu
            jump gallerybakerymenu
        "Forest" if forestroute1 == 1:
            menu galleryforestmenu:
                "[but] Caught in Forest":
                    show but1a 1 with d
                    ""
                    show but1a 2 with d
                    ""
                    hide but1a with d
                "[but] Tailjob":
                    show but1b wings t1 with d
                    ""
                    show but1b pp1 with d
                    ""
                    show but1b -t1 t2 with d
                    ""
                    show but1b pp2 cum with c
                    ""
                    show but1b -pp2 -pp1 -t2 t1 with d
                    ""
                    hide but1b with d
                "[but] Oral":
                    show but1c succ e1 with d
                    ""
                    show but1c e2 with d
                    ""
                    show but1c cum with c
                    ""
                    hide but1c with d
                "[but] Bedroom Pose" if forestroute2 == 1:
                    show but2a with d
                    ""
                    hide but2a with d
                "[but] Doggystyle" if forestroute2 == 1:
                    show but2b succ e1 with d
                    ""
                    show but2b v1 e2 with d
                    ""
                    show but2b cum v2 with c
                    ""
                    show but2b e1 -v1 -v2 with d
                    ""
                    hide but2b with d
                "[but] Paizuri" if forestroute2 == 1:
                    show but2c e1 with d
                    ""
                    show but2c e2 with d
                    ""
                    show but2c c1 with c
                    ""
                    hide but2c with d
                "Back":
                    jump gallerymenu
            jump galleryforestmenu
        "Bar" if barroute1 == 1:
            menu gallerybarmenu:
                "[sky] Handjob":
                    show sky1a e1 with d
                    ""
                    show sky1a e2 with d
                    ""
                    show sky1a e3 cum with d
                    ""
                    hide sky1a with d
                "[sky] Anal Cowgirl":
                    show sky1b e1 with d
                    ""
                    show sky1b man pp1 e2 with d
                    ""
                    show sky1b a1 e3 with d
                    ""
                    show sky1b a2 with d
                    "" 
                    show sky1b pp1 pp2 -a1 -a2 cum e2 with d
                    ""
                    hide sky1b with d
                "[sky] and [blo]" if barroute4 == 1:
                    show blosky1 e1 with d
                    ""
                    show blosky1 e2 v1 with d
                    "" 
                    show blosky1 cum v2 e3 with d
                    ""
                    show blosky1 -v1 -v2 with d
                    ""
                    hide blosky1
                    show blosky2 e1
                    with d
                    ""
                    show blosky2 blo with d
                    ""
                    show blosky2 v1 e2 with d
                    ""
                    show blosky2 v2 with d
                    ""
                    show blosky2 -v1 -v2 cum e3 with d
                    ""
                    hide blosky2 with d
                "[rik] Cunnilingus" if barroute2 == 1:
                    show rik1c with d
                    ""
                    show rik1a e1 with d
                    ""
                    show rik1a e2 oral with d
                    ""
                    show rik1a e3 -oral -squirt with d
                    ""
                    hide rik1c
                    hide rik1a 
                    with d
                "[rik] Legs-Up Anal" if barroute2 == 1:
                    show rik1b e1 with d
                    ""
                    show rik1b a1 e2 with d
                    ""
                    show rik1b cum a2 with d
                    "" 
                    show rik1b -a1 -a2 e3 with d
                    ""
                    hide rik1b with d
                "[rik] Swimsuit" if barroute3 == 1:
                    show rik2a swimsuit with d
                    ""
                    show rik2a -swimsuit with d
                    ""
                    hide rik2a with d
                "[rik] Pool Sex" if barroute3 == 1:
                    show rik2b e1 with d
                    ""
                    show rik2b v1 e2 with d
                    ""
                    show rik2b cum v2 with d
                    ""
                    show rik2b -v1 -v2 e1 with d
                    ""
                    hide rik2b with d
                "[rik] Sleepy Sex" if barroute4 == 1:
                    show rik3b e1 with d
                    ""
                    show rik3b a1 with d
                    ""
                    show rik3b a2 e2 with d
                    ""
                    show rik3b cum e3 -a1 -a2 with d
                    ""
                    hide rik3b with d
                "Back":
                    jump gallerymenu
            jump gallerybarmenu
        "Castle " if castleroute1 == 1:
            menu gallerycastlemenu:
                "[aur] Action Pose":
                    show aur0 e1 with d
                    ""
                    show daybreaker1 with d
                    ""
                    hide aur0 
                    hide daybreaker1
                    with d
                "[mor] Action Pose":
                    show mor0 with d
                    ""
                    hide mor0 with d
                "[mor] Blowjob":
                    show mor1 e1 with d
                    ""
                    show mor1 cum e2 with d
                    ""
                    hide mor1 with d
                "[rub] and [rik] Doggystyle":
                    show rubrik1 e1 with d
                    ""
                    show rubrik1 e1 male with d
                    ""
                    show rubrik1 e3 -male s1 with d
                    ""
                    show rubrik1 c1 cum2 with d
                    "" 
                    show rubrik1 -s1 -c1 e1 with d
                    ""
                    show rubrik1 e2 s2 with d
                    ""
                    show rubrik1 c2 cum1 with d
                    ""
                    show rubrik1 -s2 -c2 e1 with d
                    ""
                    hide rubrik1 with d
                "[hon] and [but] Tribbing":
                    show honbutt with d
                    ""
                    show honbutt s1 with d
                    ""
                    show honbutt c1 with d
                    ""
                    show honbutt -s1 -c1 cum with d
                    ""
                    show honbutt s2 with d
                    ""
                    show honbutt c2 with d
                    ""
                    show honbutt -c2 -s2 with d
                    ""
                    hide honbutt with d
                "[mox] Celebration Sex":
                    show mox2a e1 with d
                    ""
                    play sound2 darkness
                    show mox2a e2 with p
                    ""
                    play sound2 cum
                    show mox2a v1 v2 e3 c1 with c
                    ""
                    show mox2a e4 with d
                    ""
                    show mox2a v1 v2 e3 c1 with d
                    ""
                    show mox2a c2 e4 with c
                    ""
                    show mox2a -v1 -v2  with d
                    ""
                    hide mox2a with d
                "[aur] from Below" if castleroute2 == 1:
                    show aur1a with d
                    ""
                    hide aur1a with d
                "[aur] Giant Breast Job" if castleroute2 == 1:
                    show aur1b e1 with d
                    ""
                    play sound2 darkness
                    with p
                    show aur1b bigger with dissolve
                    ""
                    show aur1b e2 mm with d
                    ""
                    play sound2 cum
                    show aur1b e3 c1 c2 with d
                    ""
                    show aur1b -c1 with d
                    ""
                    hide aur1b with d
                "[aur] Reverse Cowgirl" if castleroute2 == 1:
                    show aur1c e1 p1 with d
                    ""
                    show aur1c v1 e2 with d
                    ""
                    show aur1c v2 cum 
                    show internalcreampie at flip
                    with d
                    ""
                    show aur1c e1 
                    hide internalcreampie
                    with d
                    ""
                    show aur1c p1 p2 with d
                    ""
                    hide aur1c with d 
                "[sel] Side-On" if castleroute3 == 1:
                    $ gen1 = 1
                    show sel1 e1 with d
                    ""
                    show sel1 v1 e2 with d
                    ""
                    show sel1 v2 cum with c
                    ""
                    show sel1 -v1 -v2 e3 with d
                    ""
                    hide sel1 with d
                "Back":
                    jump gallerymenu
            jump gallerycastlemenu
        "Act 2" if castleroute3 == 1:
            $ bigmenu = 1
            menu galleryact2menu:
                "[daw] Cowgirl":
                    show dawn1 dress e1 pp with d
                    ""
                    show dawn1 e2 -pp with d
                    ""
                    show dawn1 cum with c
                    ""
                    show dawn1 e3 pp2 with d
                    ""
                    hide dawn1 with d
                "[mox] Full-Nelson":
                    show mox4 e1 pp with d
                    ""
                    show mox4 dawn with d
                    ""
                    show mox4 v1 e2 with d
                    ""
                    show mox4 v2 e3 cum with c
                    ""
                    show mox4 pp -v2 -v1 with d
                    "" 
                    hide mox4 with d
                "[hon] Tied Cowgirl" if crystal1a == 1:
                    show hon4 e1 pp1 rope with d
                    ""
                    show hon4 e2 sex1 with d
                    ""
                    show hon4 sex2 with c
                    ""
                    show hon4 pp2 cum e3 with d
                    ""
                    hide hon4 with d
                "[rik] Spanking Balcony" if crystal1a == 1:
                    $ gen1 = 0
                    show rik4 e1 with d
                    ""
                    show rik4 e2 spanked with d
                    ""
                    show rik4 v1 e2 with d
                    ""
                    show rik4 v2 cum with c
                    ""
                    show rik4 e1 -v1 -v2 with d
                    ""
                    hide rik4 with d
                "[rub] Facesitting Denial" if crystal1b == 1:
                    show rub4a e2 fs3 with d
                    ""
                    show rub4a e3 fs3 
                    show rubhandjob:
                        xalign 1.0
                    with d
                    ""
                    hide rub4a
                    hide rubhandjob
                    show rub4d 
                    with d
                    ""
                    show rub4b with d
                    ""
                    show rub4b cum with c
                    ""
                    hide rub4b
                    hide rub4d
                    with d
                "[bla] Tail Pulling" if crystal1b == 1:
                    $ gen1 = 1
                    $ gen2 = 1
                    show bla3a e1 with d
                    ""
                    show bla3a v1 e2 with d
                    ""
                    show bla3a v2 cum with c
                    ""
                    show bla3a e1 -v1 -v2 with d
                    ""
                    hide bla3a
                    $ gen1 = 0
                    $ gen2 = 0
                    with d
                "[lil] in the Bushes" if crystal2 == 1:
                    show lil4a e1 with d
                    ""
                    show lil4a s1 e2 with d
                    ""
                    show lil4a s2 cum with c
                    ""
                    show lil4a -s1 -s2 e1 with d
                    ""
                    hide lil4a with d
                "[pen] Choked from Behind" if crystal3 == 1:
                    show pen3a e1 with d
                    ""
                    show pen3a sex1 e2 with d
                    "" 
                    show pen3a choke with d
                    ""
                    show pen3a cum sex2 with c
                    ""
                    show pen3a -sex1 -sex2 -choke e3 with d
                    ""
                    hide pen3a with d
                "[but] Succubus Then Non-Succubus" if crystal4 == 1:
                    $ gen1 = 2
                    show but3a e1 with d
                    ""
                    show but3c with d
                    ""
                    hide but3c
                    show but3a sex e2
                    with d
                    ""
                    show but3a cum with c
                    ""
                    show but3a -sex -cum e3 with d
                    ""
                    hide but3a
                    show but3b e1 
                    with d
                    ""
                    show but3b v1 e2 with d
                    ""
                    show but3b v2 cum with c
                    ""
                    show but3b -v1 -v2 e3 with d
                    ""
                    hide but3b
                    $ gen1 = 0
                "[daw] Windowsill Secret" if crystal5 == 1:
                    $ gen1 = 1
                    show dawn2a e1 dress with d
                    ""
                    show dawn2b e1 with d
                    ""
                    show dawn2b e2 cum with d
                    ""
                    show dawn2c e1 with d
                    "" 
                    show dawn2c e2 v1 with d
                    ""
                    show dawn2c v2 cum with d
                    ""
                    show dawn2c -v1 -v2 e1 with d
                    ""
                    hide dawn2a
                    hide dawn2b 
                    hide dawn2c 
                    with d
                    $ gen1 = 0
                "Princess [lil] on the Throne" if crystal5 == 1:
                    show plil1 e1 with d
                    ""
                    show plil1 e2 v1 with d
                    ""
                    show plil1 v2 cum with d
                    ""
                    show plil1 e3 -v1 -v2 with d
                    ""
                    hide plil1 with d
                "Princess [mox] Loving" if crystal5 == 1:
                    show pmox1a e1 with d
                    ""
                    show pmox1a e2 v1 with d
                    ""
                    show pmox1a v2 cum with d
                    ""
                    show pmox1a -v1 -v2 e3 with d
                    ""
                    hide pmox1a with d
                "Queens Threesome" if crystal6 == 1:
                    show queens1a
                    ""
                    show liqueens1b e1 with d
                    ""
                    show liqueens1c e2 cum with d
                    ""
                    show liqueens1d e1 outside cum1 with d
                    ""
                    show liqueens1d e2 -outside with d
                    ""
                    show liqueens1d cum2 with d
                    ""
                    hide queens1a
                    hide liqueens1b
                    hide liqueens1c
                    hide liqueens1d
                    with d
                "Back":
                    $ bigmenu = 0
                    jump gallerymenu
            jump galleryact2menu
        "Extra" if dayevent >= 4 or ros2 == 1 or cla1 == 1 or bas1 == 1 or hil1 == 1:
            menu galleryextramenu:
                "[mox] Backstage Blowjob" if moxieroute1 == 1:
                    show mox3a e4 bj1 lingerie
                    ""
                    show mox3a e5 with d
                    ""
                    show mox3a e5 c1 bj2 with c
                    ""
                    show mox3a e5 -bj1 -bj2 with d
                    ""
                    hide mox3a with d
                "[mox] Backstage Doggystyle" if moxieroute1 == 1:
                    show mox3b e1 lingerie with d
                    ""
                    show mox3b e2 v1 with d
                    ""
                    show mox3b cover e3 with d
                    ""
                    show mox3b e2 v2 cum with c
                    ""
                    show mox3b e3 with d
                    ""
                    show mox3b e1 -cover -v1 -v2 with d
                    ""
                    hide mox3b with d
                "[mor] Sex" if morriganroute1 == 1:
                    show mor2 e1 with d
                    ""
                    show mor2 v1 e2 with d
                    ""
                    show mor2 v2 cum with d
                    ""
                    show mor2 -v1 -v2 e3 with d
                    ""
                    hide mor2 with d
                "[cla] Bath From Behind" if cla1 == 1:
                    show cla1 e1 with d
                    ""
                    show cla1 e3 v1 with d
                    ""
                    show cla1 v2 cum with c
                    ""
                    show cla1 e2 -v2 -v1 with d
                    ""
                    hide cla1 with d
                "[ros] Missionary":
                    show rosa1a e1 with d
                    ""
                    show rosa1a e2 v1 with d
                    ""
                    show rosa1a e3 v2 cum with c
                    ""
                    show rosa1a e3 -v2 with d
                    ""
                    hide rosa1a with d
                "[ros] Sideways" if ros2 == 1:
                    show ros2b e1 with d
                    ""
                    show ros2b e2 v1 with d
                    ""
                    show ros2b v2 cum with c
                    ""
                    show ros2b e3 -v1 -v2 with d
                    ""
                    hide ros2b with d
                "[hil] Service" if hil1 == 1:
                    show hil1 e1 with d
                    ""
                    show hil1 v1 e2 with d
                    ""
                    show hil1 v2 cum with d
                    ""
                    show hil1 -v1 -v2 e1 with d
                    ""
                    hide hil1 with d
                "[bas] Service" if bas1 == 1:
                    show bas1 with d
                    ""
                    show bas1 oral1 with d
                    ""
                    show bas1 -oral1 v1 with d
                    ""
                    show bas1 v2 cum with d
                    ""
                    show bas1 -v2 -v1 with d
                    ""
                    hide bas1 with d
                "[hil] and [bas] Service" if hil1 and bas1 == 1:
                    show bashil1 a1 k1 with d
                    ""
                    show bashil1 s1 k2 a3 with d
                    ""
                    show bashil1 s2 c1 with d
                    ""
                    show bashil1 a1 k1 -s1 -s2 with d
                    ""
                    show bashil1 s3 k3 a2 with d
                    ""
                    show bashil1 s4 c2 with d
                    ""
                    show bashil1 -s3 -s4 a1 k1 with d
                    ""
                    hide bashil1 with d
                "Sauna" if finale == 1:
                    $ gen1 = 0
                    show sauna with d
                    ""
                    $ gen1 = 1 
                    with d
                    ""
                    hide sauna with d
                    $ gen1 = 0
                "Back":
                    jump gallerymenu
            jump galleryextramenu
        "Secrets" if secretcompletion >= 1 or finale == 1:
            menu gallerysecretsmenu:
                "Clubbing with [hon]" if honeycrispsecret == 1:
                    show hon5a with d
                    ""
                    show hon5a cum with d
                    ""
                    hide hon5a with d
                "Stargazing with [lil]" if lilysecret == 1:
                    show lil5a e1 with d
                    ""
                    show lil5a e2 v1 with d
                    ""
                    show lil5a v2 cum with d
                    ""
                    show lil5a e3 -v1 -v2 with d
                    ""
                    hide lil5a with d
                "[rik] and Stormflare" if rikusecret == 1:
                    show rik5a e1 with d
                    ""
                    show rik5b e1 with d
                    ""
                    show rik5b e2 v1 with d
                    ""
                    show rik5b cum v2 with d
                    ""
                    show rik5b -v1 -v2 e3 with d
                    ""
                    hide rik5a 
                    hide rik5b 
                    with d
                "[but] and [pen]'s Adventure" if butpensecret == 1:
                    show shrine1a e1 with d
                    ""
                    show shrine1a pp1 e2 with d
                    ""
                    show shrine1a cum pp2 with d
                    ""
                    show shrine1a -pp1 -pp2 e3 with d
                    ""
                    hide shrine1a with d
                "Midnight and [sel]" if selenesecret == 1:
                    show sel2a e1 with d
                    ""
                    show sel2a sex1 e2 with d
                    ""
                    show sel2a c1 cum with d
                    ""
                    show sel2a -sex1 -c1 e1 with d
                    ""
                    show sel2a sex2 e3 with d
                    ""
                    show sel2a c2 cum2 with d
                    ""
                    show sel2a -sex2 -c3 e1 with d
                    ""
                    hide sel2a with d
                "The Third [daw]" if dawnsecret == 1:
                    show daw3a e1 with d
                    ""
                    show daw3b e1 with d
                    ""
                    show daw3b e2 v1 with d
                    ""
                    show daw3b v2 cum with d
                    ""
                    show daw3b e3 -v1 -v2 with d
                    ""
                    show daw3c with d
                    ""
                    show daw3c v1 with d
                    ""
                    show daw3c v2 cum with d
                    ""
                    show daw3d e1 cum with dissolvepunch
                    ""
                    show daw3d s1 e2 with d
                    ""
                    show daw3d s3 e4 with d
                    ""
                    show daw3d -s1 -s3 e1 with d
                    ""
                    hide daw3a 
                    hide daw3b 
                    hide daw3c 
                    hide daw3d 
                    with d
                "Riding with [aug]" if augustasecret == 1:
                    show augustasecret1 dancer with d
                    ""
                    show augustasecret1 man with d
                    ""
                    show augustasecret1 cum with c
                    ""
                    hide augustasecret1 with d
                "[bla] Nightgown" if blackcurrantsecret == 1:
                    show blackcurrantsecret1 e1 with d
                    ""
                    show blackcurrantsecret1 v1 e2 with d
                    ""
                    show blackcurrantsecret1 v2 cum with c
                    ""
                    show blackcurrantsecret1 -v1 -v2 e3 with d
                    ""
                    hide blackcurrantsecret1 with d
                "[but] Succubutt" if butterssecret == 1:
                    show butterssecret1 e1 with d
                    ""
                    show butterssecret1 e2 v1 with d
                    ""
                    show butterssecret1 v2 cum with c
                    ""
                    show butterssecret1 -v1 -v2 e3 with d
                    ""
                    hide butterssecret1 with d
                "Morphling [lil] and Handmaiden" if morrigansecret == 1:
                    show morrigansecret1 with d
                    ""
                    show morrigansecret1 cum with d
                    ""
                    hide morrigansecret1
                    show morrigansecret2
                    with d
                    ""
                    show morrigansecret2 sex1 with d
                    ""
                    show morrigansecret2 sex2 cum1 with c
                    ""
                    show morrigansecret2 -sex2 -sex1 with d
                    ""
                    show morrigansecret2 sex3 with d
                    ""
                    show morrigansecret2 sex4 cum2 with c
                    ""
                    show morrigansecret2 -sex4 -sex3 with d
                    ""
                    hide morrigansecret2 with d
                "[mox] on Stage" if moxiesecret == 1:
                    show moxiesecret1 e1 with d
                    ""
                    show moxiesecret1 v1 e2 with d
                    ""
                    show moxiesecret1 v2 cum with c
                    ""
                    show moxiesecret1 -v1 -v2 e3 with d
                    ""
                    hide moxiesecret1 with d
                "[rub] Lingerie" if rubysecret == 1:
                    show rubysecret1 e1 with d
                    ""
                    show rubysecret1 man pp1 with d
                    ""
                    show rubysecret1 v1 e2 with d
                    ""
                    show rubysecret1 v2 cum with d
                    ""
                    show rubysecret1 pp2 e3 -v2 with d
                    ""
                    show rubysecret1 -man -pp2 with d
                    ""
                    hide rubysecret1 with d
                "Back":
                    jump gallerymenu

            jump gallerysecretsmenu
        "Back":
            $ gallery = 0
            $ textbox = 1
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            hide black with d
            call screen phone_screen with dissolve   
            return
label socials:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    $ feedupdate = 0
    menu socialmenu:
        "Select a post to read more."
        "{color=#0077ff}{b}[mel]{/b}:{/color} Huh {color=#00ff62}(4 Likes){/color}"  if brothelroute3 == 1:
            mel "Never thought I'd find someone special. Life is full of surprises, eh?"
        "{color=#0077ff}{b}[lil]{/b}:{/color} New Day, New Me {color=#00ff62}(20 Likes){/color}"  if magicroute2 == 1:
            lil "I've been more productive than ever lately! Waking up and sleeping at consistent times, getting more exercise, eating healthier. I don't know what came over me, but I hope this can be a new norm for me!"
        "{color=#0077ff}{b}[but]{/b}:{/color} Alchemist Services Available {color=#00ff62}(5 Likes){/color}"  if forestroute2 == 1:
            but "I'm selling potions for all needs, from boundless energy to unbreakable love. Write a message to this account if you're interested in a commission."
            lil "Oooh, ohhh! I checked your portfolio, and finally, a serious alchemist in town! I have so many ideas!"
        "{color=#0077ff}{b}[bla]{/b}:{/color} Grand Reopening {color=#00ff62}(12 Likes){/color}"  if bakeryroute1 == 1:
            bla "[bla]'s bakery is now open once again! Come to cliffside for all your baked delights!"
        "{color=#0077ff}{b}[rub]{/b}:{/color} Now Hiring! {color=#00ff62}(43 Likes){/color}"  if brothelroute1 == 1:
            rub "RUBY's is now looking to hire male talent! You can send me your resumes directly by messaging this account."
            "{i}Rather than messaging [rub], I should visit her instead.{/i}"
        "{color=#0077ff}{b}[mox]{/b}:{/color} Thank you everyone! {color=#00ff62}(5,430 Likes){/color}":
            mox "Thank you to everyone that saw my biggest show ever at the Grand Theatre!"
            "{i}There are hundreds of comments. Wow, it looks like [mox] is doing extremely well for herself.{/i}"
        "{color=#0077ff}{b}[pen]{/b}:{/color} Ice Cream {color=#00ff62}(1 Like){/color}":
            pen "Anyone else miss those cherry flavoured ice cream pots they used to sell at MacDairies?"
            mox "Oh yeah! Those were the bomb!"
            pen "Preach, sister."
            "{i}I could go for some ice cream right now.{/i}"
        #honeycrisp after visit 2: announcing new partnership
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return
    jump socialmenu
label shop1:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    if shoptut == 0:
        call shoptut from _call_shoptut
    menu shop1menu:
        "Money: $[money]"
        "Casual Outfits (Done)" if casualoutfits == 7:
            jump shop1menu
        "Casual Outfits" if casualoutfits != 7:
            menu shop1menu1:
                "Money: $[money]"
                "[mox] Stagewear $75" if moxieoutfit1 == 0:
                    if money >= 75:
                        play sound2 shop2
                        $ money -= 75
                        $ moxieoutfit1 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "Gymwear $75" if gymwear == 0 and barroute1 == 1:
                    if money >= 75:
                        play sound2 shop2
                        $ money -= 75
                        $ gymwear = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "[hon] Cow Lingerie $75" if honeycrispoutfit2 == 0 and farmroute1 == 1:
                    if money >= 75:
                        play sound2 shop2
                        $ money -= 75
                        $ honeycrispoutfit2 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "[hon] Gi $150" if honeycrispoutfit1 == 0 and farmroute1 == 1:
                    if money >= 150:
                        play sound2 shop2
                        $ money -= 150
                        $ honeycrispoutfit1 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "[rik] Casual $150" if rikuoutfit1 == 0 and barroute2 == 1:
                    if money >= 150:
                        play sound2 shop2
                        $ money -= 150
                        $ rikuoutfit1 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "[but] Lingerie $100" if buttersoutfit1 == 0 and forestroute1 == 1:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ buttersoutfit1 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "[but] Ultimate Alchemist $150" if buttersoutfit2 == 0 and forestroute1 == 1:
                    if money >= 150:
                        play sound2 shop2
                        $ money -= 150
                        $ buttersoutfit2 = 1
                        $ casualoutfits += 1
                    else:
                        play sound2 error
                "Back":
                    jump shop1menu
            jump shop1menu1
        "Sex Outfits (Done)" if punk == 1 and bunnygirl == 1 and goth == 1:
            jump shop1menu
        "Sex Outfits" if punk == 0 or bunnygirl == 0 or goth == 0:
            menu shop1menu2:
                "Money: $[money]"
                "Punk - $100" if punk == 0 and moxiepunk == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ punk = 1
                    else:
                        play sound2 error
                "Bunny Girl - $100" if bunnygirl == 0 and moxiebunnygirl == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ bunnygirl = 1
                    else:
                        play sound2 error
                "Goth - $100" if goth == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ goth = 1
                    else:
                        play sound2 error
                "Back":
                    jump shop1menu
            jump shop1menu2
        "Self-Repairing Pantyhose and Fishnets - $125 - Owned: [pantyhose]" if pantyhose == 0:
            if money >= 125:
                play sound2 shop2
                $ money -= 125
                $ pantyhose = 1
            else:
                play sound2 error
        "Personalized Lingerie - $250 - Owned: [lingerie]" if lingerie == 0:
            if money >= 250:
                play sound2 shop2
                $ money -= 250
                $ lingerie = 1
            else:
                play sound2 error
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return
    jump shop1menu   
label shop2:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    if shoptut == 0:
        call shoptut from _call_shoptut_1
    menu shop2menu:
        "Money: $[money]"
        "Performance Boosters - $100 - Increases Max Energy by 1" if maxenergy == 2:
            if money >= 100:
                play sound2 shop2
                $ money -= 100
                $ maxenergy += 1
                $ energy += 1
            else:
                play sound2 error
        "Secret Formula - $500 - Increases Max Energy by 1" if maxenergy == 3:
            if money >= 500:
                play sound2 shop2
                $ money -= 500
                $ maxenergy += 1
                $ energy += 1
            else:
                play sound2 error
        "Buttplugs for All - $125" if buttplug == 0:
            if money >= 125:
                play sound2 shop2
                $ money -= 125
                $ buttplug = 1
            else:
                play sound2 error
        "Makeup - $200" if makeup == 0:
                    if money >= 200:
                        play sound2 shop2
                        $ money -= 200
                        $ makeup = 1
                    else:
                        play sound2 error
        "Bottomless Anal Lubrication - $300" if lubrication == 0:
            if money >= 300:
                play sound2 shop2
                $ money -= 300
                $ lubrication = 1 
            else:
                play sound2 error
        "Lewd Spellbook - $500" if lewdspellbook == 0:
            if money >= 500:
                play sound2 shop2
                $ money -= 500
                $ lewdspellbook = 1
            else:
                play sound2 error
        "Insta-Futa Pills - $1500" if futapill == 0:
            if money >= 1500:
                play sound2 shop2
                $ money -= 1500
                $ futapill = 1
            else:
                play sound2 error
            pass
        "'Milky' Potion - $1500" if pregpotion == 0:
            if money >= 1500:
                play sound2 shop2
                $ money -= 1500
                $ pregpotion = 1
            else:
                play sound2 error
            pass
        "Guidebooks (Only Available on the World Map)" if worldmap == 0:
            jump shop2menu
        "Guidebooks" if worldmap != 0:
            menu shop2menu2:
                "Guidebooks tell you where to find certain sex scenes, and offer to immediately take you there. \nThey can be read at any time from your apartment, or alternatively, read here."
                "Alternative Positions Guidebook ($50)" if guidebook1 == 0:
                    if money >= 50:
                        play sound2 shop2
                        $ money -= 50
                        $ guidebook1 = 1
                    else:
                        play sound2 error
                    pass
                "Costume Guidebook ($75)" if guidebook2 == 0:
                    if money >= 75:
                        play sound2 shop2
                        $ money -= 75
                        $ guidebook2 = 1
                    else:
                        play sound2 error
                    pass
                "Futa Guidebook ($100)"  if guidebook3 == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ guidebook3 = 1
                    else:
                        play sound2 error
                    pass
                "Pregnancy Guidebook ($100)"  if guidebook4 == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ guidebook4 = 1
                    else:
                        play sound2 error
                    pass
                "Secrets Guidebook ($100)" if guidebookS == 0:
                    if money >= 100:
                        play sound2 shop2
                        $ money -= 100
                        $ guidebookS = 1
                    else:
                        play sound2 error
                    pass
                "Alternative Positions Guidebook (Owned)"  if guidebook1 == 1:
                    call guidebook1 from _call_guidebook1
                "Costume Guidebook (Owned)" if guidebook2 == 1:
                    call guidebook2 from _call_guidebook2
                "Futa Guidebook (Owned)" if guidebook3 == 1:
                    call guidebook3 from _call_guidebook3
                "Pregnancy Guidebook (Owned)" if guidebook4 == 1:
                    call guidebook4 from _call_guidebook4
                "Secrets Guidebook (Owned)" if guidebookS == 1:
                    call guidebookS from _call_guidebookS_1
                "Back":
                    jump shop2menu
            jump shop2menu2
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return
    jump shop2menu
label music:
    $ phoneenabled = 0
    $ bigmenu = 1
    $ renpy.music.set_volume(0)
    $ renpy.music.set_volume(0, 0, "ambience1")
    if worldmap == 0:
        show screen phone_screen
    menu musicmenu:
        "Back":
            jump musicmenuback
        "Action 1 - Crystal Kerosene by Sewerslvt":
            play music2 action1 
            $ gent1 = "Crystal Kerosene by Sewerslvt"
        "Action 2 - Car Accident (Nudul Remix)":
            play music2 action2
            $ gent1 = "Car Accident (Nudul Remix)"
        "Action 3 - sick, twisted, demented by Sewerslvt":
            play music2 action3
            $ gent1 = "sick, twisted, demented by Sewerslvt"
        "Action 4 - WOLF by Nudul":
            play music2 action4
            $ gent1 = "WOLF by Nudul"
        "Action 5 - Crimson Moon by Peritune":
            play music2 action5
            $ gent1 = "Crimson Moon by Peritune"
        "[blo]'s Theme - Discovery by Purrple Cat":
            play music2 blossomtheme 
            $ gent1 = "Discovery by Purrple Cat"
        "[but]'s Theme 1 - Dim2 by Peritune":
            play music2 butterstheme1
            $ gent1 = "Dim2by Peritune"
        "[but]'s Theme 2 - Tender Gaze by Peritune":
            play music2 butterstheme2
            $ gent1 = "Tender Gaze by Peritune"
        "Castle - La Fille Aux Cheveux De Lin by Claude Debussy":
            play music2 castle
            $ gent1 = " La Fille Aux Cheveux De Lin by Claude Debussy"
        "Casual 1 - Quiet Ocean by Peritune":
            play music2 casual1 
            $ gent1 = "Quiet Ocean by Peritune"
        "Casual 2 - Firmament Calm by Peritune":
            play music2 casual2
            $ gent1 = "Firnament Calm by Peritune"
        "City - Sparkle by Peritune":
            play music2 citytheme
            $ gent1 = "Sparkle by Peritune"
        "City2 - Sakuya 4 by Peritune":
            play music2 city2
            $ gent1 = "Sakuya 4 by Peritune"
        "Club - delirium dreams by Mindvacy":
            play music2 clubtheme
            $ gent1 = "delirium dreams by Mindvacy"
        "Comical - Larry by Purgatory Garden":
            play music2 comical
            $ gent1 = "Larry by Purgatory Garden"
        "[cre]'s Theme - Cafe Seaside by Peritune":
            play music2 creamtheme
            $ gent1 = "Cafe Seaside by Peritune"
        "Danger1 - Suspense3 by Peritune":
            play music2 danger
            $ gent1 = "Suspense3 by Peritune"
        "Danger2 - Euphoric Filth by Sewerslvt":
            play music2 danger2
            $ gent1 = "Euphoric Filth by Sewerslvt"
        "Daytheme - That's One Sly Cat - Artificial Music":
            play music2 daytheme
            $ gent1 = "That's One Sly Cat - Artificial Music"
        "Deep Dive - an angel above the ugly, mutilated corpses by mindvacy":
            play music2 deep
            $ gent1 = "an angel above the ugly, mutilated corpses by mindvacy"
        "Finale1 - Epic Battle J by Peritune":
            play music2 finale2
            $ gent1 = "Epic Battle J by Peritune"
        "Finale2 - In Memory of Lucy by Nudul":
            play music2 finale3
            $ gent1 = "In Memory of Lucy by Nudul"
        "[hon]'s Theme - Meteorites by Purrple Cat":
            play music2 honeycrisptheme 
            $ gent1 = "Meteorites by Purrple Cat"
        "Intro - microcosm by Mindvacy":
            play music2 intro 
            $ gent1 = "microcosm by Mindvacy"
        "[lil]'s Theme - Aether by Purrple Cat":
            play music2 lilytheme 
            $ gent1 = "Aether by Purrple Cat"
        "[mel]'s Theme - lorncloudshit by Sewerslvt":
            play music2 melodytheme 
            $ gent1 = "lorncloudshit by Sewerslvt"
        "[mel]'s Sex Theme - Yandere Complex by Sewerslvt":
            play music2 melodysextheme 
            $ gent1 = "Yandere Complex by Sewerslvt"
        "[mox]'s Theme - Abstract Foilage by Artificial Music":
            play music2 moxietheme 
            $ gent1 = "Abstract Foilage by Artificial Music"
        "[mor]'s Theme - Deep Sea by Peritune":
            play music2 morrigantheme 
            $ gent1 = "Deep Sea by Peritune"
        "Ominous - Ominous3 by Peritune":
            play music2 ominous 
            $ gent1 = "Ominous3 by Peritune"
        "[pen]'s Theme - Going With The Flow by Purrple Cat":
            play music2 penelopetheme 
            $ gent1 = "Going With The Flow by Purrple Cat"
        "Rainy Day - Cold & Rainy by Purrple Cat":
            play music2 rainytheme 
            $ gent1 = "Cold & Rainy by Purrple Cat"
        "[rub]'s Theme - Toe Wizard by Sewerslvt":
            play music2 rubytheme 
            $ gent1 = "Toe Wizard by Sewerslvt"
        "Sad - hopelessness by Sewerslvt":
            play music2 sad 
            $ gent1 = "hopelessness by Sewerslvt"
        "Sex Theme - Glowing Tides by Purrple Cat":
            play music2 sextheme 
            $ gent1 = "Glowing Tides by Purrple Cat"
        "Sex Theme 2- Purple Hearts in Her Eyes by Sewerslvt":
            play music2 sextheme2
            $ gent1 = "Purple Hearts in Her Eyes by Sewerslvt"
        "Slowburn by Cynthoni":
            play music2 slowburn
            $ gent1 = " Slowburn by Cynthoni"
        "Slowdeath by Sewerslvt":
            play music2 slowdeath
            $ gent1 = " Slowdeath by Sewerslvt"
        "[sky]'s Theme - Whistling Winds by Peritune":
            play music2 skyetheme
            $ gent1 = "Whistling Winds by Peritune"
        "Tension - 7 Heads, 10 Crowns by Nudul":
            play music2 tension
            $ gent1 = "7 Heads, 10 Crowns by Nudul"
        "Back":
            label musicmenuback:
                stop music2
            $ renpy.music.set_volume(1)
            $ renpy.music.set_volume(1, 0, "ambience1")
            $ phoneenabled = 1
            $ bigmenu = 0
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return
    jump musicmenu
label cheats:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    menu cheatmenu:
        "Money: $[money] \nEnergy:[energy]"
        "+/- Money":
            $ gen8 = renpy.input("Enter an amount of monies to gain or lose. Current Monies: $[money]", allow="-0123456789")
            play sound2 item
            $ money += int(gen8)
        "Max Energy":
            play sound2 item
            $ energy += maxenergy
        "Change Names/Styles":
            $ bigmenu = 1
            menu cheatmenu2:
                "Back":
                    $ bigmenu = 0
                    jump cheatmenu
                "You, [mc]":
                    $ mc = renpy.input("What is your name?")
                    if mc == "":
                        $ mc= "Anon"
                    $ mc = mc.strip()
                "[mox] Style [moxb]":
                    $ gen1 = 1
                    call screen characterchoice
                    $ moxb = gen2
                    menu:
                        "What was her name?"
                        "Default: Moxie":
                            $ moxie = "Moxie"
                        "Custom":
                            $ moxie = renpy.input("What was her name?")
                            if moxie == "":
                                $ moxie= "Moxie"
                            $ moxie = moxie.strip()
                "[pen] Style [penb]":
                    $ gen1 = 2
                    call screen characterchoice
                    $ penb = gen2
                    menu:
                        "What was her name?"
                        "Default: Penelope":
                            $ penelope = "Penelope"
                        "Alternate: Sundowner":
                            $ penelope = "Sundowner"
                        "Custom":
                            $ penelope = renpy.input("What was her name?")
                            if penelope == "":
                                $ penelope= "Penelope"
                            $ penelope = penelope.strip()
                "[hon] Style [honb]":
                    $ gen1 = 3
                    call screen characterchoice
                    $ honb = gen2
                    menu:
                        "What was her name?"
                        "Default: Honeycrisp":
                            $ honeycrisp = "Honeycrisp"
                        "Custom":
                            $ honeycrisp = renpy.input("What was her name?")
                            if honeycrisp == "":
                                $ honeycrisp= "Honeycrisp"
                            $ honeycrisp = honeycrisp.strip()
                "[rub] Style [rubb]":
                    $ gen1 = 4
                    call screen characterchoice
                    $ rubb = gen2
                    menu:
                        "What was her name?"
                        "Default: Ruby":
                            $ ruby = "Ruby"
                        "Custom":
                            $ ruby = renpy.input("What was her name?")
                            if ruby == "":
                                $ ruby= "Ruby"
                            $ ruby = ruby.strip()
                "[lil] Style [lilb]":
                    $ gen1 = 7
                    call screen characterchoice
                    $ lilb = gen2
                    menu:
                        "What was her name?"
                        "Default: Lily":
                            $ lily = "Lily"
                        "(Custom Name)":
                            $ lily = renpy.input("What was her name?")
                            if lily == "":
                                $ lily= "Lily"
                            $ lily = lily.strip()
                "[rik] Style [rikb]":
                    $ gen1 = 5
                    call screen characterchoice
                    $ rikb = gen2
                    menu:
                        "What was her name?"
                        "Default: Riku":
                            $ riku = "Riku"
                        "Alternative: Prisma":
                            $ riku = "Prisma"
                        "Custom":
                            $ riku = renpy.input("What was her name?")
                            if riku == "":
                                $ riku= "Riku"
                            $ riku = riku.strip()
                "[cre] Style [creb]":
                    $ gen1 = 6
                    call screen characterchoice
                    $ creb = gen2
                    menu:
                        "What was her name?"
                        "Default: Cream":
                            $ cream = "Cream"
                        "Custom":
                            $ cream = renpy.input("What was her name?")
                            if cream == "":
                                $ cream= "Cream"
                            $ cream = cream.strip()
                "[but] Name":
                    menu:
                        "What was her name?"
                        "Default: Butters":
                            $ butters = "Butters"
                        "Custom":
                            $ butters = renpy.input("What was her name?")
                            if butters == "":
                                $ butters= "Butters"
                            $ butters = butters.strip()
                "[mel] Style [melb]":
                    $ gen1 = 11
                    call screen characterchoice
                    $ melb = gen2
                    menu:
                        "What was her name?"
                        "Default: Melody":
                            $ melody = "Melody"
                        "Custom":
                            $ melody = renpy.input("What was her name?")
                            if melody == "":
                                $ melody= "Melody"
                            $ melody = melody.strip()
                "[blo] Style [blob]":
                    $ gen1 = 12
                    call screen characterchoice
                    $ blob = gen2
                    menu:
                        "What was her name?"
                        "Default: Blossom":
                            $ blossom = "Blossom"
                        "Custom":
                            $ blossom = renpy.input("What was her name?")
                            if blossom == "":
                                $ blossom= "Blossom"
                            $ blossom = blossom.strip()
                "[aur] Style [aurb]" if castleroute1 == 1:
                    $ gen1 = 13
                    call screen characterchoice
                    $ aurb = gen2
                    menu:
                        "What was her name?"
                        "Default: Aurora":
                            $ aurora = "Aurora"
                        "Custom":
                            $ aurora = renpy.input("What was her name?")
                            if aurora == "":
                                $ aurora= "Aurora"
                            $ aurora = aurora.strip()
                "[sel] Name" if castleroute1 == 1:
                    menu:
                        "What was her name?"
                        "Default: Selene":
                            $ selene = "Selene"
                        "Custom":
                            $ selene = renpy.input("What was her name?")
                            if selene == "":
                                $ selene= "Selene"
                            $ selene = selene.strip()
                "[daw] Style [dawb]" if castleroute3 == 1:
                    $ gen1 = 14
                    call screen characterchoice
                    $ dawb = gen2
                    menu:
                        "What was her name?"
                        "Default: Dawn":
                            $ dawn = "Dawn"
                        "Custom":
                            $ dawn = renpy.input("What was her name?")
                            if dawn == "":
                                $ aurora= "Dawn"
                            $ dawn = dawn.strip()
                "Background Characters":
                    menu cheatmenu3:
                        "[mor]'s Name" if castleroute1rewrite == 1:
                            menu:
                                "Default: Morrigan":
                                    $ morrigan = "Morrigan"
                                "Custom":
                                    $ morrigan = renpy.input("What was her name?")
                                    if morrigan == "":
                                        $ morrigan= "Morrigan"
                                    $ morrigan = morrigan.strip()
                        "[cla]'s Name":
                            menu:
                                "Default: Claire":
                                    $ claire = "Claire"
                                "Custom":
                                    $ claire = renpy.input("What was her name?")
                                    if claire == "":
                                        $ claire= "Claire"
                                    $ claire = claire.strip()
                        "[ros]'s Name":
                            menu:
                                "Default: Rosa":
                                    $ rosa = "Rosa"
                                "Custom":
                                    $ rosa = renpy.input("What was her name?")
                                    if rosa == "":
                                        $ rosa= "Rosa"
                                    $ rosa = rosa.strip()
                        "[hil]'s Name":
                            menu:
                                "Default: Hilda":
                                    $ hilda = "Hilda"
                                "Custom":
                                    $ hilda = renpy.input("What was her name?")
                                    if hilda == "":
                                        $ hilda= "Hilda"
                                    $ hilda = hilda.strip()
                        "[bas]'s Name":
                            menu:
                                "I think I recognize her. What was her name?"
                                "Default: Bastet":
                                    $ bastet = "Bastet"
                                "Custom":
                                    $ bastet = renpy.input("What was her name?")
                                    if bastet == "":
                                        $ bastet= "Bastet"
                                    $ bastet = bastet.strip()
                        "Back":
                            jump cheatmenu2
                    jump cheatmenu3
            jump cheatmenu2
        "Content Skip":
            menu skipmenu:
                "Game Completion: [completion]/[fullcompletion]\nToggling the visits out of order isn't tested and may have unintended consequences."
                "Treehouse ([magiccompletion]/3)":
                    menu trskipmenu:
                        "First Visit ([magicroute1]/1)":
                            if magicroute1 == 0:
                                $ magicroute1 = 1
                                $ magiccompletion += 1
                                $ completion += 1
                            else:
                                $ magicroute1 = 0
                                $ magiccompletion -= 1
                                $ completion -= 1
                        "Second Visit ([magicroute2]/1)":
                            if magicroute2 == 0:
                                $ magicroute2 = 1
                                $ magiccompletion += 1
                                $ completion += 1
                            else:
                                $ magicroute2 = 0
                                $ magiccompletion -= 1
                                $ completion -= 1
                        "Third Visit ([magicroute3]/1)":
                            if magicroute3 == 0:
                                $ magicroute3 = 1
                                $ magiccompletion += 1
                                $ completion += 1
                            else:
                                $ magicroute3 = 0
                                $ magiccompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump trskipmenu
                "Brothel ([brothelcompletion]/4)":
                    menu brskipmenu:
                        "First Visit ([brothelroute1]/1)":
                            if brothelroute1 == 0:
                                $ brothelroute1 = 1
                                $ brothelcompletion += 1
                                $ completion += 1
                            else:
                                $ brothelroute1 = 0
                                $ brothelcompletion -= 1
                                $ completion -= 1
                        "Second Visit ([brothelroute2]/1)":
                            if brothelroute2 == 0:
                                $ brothelroute2 = 1
                                $ brothelcompletion += 1
                                $ completion += 1
                            else:
                                $ brothelroute2 = 0
                                $ brothelcompletion -= 1
                                $ completion -= 1
                        "Third Visit ([brothelroute3]/1)":
                            if brothelroute3 == 0:
                                $ brothelroute3 = 1
                                $ brothelcompletion += 1
                                $ completion += 1
                            else:
                                $ brothelroute3 = 0
                                $ brothelcompletion -= 1
                                $ completion -= 1
                        "Fourth Visit ([brothelroute4]/1)":
                            if brothelroute4 == 0:
                                $ brothelroute4 = 1
                                $ brothelcompletion += 1
                                $ completion += 1
                            else:
                                $ brothelroute4 = 0
                                $ brothelcompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump brskipmenu
                "Farm ([farmcompletion]/4)":
                    menu faskipmenu:
                        "First Visit ([farmroute1]/1)":
                            if farmroute1 == 0:
                                $ farmroute1 = 1
                                $ farmcompletion += 1
                                $ completion += 1
                            else:
                                $ farmroute1 = 0
                                $ farmcompletion -= 1
                                $ completion -= 1
                        "Second Visit ([farmroute2]/1)":
                            if farmroute2 == 0:
                                $ farmroute2 = 1
                                $ farmcompletion += 1
                                $ completion += 1
                            else:
                                $ farmroute2 = 0
                                $ farmcompletion -= 1
                                $ completion -= 1
                        "Third Visit ([farmroute3]/1)":
                            if farmroute3 == 0:
                                $ farmroute3 = 1
                                $ farmcompletion += 1
                                $ completion += 1
                            else:
                                $ farmroute3 = 0
                                $ farmcompletion -= 1
                                $ completion -= 1
                        "Fourth Visit ([farmroute4]/1)":
                            if farmroute4 == 0:
                                $ farmroute4 = 1
                                $ farmcompletion += 1
                                $ completion += 1
                            else:
                                $ farmroute4 = 0
                                $ farmcompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump faskipmenu
                "Bakery ([bakerycompletion]/2)":
                    menu baskipmenu:
                        "First Visit ([bakeryroute1]/1)":
                            if bakeryroute1 == 0:
                                $ bakeryroute1 = 1
                                $ bakerycompletion += 1
                                $ completion += 1
                            else:
                                $ bakeryroute1 = 0
                                $ bakerycompletion -= 1
                                $ completion -= 1
                        "Second Visit ([bakeryroute2]/1)":
                            if bakeryroute2 == 0:
                                $ bakeryroute2 = 1
                                $ bakerycompletion += 1
                                $ completion += 1
                            else:
                                $ bakeryroute2 = 0
                                $ bakerycompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump baskipmenu
                "Forest ([forestcompletion]/2)":
                    menu foskipmenu:
                        "First Visit ([forestroute1]/1)":
                            if forestroute1 == 0:
                                $ forestroute1 = 1
                                $ forestcompletion += 1
                                $ completion += 1
                            else:
                                $ forestroute1 = 0
                                $ forestcompletion -= 1
                                $ completion -= 1
                        "Second Visit ([forestroute2]/1)":
                            if forestroute2 == 0:
                                $ forestroute2 = 1
                                $ forestcompletion += 1
                                $ completion += 1
                            else:
                                $ forestroute2 = 0
                                $ forestcompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump foskipmenu
                "Bar ([barcompletion]/4)":
                    menu barskipmenu:
                        "First Visit ([barroute1]/1)":
                            if barroute1 == 0:
                                $ barroute1 = 1
                                $ barcompletion += 1
                                $ completion += 1
                            else:
                                $ barroute1 = 0
                                $ barcompletion -= 1
                                $ completion -= 1
                        "Second Visit ([barroute2]/1)":
                            if barroute2 == 0:
                                $ barroute2 = 1
                                $ barcompletion += 1
                                $ completion += 1
                            else:
                                $ barroute2 = 0
                                $ barcompletion -= 1
                                $ completion -= 1
                        "Third Visit ([barroute3]/1)":
                            if barroute3 == 0:
                                $ barroute3 = 1
                                $ barcompletion += 1
                                $ completion += 1
                            else:
                                $ barroute3 = 0
                                $ barcompletion -= 1
                                $ completion -= 1
                        "Fourth Visit ([barroute4]/1)":
                            if barroute4 == 0:
                                $ barroute4 = 1
                                $ barcompletion += 1
                                $ completion += 1
                            else:
                                $ barroute4 = 0
                                $ barcompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump barskipmenu
                "Castle ([castlecompletion]/3)":
                    menu castleskipmenu:
                        "First Visit ([castleroute1rewrite]/1)":
                            if castleroute1rewrite == 0:
                                $ castleroute1rewrite = 1
                                $ castlecompletion += 1
                                $ completion += 1
                            else:
                                $ castleroute1rewrite = 0
                                $ castlecompletion -= 1
                                $ completion -= 1
                        "Second Visit ([castleroute2]/1)":
                            if castleroute2 == 0:
                                $ castleroute2 = 1
                                $ castlecompletion += 1
                                $ completion += 1
                            else:
                                $ castleroute2 = 0
                                $ castlecompletion -= 1
                                $ completion -= 1
                        "Third Visit ([castleroute3]/1)":
                            if castleroute3 == 0:
                                $ castleroute3 = 1
                                $ castlecompletion += 1
                                $ completion += 1
                            else:
                                $ castleroute3 = 0
                                $ castlecompletion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump castleskipmenu
                "Act 2 ([act2completion]/8)":
                    menu act2skipmenu:
                        "Arrival ([dawnroute1]/1)":
                            if dawnroute1 == 0:
                                $ dawnroute1 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ dawnroute1 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Physical Training ([crystal1a]/1)":
                            if crystal1a == 0:
                                $ crystal1a = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal1a = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Magical Training ([crystal1b]/1)":
                            if crystal1b == 0:
                                $ crystal1b = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal1b = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Cadia Falls ([crystal2]/1)":
                            if crystal2 == 0:
                                $ crystal2 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal2 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "[but] ([crystal3]/1)":
                            if crystal3 == 0:
                                $ crystal3 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal3 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "[pen] ([crystal4]/1)":
                            if crystal4 == 0:
                                $ crystal4 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal4 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Back to Arcadia ([crystal5]/1)":
                            if crystal5 == 0:
                                $ crystal5 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal5 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Back to Arcadia (The Other One) ([crystal6]/1)":
                            if crystal6 == 0:
                                $ crystal6 = 1
                                $ act2completion += 1
                                $ completion += 1
                            else:
                                $ crystal6 = 0
                                $ act2completion -= 1
                                $ completion -= 1
                        "Back":
                            jump skipmenu
                    jump act2skipmenu
                "Back":
                    jump cheatmenu  
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return 
    jump cheatmenu
label settings:
    $ phoneenabled = 0
    if worldmap == 0:
        show screen phone_screen
    menu settingsmenu:
        "Change Phone Background":
            menu phonebgmenu:
                "Default BG":
                    $ phonebg = 1
                "Under the Sea":
                    $ phonebg = 2
                "Ominous Moon":
                    $ phonebg = 3
                "Grand Journey":
                    $ phonebg = 4
                "Back":
                    jump settingsmenu
            jump phonebgmenu
        "Toggle Money and Day Count: [uiicons]":
            if uiicons == "On":
                $ uiicons = "Off"
            else:
                $ uiicons = "On"
            jump settingsmenu
        "Toggle Sex Scene Camera Movements: [cameramove]":
            if cameramove == "On":
                $ cameramove = "Off"
            else:
                $ cameramove = "On"
            jump settingsmenu
        "Toggle Text Sound: [beep_enabled]":
            if beep_enabled == "On":
                $ beep_enabled = "Off"
            else:
                $ beep_enabled = "On"
            jump settingsmenu
        "Back":
            $ phoneenabled = 1
            if worldmap >= 1:
                call screen worldmap with dissolve
            call screen phone_screen with dissolve   
            return 
    #jump settingsmenu  
 

################################################################################
## Initialization
################################################################################

init offset = -1
label splashscreen:
    scene black
    pause 0.5
    show image "splash1" with dissolve
    pause 1.5
    show image "splash2" with dissolve
    pause 3.0
    return

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    color "#f00"
    outlines [ (2, "#000", 2, 2) ]
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 95
    style_prefix "say"
    window id "window":
        xalign 0.5
        if textbox == 2:
            background None
        if textbox == 3:
            yalign .1
            background None
        if textbox == 4:
            yalign .85
            background None
        if textbox == 5:
            yalign .5
            background None
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what":
            size persistent.text_size

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    #if not renpy.variant("small"):
    #    add SideImage() xalign 0.0 yalign 1.0
## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    zorder 105
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    modal True
    zorder 102
    style_prefix "choice"
    if bigmenu == 1:
        on "show" action Function(disable_rollback)
        on "hide" action Function(enable_rollback)
        side "c r":
            area (380, 25, 1250, 800)
            viewport id "big_menu":
                mousewheel True
                draggable True
                side_yfill True
                vbox:
                    for i in items:
                        $ disabled = i.kwargs.get("disabled", False)
                        textbutton i.caption action i.action sensitive not disabled
            vbar value YScrollValue("big_menu")
    else:
        vbox:
            for i in items:
                $ disabled = i.kwargs.get("disabled", False)
                textbutton i.caption action i.action sensitive not disabled

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "click1.ogg"
style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu and persistent.quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 91
        yalign 0.5

        spacing 50


        if main_menu:

            textbutton _("New Game") action Start()

        else:

            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Settings") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        #textbutton _("Credits") action ShowMenu("about")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        #
        #    ## Help isn't necessary or relevant to mobile devices.
        #    textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
image mainmenuwater1:
    "mainmenuwater1.png"
    alpha 1
    linear 0.1
    linear 1 alpha 0
    linear 0.1
    linear 1.1 alpha 1.0
    repeat
image mainmenuwater2:
    "mainmenuwater2.png"
    alpha 0
    linear 0.1
    linear 1.2 alpha 1
    linear 0.1
    linear 1.3 alpha 0
    repeat
label before_main_menu:
    play ambience1 ambiencenight
    play ambience2 river volume 0.5
    play ambience3 wind volume 0.5
screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    image "mainmenuwater1"
    image "mainmenuwater2"

    imagemap:
        ground "MainMenuUI.png"
        hover "MainMenuUIh.png"

        hotspot (129, 372, 329, 81) action Start() hovered [ Play ("sound", "click1.ogg")]

        hotspot (126, 455, 332, 77) action ShowMenu("load") hovered [ Play ("sound", "click1.ogg")]

        hotspot (105, 531, 365, 81) action ShowMenu("preferences") hovered [ Play ("sound", "click1.ogg")]

        hotspot (123, 610, 339, 91)action Quit(confirm=not main_menu) hovered [ Play ("sound", "click1.ogg")]

    if steam == 0:
        imagebutton:
            idle "MainMenuP.png"
            hover "MainMenuPH.png"
            yalign 0.99
            xalign 0.99
            action OpenURL("https://www.patreon.com/TwistedScarlett") hovered Play("sound", "click1.ogg")

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action If(renpy.get_screen("save"), true=Show("savegameName", accept=FileSave(slot)), false=FileLoad(slot))


                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("%d %B - {#file_time}%H:%M"), empty=_("")):
                            style "slot_time_text"

                        if FileSaveName(slot):
                                $ fn = FileSaveName(slot)
                                if fn and ("-" in fn):
                                    $ y = fn.split("-")
                                text fn:
                                    style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5

## BadMustard's code Start (second section)
screen savegameName(accept=NullAction()):

    modal True
    add "black" alpha 0.8
    style_prefix "savegameName"

    frame:
        has vbox:
            xalign 0.5
            spacing 20

        label _("Save Name"):
            text_color gui.text_color
            xalign 0.5

        null height 10

        input size 40 color gui.hover_color default store.save_name changed Namer length 22 allow allowedChars:
            yalign 1.0
            xalign 0.5
            xysize (550, 40)

        textbutton _("{u}Save the Game{/u}"):
            xalign 0.5
            keysym ['K_RETURN', 'K_KP_ENTER']
            action [accept, (Hide("savegameName"))]

init python:
    import string
    def Namer(name):
        store.save_name = name

# Define characters that can be typed in. We allow:
# - Uppercase letters (In ascii_letters)
# - Lowercase letters (In ascii_letters)
# - Numbers 0 to 9 (In digits)
# - space, dash
define allowedChars = string.ascii_letters + string.digits + " -"
default persistent.saveName = True

style savegameName_frame:
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0.5

style savegameName_frame:
    variant "touch"
    padding gui.confirm_frame_borders.padding
    xsize 650
    xalign 0.5
    yalign 0
    ypos 50
## BadMustard's code Stop (second section)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():
    zorder 95
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    style_prefix "radio"
                    label _("Quick Menu")
                    textbutton _("Enabled") action SetField(persistent,"quick_menu", True)
                    textbutton _("Disabled") action SetField(persistent,"quick_menu", False)
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("Englist") action Language(None)
                    textbutton _("Chinese") text_font "SourceHanSansLite.ttf" action Language("chinese")
                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            
            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Size ([persistent.text_size]/45)")
                    bar value FieldValue(persistent, "text_size", offset=20, range=25, style="slider")
                    textbutton _("Set to default") action InvertSelected(SetVariable("persistent.text_size", gui.text_size))

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
