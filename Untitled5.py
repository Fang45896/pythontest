
# coding: utf-8

# In[38]:

e2f={'dog':'chien','cat':'chat','walrus':'morse'}
e2f


# In[39]:

e2f['walrus']


# In[40]:

f2e={}
for english,french in e2f.items():
    f2e[french]=english
f2e


# In[41]:

f2e['chien']


# In[42]:

set(e2f.keys())


# In[47]:

life= {
    'animals':{
        'cats':[
            'Henri','Grumpy','Lucy'
            ],
        'octopi':{},
        'emus':{}
        },
    'plants':{},
    'other':{}
    }


# In[48]:

print(list(life.keys()))


# In[49]:

print(life['animals'].keys())


# In[50]:

print(life['animals']['cats'])


# In[ ]:



