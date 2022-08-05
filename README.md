# Get Youtube Transcript

Scrapes Youtube to get transcript info by using video ID or video URL

## example
```python
from getyoutubetranscript.GetTranscript import Transcript

a = Transcript().getTranscriptFromId('RjEdmrxjIHQ')
a.timeScript
a.textScript

b = Transcript().getTranscriptFromLink('https://www.youtube.com/watch?v=RjEdmrxjIHQ')
b.timeScript
b.textScript
```

## output:
```python
>>> a.timeScript
[{'text': '10 9 8 7 6 5 4 3 2 1', 'start': 0.669, 'duration': 12.021}]
>>> a.textScript
'10 9 8 7 6 5 4 3 2 1'
>>>
```
