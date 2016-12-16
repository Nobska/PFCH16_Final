# PFCH16_Final
Write a Python script that will extract selected XML metadata from an EAD encoded finding aid and export it as a CSV file.
First, export the XML EAD finding aid file.
Then, drill down through the hierarchy of nested EAD elements to the metadata elements you want to extract.
Next, create a Python file and import the ElementTree Class from the xml.etree module and the csv module, and ask the xml module to load the xml file and parse it.
Then, loop through the XML file to get to your nested metadata: unittitle, unitdate, and container.
Export that metadata to a CSV file, which can accompany items being sent to the Internet Archive for scanning.
Use Python command module to convert all of this script to one command line that can easily run without extensive coding.
