import os
import sys
import re

def _get_files_in_path(filepath):
    return [ os.path.join(filepath, file) for file in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, file)) ]

def _get_folders_in_path(filepath):
    return [ os.path.join(filepath, folder) for folder in os.listdir(filepath) if os.path.isdir(os.path.join(filepath, folder)) ]

def strip_file_ext(filename):
    stripped = filename.split('.')[0]
    return stripped if stripped != '' else filename

def _get_all_files(files, dirs):
    if not dirs:
        return files
    else:
        current_dir = dirs.pop()
        files += _get_files_in_path(current_dir)
        dirs += _get_folders_in_path(current_dir)
        return _get_all_files(files, dirs)
    
def _get_file_dependencies(filename, regex):
    current_file = open(filename, 'r')
    matches = []
    for line in current_file:
        regex_match = re.search(regex, line)
        if regex_match:
            matches += [regex_match.groups()[-2]]      
    return matches
    
def parse(directory, regex):
    dependency_list = []
    for file in _get_all_files([],[directory]):
        filename = strip_file_ext(os.path.basename(file))
        dependency_list += [(filename,strip_file_ext(dependency)) for dependency in _get_file_dependencies(file, regex)]
    return dependency_list