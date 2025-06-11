from pyecore.resources import global_registry
from .dictionary import getEClassifier, eClassifiers
from .dictionary import name, nsURI, nsPrefix, eClass
from .dictionary import DictionaryRoot, Word, WordClass, Stem, IDictionaryEl


from . import dictionary
from .. import semantics


__all__ = ['DictionaryRoot', 'Word', 'WordClass', 'Stem', 'IDictionaryEl']

eSubpackages = []
eSuperPackage = semantics
dictionary.eSubpackages = eSubpackages
dictionary.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [dictionary] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
