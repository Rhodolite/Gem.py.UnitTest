#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('UnitTest.Pattern')
def module():
    require_module('Restructure.Build')
    require_module('UnitTest.Core')


    from Restructure import ANY_OF, DOT, END_OF_PATTERN, EMPTY, EXACT, G
    from Restructure import MINIMUM_OF_ONE_OR_MORE, MINIMUM_OF_OPTIONAL, MINIMUM_OF_REPEAT_OR_MORE, MINIMUM_OF_ZERO_OR_MORE
    from Restructure import ONE_OR_MORE, OPTIONAL, Q, REPEAT, ZERO_OR_MORE


    show = false


    @share
    def test_pattern():
        for [pattern, test] in [
                [   OPTIONAL('bc') + OPTIONAL('d' | EXACT('hi') + 'j') + 'x' + END_OF_PATTERN,      'hijx'      ],
                [   'x' + ('lemo' + ANY_OF('a-z') | G('abc', 'y')) + END_OF_PATTERN,                'xy'        ],
                [   'x' + G('abc', ANY_OF('a-z', 'A-Z')) + G('z', 'z') + END_OF_PATTERN,            'xYz'       ],
                [   OPTIONAL('a') + ONE_OR_MORE('x') + ZERO_OR_MORE('yz') + END_OF_PATTERN,         'xx'        ],
                [   'a' + (EXACT('b') | r'c\i') + 'd' + ONE_OR_MORE('e' | EMPTY) + END_OF_PATTERN,  r'ac\id'    ],
                [   'x' + MINIMUM_OF_OPTIONAL('y') + MINIMUM_OF_ONE_OR_MORE('z') + END_OF_PATTERN,  'xzz'       ],
                [   MINIMUM_OF_ZERO_OR_MORE('x') + REPEAT('yz', 2, 3) + END_OF_PATTERN,             'yzyzyz'    ],
                [   MINIMUM_OF_REPEAT_OR_MORE('x' | EXACT('z'), 0) + 'y' + END_OF_PATTERN,          'xzxy'      ],
                [   'x' + ZERO_OR_MORE(DOT) + Q('never', 'never') + END_OF_PATTERN,                 'xqq'       ],
        ]:
            if show:
                line('%s', pattern)
                line('%r', pattern)

            compiled = pattern.compile_ascii_regular_expression()
            m        = compiled.match(test)

            if show:
                line('  %s %r', portray_string(m.group()), m.groups())
                line()

        line('PASSED: pattern')
