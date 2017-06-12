import json
from os import path
from typing import List, Dict

from .conversion import unified_to_char
from .emoji_char import EmojiChar
from .replacement import replace_colons
from .search import all_doublebyte, find_by_shortname, find_by_name

# Read json data on module load to be cached
with open(path.join(path.dirname(__file__), 'data/emoji.json'), 'r') as full_data:
    # Load and parse emoji data from json into EmojiChar objects
    emoji_data = [EmojiChar(data_blob) for data_blob in json.loads(full_data.read())]  # type: List[EmojiChar]

    # Build a cached dictionary of short names for quicker access, short code keys are normalized with underscores
    emoji_short_names = {
        emoji.short_name.replace('-', '_'): emoji for emoji in emoji_data
    }  # type: Dict[str, EmojiChar]

    # Add other short names if they are not already used as a primary short name for an other emoji
    for emoji in emoji_data:
        for short_name in emoji.short_names:
            if short_name not in emoji_short_names:
                emoji_short_names[short_name] = emoji


__all__ = ['unified_to_char', 'EmojiChar', 'replace_colons', 'all_doublebyte', 'find_by_shortname', 'find_by_name']
