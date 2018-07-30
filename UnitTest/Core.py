#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
@module('UnitTest.Core')
def module():
    transport('Capital.Cache2',                     'create_cache')
    transport('Capital.Cache2',                     'produce_conjure_by_name__V2')
    transport('Capital.DumpCache',                  'dump_cache_to_string')
    transport('Capital.DumpCache',                  'print_cache')
    transport('Capital.Exception',                  'Exception')
    transport('Capital.Global',                     'capital_global')
    transport('Capital.Herd_2',                     'create_herd_2')
    transport('Capital.Herd',                       'empty_herd')
    transport('Capital.Horde',                      'create_horde_2')
    transport('Capital.Map',                        'values_tuple_sorted_by_key')
    transport('Capital.Path',                       'write_binary_to_path')
    transport('Capital.System',                     'reference_count')
