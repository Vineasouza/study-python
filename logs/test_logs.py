"""
Testing logging
"""

import logging
logging.basicConfig(format='[%(levelname)s]:%(message)s', level=logging.DEBUG)


logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

RESULT = 5
logging.addLevelName(RESULT, 'RESULT')

def result(self, message, *args, **kws):
    """Define a custom level RESULT"""
    self.log(RESULT, message, *args, **kws)
logging.Logger.result = result

#logging.basicConfig()
l = logging.getLogger()
l.setLevel(RESULT)
l.result('test')
l.setLevel(logging.DEBUG)
l.result('test')
