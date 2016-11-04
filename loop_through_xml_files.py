
#Here we are importing the ElementTree Class from the xml.etree module, we ask python to refer to it as etree
import xml.etree.ElementTree as etree
import glob

xmlfiles = glob.glob("/path/to/ead/*.xml")


for a_xml in xmlfiles:
	#ask the xml module to load the xml file and parse it
	tree = etree.parse(a_xml)

	#return the root xml element and store it into the root variable
	root = tree.getroot()


	for a_element in root:


		if a_element.tag == "{http://www.loc.gov/mods/v3}abstract":
			print (a_element.text)