# zz_cn_credit.rpy —— 在原有开机两张图(splashscreen)之后，追加一次“汉化组致谢图”

define CN_CREDIT_SHOW_ONCE_PER_INSTALL = False   
define CN_CREDIT_FORCE_ZH = False               


init python early:
    renpy.session.setdefault("cn_credit_shown", False)   
    renpy.session.setdefault("cn_credit_pending", False) 


default persistent.cn_credit_seen_ever = False

screen cn_credit_once():
    modal True
    add "zz_credit.png"            # 图片路径
    key "mouseup_1" action Return(True)
    key "K_RETURN" action Return(True)
    key "K_SPACE" action Return(True)
    timer 2.5 action Return(True)  # 2.5 秒自动关闭

# ================== 入口：主菜单出现前（在 splashscreen 之后调用） ==================
label before_main_menu:

    # 1) 终身只弹一次
    if CN_CREDIT_SHOW_ONCE_PER_INSTALL and persistent.cn_credit_seen_ever:
        return

    # 2) 本次启动已显示过
    if renpy.session["cn_credit_shown"] and not renpy.session["cn_credit_pending"]:
        return

    # 3) 如需强制切中文
    if CN_CREDIT_FORCE_ZH and getattr(preferences, "language", None) != "schinese" and not renpy.session["cn_credit_pending"]:
        $ renpy.session["cn_credit_pending"] = True
        $ renpy.change_language("schinese")
        return 

    # 4) 显示一次致谢图
    call screen cn_credit_once
    $ renpy.session["cn_credit_shown"] = True
    $ renpy.session["cn_credit_pending"] = False

    if CN_CREDIT_SHOW_ONCE_PER_INSTALL:
        $ persistent.cn_credit_seen_ever = True
        $ renpy.save_persistent()

    return
