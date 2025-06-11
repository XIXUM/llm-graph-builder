from pyecore.resources import global_registry
from .knowledgegraph import getEClassifier, eClassifiers
from .knowledgegraph import name, nsURI, nsPrefix, eClass
from .knowledgegraph import Document, Chunk, Entity, KGroot, Relation, INode


from . import knowledgegraph
from .. import semantics


__all__ = ['Document', 'Chunk', 'Entity', 'KGroot', 'Relation', 'INode']

eSubpackages = []
eSuperPackage = semantics
knowledgegraph.eSubpackages = eSubpackages
knowledgegraph.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [knowledgegraph] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
