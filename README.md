
# WebDoc-Bot: Document & WebURL-Based Q&A Chatbot

This project implements an AI-powered document and URL-based Q&A system using LlamaIndex and Google Gemini for information retrieval, deployed on Streamlit.

CheckOut the Project here:  https://info-retrieval.streamlit.app/

![image](https://github.com/user-attachments/assets/9ce6c812-d618-4cae-8682-c7c2e85e3a42)     ![image](https://github.com/user-attachments/assets/803f01da-8db6-48a1-afab-c07c3118884a)

![image](https://github.com/user-attachments/assets/eb63d0bd-7503-42b6-9f2c-bdfc56817752)




## Features

- Upload documents in PDF, DOCX, and TXT formats for Q&A processing.
- Provide web URLs for the bot to extract information and answer questions.
- Answers questions using a combination of LlamaIndex and Google Gemini's language models.
- Simple and intuitive user interface, built with Streamlit.

## Requirements

Before you start, make sure you have installed:

```bash
pip install streamlit llama-index google-gemini-api PyPDF2 python-docx pandas matplotlib seaborn
```

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/webdoc-bot.git
   cd webdoc-bot
   ```

2. **Set Up API Keys**

   Create a `.env` file and add your Google Gemini API Key and other necessary credentials for authentication.

   ```bash
   GOOGLE_GEMINI_API_KEY=your_api_key
   ```

3. **Run the Streamlit App**

   Start the Streamlit server using the following command:

   ```bash
   streamlit run app.py
   ```

4. **Upload Files or Provide a URL**

   Once the app is running, you can upload documents (PDF, DOCX, or TXT) or provide a web URL. The bot will process the content and answer your queries based on the retrieved data.


## How It Works

1. **Document and URL Upload:**
   - The user can upload a file (PDF, DOCX, TXT) or enter a web URL.
   
2. **Processing:**
   - Uploaded files are processed using LlamaIndex to extract relevant information.
   - URLs are scraped to extract content for answering questions.
   
3. **Query Processing:**
   - The user submits a question related to the content.
   - The question is processed using LlamaIndex, which interacts with Google Gemini for enhanced responses.

4. **Response Generation:**
   - The bot generates an answer to the question, utilizing both the document content and Google Gemini’s language model capabilities.
   - If applicable, the response includes data analysis or visualization based on the extracted content.

## Example Usage

- **Upload a PDF:**
  Upload a research paper and ask questions about specific sections or data.
  
- **Provide a Web URL:**
  Enter the URL of a blog post or technical article, and the bot will summarize or answer specific questions from it.

## Future Enhancements

- Adding support for more file types (e.g., Excel, PPTX).
- Improving answer accuracy with multi-document summarization.
- Enhancing the UI with better visualizations.

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request. Contributions are welcome!
