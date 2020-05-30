# text-summarization
Maybe the most simple text summarization with TF-IDF on Python

# How does it work?

(https://www.kdnuggets.com/wp-content/uploads/text-summarization.jpg)

::by Nazar Tropanets

create python file in directory which contains textsummarization.py file from this repository and write:
``` python
from textsummarization import *

summarizer = TextSummarization('Some Text Here',percentage=1/2)
print(summarizer.summarize())
```
or you can directly download and run textsummarization.py file from this repository and change text in __name__ == '__main__'
