# XML to JSON Conversion Assignment

## Overview

This repository contains the solution for the assignment to convert XML files into JSON format. The objective was to create a Python script that reads XML files from a specified directory, converts their content into JSON format. As well created a SQLite database.

## Approach

1. **Understanding Requirements**:
   - Analyzed the assignment requirements to determine the necessary functionalities: reading XML files, converting them to JSON, and storing both formats in a database.

2. **Setting Up Environment**:
   - Installed necessary libraries such as `xmltodict` for XML parsing and python.
   - Installed the python with required libraries to conver the XML files into the JSON formate.

3. **Implementation**:
   - Developed a Python script that:
     - Reads all XML files from a specified directory.
     - Parses each XML file and converts it into a JSON format.

## Challenges Faced

- **XML Structure Variability**: 
  - Different XML files had varying structures, which required careful handling during parsing to ensure accurate conversion to JSON.
- **Python Library Dependencies**:
  - Faced issues related to library dependencies, particularly with `xmltodict`.
  - Ensuring that all required libraries were installed and compatible with my Python version took additional time.
 
- **Error Handling**: 
  - Implementing robust error handling to manage issues such as file read errors or database insertion failures was crucial for stability.

- **Python Library Dependencies**:
  - Faced issues related to library dependencies, particularly with `xmltodict`. Ensuring that all required libraries were installed and compatible with my Python version took additional time. This was resolved by creating a virtual environment and managing dependencies effectively.

## Errors Encountered

- **File Not Found Error**:
  - Initially faced issues with file paths when trying to read XML files. Resolved by ensuring correct directory paths were used in the script.
Traceback (most recent call last):
File "C:\Users\hreddy\Downloads\xml-files\XML_JSON.py", line 71, in <module>
convert_all_xml_to_json()
~~~~~~~~~~~~~~~~~~~~~~~

Traceback (most recent call last):
File "C:\Users\hreddy\Downloads\xml-filesScript\XML_JSON.py", line 71, in <module>
convert_all_xml_to_json()
~~~~~~~~~~~~~~~~~~~~~~~^^
File "C:\Users\hreddy\Downloads\xml-filesScript\XML_JSON.py", line 66, in convert_all_xml_to_json
convert_xml_to_json(xml_file_path, json_file_path)
~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\hreddy\Downloads\xml-filesScript\XML_JSON.py", line 35, in convert_xml_to_json
data_dict = xmltodict.parse(xml_content)
File "C:\Users\hreddy\AppData\Roaming\Python\Python313\site-packages\xmltodict.py", line 359, in parse
parser.Parse(xml_input, True)
~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
xml.parsers.expat.ExpatError: not well-formed (invalid token): line 8, column 4
