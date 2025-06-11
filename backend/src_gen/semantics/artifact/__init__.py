from pyecore.resources import global_registry
from .artifact import getEClassifier, eClassifiers
from .artifact import name, nsURI, nsPrefix, eClass
from .artifact import Artifact, Document, TextDocument, SpreadSheet, RichTextDocument, Sheet, Table, Row, Cell, Paragraph, Heading, ITextBodyEl, Sentence, Token, Word, Number, NamedIdentity, IPropertyable, SpreatSheetComponent


from . import artifact
from .. import semantics


__all__ = ['Artifact', 'Document', 'TextDocument', 'SpreadSheet', 'RichTextDocument', 'Sheet', 'Table', 'Row', 'Cell', 'Paragraph',
           'Heading', 'ITextBodyEl', 'Sentence', 'Token', 'Word', 'Number', 'NamedIdentity', 'IPropertyable', 'SpreatSheetComponent']

eSubpackages = []
eSuperPackage = semantics
artifact.eSubpackages = eSubpackages
artifact.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [artifact] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
