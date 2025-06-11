"""Definition of meta model 'artifact'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from src_gen.semantics.semantics import INamable, IContainable, IIdentifiable, IDataComponent


name = 'artifact'
nsURI = 'http://www.xixum.org/semantics/artifact'
nsPrefix = 'artifact'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class ITextBodyEl(EObject, metaclass=MetaEClass):

    chunk = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, chunk=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if chunk is not None:
            self.chunk = chunk


@abstract
class IPropertyable(EObject, metaclass=MetaEClass):

    property = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, property=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if property:
            self.property.extend(property)


@abstract
class Token(IDataComponent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Artifact(INamable, IPropertyable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Word(Token):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    word = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, word=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if word is not None:
            self.word = word


class Number(Token):

    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class NamedIdentity(Token):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


@abstract
class SpreatSheetComponent(IPropertyable, IDataComponent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Document(Artifact):

    kg_reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, kg_reference=None, **kwargs):

        super().__init__(**kwargs)

        if kg_reference is not None:
            self.kg_reference = kg_reference


class Sheet(IDataComponent, SpreatSheetComponent):

    table = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, table=None, **kwargs):

        super().__init__(**kwargs)

        if table:
            self.table.extend(table)


class Table(IDataComponent, SpreatSheetComponent):

    row = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, row=None, **kwargs):

        super().__init__(**kwargs)

        if row:
            self.row.extend(row)


class Row(IDataComponent, SpreatSheetComponent):

    index = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    cell = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, cell=None, index=None, **kwargs):

        super().__init__(**kwargs)

        if index is not None:
            self.index = index

        if cell:
            self.cell.extend(cell)


class Cell(IDataComponent, SpreatSheetComponent):

    column = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    rowSpan = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    colSpan = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    paragraph = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, column=None, rowSpan=None, colSpan=None, paragraph=None, **kwargs):

        super().__init__(**kwargs)

        if column is not None:
            self.column = column

        if rowSpan is not None:
            self.rowSpan = rowSpan

        if colSpan is not None:
            self.colSpan = colSpan

        if paragraph:
            self.paragraph.extend(paragraph)


class Paragraph(ITextBodyEl, IIdentifiable, IDataComponent):

    sentence = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, sentence=None, **kwargs):

        super().__init__(**kwargs)

        if sentence:
            self.sentence.extend(sentence)


class Heading(ITextBodyEl, IIdentifiable, IDataComponent):

    sentence = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, sentence=None, **kwargs):

        super().__init__(**kwargs)

        if sentence:
            self.sentence.extend(sentence)


class Sentence(IDataComponent, IContainable):

    token = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, token=None, **kwargs):

        super().__init__(**kwargs)

        if token:
            self.token.extend(token)


class TextDocument(Document):

    blockElement = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, blockElement=None, **kwargs):

        super().__init__(**kwargs)

        if blockElement:
            self.blockElement.extend(blockElement)


class SpreadSheet(Document):

    sheet = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, sheet=None, **kwargs):

        super().__init__(**kwargs)

        if sheet:
            self.sheet.extend(sheet)


class RichTextDocument(TextDocument):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
