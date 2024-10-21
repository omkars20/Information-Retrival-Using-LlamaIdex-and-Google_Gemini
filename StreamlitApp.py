import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
import os
import tempfile
import uuid
import shutil
from llama_index.core import SummaryIndex
def main():
    def cleanup():
        if 'user_folder' in st.session_state and os.path.exists(st.session_state['user_folder']):
            shutil.rmtree(st.session_state['user_folder'])
    st.set_page_config("QA with Documents")
    st.markdown('<h2 style="text-align: center;padding:0px">🤖 WebDoc-Bot</h2>', unsafe_allow_html=True)
    st.header("Document & WebURL-Based Q&A Chatbot")
    cleanup()
    temp_dir = 'Data'
    st.markdown('<p class="custom-label">Upload your documents:</p>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("", 
                                  type=['pdf', 'docx', 'txt'], 
                                  accept_multiple_files=True)
    
    # If files are uploaded
    if uploaded_files:
        # Ensure that 'uploaded_files' and 'user_folder' are initialized in session state
        if 'uploaded_files' not in st.session_state:
            st.session_state['uploaded_files'] = []

        if 'user_folder' not in st.session_state:
            # Generate a unique folder name for each session
            st.session_state['user_folder'] = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))

        # Create the unique session folder if it doesn't exist
        if not os.path.exists(st.session_state['user_folder']):
            os.makedirs(st.session_state['user_folder'])
        for uploaded_file in uploaded_files:
            # Save files into the unique session-based folder
            file_path = os.path.join(st.session_state['user_folder'], uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Store the file paths in session state for later use
            if file_path not in st.session_state['uploaded_files']:
                st.session_state['uploaded_files'].append(file_path)
        temp_dir = st.session_state['user_folder']

        st.success(f"Uploaded {len(uploaded_files)} files.")
        
    # doc=st.file_uploader("upload your document")
    st.markdown("""
    <style>
    .custom-label {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: -100px;
        color: #4CAF50; /* Example green color */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h6 style="text-align: center;">Or</h6>', unsafe_allow_html=True)

    st.markdown('<p class="custom-label">Enter the URL:</p>', unsafe_allow_html=True)
    user_URL = st.text_input("", placeholder="https://example.com")
    
    
    
    
    st.markdown('<p class="custom-label">Ask your question:</p>', unsafe_allow_html=True)
    user_question= st.text_input("",placeholder='Type your question...')
    st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green background */
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        cursor: pointer;
        transition-duration: 0.4s;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Shadow */
    }

    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
        box-shadow: 0px 8px 12px rgba(0, 0, 0, 0.4); /* Increase shadow on hover */
        transform: scale(1.05); /* Slightly increase the size */
    }
    </style>
    """, unsafe_allow_html=True)
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            isWeb = False
            if user_URL:
                temp_dir = user_URL
                isWeb = True
            document=load_data(temp_dir,isWeb)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
            st.markdown('<p class="custom-label">Response from Bot:</p>', unsafe_allow_html=True)
            if user_URL:
                index = SummaryIndex.from_documents(document)
                # set Logging to DEBUG for more detailed outputs
                query_engine = index.as_query_engine()
                response = query_engine.query(user_question)
                # st.write(response.response)
                
            else:
                response = query_engine.query(user_question)
                    
            st.text_area("", value=response.response, height=300)
            cleanup()

    # st.markdown('<h6 style="text-align: center;margin-top:20px;">Made by Karan Shrestha with ❤️</h6>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .footer {
        text-align: center;
        margin-top: 20px;
    }
    .footer-icons {
        display: inline-block;
        margin-left: -40px;
        margin-top: -20px;
    }
    .footer-icons a {
        color: #000;
        text-decoration: none;
        margin: 0 10px;
        font-size: 24px;
    }
    .footer-icons a:hover {
        color: #0072b1; /* Hover color for LinkedIn */
    }
    .footer-icons a.github:hover {
        color: #333; /* Hover color for GitHub */
    }
    </style>

    <div class="footer">
        <h6>Made by Omkar singh with ❤️</h6>
        <div class="footer-icons">
            <a href="https://github.com/omkars20" target="_blank" class="github">
                <i class="fab fa-github"></i>
            </a>
            <a href="https://www.linkedin.com/in/omkar-singh-8976767220/" target="_blank">
                <i style="color:#0a66c2;" class="fab fa-linkedin"></i>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add Font Awesome for icons
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        """, unsafe_allow_html=True)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    
