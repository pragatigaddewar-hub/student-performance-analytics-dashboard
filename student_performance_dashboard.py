import streamlit as st

st.title("Student Performance Analytics Dashboard")

with st.form("Student Performance"):
    st.subheader("Student Information")

    name = st.text_input("Student Name :")
    age = st.number_input("Age :")
    gender = st.radio("Gender",
                    ["Male","Female","Other"])

    st.subheader("Subject Marks")

    python = st.number_input("Python :",min_value=0,max_value=100)
    sql = st.number_input("SQL :",min_value=0,max_value=100)
    statistics = st.number_input("Statistics :",min_value=0,max_value=100)
    pandas = st.number_input("Pandas :",min_value=0,max_value=100)

    submit = st.form_submit_button("Submit")
    if submit:
        st.write("Student Information")
        st.write("Student Name :",name)
        st.write("Age :",age)
        st.write("Gender :",gender)

        st.write("Subject Marks")

        st.write("Python :",python)
        st.write("SQL :",sql)
        st.write("Statistics :",statistics)
        st.write("Pandas :",pandas)

st.subheader("Performance Calculation")

total_marks = python + sql + statistics + pandas
avg_marks = total_marks / 4
percentage = (total_marks/400) * 100

st.write("Total Marks :" ,total_marks)
st.write("Average Marks :" ,avg_marks)
st.write("Percentage :" ,percentage)


st.subheader("Subject Analysis")

marks = {
    "Python"      : python ,
    "SQL"         : sql ,
    "Statistics"  : statistics ,
    "Pandas"      : pandas
   }

highest_marks = max(marks , key = marks.get)
lowest_marks = min(marks , key = marks.get)

st.write("Highest Scoring Subject :" ,highest_marks)
st.write("Lowest Scoring Subject :" ,lowest_marks)
st.write("Python :" ,python)
st.write("SQL :" ,sql)
st.write("Statistics :" ,statistics)
st.write("Pandas :" ,pandas)

st.subheader("Grade")

if percentage >=90:
    grade = 'A+'
    st.write("A+")
elif percentage >=80:
    grade = 'A' 
    st.write("A")  
elif percentage >=70:
    grade = 'B'
    st.write("B")    
elif percentage >=60:
    grade = 'C'
    st.write("C")    
elif percentage >=50:
    grade = 'D'
    st.write("D")    
else:
     grade = 'E'
     st.write("Fail")    


st.subheader("Result Status")

if percentage >=50:
    result = 'Pass'
    st.write("Pass")
else:
    result = 'Fail'
    st.write("Fail")    

st.subheader("Performance Category")    

if percentage >=90:
    performance = "Excellent"
    st.write("Excellent")
elif percentage >=80:
    performance ="Good"
    st.write("Good")  
elif percentage >=70:
    performance = "Average"
    st.write("Average")    
else: 
    performance = "Needs Improvement"
    st.write("Needs Improvement")    


st.subheader("Visualization")

import matplotlib.pyplot as plt

subjects = ["Python","SQL","Statistics","Pandas"]
fig , ax = plt.subplots()
ax.bar(subjects,marks.values())
ax.set_xlabel("Subjects")
ax.set_ylabel("Marks")
ax.set_title("Subject-wise Performance")
st.pyplot(fig)

st.subheader("Performance Summary")

st.write("Student Name :" ,name)
st.write("Percentage :" ,percentage)
st.write("Grade :" ,grade)
st.write("Result :" ,result)
st.write("Strongest Subject :" ,highest_marks)
st.write("Weakest Subject :" ,lowest_marks)
st.write("Performance Category :" ,performance)

report =f'''
    Student Name : {name}
    Age : {age}
    Gender : {gender}
    Python Marks : {python}
    SQL Marks : {sql}
    Statistics Marks : {statistics}
    Pandas Marks : {pandas}
    Total Marks : {total_marks}
    Average Marks : {avg_marks}
    Percentage : {percentage}
    Grade : {grade}
    Result : {result}
    Strongest Subject : {highest_marks}
    Weakest Subject : {lowest_marks}
    Performance Category : {performance}'''

st.download_button("Download Student Report",data=report)

    