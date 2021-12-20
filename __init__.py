
from renpy import ast, python

from modloader import modinfo
from modloader.modclass import Mod, loadable_mod

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
        valid = sum((python.py_eval(condition) for (_label, condition, _block) in c2inv_sec_menu.items))
        if valid > 1:
            ast.next_node(c2inv_sec_menu)
        return True

    c2inv_cont = ml.find_label('chap2cont').node

    ml.utils._create_hook(node_from=c2inv_cont, node_to=c2inv_sec_menu, func=condition_closure)

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
        valid = sum((python.py_eval(condition) for (_label, condition, _block) in c3inv_sec_menu.items))
        if valid > 1:
            ast.next_node(c3inv_sec_menu)
        return True

    elsebranch = if_block.branch_else()
    old_next = elsebranch.first().node
    elsebranch._add_node_front(ml.utils._create_hook(node_to=c3inv_sec_menu, func=condition_closure, old_next=old_next))

def chapter3archiveinv(ml):
    label = ml.find_label('c3arcques')

    c3arcinv_sec_menu = ( label
        .search_if('c3arcquesx <= 1')
        .branch()
        .search_menu()
        .add_choice("That's everything I want to do here.", condition='c3arcquesx > 0', jump="invevrything_four_c3arcques_complete")
        .node
    )

    def condition_closure(hook):
        ast.next_node(hook.old_next)
        valid = sum((python.py_eval(condition) for (_label, condition, _block) in c3arcinv_sec_menu.items))
        if valid > 1:
            ast.next_node(c3arcinv_sec_menu)
        return True

    ml.utils._create_hook(node_from=label.node, func=condition_closure)

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
        valid = sum((python.py_eval(condition) for (_label, condition, _block) in c4inv_sec_menu.items))
        if valid > 1:
            ast.next_node(c4inv_sec_menu)
        return True

    elsebranch = if_block.branch_else()
    old_next = elsebranch.first().node
    elsebranch._add_node_front(ml.utils._create_hook(node_to=c4inv_sec_menu, func=condition_closure, old_next=old_next))

    ( ml.find_label('c4rest')
        .search_scene('office')
        .hook_to('c4postsections', return_link=False) 
    )


@loadable_mod
class MyAwSWMod(Mod):
    name = "Investigate Everything"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @classmethod
    def mod_load(cls):
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        chapter2inv(ml)
        chapter3inv(ml)
        chapter3archiveinv(ml)
        chapter4inv(ml)

    @staticmethod
    def mod_complete():
        pass
