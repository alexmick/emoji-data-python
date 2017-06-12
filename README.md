# emoji_data_python - A python emoji toolkit

Forget about handling obscure shortcodes from slack or user input, this lib knows all about them !

### Features

* Conversion from slack-style colon short codes : `:smiley:` ⇒ 😃
* Lookup emoji by official name or any known short name
* Render emoji chars from their codepoint

## Installing

Installation should be as simple as :

```bash
pip install emoji_data_python
```

## Usage
```python
>>> import emoji_data_python
>>> len(emoji_data_python.emoji_data)
1489
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
>>> emoji_data_python.find_by_shortname('moon')
[
    EmojiChar("NEW MOON SYMBOL"),
    EmojiChar("WAXING CRESCENT MOON SYMBOL"),
    EmojiChar("FIRST QUARTER MOON SYMBOL"),
    EmojiChar("WAXING GIBBOUS MOON SYMBOL"),
    EmojiChar("FULL MOON SYMBOL"),
    EmojiChar("WANING GIBBOUS MOON SYMBOL"),
    EmojiChar("LAST QUARTER MOON SYMBOL"),
    EmojiChar("WANING CRESCENT MOON SYMBOL"),
    EmojiChar("CRESCENT MOON"),
    EmojiChar("NEW MOON WITH FACE"),
    EmojiChar("FIRST QUARTER MOON WITH FACE"),
    EmojiChar("LAST QUARTER MOON WITH FACE"),
    EmojiChar("FULL MOON WITH FACE"),
]
>>> [ (emoji.name, emoji.short_name, emoji.char) for emoji in emoji_data_python.find_by_name('tree')]
[
    ('EVERGREEN TREE', 'evergreen_tree', '🌲'),
    ('DECIDUOUS TREE', 'deciduous_tree', '🌳'),
    ('PALM TREE', 'palm_tree', '🌴'),
    ('CHRISTMAS TREE', 'christmas_tree', '🎄'),
    ('TANABATA TREE', 'tanabata_tree', '🎋')
]
>>> emoji_data_python.replace_colons('Hello world ! :wave::skin-tone-3: :earth_africa: :exclamation:')
'Hello world ! 👋🏼 🌍 ❗'
```

## Testing

```bash
python -m unittest discover
```
