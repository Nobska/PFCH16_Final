
#Import ElementTree Class from xml.etree module
import xml.etree.ElementTree as etree

#ask xml module to load xml file and parse it
tree = etree.parse('/Users/jrider/Desktop/Final_Project/NeumannFrederick.xml')

#return the root xml element and store it in root variable
root = tree.getroot()

#use for loop to loop through root element
for a_element in root:

	if 'archdesc' in a_element.tag:
		for a_element in archdesc:

			if 'dsc' in a_element.tag:

			print(a_element.tag)
		

			
#	print(a_element.attrib)
#	print(a_element.text)