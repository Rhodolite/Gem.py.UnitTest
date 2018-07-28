#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('UnitTest.Path')
def module():
    require_module('Capital.Path')
    require_module('UnitTest.Core')


    from Capital import remove_path__ignore_file_not_found, rename_path__ignore_file_not_found


    @share
    def test_remove_path():
        r = remove_path__ignore_file_not_found('nonexistent')

        assert r is false

        line('PASSED: remove_path')


    @share
    def test_rename_path():
        r = rename_path__ignore_file_not_found('nonexistent', 'even-more-nonexistent')

        assert r is false

        line('PASSED: rename_path')
