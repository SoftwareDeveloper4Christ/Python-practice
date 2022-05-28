#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word)==sorted(anagram)):
        return True
    else:
        return False


# In[17]:


find_anagram("hello", "check")


# In[18]:


find_anagram("below", "elbow")

