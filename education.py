
import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(layout= 'wide', page_title= 'egypt_education_dataset')
st.markdown("<h1 style='text-align: center; color: white;'>education dataset with Analysis</h1>", unsafe_allow_html=True)
st.image('https://www.edutrapedia.com/resources/thumbs/article_photos/TRhpJPbgYp-662.jpg_729x410.jpg')
df = pd.read_csv('cleand_data.csv',index_col=0)
page = st.sidebar.radio('Pages', ['Introduction', 'Analysis Questions', 'Reporting'])
if page == 'Introduction':

    st.dataframe(df.head())

    st.header('education_dataset Description')

    st.write('''Description: This dataset contains information about 50,000 students in Egypt, 
    including their personal details, parental education levels, type of education,
    and grades in various subjects.
    The data is synthetically generated to simulate real-world educational data and can be used for exploratory data analysis (EDA), 
    classification tasks, and regression analysis.:

    Student Name: The name of the student.
    Student Age: The age of the student, ranging from 14 to 18 years.
    Student Year: The year level of the student, ranging from Year 9 to Year 12.
    Father Degree: The highest educational degree obtained by the student’s father (None, High School, Bachelor, Master, PhD).
    Mother Degree: The highest educational degree obtained by the student’s mother (None, High School, Bachelor, Master, PhD).
    Education Type: The type of education the student is enrolled in (IGCSE, IB, Thanweya).
    Subject_1 to Subject_10: Grades for 10 different subjects, with values ranging from 20% to 100%, and a median around 75% - 80%.''')

elif page == 'Analysis Questions':

    st.header('Q1 What is the average performance per education type?')
    avg_by_edu_type = df.groupby('education type')['Average Score'].mean().round(2).reset_index()
    st.write(px.bar(data_frame= avg_by_edu_type ,x='education type', y='Average Score' , title= 'average performance for Average Score per education type'))
    st.write(''' #### Insight:
Yes average performance does vary slightly by education type
Students in the Thanweya system have the highest average performance followed closely by those in the IB and IGCSE systems   ''')
    st.header('Q2 Does the father’s education level affect student performance ?')
    aff_of_fath_per =df.groupby("father degree")["Average Score"].mean().sort_values(ascending= False).reset_index()
    st.write(px.box(data_frame= aff_of_fath_per  ,x='father degree', y='Average Score' , title= 'fathers education level affect student performance'))
    st.write(''' #### Yes, the father’s education level does appear to affect student performance.
Students whose fathers have higher education levels (e.g., PhD, Master) tend to score higher on average than those whose fathers have lower or no formal education. ''')
    st.header('Q3 Does the mother’s education level affect student performance ?')
    aff_of_moth_per = df.groupby("mother degree")["Average Score"].mean().sort_values(ascending= False).reset_index()
    st.write(px.scatter(data_frame= aff_of_moth_per ,x='mother degree', y='Average Score' , title= 'mothers education level affect student performance'))
    st.write(''' #### Yes, a mother's education level affects a student's performance. Analysis has shown that students whose mothers have a higher education (such as a doctorate or master's degree) perform better than their peers. ''')
    st.header('Q4 Does student age affect performance for ?')
    aff_age_per = df.groupby("student age")["Average Score"].mean().sort_values(ascending=False).reset_index()
    st.write(px.bar(data_frame= aff_age_per ,x='student age', y='Average Score' , title= 'effect of student age on performance'))
    st.write(''' Yes, a student's age appears to have some impact on performance.
* Students of certain ages (17-18 years) may perform better than those of younger or older ages.
* This may reflect academic or psychological maturity, or differences in academic level ''')
    st.header('Q5 Does student year affect student performance?')
    aff_stu_year_per = df.groupby("student year")["Average Score"].mean().sort_values(ascending=False).reset_index()
    st.write(px.scatter(data_frame= aff_stu_year_per ,x='student year', y='Average Score' , title= 'effect of student year on performance'))
    st.write(''' Yes, student year does affect student performance.
After grouping students by their academic year (Student Year) and calculating the average score across all subjects, we typically observe variations in performance between years. ''')
    st.header('Q6 Who are the top 10 students ? What are their characteristics ?')
    top_10_info = df.sort_values(by="Average Score", ascending=False).head(10)
    st.plotly_chart(px.bar(data_frame= top_10_info, x= 'student name', y= 'Average Score', barmode= 'group',
        color= 'education type'))
    st.write(''' #### Insight:
. These characteristics can be used to discover factors associated with excellence
• Students can be supported in similar circumstances to those that helped high achievers
• These analyses can be used to support educational decisions or improve performance in schools ''')

elif page == 'Reporting':
    education_type = st.sidebar.selectbox('education_type' ,df['education type'].unique())
    student_year = st.sidebar.selectbox('student_year', df['student year'].unique())
    father_degree = st.sidebar.selectbox('father_degree', df['father degree'].unique())
    mother_degree = st.sidebar.selectbox('mother_degree', df['mother degree'].unique())
    df2 = df[(df['father degree']== father_degree) & (df['education type'] == education_type) &(df['student year']== student_year) &(df['father degree']== father_degree)]
    st.dataframe(df2.head(50))
