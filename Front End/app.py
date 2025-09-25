import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Smart Polling App")

response=requests.get(f"{API_URL}/poll/options")
options=response.json()

option_dict={opt['option']:opt['id'] for opt in options}

selected_option=st.selectbox("Choose an option to vote:", list(option_dict.keys()))

if st.button("Vote"):
    option_id=option_dict[selected_option]
    response=requests.put(f"{API_URL}/poll/vote/{option_id}")
    
    if response.status_code==200:
        st.success("Vote recorded successfully!")
    else:
        st.error("Failed to record vote.")
        
if st.button("View Results"):
    response=requests.get(f"{API_URL}/poll/results")
    
    if response.status_code==200:
        results=response.json()
        st.subheader("Poll Results:")
        total_votes=sum(opt['votes'] for opt in options)
        for opt in options:
            percentage=(opt['votes']/total_votes)*100 if total_votes>0 else 0
            st.write(f"{opt['option']}: {opt['votes']} votes ({percentage:.2f}%)")
    else:
        st.error("Failed to fetch results.")

