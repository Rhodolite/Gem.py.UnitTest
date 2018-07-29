#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    path_0 = module_path[0]

    module_path.insert(0, path_absolute(path_join(path_0, '../../Capital')))
    module_path.insert(1, path_absolute(path_join(path_0, '../')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Parser')))
    module_path.insert(3, path_absolute(path_join(path_0, '../../Tremolite')))

    #
    #   For SqlParser.ConjureTreeComment we need '../../Parser/Mothballed'
    #
    module_path.insert(4, path_absolute(path_join(path_0, '../../Parser/Mothballed')))


    import Capital


@module('UnitTest.Main')
def module():
    transport('Capital.Global',                     'capital_global')


    capital_global.sql_parser = true                                    #   For `lookup_name` in CoreParser.Atom
    capital_global.testing    = true


    require_module('UnitTest.ConjureDual')
    require_module('UnitTest.ConjureQuadruple')
    require_module('UnitTest.ConjureSingle')
    require_module('UnitTest.ConjureTreeComment')
    require_module('UnitTest.ConjureTriple')
    require_module('UnitTest.Drove')
    require_module('UnitTest.ExceptionChain')
    require_module('UnitTest.Herd')
    require_module('UnitTest.Path')
    require_module('UnitTest.Pattern')
    require_module('UnitTest.PortrayString')
    require_module('UnitTest.Sequence')
    require_module('UnitTest.Series')
    require_module('UnitTest.StringOutput')


    @share
    def main(arguments):
        test_conjure_dual()
        test_conjure_quadruple()
        test_conjure_single()
        test_conjure_triple()
        test_conjure_tree_comment()
        test_drove()
        test_herd()
        test_pattern()
        test_portray_raw_string()
        test_remove_path()
        test_rename_path()
        test_sequence()
        test_series()
        test_string_output()
        #test_exception_chain()
