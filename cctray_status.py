import requests
import xml.etree.ElementTree as etree

class CCTray:
    url = None
    max_len = 1

    def __init__(self, url, max_len):
        self.url = url
        self.max_len = max_len

    def fetch(self):
        response = requests.get(self.url)
        print(str(response))

        xml = response.text

        tree = etree.fromstring(xml)

        status = []

        if tree.find('Project') is not None:
          status = [
                      [
                          project.attrib.get('activity').lower(),
                          project.attrib.get('lastBuildStatus').lower(),
                          project.attrib.get('name').count('::')
                      ]
                      for project in tree.findall('Project')
                   ]

        total_count = len(status)
        if total_count > self.max_len:
            status = [s for s in status if s[2] <= 1]

        input = [
            'BUILDING' if s[0] == 'building' else
            'OK' if s[1] == 'success' else
            'ERROR' if s[1] == 'failure'
            else 'UNKNOWN'
            for s in status
        ]

        return input