
#Import ElementTree Class from xml.etree module
import xml.etree.ElementTree as etree

#import csv module
import csv

#ask xml module to load xml file and parse it
tree = etree.parse('/Users/jrider/Desktop/Final_Project/NeumannFrederick.xml')

#return the root xml element and store it in root variable
root = tree.getroot()

#use for loop to loop through root element
for a_element in root:

	if 'archdesc' in a_element.tag:

		for another_element in a_element:

			if 'dsc' in another_element.tag:

				for still_another_element in another_element:

					if 'c01' in still_another_element.tag:

						for yet_another_element in still_another_element:

							if 'c02' in yet_another_element.tag:

								for one_more_element in yet_another_element:

									if 'did' in one_more_element.tag:

										for even_one_more_element in one_more_element:

											if 'unittitle' in even_one_more_element.tag:

												print(even_one_more_element.text)

											if 'unitdate' in even_one_more_element.tag:
												
												print(even_one_more_element.text)

											if 'container' in even_one_more_element.tag:
												
												print(even_one_more_element.attrib['type'])

												#create file called metadata.csv with contents of arrayofdata and write each row as writerow.
												arrayofdata=['unittitle','unitdate','container']
																										
												with open('metadata.csv', 'w') as csvfile:
													metadatawriter = csv.writer(csvfile, delimiter='')
													for row in arrayofdata:
														metadatawriter.writerow(row)



											
		
