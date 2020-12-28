# Types Lab

In this lab, we learn about types by writing functions whose inputs and outputs 
are English parts of speech. Once you finish, you will be able to generate
syntactically-correct phrases which you can use to write auto-poetry like:

Roses are red<br>
Violets are blue<br>
Evenings are poisonous<br>
And so are you.<br>

I used to have a formative scratch<br>
Until i swapped it for an icy latch.

There once was a person named pete<br>
Who owned an optical cleat.<br>
He widely canvassed it,<br>
And then he canvased it,<br>
Until it turned into a beat.


## Installation

After cloning this repository, install its dependencies:

```
$ pip install requirements.txt
```

## Usage

- `vocabulary.py` has a bunch of functions for picking random words.
` `grammatical_types.py` defines types like `Noun`, `Adjective`, and `TransitiveVerb`.
- `grammar.py` has a bunch of functions for combining and transforming
  grammatical types. These are unfinished; it's your job to write them.
- `poetry.py` has functions for writing beautiful auto-poems. Once `grammar.py` 
  is complete, try running `python poetry.py`.
