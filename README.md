# Get Youtube Transcript

Youtube web scraper to get transcript from for video ID or video URL

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
