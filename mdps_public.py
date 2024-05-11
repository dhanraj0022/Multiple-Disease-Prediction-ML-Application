import pickle
import streamlit as st
from streamlit_option_menu import option_menu 
import sklearn
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(dir_path, 'Diabetes_trained_model.sav')

diabetes_model = pickle.load(open(model_path, 'rb'))

heart_disease_model = pickle.load(open('heart_disease_predictions.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinson_trained_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        bmi = st.slider("Enter body mass index",12.02,94.85)
        
    with col2:
        Smoking=st.selectbox("your Smoking status yes=1,or no=0",[1,0])
        
    with col3:
         AlcoholDrinking=st.selectbox("your alcohol drinking status yes=1,or no=0",[1,0])
        
    with col1:
        Stroke=st.selectbox("your Stroke status yes=1,or no=0",[1,0])
        
    with col2:
        PhysicalHealth=st.slider("Enter PhysicalHealth",0.0,30.0,0.1) 

    with col3:
        MentalHealth=st.slider("Enter MentalHealth",0.0,30.0,0.1)
        
    with col1:
        DiffWalking=st.selectbox("your DiffWalking status yes=1,or no=0",[1,0])
        
    with col2:
        Sex=st.selectbox("(1=Male,0=Female)",[1,0])
        
    with col3:
        AgeCategory=st.selectbox("(55-59,80 or older, 65-69, 75-79, 40-44,70-74,60-64, 50-54, 45-49, 18-24, 35-39,30-34,25-29)",[ 7, 12, 9, 11, 4, 10,8,6,5,0,3,2,1])
        
    with col1:
        Race=st.selectbox("(White=5, Black=4, Asian=3, American Indian/Alaskan Native=2,Other=1, Hispanic=0)",[5,4,3,2,1,0])
        
    with col2:
        Diabetic=st.selectbox("your Diabetic status yes=1,or no=0",[1,0])

    with col3:
         PhysicalActivity=st.selectbox("your PhysicalActivity status yes=1,or no=0",[1,0])
        
    with col1:
        GenHealth=st.selectbox("(Very good=4, Fair=3, Good=2, Poor=1, Excellent=0)",[4,3,2,1,0])
        
    with col2:
        SleepTime=st.slider("Enter your sleeptime",1.0,24.0,1.0)

    with col3:
        Asthma=st.selectbox("your Asthma status yes=1,or no=0",[1,0])

    with col1:
        KidneyDisease=st.selectbox("your KidneyDiseas status yes=1,or no=0",[1,0])
    with col2:
        SkinCancer=st.selectbox("your SkinCancer status yes=1,or no=0",[1,0])
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[bmi, Smoking, AlcoholDrinking, Stroke,
       PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory,
       Race, Diabetic, PhysicalActivity, GenHealth, SleepTime,
       Asthma, KidneyDisease, SkinCancer]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
















