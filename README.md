# simplewebscraper
This is a simple web scraper to hit a website and download the parent and child pages to html files for processing into a RAG pipeline for embeddings and into a Vector Database/Store.

In any good AI and RAG application, you need to have a good dataset so scraping is critical for our Generative AI Applications. This the simplest version that will save everything into the data directory which will hold numerous html files. If you later use LlamaIndex, you can use the simpledirectory loader to load these into a document.

The simple app can be run from the command line from most linux distributions but remember to chmod+x on the file so that it can be executed. You will also need to install all libraries in the requirements.txt.

Basic Usage:
