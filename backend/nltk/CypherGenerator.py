from pyecore.utils import dispatch
from semantics import Artifact, Document


class CypherGenerator(object):
    @dispatch
    def do_generate(self, o):
        print('Fallback for objects of kind ', o.eClass.name)

    @do_generate.register(Artifact)
    def writer_switch(self, o):
        print('Visiting a ', o.eClass.name, ' named ', o.name)

    @do_generate.register(Document)
    def book_switch(self, o):
        print('Reading a ', o.eClass.name, ' titled ', o.name)


# switch = LibrarySwitch()
# # assuming we have a Library instance in 'mylib'
# for obj in mylib.eAllContents():
#     switch.do_switch(obj)