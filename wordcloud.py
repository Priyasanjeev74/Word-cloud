# import wordcloud and matplotlib libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Intialize the Paragraph
text = '''I am priyanka raminepalli,hails from dharmavaram.
          My father is a handsome looking man with good heart.
          Dharmavaram is the silk city of Andhra pradesh'''

# Create a WordCloud object
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
