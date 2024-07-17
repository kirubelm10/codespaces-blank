import pandas as pd 
import numpy as np

df=pd.read_csv('adult.data.csv')

def Demographic_Data_Calculator ():

    v=df['race'].value_counts()


    men_age=df[df['sex'] == 'Male']
    st=men_age['age'].mean()
    print(st)

    Bachelors=df[df['education'] == 'Bachelors']
    Educate=df['education']
    ds=len(Bachelors)/len(Educate) * 100
    print(ds)

 
    Advanced_Edu=len(df[df['education'].isin(['Bachelors','Masters','Doctorate'])])
    UnAdvanced_Edu=len(df[~df['education'].isin(['Bachelors','Masters','Doctorate'])])
    Advanced_Edu=Advanced_Edu[type:object]
    amt=len(Advanced_Edu[Advanced_Edu.salary=='>50K'])
    unamt=len(UnAdvanced_Edu[UnAdvanced_Edu.salary=='>50K'])
    cv=round(amt/Advanced_Edu*100,1)
    cd=round(unamt/UnAdvanced_Edu*100,1)
    


    lol=df[df['salary'].str.contains('>50K')]
    vc=round(len(lol)/len(df) * 100, 1)


    bc=df['hours-per-week'].min()

 
    Hours_Per_Week=df[df['hours-per-week']==bc]
    Rich_workers=len(Hours_Per_Week[Hours_Per_Week.salary=='>50K'])/len(Hours_Per_Week) * 100
    vp=round(Rich_workers,1)

    Country=df['native-country'].value_counts()
    Country_Salary=df[df['salary']== '>50K']['native-country'].value_counts()
    highest=round(Country_Salary/Country * 100,1)
    highest=highest.sort_values(ascending=False)
    highest_c=highest.index[0]


    high=round((Country_Salary/Country * 100),1).max()

    Rich_Indian=df[(df['salary'] == '>50K')&(df['native-country'] == 'India')]
    Rich_Indian_Job=Rich_Indian['occupation'].value_counts()
    vs=Rich_Indian_Job.index[0]      








