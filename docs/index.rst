Emoji Data Python documentation
===============================

This is the documentation for the `emoji_data_python` module

Also available in :ref:`Aphabetical order <genindex>`

Module documentation
--------------------

.. automodule:: emoji_data_python
    :members: unified_to_char, char_to_unified, replace_colons, all_doublebyte, find_by_shortname, find_by_name, get_emoji_regex

    .. attribute:: emoji_data

        List of all emoji as :mod:`emoji_data_python.EmojiChar` objects.

        >>> len(emoji_data_python.emoji_data)
        489

    .. attribute:: emoji_short_codes

        Dict of all emoji as :mod:`emoji_data_python.EmojiChar` objects indexed by short names.

        **Note** : All short names (even secondary) are indexed. If any conflicts are found, only the emoji who has the conflicitng shortname as primary name is indexed under that name
        ie. if an emoji has a secondary short name that is already taken as primary for an other emoji, this will not be referenced under that shortname

        >>> emoji_data_python.emoji_short_names['hearts'].__dict__
        {
            'name': 'BLACK HEART SUIT',
            'unified': '2665',
            'variations': ['2665-FE0F'],
            'docomo': 'E68D',
            'au': 'EAA5',
            'softbank': 'E20C',
            'google': 'FEB1A',
            'short_name': 'hearts',
            'short_names': ['hearts'],
            'text': None,
            'texts': None,
            'category': 'Symbols',
            'sort_order': 245,
            'added_in': '1.1',
            'skin_variations': {},
            'obsoletes': None,
            'obsoleted_by': None
        }


Classes
-------

.. autoclass:: EmojiChar
    :members:
