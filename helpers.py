import os
import re
import requests
import sys

INVISIBLE_TAGS = ['a', 'span', 'link', 'style', 'script', '[document]', 'head', 'title']
DEFAULT_STOPWORDS_FILE = 'stopwords.txt'


def load_stop_word(file=None):
    """
    stopword list loading from file
    :param file: str
    :return: list
    """
    if not file or not os.path.isfile(file):
        file = DEFAULT_STOPWORDS_FILE
    stopwords = set()
    with open(file, 'r') as file:
        for line in file.readlines():
            stopwords.add(get_prepared_string(line, ''))
    return sorted(stopwords)


def get_prepared_string(text, space=None):
    """
    regexp text for alphabetical characters
    :param text: str
    :param space: str
    :return: str
    """
    if space is None or not isinstance(space, str):
        space = ' '
    return re.sub('[^A-Za-z]+', space, text).strip().lower()


def get_response_content(url):
    try:
        response = requests.get(url)
        status = response.ok
    except Exception as e:
        raise Exception('An error occured with message: {}'.format(e))
    else:
        if not status:
            raise Exception('Bad url')
    return response.text


def sort_dict(data_dict):
    return sorted(data_dict.items(), key=lambda kv: kv[1], reverse=True)


def get_url():
    args = sys.argv
    size = len(args)
    if size == 2:
        return sys.argv[1]
    raise Exception('Bad input parameters: need only url')
