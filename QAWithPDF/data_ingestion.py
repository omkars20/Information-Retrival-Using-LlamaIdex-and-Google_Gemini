from llama_index.core import SimpleDirectoryReader
from llama_index.readers.web import SimpleWebPageReader
import sys
from exception import customexception
from logger import logging

def load_data(data,isWeb):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        print('loader1')
        if isWeb:
            documents = SimpleWebPageReader(html_to_text=True).load_data([data])
        else:
            loader = SimpleDirectoryReader(data)
            documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    