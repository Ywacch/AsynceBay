class FindingRequest:
    """

    """

    def __init__(self, config):
        self.headers = dict()
        self.config = config
        self.urls = []
        self.response_list = []

    def build_request_header(self):
        self.headers['X-EBAY-SOA-SERVICE-NAME'] = self.config.get('service_name')
        self.headers['X-EBAY-SOA-SECURITY-APPNAME'] = self.config.get('app_id')
        self.headers['X-EBAY-SOA-GLOBAL-ID'] = self.config.get('site_id')
        self.headers['X-EBAY-SOA-OPERATION-NAME'] = self.config.get('op_name')
        self.headers['X-EBAY-SOA-RESPONSE-DATA-FORMAT'] = self.config.get('response_format')

    def build_request_urls(self, url, page_numbers):
        """
        iterates over a number, adding that number to the url parameter and adding it to the list of urls to  request
        :param url: url to be duplicated by making new page numbers in the url parameter
        :param page_numbers: the number of pages to request
        :return: None
        """

        for page_number in range(1, page_numbers+1):
            try:
                new_url = url.replace("{}", str(page_number))
            except Exception as e:
                print(e)
            else:
                self.urls.append(new_url)
