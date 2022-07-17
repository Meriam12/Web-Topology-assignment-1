#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[5]:


import networkx as nx


# In[6]:


from networkx.algorithms.community.centrality import girvan_newman


# In[7]:


G= nx.karate_club_graph()


# In[9]:


Communities = girvan_newman(G)


# In[10]:


node_groups =[]


# In[12]:


for com in next (Communities):
    node_groups.append(list(com))


# In[13]:


print(node_groups)


# In[14]:


color_map = []


# In[15]:


for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else:
        color_map.append("green")


# In[23]:


nx.draw(G,node_color=color_map, with_labels = True)
plt.show()

