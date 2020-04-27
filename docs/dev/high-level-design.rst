High Level Design
=================

Creation and expansion of code should be document-driven-development_ first, followed by test-driven-development_.

|cla| "Dream" Core Features
---------------------------

Dictionary
~~~~~~~~~~

- Document

  - Phonology using IPA_
  - Able to include language's orthography

    - User can define their language's version of alphabetical-order

  - Word pronunciation, definitions, and their part of speech

    - Written in language's orthography if applicable
    - Pronunciation in IPA_ or latin alphabet

- Search based on

  - Definition
  - Pronunciation
  - Part of speech

- Display added words in something like a table

- Can change sort order of search and word list

    - Alphabetical order from pronunciation
    - Alphabetical order from definition
    - User-defined alphabetical order
    - Part of speech

Grammar
~~~~~~~

- Define language's grammar rules using

  - Regex
  - Human-readable syntax

- Searchable
- Created rules displayed in user-defined order

Tutorials
~~~~~~~~~

- How to use program's features
- Basic linguistic concepts used in making conLangs

Features for Demo
-----------------

Dictionary
~~~~~~~~~~

- Phonology
- Word definitions
- Word pronunciation

  - In IPA and/or English

- What part of speech a word belongs to

- Search by definition or pronunciation

Grammar
~~~~~~~



.. _document-driven-development: https://gist.github.com/zsup/9434452
.. _test-driven-development: https://www.agilealliance.org/glossary/tdd/#q=~(infinite~false~filters~(postType~(~'page~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'tdd))~searchTerm~'~sort~false~sortDirection~'asc~page~1)
.. _IPA: https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
