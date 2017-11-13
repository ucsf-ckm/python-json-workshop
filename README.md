# python-json-workshop

This repository contains teaching notes for a UCSF data science initiative workshop on reading data in JSON format from a web based API.  The workshop covers using and creating JSON based web services in Python. The first part reviews the dictionary data structure, connecting to a URL for a web service, and parsing JSON.  The second part reviews creating a web service using the bottle module.  

### Dictionaries.ipynb
How to create and use a dictionary in Python.  How to nest arrays and dictionaries in a dictionary, a common pattern in a JSON response.  

### UCSFProfilesJSON.ipynb

How to request data from an api endpoint.  How to include request parameters in a URL.  How to read and parse JSON reponse as a python dictionary. Example code uses the json api for the the UCSF profiles web service, available through the UCSF Clinical and Translational Sciences Institute (CTSI).  

### APIRequest.ipynb

Using a spell checking web service from the National Library of Medicine, how to request data from an api endpoint.  How to include request parameters in a URL.  How to read and parse JSON reponse as a python dictionary.  

### Interactions.ipynb

Investigate a more elaborate JSON response by querying a National Library of Medicine api for drug interactions.

### InteractionList.ipynb

Using the interaction api, how to parse and select data from an api.

### SimpleService.py

Use the bottle module to create a simple web sevice that returns JSON.  Read and parse your web service.

### InteractionService.py

Build on the simple service to provide a new api endpoint that provides a summary of drug interaction data from the NLM interactions api.  
