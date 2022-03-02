#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import pylab


# In[2]:


path = 'Downloads\iqds\iqds'
'''
case.csv – таблица с описанием подтверждённых аномалий. Содержит информацию по связанному с аномалией оборудованию ("equipment_id") и объекту ("facility_id").
equipment.csv – таблица, показывающая из каких датчиков ("io_id") состоит оборудование.
facility.csv – таблица, показывающая из каких датчиков микроклимата ("io_id") состоит объект.
*_ data_meter_*.csv – таблицы, содержащие данные для соответствующих датчиков.
'''


# In[3]:


elec = pd.read_csv('Downloads/iqds/iqds/0_data_meter_electricity.csv')
hum = pd.read_csv('Downloads/iqds/iqds/0_data_meter_humidity.csv')
temp = pd.read_csv('Downloads/iqds/iqds/0_data_meter_temperature.csv')
case = pd.read_csv('Downloads/iqds/iqds/case.csv')
equipment = pd.read_csv('Downloads/iqds/iqds/equipment.csv')
facility = pd.read_csv('Downloads/iqds/iqds/facility.csv')


# In[4]:


def gr(data, col1, col2, c):
    date = data[col1]
    x = data[col2]
    plt.figure(figsize=(20,12))

#plt.title('Зависимость кол-ва выпущенных фильмов от года выпуска', fontsize=10)

    plt.plot(date, x, linestyle='-', color=c)

    plt.grid(True) 

#plt.yticks(range(min(x), max(x), 30))
#plt.xticks(range(1925, 2021, 6))

#plt.ylabel('quantity',  fontsize=10)
#plt.xlabel('release year',  fontsize=10)


    plt.show()


# # 0_data_meter_electricity.csv 
# event_timestamp: Unix time. 2020-12-31 21:00:33 - 2022-01-31 20:59:54 \
# Известно: 19.01.2022 – корректная работа оборудования, 20.01.2022 – повышенное энергопотребление.\
# Вкл: \
# Выкл:

# In[6]:


elec


# In[5]:


for i, j in enumerate(elec['event_timestamp']):
    #print(j)
    elec['event_timestamp'][i] = datetime.utcfromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S')
    #print(i, j, elec['event_timestamp'][i])
#print(datetime.utcfromtimestamp(elec['event_timestamp']).strftime('%Y-%m-%d %H:%M:%S'))


# In[49]:


elec['event_timestamp'].to_csv('event_timestamp.csv')


# In[50]:


ind = elec[elec['event_timestamp'].str.contains('2021-02-08', regex=False) == True].index
print(ind)
curr = elec[ind[0] : ind[ind.shape[0] - 1]]
curr['Total_P'].mean()


# # Total_P

# In[38]:


gr(curr, 'event_timestamp', 'Total_P', 'b')


# In[47]:


ind = elec[elec['event_timestamp'].str.contains('2022-08-15', regex=False) == True].index
#anom = elec[ind[0] : ind[719]]
ind


# In[73]:


norm['Total_P'].mean()


# In[74]:


anom['Total_P'].mean()


# In[68]:


gr(norm, 'event_timestamp', 'Total_P', 'b')


# In[69]:


gr(anom, 'event_timestamp', 'Total_P', 'r')


# In[71]:


gr(norm, 'event_timestamp', 'Total_AP_energy', 'b')


# In[14]:


gr(elec[:5000], 'event_timestamp', 'Total_P', 'r')


# In[51]:


gr(elec[27243:32243], 'event_timestamp', 'Total_P', 'r')


# In[52]:


gr(elec[91930:96930], 'event_timestamp', 'Total_P', 'r') #май


# In[53]:


gr(elec[12984:17984], 'event_timestamp', 'Total_P', 'r')


# In[40]:


gr(elec[270395:275395], 'event_timestamp', 'Total_P', 'r')


# In[90]:


elec[238118:241118]


# In[96]:


#2021
el1 = elec.Total_P[90:3090] 
el2 = elec.Total_P[22289:25289]
el3 = elec.Total_P[42270:45270]

el4 = elec.Total_P[64471:67471] 
el5 = elec.Total_P[83059:86059]
el6 = elec.Total_P[103413:106413]

el7 = elec.Total_P[124943:127943] 
el8 = elec.Total_P[146959:149959]
el9 = elec.Total_P[172823:175823]

el10 = elec.Total_P[191337:194337] 
el11 = elec.Total_P[213579:216579]
el12 = elec.Total_P[238118:241118]


# In[97]:


y = np.arange(0, 3000)
plt.figure(figsize=(30,12))
plt.subplot(3, 4, 1)
plt.title('Январь')
plt.plot(y, el1)  
plt.subplot(3, 4, 2)
plt.title('Февраль')
plt.plot(y, el2)
plt.subplot(3, 4, 3)
plt.title('Март')
plt.plot(y, el3)

plt.subplot(3, 4, 4)
plt.title('Апрель')
plt.plot(y, el4)
plt.subplot(3, 4, 5)
plt.title('Май')
plt.plot(y, el5)
plt.subplot(3, 4, 6)
plt.title('Июнь')
plt.plot(y, el6)

plt.subplot(3, 4, 7)
plt.title('Июль')
plt.plot(y, el7)
plt.subplot(3, 4, 8)
plt.title('Август')
plt.plot(y, el8)
plt.subplot(3, 4, 9)
plt.title('Сентябрь')
plt.plot(y, el9)

plt.subplot(3, 4, 10)
plt.title('Октябрь')
plt.plot(y, el10)
plt.subplot(3, 4, 11)
plt.title('Ноябрь')
plt.plot(y, el11)
plt.subplot(3, 4, 12)
plt.title('Декабрь')
plt.plot(y, el12)

plt.savefig('Total_P_year.png')


# In[98]:


el1 = elec.Total_P[257434:262434] 
el2 = elec.Total_P[262434:267434]
el3 = elec.Total_P[267434:272434]
el4 = elec.Total_P[272434:277434]
y = np.arange(5000)
#el3 = elec.Total_P[257434:257434]

plt.figure(figsize=(30,12))
plt.subplot(4, 1, 1)
plt.plot(y, el1)  
plt.subplot(4, 1, 2)
plt.plot(y, el2)
plt.subplot(4, 1, 3)
plt.plot(y, el3)
plt.subplot(4, 1, 4)
plt.plot(y, el4)

plt.savefig('Total_P_2022.png')


# In[93]:


x = 5000
s = 169823
el1 = elec.Total_P[s:s + x] 
el2 = elec.Total_P[s + x:s + 2*x]
el3 = elec.Total_P[s + 2 *x:s + 3 * x]
el4 = elec.Total_P[s + 3 * x:s + 4*x]
y = np.arange(5000)
#el3 = elec.Total_P[257434:257434]

plt.figure(figsize=(30,12))
plt.subplot(4, 1, 1)
plt.plot(y, el1)  
plt.subplot(4, 1, 2)
plt.plot(y, el2)
plt.subplot(4, 1, 3)
plt.plot(y, el3)
plt.subplot(4, 1, 4)
plt.plot(y, el4)


# In[99]:


plt.figure(figsize=(20,12))
#plt.subplot(3, 4, 1)
y = np.arange(3000)
plt.plot(y, el12)

plt.savefig('Total_P_decemb.png')


# In[82]:


off = []
for i in range(279665):
    #print(elec['Total_P'][i])
    if type(elec['Total_P'][i]) == float and elec['Total_P'][i] < 1500:
        off.append(elec['event_timestamp'][i])


# In[83]:


off


# In[98]:


#delta = timedelta('0:30:0', '%H:%M:%S')
for i in range(len(off) - 1):
    d1 = datetime.strptime(off[i], '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(off[i + 1], '%Y-%m-%d %H:%M:%S')
    #print(d2-d1, (d2 - d1).total_seconds())
    if (d2 - d1).total_seconds() > 1800:
        print(off[i], off[i + 1])
        print()


# # 0_data_meter_humidity.csv

# In[7]:


hum


# # 0_data_meter_temperature.csv

# In[10]:


temp


# In[23]:


elec[86100:]


# In[9]:


for i, j in enumerate(temp['event_timestamp']):
    #print(j)
    temp['event_timestamp'][i] = datetime.utcfromtimestamp(j).strftime('%Y-%m-%d %H:%M:%S')


# In[9]:


case


# In[14]:


case['description'][0]


# In[10]:


equipment


# In[11]:


facility


# In[19]:


data = pd.DataFrame({'date': [], 'time': [], 'Total_P':[], 'temp': [], 'hum': []})


# In[20]:


data


# In[25]:


t = np.array(temp['event_timestamp'])
e = np.array(elec['event_timestamp'])


# In[29]:


for i in range(e.shape[0]):
    for j in range(t.shape[0]):


# In[28]:


t


# Что надо сделать:
# Соединить данные и поиграть с графиками

# # Total_AP_max

# In[8]:


elec.columns


# In[51]:


AP = elec['Total_AP_energy_max']#np.array(elec['Total_AP_energy_max'][:279664]) - np.array(elec['Total_AP_energy_max'][1:])
t = elec['event_timestamp']


# In[42]:


a = []
#AP[28618] = AP[28618 - 1]
for j, i in enumerate(elec['Total_AP_energy_max'][:279664]):
    #print(j, i)
    try:
        i = float(i)
    except ValueError:
        a.append(j)
    #if type(i) != float:
        #print(i)


# In[43]:


for i in a:
    AP[i] = AP[i - 1]


# 152677,2021-08-08 19:24:00 - 153242,2021-08-09 04:54:00

# In[44]:


AP = np.array(AP, dtype = float)


# In[47]:


dAP = -1 * AP[:-1] + AP[1:]


# In[48]:


dAP


# In[61]:


#t_dt = datetime.strptime(t, '%Y-%m-%d %h:%M:%s')
t = pd.to_datetime(t)
t


# In[62]:


dt = []
for i, j in enumerate(t):
    i += 1
    dt.append(t[i] - t[i - 1])


# In[66]:


for i in range(len(dt)):
    dt[i] = dt[i].total_seconds()


# In[68]:


len(dt)


# In[72]:


dAP *= 1000


# In[73]:


X = dAP/dt


# In[74]:


X


# In[77]:


el1 = X[90:3090] 
el2 = X[22289:25289]
el3 = X[42270:45270]

el4 = X[64471:67471] 
el5 = X[83059:86059]
el6 = X[103413:106413]

el7 = X[124943:127943] 
el8 = X[146959:149959]
el9 = X[172823:175823]

el10 = X[191337:194337] 
el11 = X[213579:216579]
el12 = X[238118:241118]


# In[79]:


y = np.arange(0, 3000)
plt.figure(figsize=(30,12))
plt.subplot(3, 4, 1)
plt.title('Январь')
plt.plot(y, el1)  
plt.subplot(3, 4, 2)
plt.title('Февраль')
plt.plot(y, el2)
plt.subplot(3, 4, 3)
plt.title('Март')
plt.plot(y, el3)

plt.subplot(3, 4, 4)
plt.title('Апрель')
plt.plot(y, el4)
plt.subplot(3, 4, 5)
plt.title('Май')
plt.plot(y, el5)
plt.subplot(3, 4, 6)
plt.title('Июнь')
plt.plot(y, el6)

plt.subplot(3, 4, 7)
plt.title('Июль')
plt.plot(y, el7)
plt.subplot(3, 4, 8)
plt.title('Август')
plt.plot(y, el8)
plt.subplot(3, 4, 9)
plt.title('Сентябрь')
plt.plot(y, el9)

plt.subplot(3, 4, 10)
plt.title('Октябрь')
plt.plot(y, el10)
plt.subplot(3, 4, 11)
plt.title('Ноябрь')
plt.plot(y, el11)
plt.subplot(3, 4, 12)
plt.title('Декабрь')
plt.plot(y, el12)

#plt.savefig('AP_max_year.png')


# In[87]:


norm = X[270395:270395 + 720]
y = np.arange(720)
plt.figure(figsize=(30,12))
plt.plot(y, norm)

#plt.savefig('AP_max_norm.png')


# In[88]:


anom = X[270395 + 720:270395 + 2 *720]
y = np.arange(720)
plt.figure(figsize=(30,12))
plt.plot(y, anom)
#plt.savefig('AP_max_anom.png')


# In[82]:


norm.mean()


# In[83]:


anom.mean()


# In[85]:


norm[np.where(norm > 1)].mean()


# In[86]:


anom[np.where(anom > 1)].mean()


# In[100]:


x = 5000
s = 270125
el1 = X[s:s + x] 
el2 = X[s + x:s + 2*x]
el3 = X[s + 2 *x:s + 3 * x]
el4 = X[s + 3 * x:s + 4*x]
y = np.arange(5000)
#el3 = elec.Total_P[257434:257434]

plt.figure(figsize=(30,12))
plt.subplot(4, 1, 1)
plt.plot(y, el1)  
plt.subplot(4, 1, 2)
plt.plot(y, el2)
plt.subplot(4, 1, 3)
plt.plot(y, el3)
plt.subplot(4, 1, 4)
plt.plot(y, el4)


# In[ ]:




