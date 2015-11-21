import cli

languages = {'c': '(#include|#import)\s("|<)(.*\..*)("|>)',
                'objectivec': '(#include|#import)\s("|<)(.*\..*)("|>)',
                'python': '^(from|import)\s(\w*\.?\w*)(.*)'}

def get(lang_string):
    if lang_string in languages.keys():
        return languages[lang_string]
    else:
        cli.show_help('Unsupported or unknown language')