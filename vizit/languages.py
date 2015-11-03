def enum(**enums):
    return type('Enum', (), enums)

Languages = enum(C = '(#include|#import) ("|<)(.*\..*)("|>)',
                OBJECTIVEC = '(#include|#import) ("|<)(.*\..*)("|>)')