import sys
sys.path.append("../")

from pyke.pyke import Pyke

def test_adding_tasks():
    pyke = Pyke()
    pyke.add_task("bla")
    pyke.add_task("blup")

    assert 2 == len(pyke.tasks)
