__author__ = "geduldig"
__date__ = "November 30, 2014"
__license__ = "MIT"


import logging


class TwitterError(Exception):

    """Base class for Twitter exceptions"""
    pass


class TwitterConnectionError(TwitterError):

    """Raised when the connection needs to be re-established"""

    def __init__(self, value):
        super(Exception, self).__init__(value)
        logging.warning('%s %s' % (type(value), value))


class TwitterRequestError(TwitterError):

    """Raised when request fails"""

    def __init__(self, response):
        logging.info(
            'Status code %d: %s' % (response.status_code, response.text)
        )
        super(Exception, self).__init__(response)
        self.response = response
        
    def __str__(self):
        return '%s (%d)' % (self.args[0], self.response.status_code)
