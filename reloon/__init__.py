import re

def _re(s):
    return re.compile(s), re.compile('^' + s + '$')

ANYTHING, _ = _re('.*')
NOTHING, _ = _re('$.')

_INT = r'\d+'

INT, INT_X = _re('(%s)' % _INT)
NEG_INT, NEG_INT_X = _re('-(%s)' % _INT)
SIGNED_INT, SIGNED_INT_X = _re('(([+-])?(%s))' % _INT)

_NUM = r'({n})(?:\.({n})?)?'.format(n=_INT)

NUM, NUM_X = _re(r'(%s)' % _NUM)
NEG_NUM, NEG_NUM_X = _re(r'-(%s)' % _NUM)
SIGNED_NUM, SIGNED_NUM_X = _re('(([+-])?%s)' % _NUM)

_DOMAIN_CHAR = '-a-zA-Z0-9'
# for unicode gTLDs
_DOMAIN_UCHAR = _DOMAIN_CHAR + (u'\u0370-\u1CDF' u'\u2C00-\u30FF'
                                u'\u4E00-\u9FBF')
_DOMAIN = r'([{c}]+\.[{c}.]+)'.format(c=_DOMAIN_CHAR)
_DOMAIN_UNICODE = r'([{c}]+\.[{c}.]+)'.format(c=_DOMAIN_UCHAR)

DOMAIN, DOMAIN_X = _re(_DOMAIN)
DOMAIN_UNICODE, DOMAIN_UNICODE_X = _re(_DOMAIN_UNICODE)

# from http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/useful_regex.ipynb
EMAIL, EMAIL_X = _re('([a-zA-Z0-9_.+-]+)@%s' % _DOMAIN)
EMAIL_UNICODE, EMAIL_UNICODE_X = _re('([a-zA-Z0-9_.+-]+)@%s' % _DOMAIN_UNICODE)

IPV4, IPV4_X = _re(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
                   r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')

IPV6, IPV6_X = _re(r'((([0-9A-Fa-f]{1,4}:){7}(?:[0-9A-Fa-f]{1,4}|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
                   r'|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))'
                   r'|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))')

MAC, MAC_X = _re(r'(?i)([0-9A-F]{2}[:-]){5}([0-9A-F]{2})')
