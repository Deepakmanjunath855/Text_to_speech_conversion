#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyttsx3

text_speech=pyttsx3.init()

answer=input("what text do you want to convert to speech")

text_speech.say(answer)
text_speech.runAndWait()


# In[ ]:




