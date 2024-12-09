import pickle
import streamlit as st
import utility_funct

model=pickle.load(open(r'src/pickle_files/model3.pkl','rb'))
# preproc=pickle.load(open(r'C:\Users\LENOVO\OneDrive\Desktop\MY_PROJECT_ML\src\pickle_files\preprocess_func.pkl','rb'))
vectoriser=pickle.load(open(r'src/pickle_files/vectoriser.pkl','rb'))

st.title('EMAIL SPAM CLASSIFIER')
input_sms=st.text_input('input your message here')
if st.button('predict'):
    preprocessed_text=utility_funct.data_preprocessing(input_sms)
    preprocessed_text = [preprocessed_text]
    vectorised_input=vectoriser.transform(preprocessed_text).toarray()

    output=model.predict(vectorised_input)

    if output==1:
        st.text('mail is spam')
    else:
        st.text('mail is not spam')
        
