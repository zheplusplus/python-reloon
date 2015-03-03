# ReLoon

A collection of various Python regular expressions.

## Examples

    from reloon import ANYTHING

    print(ANYTHING.match('') is not None)
    # True

    from reloon import INT, INT_X
    print(INT.match('123') is not None)
    # True
    print(INT.match('123a') is not None)
    # True
    print(INT_X.match('123a') is not None)
    # False

## Usage

Each name in this package is a regular expression. Regexes whose name ends up with `_X` means it matches entire string.

List of all regexes

Regex | Usage
--- | ---
`ANYTHING` | anything
`NOTHING` | nothing
`INT` `INT_X` | integers
`NEG_INT` `NEG_INT_X` | negative integers
`SIGNED_INT` `SIGNED_INT_X` | integers with an optional sign (`+` or `-`)
`NUM` `NUM_X` | numbers
`NEG_NUM` `NEG_NUM_X` | negative numbers
`SIGNED_NUM` `SIGNED_NUM_X` | numbers with an optional sign (`+` or `-`)
`DOMAIN` `DOMAIN_X` | domain names (ASCII only)
`DOMAIN_UNICODE` `DOMAIN_UNICODE_X` | domain names (ASCII or unicode gTLDs)
`EMAIL` `EMAIL_X` `EMAIL_UNICODE` `EMAIL_UNICODE_X` | email addresses
`IPV4` `IPV4_X` | IPv4 addresses
`IPV6` `IPV6_X` | IPv6 addresses
`MAC` `MAC_X` | MAC addresses

## Test

Run

    python test.py
