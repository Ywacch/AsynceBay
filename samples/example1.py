import time

from asyncebay.config import Config
from asyncebay.request_builder import FindingRequest
from asyncebay import ebay_caller

# setup configuration
config_dict = {
        'service_name': 'FindingService',
        'app_id': 'You APP ID',
        'site_id': 'EBAY-ENCA',
        'op_name': 'findItemsByKeywords',
        'response_format': 'JSON'}

config = Config(config_dict)

# setup finding api requests building class
finding = FindingRequest(config)
finding.build_request_header()

# end user must provide the url request to the request builder. The placeholder for the number of pages to request should be indicated with '{}'
base_ur = 'https://svcs.ebay.com/services/search/FindingService/v1?REST-PAYLOAD&itemFilter(' \
          '0).name=Condition&itemFilter(0).value=Used&itemFilter(1).name=MaxPrice&itemFilter(' \
          '1).value=1500.0&itemFilter(1).paramName=Currency&itemFilter(1).paramValue=CAD&aspectFilter(' \
          '0).aspectName=Storage Capacity&aspectFilter(0).aspectValueName=64 ' \
          'GB&paginationInput.entriesPerPage=10&paginationInput.pageNumber={}&keywords=Apple iPhone Xr'

calls = 1
finding.build_request_urls(base_ur, calls)

start = time.time()
ebay_caller.start(finding.response_list, finding.urls, finding.headers)

# 100 requests can be made in less 2 seconds whereas synchronous requests will take about 70 seconds
print(f"{calls} calls made in {time.time()-start} seconds")

for response in finding.response_list:
    print(response)
