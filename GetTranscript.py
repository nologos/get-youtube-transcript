import requests
import json
import re
from xml.etree import ElementTree
from html import unescape
"""
from getyoutubetranscript.GetTranscript import Transcript

a = Transcript().getTranscriptFromId('RjEdmrxjIHQ')
a.timeScript
a.textScript

b = Transcript().getTranscriptFromLink('https://www.youtube.com/watch?v=RjEdmrxjIHQ')
b.timeScript
b.textScript
"""
class Transcript(object):
    def __init__(self):
        self.timeScript = []
        self.textScript = []

    def returnTextScript(self):
        textblock = []
        for i in self.timeScript:
            textblock.append(i['text'])
        self.textScript = ' '.join(textblock)
        return self
    
    def getTranscript(self, link):
        sitedata = requests.get(link).text
        splitted_html = sitedata.split('"captions":')
        captions_json = json.loads(
                    splitted_html[1].split(',"videoDetails')[0].replace('\n', '')
                ).get('playerCaptionsTracklistRenderer')
        captionUrl = captions_json["captionTracks"][0]["baseUrl"]
        response = requests.get(captionUrl).text
        self.timeScript = self.parse(response)
        self.returnTextScript()
        return self

    def getTranscriptFromLink(self, link):
        return self.getTranscript(link)

    def getTranscriptFromId(self, ID):
        link = 'https://www.youtube.com/watch?v={}'.format(ID)
        return self.getTranscript(link)

    def parse(self, plain_data):
        HTML_TAG_REGEX = re.compile(r'<[^>]*>', re.IGNORECASE)
        return [
            {
                'text': re.sub(HTML_TAG_REGEX, '', unescape(xml_element.text)),
                'start': float(xml_element.attrib['start']),
                'duration': float(xml_element.attrib.get('dur', '0.0')),
            }
            for xml_element in ElementTree.fromstring(plain_data)
            if xml_element.text is not None
        ]