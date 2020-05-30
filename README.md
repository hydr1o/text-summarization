# text-summarization
Maybe the most simple text summarization with TF-IDF on Python

::by Nazar Tropanets

``` python
from textsummarization import *

summarizer = TextSummarization('Some Text Here',percentage=1/2)
print(summarizer.summarize())
```
