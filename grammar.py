from vocabulary import starts_with_vowel_sound
from grammatical_types import (
    Noun, 
    PluralNoun,
    TransitiveVerb,
    IntransitiveVerb,
    PastTenseTransitiveVerb,
    PastTenseIntransitiveVerb,
    Adjective,
    Adverb, 
    NounPhrase,
    Determiner, 
    DeterminedNounPhrase,
    VerbPhrase, 
    Sentence
)

def pluralize(noun):
    "Noun -> PluralNoun"
    assert type(noun) == Noun
    if noun.endswith("s") or noun.endswith("ch") or noun.endswith("sh"):
        return PluralNoun(noun + 'es')
    else:
        return PluralNoun(noun + 's')

def past_tense_transitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    assert type(verb) == TransitiveVerb
    if verb.endswith('e'):
        return PastTenseTransitiveVerb(verb + 'd')
    else:
        return PastTenseTransitiveVerb(verb + 'ed')

def past_tense_intransitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    assert type(verb) == IntransitiveVerb
    if verb.endswith('e'):
        return PastTenseIntransitiveVerb(verb + 'd')
    else:
        return PastTenseIntransitiveVerb(verb + 'ed')

def noun_phrase(adjective, noun):
    "(Adjective, Noun) -> NounPhrase"
    assert isinstance(adjective, Adjective)
    assert isinstance(noun, NounPhrase)
    return NounPhrase(adjective + ' ' + noun)

def determine_noun_phrase(determiner, noun_phrase):
    "(Determiner, NounPhrase) -> Determined NounPhrase"
    assert isinstance(determiner, Determiner)
    assert isinstance(noun_phrase, NounPhrase)
    assert not isinstance(noun_phrase, DeterminedNounPhrase)
    return DeterminedNounPhrase(determiner + ' ' + noun_phrase)

def make_definite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    article = Determiner("the")
    return determine_noun_phrase(article, noun_phrase)

def make_indefinite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    if starts_with_vowel_sound(noun_phrase):
        article = Determiner("an")
    else:
        article = Determiner("a")
    return determine_noun_phrase(article, noun_phrase)

def verb_phrase_transitive(verb, noun_phrase):
    "(TransitiveVerb, NounPhrase) -> VerbPhrase"
    assert isinstance(verb, TransitiveVerb)
    assert isinstance(noun_phrase, NounPhrase)
    return VerbPhrase(verb + ' ' + noun_phrase)

def verb_phrase(adverb, verb_phrase):
    "(Adverb, VerbPhrase) -> VerbPhrase"
    assert isinstance(adverb, Adverb)
    assert isinstance(verb_phrase, VerbPhrase)
    return VerbPhrase(adverb + " " + verb_phrase)
