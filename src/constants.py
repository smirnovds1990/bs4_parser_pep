from pathlib import Path


LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PRETTY_OUTPUT = 'pretty'
FILE_OUTPUT = 'file'
MAIN_DOC_URL = 'https://docs.python.org/3/'
BASE_DIR = Path(__file__).parent
DOWNLOADS_DIR = 'downloads'
RESULTS_DIR = 'results'
LOG_DIR = BASE_DIR / 'logs'
MAIN_PEP_URL = 'https://peps.python.org/'
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
