Documentation Style Guide
=========================

The goal of this page is to keep |cla|'s documentation easy to read and consistent for choices from the source code to spelling to tone. If you have feedback or suggestions for this document please read our :doc:`../contributing.rst` guide.

Mechanics
---------

Graphic Inserts
~~~~~~~~~~~~~~~~
  We include figures, images, and screenshots when useful. These always include a brief caption and also a description using alternative text. We do this with reStructuredText directives as described here_.

Punctuation
~~~~~~~~~~~
  We use standard American punctuation. If we need to list three or more items in a sentence we use the Oxford comma.

Language Use
~~~~~~~~~~~~
|  We aim to use short, simple, easy-to-understand words and sentences.
|  We avoid the passive voice when we can. (One way to tell if a sentence is passive is to add "by zombies" to the end of it. If the sentence still makes sense then it's passive.)
|  We use the present tense and imperative mood when possible.
|  We aim to be concise when writing.
|  We use gender-neutral language.

Capitalization
~~~~~~~~~~~~~~
  For titles, headers inside of a document, etc., we capitalize everything but prepositions and articles.
  We capitalize and spell screen element names to match what they are in the user interface unless they are something like a dialog option or menu name. For these we follow the same rules as we do for documentation titles.

Spelling
~~~~~~~~
We use American spelling.

Articles
~~~~~~~~
If a term has special leading characters we use the article that agrees with how the term's pronunciation. For example, if you used "#include" in a sentence then the article would be "an" since it's pronounced as "include".

Measurements
~~~~~~~~~~~~
If you need to include measurements write them in the imperial system followed by the metric conversion in parenthesis. Example: 32°F (0°C)

Numbers
~~~~~~~
When numbers are in a sentence we spell them if they are between zero and nine. This also applies to ordinal numbers in sentences. Examples: Fifth, 50th

List Rules
~~~~~~~~~~
If a list item isn't a complete sentence we capitalize the first letter of the first word.
Refer to Lists_ under reStructuredText_ for how to format nested enumerated lists.

reStructuredText
----------------

We write |cla|'s documentation in reStructuredText and built with sphinx_. reStructuredText is flexible in some respects, so the following are conventions to keep the doc source code consistent no matter who is writing. If you are unfamiliar with reStructuredText or need a refresher, please take a look at their quickstart_ guide.

Sections
~~~~~~~~

.. code-block:: rest
  :linenos:

  Page Title 
  ===============

  Section 1 
  -------------

  Section 1.1 
  ~~~~~~~~~~~~~~~

  Section 1.1.1
  *****************

Lists
~~~~~

For bulleted lists, use "``*``" for each item.

The order to use for enumerated lists is as follows

.. code-block:: rest
  :linenos:

  1. Arabic numeral

    I. Uppercase roman numeral

      A. Uppercase alphabet character

        i. Lowercase roman numeral

          a. Lowercase alphabet character


.. _quickstart: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _here: https://docutils.sourceforge.io/docs/ref/rst/directives.html#images
.. _sphinx: https://sphinx-doc.org
