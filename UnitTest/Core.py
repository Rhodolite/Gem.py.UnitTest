#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('UnitTest.Core')
def module():
    require_module('Capital.Cache2')
    require_module('Capital.DumpCache')
    require_module('Capital.GeneratedConjureQuadruple')
    require_module('Capital.Global')
    require_module('Capital.Map')
    require_module('Capital.Method')
    require_module('Capital.Path')
    require_module('Capital.System')


    from Capital import capital_global, create_cache, create_herd_2, create_horde_2, dump_cache_to_string, empty_herd
    from Capital import print_cache, produce_conjure_by_name__V2
    from Capital import produce_conjure_unique_dual, produce_conjure_unique_dual__21
    from Capital import produce_conjure_quadruple__4123
    from Capital import produce_conjure_unique_triple, produce_conjure_unique_triple__312
    from Capital import reference_count, values_tuple_sorted_by_key, write_binary_to_path


    share(
        #
        #   Imported functions
        #
        'create_cache',                         create_cache,
        'create_herd_2',                        create_herd_2,
        'create_horde_2',                       create_horde_2,
        'dump_cache_to_string',                 dump_cache_to_string,
        'print_cache',                          print_cache,
        'produce_conjure_by_name__V2',          produce_conjure_by_name__V2,
        'produce_conjure_unique_dual__21',      produce_conjure_unique_dual__21,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_unique_dual',          produce_conjure_unique_dual,
        'produce_conjure_quadruple__4123',      produce_conjure_quadruple__4123,
        'produce_conjure_unique_triple__312',   produce_conjure_unique_triple__312,
        'produce_conjure_unique_triple',        produce_conjure_unique_triple,
        'reference_count',                      reference_count,
        'values_tuple_sorted_by_key',           values_tuple_sorted_by_key,
        'write_binary_to_path',                 write_binary_to_path,


        #
        #   Imported Values
        #
        'capital_global',   capital_global,
        'empty_herd',       empty_herd,
    )
