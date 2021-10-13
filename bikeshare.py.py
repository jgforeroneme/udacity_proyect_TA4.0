#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load the librarys required by the program

import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# In[2]:


#Load the files required by the program
chicago=pd.read_csv('chicago.csv')
new_york=pd.read_csv('new_york_city.csv')
washington=pd.read_csv('washington.csv')


# In[3]:


#Initialization sequence and request of program input parameters

while True:
    
    '''City variable, this variable allows you to choose which dataframe is 
    going to be consulted in the program, it returns the data of one of the 3 cities served'''
    
    city=input('Hello! Let\'s explore some US bikeshare data!\n'
        'Would you like to see data for Chicago, New York or Washington?\n')
    city=city.title()
    if city == 'Chicago' or city=='New York' or city=='Washington':
        if city == 'Chicago':
            df1=chicago
        if city=='New York':
            df1=new_york
        if city=='Washington':
            df1=washington
        break
    else:
        print('The city is not valid')
        
while True:
    
    '''Month variable, this variable allows you to choose the month on which to consult
     in the program, it returns the data of the previously selected city filtered by month'''
    
    month=input('Which month? January, February, March, April, May, June or All?\n')
    month=month.title()
    months=('January', 'February', 'March', 'April', 'May', 'June', 'All')
    if month in months:
        break
    else:
        print('The month is not valid')
        
while True:
    
    '''Variable day, this variable allows you to choose the day on which to consult 
    in the program, it returns the data of the previously selected city filtered by month and by day'''
    
    day=input('Which day? Please type ypur response as an integer (0=Sunday, 1=Monday, 2=Tuesday,\n '
          '3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday, 7=all)\n')
    try:
        day=int(day)
    except:
        True
    if day in range(0,8):
        break
    else:
        print('The vale insert is not valid')
seconds = time.process_time()
print("Seconds since epoch = {}".format(seconds))
        


# In[4]:


def cabecera_cinco(df):
    
    '''It generates the first 5 records 
    of the dataframe, its result is similar to the function df.head()'''
    
    dff=df.head()
    return dff    


# In[5]:


def mas_salidas(df):
    
    '''Generates the most used output station record in the filtered data set'''
    
    s=df['Start Station'].mode()[0]
    return s


# In[6]:


def mas_llegadas(df):
    
    '''Generates the most used arrival station record in the filtered dataset'''
    
    s=df['End Station'].mode()[0]
    return s


# In[7]:


def hora_mas_popular(df):
    
    '''Generates the time stamp where 
    the bike rental service is most used in the filtered data set'''
    
    s=df['Hour'].mode()[0]
    return s


# In[8]:


def ajustes_fechas(df):
    
    '''Clears the formats of the start and end dates of the rental, 
    changing from str to datetime format, additionally calculates the variable 
    month, day, hour, minute and the difference between start time and end time'''
    
    df['Start Time']=df['Start Time'].apply(lambda _: datetime.strptime(_,"%Y-%m-%d %H:%M:%S"))
    df['End Time']=df['End Time'].apply(lambda _: datetime.strptime(_,"%Y-%m-%d %H:%M:%S"))
    df['Diff']=df['End Time']-df['Start Time']
    df['Month']=df['Start Time'].dt.month
    df['Day_of_week']=df['Start Time'].dt.weekday
    df['Hour']=df['Start Time'].dt.hour
    df['Minute']=df['Start Time'].dt.minute  

    return df


# In[9]:


def flag(df):
    lista=list()
    for i in list(df['Hour']):
        if i in range(0,13):
            a='Morning'
            lista.append(a)
        if i in range(13,19):
            a='Evening'
            lista.append(a)
        if i in range(19,25):
            a='Nigth'
            lista.append(a)
    df['Flag']=lista
    return df


# In[10]:


def ajuste_birthday(df):
    
    '''clear the Birthday variable by removing the 
    missing data and repopulating the empty fields with the 
    average value of the total data'''
    
    aj1=df['Birth Year'].fillna(df['Birth Year'].mean())
    df1['Birth Year']=aj1
    ls1=list()
    for i in aj1:
        i=int(i)
        ls1.append(i)
    df['Birth Year']=ls1
    return df


# In[11]:


def ajustes_datos_perdidos(df):
    
    '''clean the variable gender and iser type by 
    removing the missing data and repopulating the empty fields with the value 'No data'''
    
    df['User Type'].fillna('Not Data', inplace=True)
    df['Gender'].fillna('Not Data', inplace=True)
    return df


# In[12]:


def tipo_usuario(df):
    
    '''Sort data by user type'''
    
    s=df['User Type'].value_counts()
    return s


# In[13]:


def gender(df):
    
    '''Classify the data by gender'''
    
    s=df['Gender'].value_counts()
    return s


# In[14]:


def birth_count(df):
    
    '''Sort the data by birthday year'''
    
    s=df['Birth Year'].value_counts()
    return s


# In[15]:


def estadisticas_tiempo(df):
    
    '''Create basic statistics on the Diff column (difference between the start date 
    and the end date of the rental) these statistics are sum, mean, standard deviation, 
    maximum and minimum'''
    
    a=df['Diff'].sum()
    b=df['Diff'].mean()
    c=df['Diff'].max()
    d=df['Diff'].min()
    e=df['Diff'].std()
    return a, b, c, d, e


# In[16]:


def alquiler_meses(df):
    
    '''Calculate the month where the rental service has been used the most, 
    it has better applicability if when generating the data they are consulted 
    every month'''
    
    a=df['Month'].mode()[0]
    if a == 1:
        a='January'
    if a == 2:
        a='February'
    if a == 3:
        a='March'
    if a == 4:
        a='April'
    if a == 5:
        a='May'
    if a == 6:
        a='June'
    return a


# In[17]:


def alquiler_dias(df):
    
    '''Calculate the day where the rental service has been used the most, 
    it has better applicability if when generating the data they are consulted 
    every days'''
    
    a=df['Day_of_week'].mode()[0]
    if a == 0:
        a='Sunday'
    if a == 1:
        a='Monday'
    if a == 2:
        a='Tuesday'
    if a == 3:
        a='Wednesday'
    if a == 4:
        a='Thursday'
    if a == 5:
        a='Friday'
    if a == 6:
        a='Saturday'
    return a


# In[18]:


def cuenta_flag(df):
    
    '''calculate the number of rentals per time slot'''
    
    s=df['Flag'].value_counts()
    return s


# In[19]:


'''This code sequence applies the previously 
created functions to the selected data set (without filtering).'''
try:
    ajustes_fechas(df1) 
except:
    print('No se requiere aplicar ajustes') 
try:
    flag(df1) 
except:
    print('No se requiere aplicar ajustes') 
try:
    ajustes_datos_perdidos(df1)
except:
    print('No se requiere aplicar ajustes')
try:
    ajuste_birthday(df1)
except:
    print('No se requiere aplicar ajustes')   
finally:
    print('Proceso finalizado')
seconds = time.process_time()
print("Seconds since epoch = {}".format(seconds))


# In[20]:


'''This sequence of code filters the dataframe according to the month 
and day selection, if you want to see every month and / or every day 
you must choose the option there for the month and for the day choose 
the option 7'''

try:
    if month == 'January':
        df2=df1[df1['Month']==1]
    if month == 'February':
        df2=df1[df1['Month']==2]
    if month == 'March':
        df2=df1[df1['Month']==3]
    if month == 'April':
        df2=df1[df1['Month']==4]
    if month == 'May':
        df2=df1[df1['Month']==5]
    if month == 'June':
        df2=df1[df1['Month']==6]
    if month == 'All':
        df2=df1
except:
    print('Error')
try:
    if day == 0:
        df3=df2[df2['Day_of_week']==0]
    if day == 1:
        df3=df2[df2['Day_of_week']==1]
    if day == 2:
        df3=df2[df2['Day_of_week']==2]
    if day == 3:
        df3=df2[df2['Day_of_week']==3]
    if day == 4:
        df3=df2[df2['Day_of_week']==4]
    if day == 5:
        df3=df2[df2['Day_of_week']==5]
    if day == 6:
        df3=df2[df2['Day_of_week']==6]
    if day == 7:
        df3=df2
except:
    print('error')
seconds = time.process_time()
print("Seconds since epoch = {}".format(seconds))


# In[21]:


'''Generation of basic dataset statistics'''

print('*'*100)
try:
    aa=mas_salidas(df3)
    print("The station where most bicycle trips leave is {}".format(aa))
    seconds = time.process_time()
    print("Seconds since epoch = {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:    
    ab=mas_llegadas(df3)
    print("The station where most bicycle trips arrive is {}".format(ab))
    seconds = time.process_time()
    print("Seconds since epoch = {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    ac=hora_mas_popular(df3)
    print("The most popular time to rent bicycles is = {}".format(ac))
    seconds = time.process_time()
    print("The time where more trips are made is {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    ad=tipo_usuario(df3)
    print("Customers using the rental service are classified into \n{}".format(ad))
    seconds = time.process_time()
    print("The time where more trips are made is {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    ae=birth_count(df3)
    print("Clients can be classified by year of birth as follows \n{}".format(ae))
    seconds = time.process_time()
    print("The time where more trips are made is {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    af, ag, ah, ai, aj=estadisticas_tiempo(df3)
    print("The total time recorded in the bike rental is \n{}".format(af))
    print("Average recorded bike rental time is \n{}".format(ag))
    print("The maximum recorded bike rental time is \n{}".format(ah))
    print("The minimun recorded bike rental time is \n{}".format(ai))
    print("the standard desviation of the data set is \n{}".format(aj))
    seconds = time.process_time()
    print("The time where more trips are made is {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    ak=alquiler_meses(df3)
    print("The month in which more rentals were made was {}".format(ak))
    al=alquiler_dias(df3)
    seconds = time.process_time()
    print("The day in which more rentals were made was {}".format(al))
    print("The time where more trips are made is {}".format(seconds))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    am=gender(df3)
    print("The classification of clients by gender is as follows:\n{}".format(am))
except:
    print('No se puede aplicar función')
print('*'*100)
try:
    an=cuenta_flag(df3)
    print("Bicycle rental by time slot is distributed as follows:\n{}".format(an))
except:
    print('No se puede aplicar función')
print('*'*100)


# In[22]:


'''Creates the loops required for data visualization of 5 tuples per request'''

a=0
b=5
while True:
    pregunta=input('desea ver los 5 primeros registros? - 0 = si, 1 = no\n')
    pregunta= int(pregunta)
    if pregunta in range(0,2):
        break
    else:  
        print('El valor ingresado no es valido')
     
if pregunta==0:
    print('Funciono')
    #break
    print(df3[a:b])
    while True:
        preg2=input('Desea seguir viendo registros?- 0 = si, 1 = no\n')
        preg2= int(preg2)
        if preg2 in range(0,2):
            if preg2==0:
                print('Funciono')
                a = a+5
                b=b+5
                print(df3[a:b])
            if preg2==1:
                break   
        else:  
            print('El valor ingresado no es valido')
            True
seconds = time.process_time()
print("Seconds since epoch = {}".format(seconds))    

