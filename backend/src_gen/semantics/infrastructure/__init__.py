from pyecore.resources import global_registry
from .infrastructure import getEClassifier, eClassifiers
from .infrastructure import name, nsURI, nsPrefix, eClass
from .infrastructure import Device, PathEl, Domain, ISubDir, IInfrastructureEl, Environment, ILocation, ILocalLocation, IWebLocation


from . import infrastructure
from .. import semantics


__all__ = ['Device', 'PathEl', 'Domain', 'ISubDir', 'IInfrastructureEl',
           'Environment', 'ILocation', 'ILocalLocation', 'IWebLocation']

eSubpackages = []
eSuperPackage = semantics
infrastructure.eSubpackages = eSubpackages
infrastructure.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [infrastructure] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
