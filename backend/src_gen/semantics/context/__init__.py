from pyecore.resources import global_registry
from .context import getEClassifier, eClassifiers
from .context import name, nsURI, nsPrefix, eClass
from .context import ContextRoot, Entity, Event, State, Time, AbsTime, RelativeTime, Relation, IContextEl, IChronological, PysicalE, VirtualE, Class, IRefferable


from . import context
from .. import semantics


__all__ = ['ContextRoot', 'Entity', 'Event', 'State', 'Time', 'AbsTime', 'RelativeTime',
           'Relation', 'IContextEl', 'IChronological', 'PysicalE', 'VirtualE', 'Class', 'IRefferable']

eSubpackages = []
eSuperPackage = semantics
context.eSubpackages = eSubpackages
context.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [context] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
