High Level Design
=================

Creation and expansion of code should be document-driven-development_ first, followed by test-driven-development_.

|cla| "Dream" Core Features
---------------------------

Dictionary
~~~~~~~~~~

* Document

  * Phonetic inventory using IPA_

  * Able to include language's orthography

    * User can define their language's version of alphabetical-order

  * Word pronunciation, definitions, and their syntax

    * Written in language's orthography if applicable

    * Pronunciation in IPA_ or latin alphabet

* Search based on

  * Definition

  * Pronunciation

  * Syntax

* Display added words in some sort of table or list

* Can change sort order of search and word list

  * Alphabetical order from pronunciation

  * Alphabetical order from definition

  * User-defined alphabetical order

  * Part of speech

Grammar
~~~~~~~

* Define language's grammar rules using

  * Regex

  * Human-readable syntax

* Searchable

* Created rules displayed in user-defined order

  * Nestable

* Apply rules to an entire passage to conjugate

Tutorials
~~~~~~~~~

* How to use program's features

* Basic linguistic concepts used in making conLangs

Features for Demo
-----------------

Dictionary Demo
~~~~~~~~~~~~~~~~

* Phonetic Inventory

* Word definitions

* Word pronunciation

  * In IPA and/or English

* What part of speech a word belongs to

* Search by definition or pronunciation

Grammar Demo
~~~~~~~~~~~~

* Define rules using Regex

* Each rule has a unique, user-defined name

* User-defined sort order for displaying rules

  * Drag and drop

  * Nestable

  * Other?

* Able to apply a selected rule to a word defined in the language's dictionary

Other
~~~~~

The app will be fully accessible per the checklist from a11y_. Part of this is done with the ESLint plugin jsx-a11y_.

.. _document-driven-development: https://gist.github.com/zsup/9434452
.. _test-driven-development: https://www.agilealliance.org/glossary/tdd/#q=~(infinite~false~filters~(postType~(~'page~'post~'aa_book~'aa_event_session~'aa_experience_report~'aa_glossary~'aa_research_paper~'aa_video)~tags~(~'tdd))~searchTerm~'~sort~false~sortDirection~'asc~page~1)
.. _IPA: https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
.. _a11y: https://a11yproject.com/checklist/
.. _jsx-a11y: https://github.com/jsx-eslint/eslint-plugin-jsx-a11y
