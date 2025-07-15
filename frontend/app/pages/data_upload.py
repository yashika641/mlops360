import streamlit as st
import requests
import tempfile
import os 

def render():
    try:
        st.title("Data Upload")
        API_URL = "http://localhost:8000/upload"
        uploaded_file= st.file_uploader("*choose a file to upload [in **csv** or **xlsx**]",type=["csv", "xlsx"])
        
        if uploaded_file is not None:
            
            st.success(f'file selected: {uploaded_file.name}')
            
            if st.button("Upload"):
                with st.spinner("Uploading...."):
                    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                        tempfile.write (uploaded_file.getvalue())
                        temp_fiel_path = tmp_file.name
                        
                    with open(temp_fiel_path, "rb") as f:
                        files = {'file': (uploaded_file.name, f, uploaded_file.type)}
                        response = requests.post(API_URL, files=files)
                        if response.status_code == 200:
                            data=response.json()
                            st.success("File uploaded successfully!")
                            st.write("🗂️ File URL:", data.get("file_url"))
                            st.write("🧠 Result:", data.get("message"))
                            
                        else:
                            st.error(f"Failed to upload file: {response.status_code} - {response.text}")
    except FileNotFoundError:
                        st.error("Temporary file not found. Please try again.")
    except requests.exceptions.RequestException as e:
                        st.error(f"Request failed: {e}")
    finally:
                        if os.path.exists(temp_fiel_path):
                            os.remove(temp_fiel_path)
