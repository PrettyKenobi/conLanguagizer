Documentation Style Guide
=========================

reStructuredText
----------------

|cla|'s documentation is written in reStructuredText_ and built with sphinx_. reStructuredText is flexible in some respects, so the following are conventions to keep things consistent no matter who is writing.

Sections
~~~~~~~~

.. code-block:: rest
  :linenos:

  Page Title (H1)
  ===============

  Section 1 (H2)
  -------------

  Section 1.1 (H3)
  ~~~~~~~~~~~~~~~

  Section 1.1.1 (H4)
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


.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickstart.html
.. _sphinx: https://sphinx-doc.org
