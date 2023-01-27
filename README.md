# ReLoon

A collection of various Python regular expressions.

## Install

    pip install reloon

As of `reloon==0.3.0`, supporting of Python2 and `setup.py` has been stopped.
Upgrade to `pip>=22.3` or you have to specify an older version to install.

    pip install reloon==0.2.0

Regexes in `0.3.0` are the same as those in `0.2.0`.

## Examples

    from reloon import ANYTHING

    print(ANYTHING.match('') is not None)
    # True

    from reloon import INT, INT_X
    print(INT.match('123') is not None)
    # True
    print(INT.match('123a') is not None)
    # True
    print(INT_X.match('123a') is None)
    # True

## Usage

Each name in this package is a regular expression. Regexes whose names end up with `_X` match entire strings.

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
