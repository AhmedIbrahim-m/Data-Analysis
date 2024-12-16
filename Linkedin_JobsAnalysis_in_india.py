import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np
import re


df = pd.DataFrame( pd.read_csv("C:/linkdin_Job_data.csv",encoding='ISO-8859-1'))
df.duplicated().sum()

percent_missing = df.isnull().sum() * 100 / len(df)

print(percent_missing)

#cleaning NA values
del df['ï»¿job_ID'],df['alumni'],df['Hiring_person'],df['hiring_person_link'],
df['company_id'],df["Column1"],df['job_details'],df['linkedin_followers'],
df['no_of_application'],df['posted_day_ago'],df['no_of_employ']

col_to_fill = ['location','work_type','full_time_remote','company_name','job']
for column in col_to_fill:
    f_mode = df[column].mode()[0]
    df[column].fillna(f_mode,inplace = True)

# this function finds the row with the match, 
#then replaces it with the specified job name 
#

def group_jobs(regex, job_name):
    unique_jobs = []
    for i in df['job']:
        unique_jobs.append(i)
    common_strings=[]
    for i in unique_jobs: 
        job = i
        if bool(re.match(regex,str(job), flags=re.IGNORECASE)):
            common_strings.append(job)
    df['job']=df['job'].replace(common_strings,job_name)
    # print(len(df["job"].unique()))

print(len(df["job"].unique()))
group_jobs(".*Data Analyst.*|.*Sr. Analyst.*|.*Senior Analyst.*", "Data Analyst")
group_jobs(".*Devops.*|.*Automation.*", "DevOps/Automation Engineer/SRE")
group_jobs(".*Data Engineer.*", "Data Engineer")
group_jobs(".*Business Analyst.*", "Business Analyst")
group_jobs(".*front.*|.*react.*", "Front End Developer")
group_jobs(".*back.*|.*Dotnet.*|.*net.*", "Backend Developer")
group_jobs(".*Data Scientist.*", "Data Scientist")
group_jobs(".*Quality.*Engineer.*", "QA Engineer/SDET")
group_jobs(".*Java.*|.*flutter.*|.*php.*|.*python.*", "Backend Developer")

#here we use a similar function to group job types with extra strings
def job_type (regex, job_type):
    unique_type = []
    for i in df['full_time_remote']:
        unique_type.append(i)
    common_strings=[]
    for i in unique_type: 
        full_time_remote = i
        if bool(re.match(regex,str(full_time_remote), flags=re.IGNORECASE)):
            common_strings.append(full_time_remote)
    df['full_time_remote']=df['full_time_remote'].replace(common_strings,job_type)
job_type("Full-time.*","Full-time")
job_type("Internship.*", "Internship")
job_type("Part-time.*", "Part-time")
job_type("Contract.*", "Contract")

# data visualization





common_type_jobs = df['work_type'].value_counts()


plt.figure(figsize=(10,6))
plot = sns.barplot(x = common_type_jobs.index , y=common_type_jobs.values ,width=0.8, edgecolor= 'black' , color='#ccc9c9')
plt.xlabel('Work Type')
plt.ylabel('Count')
plt.title('Most Work Types')
plt.legend()
plt.tight_layout()
plt.show()

location_counts = df['location'].value_counts()
location_counts = location_counts.head(10)
plot = sns.barplot(y= location_counts.index, x = location_counts.values)

plt.xlabel('Count')
plt.ylabel('Location')
plt.title('Most Common Job Locations')
plt.show()


job_counts = df['job'].value_counts()
job_counts = job_counts.head(10)

plt.figure(figsize=(10,6))
plot = sns.barplot(y= job_counts.index, x = job_counts.values)

plt.xlabel('Count')
plt.ylabel('Location')
plt.title('Most Common Professions')
plt.show()




filtered_df = df[df['job'] == 'Software Engineer']
location_counts = filtered_df['company_name'].value_counts().head(10)

plt.figure(figsize=(10, 6)) 

plt.barh(location_counts.index, location_counts.values, color='skyblue')  
plt.xlabel('Number of Job Postings', fontsize=12) 
plt.ylabel('Company Name', fontsize=12)
plt.title('Top Companies Hiring Software Engineers', fontsize=14) 
plt.tight_layout()  
plt.show()

filtered_df = df[df['job'] == 'Data Analyst']
location_counts = filtered_df['company_name'].value_counts().head(10)

plt.figure(figsize=(10, 6)) 

plt.barh(location_counts.index, location_counts.values, color='skyblue')  
plt.xlabel('Number of Job Postings', fontsize=12) 
plt.ylabel('Company Name', fontsize=12)
plt.title('Top Companies Hiring Data Analyst', fontsize=14) 
plt.tight_layout()  
plt.show()
