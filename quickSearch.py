#!/usr/bin/env python

import webbrowser
import sys
from urllib.parse import quote

try:
  search_request = sys.argv[1]
  query_param = quote(search_request)
  webbrowser.open('https://www.youtube.com/results?search_query={}'.format(query_param))
except:
  print('you must add a search term')
