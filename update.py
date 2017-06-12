from os import path

import logging
from requests import get

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

JSON_LOCATION = 'https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json'

logger.info(f'📶  Downloading data from {JSON_LOCATION}')
r = get(JSON_LOCATION)
r.raise_for_status()

output_path = path.join(path.dirname(__file__), 'emoji_data_python/data/emoji.json')
logger.info(f'📝  Writing data to {output_path}')
with open(output_path, 'w') as f:
    f.write(r.text)

logger.info('✅  Done, successfully updated data, '
            'run "python -m unittest discover" to make sure the format is still supported')
