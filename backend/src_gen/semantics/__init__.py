from pyecore.resources import global_registry
from .semantics import getEClassifier, eClassifiers
from .semantics import name, nsURI, nsPrefix, eClass
from .semantics import INamable, IDataComponent, Property, IValueComponent, StringProperty, IntProperty, FloatProperty, BoolProperty, ListProperty, MapProperty, Pair, IIdentifiable, IAtomic, IAggregated, IIterable, IContainable, IPropertyable


from .artifact import Token, NonVoidTag, Document, ITextBodyEl, Styleable, RowBlockEl, Number, Paragraph, Word, Cell, MetaElement, Artifact, GridBlockEl, Sentence, XMLdocument, RowContainer, CSS_Style, PlainText
from .infrastructure import Environment, PathEl, ISubDir, Domain, Device, ILocation
from .context import Relation, State, Class, Event, Time, IRefferable, IChronological, Entity, ContextRoot
from .dictionary import LexicalWord, Stem, DictionaryRoot, WordClass
from .ruleset import RuleRoot, Predicate, Token
from .knowledgegraph import INode, KGrelation, KGchunk, KGentity, KGdocument, KGroot
from . import semantics
from . import artifact

from . import infrastructure

from . import context

from . import dictionary

from . import ruleset

from . import knowledgegraph


__all__ = ['INamable', 'IDataComponent', 'Property', 'IValueComponent', 'StringProperty', 'IntProperty', 'FloatProperty', 'BoolProperty',
           'ListProperty', 'MapProperty', 'Pair', 'IIdentifiable', 'IAtomic', 'IAggregated', 'IIterable', 'IContainable', 'IPropertyable']

eSubpackages = [artifact, infrastructure, context, dictionary, ruleset, knowledgegraph]
eSuperPackage = None
semantics.eSubpackages = eSubpackages
semantics.eSuperPackage = eSuperPackage

Paragraph.sentence.eType = Sentence
Sentence.token.eType = Token
Word.word.eType = LexicalWord
Number.value.eType = IAtomic
PlainText.blockElement.eType = ITextBodyEl
PlainText.rowblockel.eType = RowBlockEl
XMLdocument.metaelement.eType = MetaElement
GridBlockEl.row.eType = RowContainer
RowBlockEl.gridblockel.eType = GridBlockEl
RowBlockEl.paragraph.eType = Paragraph
RowContainer.cell.eType = Cell
Cell.rowblockel.eType = NonVoidTag
Styleable.css_style.eType = CSS_Style
NonVoidTag.rowblockel.eType = RowBlockEl
Device.subdir.eType = ISubDir
PathEl.isubdir.eType = ISubDir
PathEl.artifact.eType = Artifact
Domain.subdir.eType = ISubDir
Environment.location.eType = ILocation
ContextRoot.entity.eType = Entity
ContextRoot.event.eType = Event
ContextRoot.time.eType = Time
ContextRoot.relation.eType = Relation
ContextRoot.class_.eType = Class
Entity.state.eType = State
IChronological.synchronous.eType = IChronological
DictionaryRoot.wordclass.eType = WordClass
DictionaryRoot.word.eType = LexicalWord
LexicalWord.ofType.eType = WordClass
LexicalWord.baseform.eType = LexicalWord
LexicalWord.stem.eType = Stem
RuleRoot.token.eType = Token
RuleRoot.command.eType = Predicate
KGdocument.chunk.eType = KGchunk
KGroot.document.eType = KGdocument
KGroot.relation.eType = KGrelation
KGroot.entity.eType = KGentity
ListProperty.entry.eType = Property
MapProperty.entry.eType = Pair
Pair.key.eType = Property
Pair.value.eType = Property
IPropertyable.property.eType = Property
Document.kg_reference.eType = KGdocument
ITextBodyEl.chunk.eType = KGchunk
Entity.kg_entity.eType = KGentity
Entity.class_.eType = Class
Event.next.eType = Event
Event.previous.eType = Event
Event.previous.eOpposite = Event.next
Event.state.eType = State
Event.time.eType = Time
State.event.eType = Event
State.event.eOpposite = Event.state
Time.event.eType = Event
Time.event.eOpposite = Event.time
Relation.active_entity.eType = IRefferable
Relation.passive_entity.eType = IRefferable
Relation.kg_relation.eType = KGrelation
IChronological.after.eType = IChronological
IChronological.before.eType = IChronological
IChronological.before.eOpposite = IChronological.after
Class.abstract.eType = Class
Class.extension.eType = Class
Class.extension.eOpposite = Class.abstract
Class.entity.eType = Entity
Class.entity.eOpposite = Entity.class_
IRefferable.operation.eType = Relation
IRefferable.operation.eOpposite = Relation.passive_entity
IRefferable.command.eType = Relation
IRefferable.command.eOpposite = Relation.active_entity
Token.command.eType = Predicate
Token.operation.eType = Predicate
Predicate.activeToken.eType = Token
Predicate.activeToken.eOpposite = Token.command
Predicate.passiveToken.eType = Token
Predicate.passiveToken.eOpposite = Token.operation
KGdocument.context_ref.eType = Document
KGdocument.context_ref.eOpposite = Document.kg_reference
KGchunk.context_ref.eType = ITextBodyEl
KGchunk.context_ref.eOpposite = ITextBodyEl.chunk
KGentity.context_ref.eType = Entity
KGentity.context_ref.eOpposite = Entity.kg_entity
KGrelation.target_node.eType = INode
KGrelation.source_node.eType = INode
KGrelation.context_ref.eType = Relation
KGrelation.context_ref.eOpposite = Relation.kg_relation
INode.in_relation.eType = KGrelation
INode.in_relation.eOpposite = KGrelation.target_node
INode.out_relation.eType = KGrelation
INode.out_relation.eOpposite = KGrelation.source_node

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [semantics] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
