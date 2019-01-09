# Python, JSON, and Web APIs

### Short Description

This tutorial is an introduction to reading JSON data from a web based API with Python. It's aimed at programmers, data scientists, and data engineers who need to access data from RESTful web services, flat files, and other JSON based data sources. 

### Long Description

This tutorial is an introduction to reading, processing, and parsing with JSON documents with Python. 

JSON is a commonly used data format, consisting of key-value pairs stored in a nested tree structure. Because many web services return data in JSON format, data scientists and engineers frequently need to read, process, and parse JSON data using Python.

This tutorial will consist of a series of notebooks and tutorial exercises. Rather than discussing the JSON format in the abstract, participants will learn the structure of JSON documents by working directly with web APIs with Python. Through these exercises, participants will use the JSON API from the National Library of Medicine to:

1. Retrieve and view a JSON document from an API through a browser, using the service endpoint URL.

2. Review the concept of a dictionary in Python, and explore how a JSON tree can be represented as a dictionary in Python.

3. Read a JSON document into a Python dictionary using the Requests module, and retrieve individual key-value pairs through dictionary and list operations.

4. Investigate how to use conditionals and loops to parse JSON documents to extract specific key-value pairs. 

5. Learn how to use recursion to take advantage of the tree like structure of a JSON document. Exercises will include basic recursion concepts, followed by the use of recursion to extract all values corresponding to a particular key. 

6. (Optional). If time permits, participants will write a simple JSON web service and make the results available through a localhost endpoint using the Bottle framework. 

### Prerequisites

This tutorial is intended for participants who have basic programming experience with Python, including loops, conditionals, and lists. No previous experience with JSON is expected. Some familiarity with tree structures and recursion will help, but we will cover these concepts in the context of parsing JSON documents.  

## Workbooks

This tutorial consists of a series of notebooks. Further explanatory text is available in the notebook for each section or the tutorial. 

### Dictionaries.ipynb

How to create and use a dictionary in Python.  How to nest arrays and dictionaries in a dictionary, a common pattern in a JSON response.   

### APIRequest.ipynb

Using a spell checking web service from the National Library of Medicine, how to request data from an api endpoint.  How to include request parameters in a URL.  How to read and parse JSON reponse as a python dictionary.  

### Interactions.ipynb

Investigate a more elaborate JSON response by querying a National Library of Medicine api for drug interactions.

### InteractionList.ipynb

Using the interaction api, how to parse and select data from an api.

### Recursion.ipynb

Since dictionaries and JSON can contain tree like structures, it can be useful to understand how to use recursion to traverse, print, and search trees. This notebook contains a basic recursion example followed by an example using recursion to print all keys in a JSON document.  

### SimpleService.py

Use the bottle module to create a simple web sevice that returns JSON.  Read and parse your web service.

### InteractionService.py

Build on the simple service to provide a new api endpoint that provides a summary of drug interaction data from the NLM interactions api.  


