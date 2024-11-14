# simplewebscraper
This is a simple web scraper to hit a website and download the parent and child pages to html files for processing into a RAG pipeline for embeddings and into a Vector Database/Store.

In any good AI and RAG application, you need to have a good dataset so scraping is critical for our Generative AI Applications. This is the simplest version that will save everything into the data directory which will hold numerous html files. If you later use LlamaIndex, you can use the simpledirectory loader to load these into a document.

The simple app can be run from the command line from most linux distributions but remember to chmod+x on the file so that it can be executed. You will also need to install all libraries in the requirements.txt.

Basic Usage:
#Providing the page to explicitly to scrape.
./scraper.py https://docs.llamaindex.ai/en/stable/examples/output_parsing/guidance_sub_question/

#If no settings are provided - it will default to the page variable, default_url which is by default set to:
https://docs.llamaindex.ai/en/stable/examples/

#Optional Switches:
--t This Sets the time to wait before scraping the page - default is 2s if none is provided.
