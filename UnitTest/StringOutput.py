#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('UnitTest.StringOutput')
def module():
    require_module('Capital.StringOutput')
    require_module('UnitTest.Core')


    from Capital import create_StringOutput


    @share
    def test_string_output():
        f = create_StringOutput()

        f.line()
        f.line('line #2')
        f.line('line #%d', 3)

        s = f.finish()

        assert s == '\nline #2\nline #3\n'

        line('PASSED: StringOutput')
