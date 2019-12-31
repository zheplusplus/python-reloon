# encoding=utf-8

import unittest
from reloon import *


class R(unittest.TestCase):
    def assert_match(self, pattern, s):
        self.assertIsNotNone(pattern.match(s))

    def assert_not_match(self, pattern, s):
        self.assertIsNone(pattern.match(s))

    def assert_groups(self, pattern, s, *groups):
        if len(groups) == 1:
            groups = groups[0]
        self.assertEqual(groups, pattern.findall(s)[0])

    def test_universal(self):
        self.assert_match(ANYTHING, '')
        self.assert_match(ANYTHING, 'a')
        self.assert_match(ANYTHING, 'the quick brown fox jump a lazy dog.')

        self.assert_not_match(NOTHING, '')
        self.assert_not_match(NOTHING, 'a')
        self.assert_not_match(NOTHING, 'the quick brown fox jump a lazy dog.')

    def test_nums(self):
        self.assert_match(INT_X, '0')
        self.assert_match(INT_X, '1')
        self.assert_groups(INT, '0', '0')
        self.assert_not_match(INT_X, '1a')
        self.assert_not_match(INT_X, '1.1')

        self.assert_match(NEG_INT_X, '-0')
        self.assert_groups(NEG_INT, '-0', '0')
        self.assert_not_match(NEG_INT_X, '--0')
        self.assert_not_match(NEG_INT_X, '-')

        self.assert_match(SIGNED_INT_X, '0')
        self.assert_match(SIGNED_INT_X, '-0')
        self.assert_match(SIGNED_INT_X, '+0')
        self.assert_groups(SIGNED_INT_X, '-0', '-0', '-', '0')
        self.assert_groups(SIGNED_INT_X, '0', '0', '', '0')
        self.assert_not_match(SIGNED_INT_X, '-')
        self.assert_not_match(SIGNED_INT_X, '+')

        self.assert_match(NUM_X, '3')
        self.assert_match(NUM_X, '3.1')
        self.assert_groups(NUM, '03.14', '03.14', '03', '14')
        self.assert_not_match(NUM_X, '1.0.1')

        self.assert_match(NEG_NUM_X, '-3.14')
        self.assert_groups(NEG_NUM, '-3.14', '3.14', '3', '14')
        self.assert_not_match(NEG_NUM_X, '--3.14')
        self.assert_not_match(NEG_NUM_X, '-')
        self.assert_not_match(NEG_NUM_X, '--2.7.1.8.2')

        self.assert_match(SIGNED_NUM_X, '+2.71828')
        self.assert_groups(SIGNED_NUM, '+2.718', '+2.718', '+', '2', '718')
        self.assert_groups(SIGNED_NUM, '2.718', '2.718', '', '2', '718')
        self.assert_not_match(SIGNED_NUM_X, '-+')

    def test_net(self):
        self.assert_match(DOMAIN_X, 'example.org')
        self.assert_not_match(DOMAIN_X, 'example')

        self.assert_match(DOMAIN_UNICODE_X, 'example.汉')
        self.assert_match(DOMAIN_UNICODE_X, 'example.org')
        self.assert_not_match(DOMAIN_UNICODE_X, 'ドメイン')
        self.assert_not_match(DOMAIN_UNICODE_X, 'example')

        self.assert_match(EMAIL_X, 'someone@example.org')
        self.assert_match(EMAIL_X, 'someone@example.re.loon')
        self.assert_match(EMAIL_X, 'some.one+post@example.re.loon')
        self.assert_groups(EMAIL, 'someone@example.org',
                           'someone', 'example.org')
        self.assert_not_match(EMAIL_X, '@example.com')
        self.assert_not_match(EMAIL_X, 'a b@example.com')
        self.assert_not_match(EMAIL_X, 'someone@example')
        self.assert_not_match(EMAIL_X, u'someone@example.漢')

        self.assert_match(EMAIL_UNICODE_X, u'someone@example.漢')
        self.assert_groups(EMAIL_UNICODE, u'someone@example.漢',
                           'someone', u'example.漢')

        self.assert_match(IPV4_X, '172.16.254.1')
        self.assert_match(IPV4_X, '1.2.3.4')
        self.assert_match(IPV4_X, '01.102.103.104')
        self.assert_not_match(IPV4_X, '1172.16.254.1')
        self.assert_not_match(IPV4_X, '1.2.3')
        self.assert_not_match(IPV4_X, '01.102.103.104.4')

        self.assert_match(IPV6_X, '2001:470:9b36:1::2')
        self.assert_match(IPV6_X, '2001:cdba:0000:0000:0000:0000:3257:9652')
        self.assert_match(IPV6_X, '2001:cdba:0:0:0:0:3257:9652')
        self.assert_match(IPV6_X, '2001:cdba::3257:9652')
        self.assert_not_match(IPV6_X, '1200::AB00:1234::2552:7777:1313')
        self.assert_not_match(IPV6_X, '1200:0000:AB00:1234:o000:2552:777:1313')

        self.assert_match(MAC_X, '94-AE-70-A0-66-83')
        self.assert_match(MAC_X, '58-f8-1a-00-44-c8')
        self.assert_match(MAC_X, '00:A0:C9:14:C8:29')
        self.assert_not_match(MAC_X, '00:A0:C9:14:C8:29:')
        self.assert_not_match(MAC_X, '00:A0:C9:14:C8')
        self.assert_not_match(MAC_X, 'oo:A0:C9:14:C8:29')

if __name__ == '__main__':
    unittest.main()
