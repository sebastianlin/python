
"""
This supports log file rotating.

We donot know how to filter some types of message to the console and the file.
Now only error and critical message will be directed to the console and the file.
"""


import logging, logging.config

LOG_SETTINGS = {
	'version': 1,
	'handlers': {
	    'console': {
    	    'class': 'logging.StreamHandler',
        	'level': 'ERROR',
	        'formatter': 'detailed',
    	    'stream': 'ext://sys.stdout',
	    },
    	'file': {
	        'class': 'logging.handlers.RotatingFileHandler',
    	    'level': 'INFO',
        	'formatter': 'detailed',
	        'filename': 'junk.log',
    	    'mode': 'a',
        	'maxBytes': 10480,
	        'backupCount': 5,
    	},
	},
	'formatters': {
	    'detailed': {
	        'format': '%(asctime)s %(module)-17s line:%(lineno)-4d ' \
	        '%(levelname)-8s %(message)s',
	    },
	    'email': {
	        'format': 'Timestamp: %(asctime)s\nModule: %(module)s\n' \
	        'Line: %(lineno)d\nMessage: %(message)s',
	    },
	},
	'loggers': {
	    'extensive': {
	        'level:':'DEBUG',
#	        'handlers': ['file',]
	        'handlers': ['file', 'console']
	        },
	}
}

logging.config.dictConfig(LOG_SETTINGS)
logger = logging.getLogger('extensive')

for i in range(0,10):
	logger.info("This is from Runner %d"%(i))
	logger.debug("This is from Runner %d"%(i))
	logger.error("This is from Runner %d"%(i))
	logger.critical("This is from Runner %d"%(i))



