# Text Summarization
Maybe the most simple text summarization with TF-IDF on Python

# How does it work?

![text summarization](https://www.kdnuggets.com/wp-content/uploads/text-summarization.jpg)


Programm using TF-IDF alghoritm for sentence score(importance) and returning only the most important sentences in text.
You can see more about TF-IDF here - https://en.wikipedia.org/wiki/Tf%E2%80%93idf
# by Nazar Tropanets
This project and repository was created by Nazar Tropanets

# Usage
create python file in directory which contains textsummarization.py file from this repository and write:
``` python
from textsummarization import *

summarizer = TextSummarization('Some Text Here',percentage=1/2)
print(summarizer.summarize())
```
or you can directly download and run textsummarization.py file from this repository and change text in __name__ == '__main__'
