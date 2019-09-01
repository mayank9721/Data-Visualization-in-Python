#!/usr/bin/env python
# coding: utf-8

# %pylab inline
# import pandas
# import seaborn

get_ipython().run_line_magic('pylab', 'inline')
import pandas 
import seaborn
data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')

data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')


data

data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')

data


data.tail()


# Load CSV into memory


dt='4/30/2014 23:22:00'


dt=pandas.to_datetime(dt)



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



dt=pandas.to_datetime(dt)



data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)




data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)



data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')



dt='4/30/2014 23:22:00'




dt=pandas.to_datetime(dt)




data['Date/Time']=data['Date/Time'].map(pandas.to_datetime)


data.head()



def get_dom(dt):



def get_dom(dt)




def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)



def get_weekday(dt):
    return dt_weekday

data['weekday']=data['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt_hour
data['hour']=data['Date/Time'].map(get_hour)
data.tail()



def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)



dt.month



dt.day



dt.dom



def get_dom(dt):
    return dt_day

data['dom']=data['Date/Time'].map(get_dom)


def get_dom(dt):
    return dt.day

data['dom']=data['Date/Time'].map(get_dom)



def get_weekday(dt):
    return dt.weekday

data['weekday']=data['Date/Time'].map(get_weekday)
def get_hour(dt):
    return dt.hour
data['hour']=data['Date/Time'].map(get_hour)
data.tail()


# analysis

# analyse the DOM


hist(data.dom, bins=30, rwidth=.8, range=(0.5,30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by uber april 2014')



#for k,rows in data.groupby('dom'):
  #  print((k,rows))
   
def count_rows(rows):
    return len(rows)
by_date=data.groupby('dom').apply(count_rows)
by_date
    #print((k,len(rows)))



plot(by_date)


bar(range(1,3),by_date)



bar(range[1,3],by_date)



bar(range[1,31],by_date)


bar(range(1,31),by_date_sorted)
xticks(range(1,31),by_date_sorted.index)
xlabel('date of the month')
ylabel('frequency')
title('Frequency by uber april 2014')
("")



by_date_sorted=by_date.sort_values()
by_date_sorted



bar(range(1,31),by_date_sorted)




hist(data.hour, bins=24, range=(.5,24)) 


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7),'mon tue wed thu fri sat sun'.split())



hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='#AA6666', alpha=.4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())



data.groupby('hour weekday' .split()).apply(count_rows)


hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green', alpha=.4)
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())



hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green')




hist(data.weekday, bins=7, range =(-.5,6.5), rwidth=.8, color='green')
xticks(range(7),'Mon Tue Wed Thu Fri Sat Sun'.split())



data.weekday


data.groupby('hour weekday'.split()).apply(count_rows)



data.groupby('weekday weekday'.split()).apply(count_rows).unstack()



hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8, color='green')
xticks(range(7),'mon tue wed thu fri sat sun'.split())


plot(data['Lon'],data['Lat'],'.')


figure(figsize=(20,20))
plot(data['Lon'],data['Lat'],'.',ms=1,alpha=.5)
xlim(-74.2,-73.7)
ylim(40.7,41)



