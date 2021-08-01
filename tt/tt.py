"""
This module is used to generate files based on Jinja2 template structures.

"""
import os
import json
from jinja2 import Environment, FileSystemLoader


def ensure_dir_path_exists(file_path: str):
    dir_path = file_path.rpartition('/')[0]
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)


def write(txt: str, file_path: str):
    ensure_dir_path_exists(file_path)
    with open(file_path, 'w') as file:
        file.write(txt)


def load(file_path: str):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_files(scheme_path: str, template_path: str):
    """Generates file structure based on jinja2 templates.
    Example run:
    >>> generate_files('./tests/data/example.json', './path/to/template')
    transcribing templates...
    transcription completed


    :return:
    """
    print('transcribing templates...')

    curr_path = os.getcwd()

    file_list = [
        os.path.join(r, f)
        for r, _, fs in os.walk(template_path)
        for f in fs
    ]

    env = Environment(
        loader=FileSystemLoader(template_path),
    )

    scheme = load(scheme_path)
    resulting_folder_name = scheme.get('resulting_folder_name')
    resulting_folder_name = resulting_folder_name if resulting_folder_name else 'template-result'
    print('scheme used: ', scheme)

    for file_path in file_list:
        print(file_path)

        file_path_from_env = file_path.replace(template_path, '')
        template = env.get_template(file_path_from_env)
        file_txt = template.render(**scheme)
        write(file_txt, os.path.join(curr_path, resulting_folder_name, file_path_from_env))

    print('transcription completed')
