from logging.config import dictConfig
from os import makedirs

makedirs('logs', exist_ok=True)

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(name)s] %(levelname)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
        'error_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'logs/extractor-errors.log',
            'formatter': 'default',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 3,
            'encoding': 'utf8',
        },
        'info_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'logs/extractor-info.log',
            'formatter': 'default',
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 3,
            'encoding': 'utf8',
        },
    },
    'loggers': {
        'extractor': {'level': 'DEBUG', 'handlers': ['error_file', 'info_file', 'console']}
    }
}

dictConfig(LOG_CONFIG)
