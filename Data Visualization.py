#!/usr/bin/env python
# coding: utf-8

# %pylab inline
# import pandas
# import seaborn

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas 
import seaborn


# In[2]:


data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[3]:


data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[4]:


data


# In[5]:


data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[6]:


data


# In[7]:


data.tail()


# Load CSV into memory

# In[1]:


dt='4/30/2014 23:22:00'


# In[2]:


dt=pandas.to_datetime(dt)


# In[3]:


d,t=dt.split(' ')
print(d)
print(t)


# In[4]:


m,d,y=d.split('/')


# In[5]:


int(d)


# In[6]:


pandas.to_datetime(dt)


# In[7]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas 
import seaborn


# In[8]:


dt=pandas.to_datetime(dt)


# In[9]:


data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)


# In[10]:


data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)


# In[11]:


data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


# In[12]:


dt='4/30/2014 23:22:00'


# In[13]:


dt=pandas.to_datetime(dt)


# In[14]:


data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)


# In[15]:


data.head()


# In[16]:


def get_dom(dt):


# In[17]:


def get_dom(dt)


# In[18]:


def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)


# In[19]:


def get_weekday(dt):
    return dt_weekday

data['weekday']=data['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt_hour
data['hour']=data['Date/Time'].map(get_hour)
data.tail()


# In[20]:


def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)


# In[21]:


dt.month


# In[22]:


dt.day


# In[23]:


dt.dom


# In[24]:


def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)


# In[25]:


def get_dom(dt):
    return dt.day

data['dom']=data['Date/Time'].map(get_dom)


# In[26]:


def get_weekday(dt):
    return dt.weekday

data['weekday']=data['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt.hour
data['hour']=data['Date/Time'].map(get_hour)
data.tail()


# analysis

# analyse the DOM
# 

# In[29]:


hist(data.dom, bins=30, rwidth=.8, range=(0.5,30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by uber april 2014')


# In[32]:


#for k,rows in data.groupby('dom'):
  #  print((k,rows))
   
def count_rows(rows):
    return len(rows)
by_date=data.groupby('dom').apply(count_rows)
by_date
    #print((k,len(rows)))


# In[33]:


plot(by_date)


# In[34]:


bar(range(1,3),by_date)


# In[35]:


bar(range[1,3],by_date)


# In[36]:


bar(range[1,31],by_date)


# In[41]:


bar(range(1,31),by_date_sorted)
xticks(range(1,31),by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by uber april 2014')
("")


# In[38]:


by_date_sorted=by_date.sort_values()
by_date_sorted


# In[39]:


bar(range(1,31),by_date_sorted)


# In[44]:


hist(data.hour, bins=24, range=(.5,24)) 


# In[46]:


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7),'mon tue wed thu fri sat sun'.split())


# In[48]:


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())


# In[49]:


data.groupby('hour weekday' .split()).apply(count_rows)


# In[51]:


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green', alpha=.4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())


# In[54]:


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green')


# In[57]:


hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='green')
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())


# In[56]:


data.weekday


# In[58]:


data.groupby('hour weekday'.split()).apply(count_rows)


# In[59]:


data.groupby('weekday weekday'.split()).apply(count_rows).unstack()


# In[61]:


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green')
xticks(range(7),'mon tue wed thu fri sat sun'.split())


# In[62]:


plot(data['Lon'],data['Lat'],'.')


# In[65]:


figure(figsize=(20,20))
plot(data['Lon'],data['Lat'],'.',ms=1,alpha=.5)
xlim(-74.2,-73.7)
ylim(40.7,41)


# In[1]:


pip install nbconvert


# In[2]:


pip install ipython


# In[3]:


ipython nbconvert — to script abc.ipynb


# In[4]:


ipython nbconvert — to script abc.py


# In[ ]:




