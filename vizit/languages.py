def enum(**enums):
    return type('Enum', (), enums)

Languages = enum(C = '(#include|#import)\s("|<)(.*\..*)("|>)',
                OBJECTIVEC = '(#include|#import)\s("|<)(.*\..*)("|>)',
                PYTHON = '^(from|import)\s(\w*\.?\w*)(.*)')