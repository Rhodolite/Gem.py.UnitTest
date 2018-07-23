#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@gem('UnitTest.StringOutput')
def gem():
    require_gem('Gem.StringOutput')
    require_gem('UnitTest.Core')


    from Gem import create_StringOutput


    @share
    def test_string_output():
        f = create_StringOutput()

        f.line()
        f.line('line #2')
        f.line('line #%d', 3)

        s = f.finish()

        assert s == '\nline #2\nline #3\n'

        line('PASSED: StringOutput')
