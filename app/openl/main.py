from .depen_tree import open_dependency_tree

'''
entry point for the open command(named openl to not cause conflicts with python's open keyword).
'''

def openl(file):
    if file=="dependency_tree.json":
        open_dependency_tree()