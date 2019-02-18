import helpers
from bs4 import BeautifulSoup


class HtmlContentScanner:
    def __init__(self, url, file=None):
        self.url = url
        self.stopwords = helpers.load_stop_word(file)
        self.text = ''
        self.title = ''
        self.results = dict()

    def fetch_valid_content(self):
        """
        fetching visible content
        """
        content = helpers.get_response_content(self.url)
        soup = BeautifulSoup(content, 'html.parser')
        self.title = soup.title.text
        [data.extract() for data in soup(helpers.INVISIBLE_TAGS)]
        self.text = soup.getText()

    def get_validated_words(self, text):
        """
        return filtered words
        :param text: str
        :return: list
        """
        words = text.split(' ')
        return [word for word in words if word not in self.stopwords and len(word) > 1]

    def add_to_results(self, words):
        for word in words:
            self.results[word] = self.results.get(word, 0) + 1

    def fetch_results(self):
        """
        words counts to results
        """
        for text in helpers.get_prepared_string(self.text).split(' '):
            self.add_to_results(self.get_validated_words(text))

    def execute_scanner(self):
        """
        html scanner executor
        """
        self.fetch_valid_content()
        self.fetch_results()
        self.print_results()

    def print_results(self):
        """
        print title and words counts
        """
        print(self.title, end='\n\n')
        max_length = helpers.get_max_length(self.results)
        for value in helpers.sort_dict(self.results):
            print(helpers.get_formatted_string(value, max_length))


if __name__ == '__main__':
    url_link = helpers.get_url()
    scanner = HtmlContentScanner(url_link)
    scanner.execute_scanner()
