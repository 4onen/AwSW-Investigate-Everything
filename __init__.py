
from renpy import ast, python, store

from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod

def chapter1inv_skip(ml):
    ( ml.find_label('investigation')
        .search_menu("I guess so.")
        .add_choice("Don't say anything. Just let me draw conclusions.", jump='invevrything_four_c1skip', condition='persistent.c1invhigh')
    )

    ( ml.find_label('quest6')
        .search_say("Hm. I think that's about everything.")
        .link_behind_from('invevrything_four_c1skip_end')
    )

def chapter2inv(ml):
    c2inv_sec_menu = ( ml
        .find_label('chapter2sections')
        .search_if('chapter2sectionsplayed == 1')
        .branch()
        .search_menu()
        .node
    )

    def condition_closure(hook):
        ast.next_node(hook.old_next)
        if store.persistent.invevrything_four_chapter2_limit != True:
            valid = sum((python.py_eval(condition) for (_label, condition, _block) in c2inv_sec_menu.items))
            if valid > 1:
                ast.next_node(c2inv_sec_menu)
        return True

    c2inv_cont = ml.find_label('chap2cont').node

    hook = modast.ASTHook(("InvestigateEverything", 20), condition_closure, c2inv_cont)
    hook.old_next = c2inv_cont.next
    hook.next = hook.old_next
    c2inv_cont.next = hook

    condition = ml.find_label('chap2skip3').search_if('chap2clues == 2')
    ( condition
        .branch()
        .search_say("Well done, [player_name]. That gives us some solid points from which we can continue our investigation.")
        .link_from('invevrything_four_c2skip3')
        .hook_to(
            'invevrything_four_c2skip3_highinv',
            return_link=True,
            condition='chap2clues > 2',
        )
    )
    condition.add_entry(
        condition='chap2clues > 2',
        before='chap2clues == 2',
        jump='invevrything_four_c2skip3'
    )
    

def chapter3inv(ml):
    if_block = ( ml
        .find_label('c3sections')
        .search_if('c3sectionsplayed == 1')
    )

    c3inv_sec_menu = ( if_block
        .branch()
        .search_menu("Stay inside and call the police.")
        .branch()
        .search_menu()
        .node
    )

    def condition_closure(hook):
        ast.next_node(hook.old_next)
        if store.persistent.invevrything_four_chapter3_limit != True:
            valid = sum((python.py_eval(condition) for (_label, condition, _block) in c3inv_sec_menu.items))
            if valid > 1:
                ast.next_node(c3inv_sec_menu)
        return True

    elsebranch = if_block.branch_else()
    hook = modast.ASTHook(("InvestigateEverything", 30), condition_closure)
    hook.old_next = elsebranch.first().node
    hook.next = hook.old_next
    elsebranch._add_node_front(hook)

    condition = ml.find_label('c3go').search_if('c3clues == 2')
    ( condition
        .branch()
        .search_say("You did great today, [player_name]. The police department is glad to have you on our side.")
        .link_from('invevrything_four_c3go_highinv')
    )
    condition.add_entry(
        condition='c3clues > 2',
        before='c3clues == 2',
        jump='invevrything_four_c3go_highinv'
    )

def chapter3archiveinv(ml):
    label = ml.find_label('c3arcques')

    c3arcinv_sec_menu = ( label
        .search_if('c3arcquesx <= 1')
        .branch()
        .search_menu()
        .add_choice("That's everything I want to do here.", condition='c3arcquesx > 0 and persistent.invevrything_four_police_archive_limit != True', jump="invevrything_four_c3arcques_complete")
        .node
    )

    def condition_closure(hook):
        ast.next_node(hook.old_next)
        if store.persistent.invevrything_four_police_archive_limit != True:
            valid = sum((python.py_eval(condition) for (_label, condition, _block) in c3arcinv_sec_menu.items))
            if valid > 1:
                ast.next_node(c3arcinv_sec_menu)
        return True

    hook = modast.ASTHook(("InvestigateEverything", 31), condition_closure, label.node, "InvestigateEverythingChap3Arc")
    hook.old_next = label.node.next
    label.node.next = hook


def chapter4inv(ml):
    if_block = ( ml
        .find_label('c4sections')
        .search_if('c4sectionsplayed == 1')
    )

    c4inv_sec_menu = ( if_block
        .branch()
        .search_menu()
        .node
    )

    def condition_closure(hook):
        ast.next_node(hook.old_next)
        if store.persistent.invevrything_four_chapter4_limit != True:
            valid = sum((python.py_eval(condition) for (_label, condition, _block) in c4inv_sec_menu.items))
            if valid > 1:
                ast.next_node(c4inv_sec_menu)
        return True

    elsebranch = if_block.branch_else()
    hook = modast.ASTHook(("InvestigateEverything", 40), condition_closure)
    hook.old_next = elsebranch.first().node
    hook.next = hook.old_next
    elsebranch._add_node_front(hook)

    ( ml.find_label('c4rest')
        .search_scene('office')
        .hook_to('c4postsections', return_link=False) 
    )


def chapter1char(ml):
    c1if = (
        ml.find_label('chapter1chars')
        .search_if('chapter1csplayed == 1')
    )

    c1if.branch().search_scene('black').link_from('invevrything_four_c1char')
    c1if.add_entry('not store.persistent.invevrything_four_chapter1_character_limit', jump='invevrything_four_c1char', before='True')

def chapter2char(ml):
    c2fadeif = (
        ml.find_label("chapter2chars")
        .search_if("chapter2csplayed == 1")
    )

    c2fadeif.branch().search_scene('black').link_from('invevrything_four_c2fade')
    c2fadeif.add_entry('not store.persistent.invevrything_four_chapter2_character_limit', jump='invevrything_four_c2fade', before='True')

    c2if = (
        c2fadeif
        .search_if("chapter2csplayed == 1")
    )

    c2if.branch().search_say("(Nothing going on today. Guess I can do whatever.)").link_from('invevrything_four_c2char')
    c2if.add_entry('not store.persistent.invevrything_four_chapter2_character_limit', jump='invevrything_four_c2char', before='True')

def chapter3char(ml):
    c3fadeif = (
        ml.find_label("chapter3chars")
        .search_if("c3csplayed == 1")
    )

    c3fadeif.branch().search_scene('black').link_from('invevrything_four_c3fade')
    c3fadeif.add_entry('not store.persistent.invevrything_four_chapter3_character_limit', jump='invevrything_four_c3fade', before='True')

    c3alldeadif = (
        c3fadeif
        .search_if("remyavailable == False")
    )

    c3alldeadif.link_behind_from('invevrything_four_c3charnotalldead')
        
    ( c3alldeadif.branch()
        .search_if("bryceavailable == False").branch()
        .search_if("adineavailable == False").branch()
        .search_if("adine1unplayed == False").branch()
        .search_if("annaavailable == False").branch()
        .search_if("loremavailable == False").branch()
        .search_if("katsuavailable == False").branch()
        .hook_to('invevrything_four_c3charnotalldead', return_link=False, condition='not store.persistent.invevrything_four_chapter3_character_limit')
    )

    c3if = (
        c3alldeadif
        .search_if("c3csplayed == 1")
    )

    c3if.branch().search_say("(Looks like I have some free time today.)").link_from('invevrything_four_c3char')
    c3if.add_entry('not store.persistent.invevrything_four_chapter3_character_limit', jump='invevrything_four_c3char', before='True')

    ml.find_label('chapter3chars2').hook_to('chapter3chars', return_link=False, condition='c3csplayed > 1 and not store.persistent.invevrything_four_chapter3_character_limit')

def chapter4char(ml):
    c4fadeif = (
        ml.find_label("chapter4chars")
        .search_if("c4csplayed == 1")
    )

    c4fadeif.branch().search_scene('black').link_from('invevrything_four_c4fade')
    c4fadeif.add_entry('not store.persistent.invevrything_four_chapter4_character_limit', jump='invevrything_four_c4fade', before='True')

    c4if = (
        c4fadeif
        .search_if("c4csplayed == 1")
    )

    c4if.branch().search_say("(Another free day. Yay me.)").link_from('invevrything_four_c4char')
    c4if.add_entry('not store.persistent.invevrything_four_chapter4_character_limit', jump='invevrything_four_c4char', before='True')

def chapter_chars(ml):
    chapter1char(ml)
    chapter2char(ml)
    chapter3char(ml)
    chapter4char(ml)

@loadable_mod
class MyAwSWMod(Mod):
    name = "Investigate Everything"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @classmethod
    def mod_load(cls):
        import jz_magmalink as ml

        ml.register_mod_settings(cls, screen='invevrything_four_modsettings')
        chapter1inv_skip(ml)
        chapter2inv(ml)
        chapter3inv(ml)
        chapter3archiveinv(ml)
        chapter4inv(ml)
        chapter_chars(ml)

    @staticmethod
    def mod_complete():
        pass
