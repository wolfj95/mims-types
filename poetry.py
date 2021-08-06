from vocabulary import random_word, rhyming_pair, get_meter
from grammar import *
from grammatical_types import *

def love_poem():
    "() -> Poem"
    poem = Poem() 
    poem.append("roses are red")
    poem.append("violets are blue")
    poem.append(pluralize(random_word(Noun)) + " are " + random_word(Adjective))
    poem.append("and so are you.")
    return poem

def couplet():
    "() -> Poem"
    poem = Poem() 
    first_noun, second_noun = rhyming_pair(Noun, Noun, meter=Meter("1"))
    first_adjective = random_word(Adjective, meter=Meter("100"))
    first_np = make_indefinite(noun_phrase(first_adjective, first_noun))
    second_adjective = random_word(Adjective, meter=Meter("10"))
    second_np = make_indefinite(noun_phrase(second_adjective, second_noun))
    poem.append("I used to have " + first_np)
    poem.append("Until I swapped it for " + second_np + ".")
    return poem
    
def limerick(name, subjective_pronoun):
    "str, str -> Poem"
    noun0, noun1 = random_word(Noun, count=2, rhymes_with=name)
    adjective = random_word(Adjective, meter=Meter("100"))
    adverb = random_word(Adverb, meter=Meter("10"))
    verb0, verb1 = rhyming_pair(TransitiveVerb, TransitiveVerb, meter=Meter("10"))
    object_pronoun = Pronoun("it")

    np0 = make_indefinite(noun_phrase(adjective, noun0))
    np1 = make_indefinite(noun1)
    verb0 = past_tense_transitive(verb0)
    verb1 = past_tense_transitive(verb1)
    vp0 = verb_phrase(adverb, verb_phrase_transitive(verb0, object_pronoun))
    vp1 = verb_phrase_transitive(verb1, object_pronoun)

    poem = Poem() 
    poem.append("there once was a person named " + name)
    poem.append("who owned " + np0 + ".")
    poem.append(subjective_pronoun + " " + vp0 + ",") 
    poem.append("and then " + subjective_pronoun + " " + vp1 + ",")
    poem.append("until it turned into " + np1 + ".")
    return poem
