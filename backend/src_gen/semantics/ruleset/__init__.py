from pyecore.resources import global_registry
from .ruleset import getEClassifier, eClassifiers
from .ruleset import name, nsURI, nsPrefix, eClass
from .ruleset import RuleRoot, Token, Command, IRuleEl


from . import ruleset
from .. import semantics


__all__ = ['RuleRoot', 'Token', 'Command', 'IRuleEl']

eSubpackages = []
eSuperPackage = semantics
ruleset.eSubpackages = eSubpackages
ruleset.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [ruleset] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
