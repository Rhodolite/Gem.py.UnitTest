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

    module_path.insert(0, path_absolute(path_join(path_0, '../../Gem')))
    module_path.insert(1, path_absolute(path_join(path_0, '../')))
    module_path.insert(2, path_absolute(path_join(path_0, '../../Parser')))
    module_path.insert(3, path_absolute(path_join(path_0, '../../Tremolite')))


    import Gem


@gem('UnitTest.Main')
def gem():
    require_gem('UnitTest.ConjureDual')
    require_gem('UnitTest.ConjureQuadruple')
    require_gem('UnitTest.ConjureSingle')
    require_gem('UnitTest.ConjureTreeComment')
    require_gem('UnitTest.ConjureTriple')
    require_gem('UnitTest.Drove')
    require_gem('UnitTest.ExceptionChain')
    require_gem('UnitTest.Herd')
    require_gem('UnitTest.Path')
    require_gem('UnitTest.Pattern')
    require_gem('UnitTest.PortrayString')
    require_gem('UnitTest.Sequence')
    require_gem('UnitTest.Series')
    require_gem('UnitTest.StringOutput')


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
