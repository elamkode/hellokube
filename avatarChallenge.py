import re
import pdb
from selenium import webdriver


def openBrowser():
	driver=webdriver.Firefox()
	if driver:
		print("Browser driver was successful")
		driver.get('https://the-internet.herokuapp.com/dynamic_content')
		return driver
	else:
		print("Unable to get Browser driver handle")

def findLongestWord(allwordsList):
	allwordsList = sorted(allwordsList,key=len)
	longestWord=allwordsList[-1]
	print("Longest word is ",longestWord)
	return longestWord

def getDynamicContentsList(rawtext):
	match=re.search('^Dynamic(.*)click here\.(.*)Powered by Elemental Selenium',rawtext)
	dynamicText=match.group(2)
	return dynamicText.split()


if __name__ == '__main__':
	#Call the driver library
	driver=openBrowser()
	
	#Get all the Text contents
	raw_text=driver.find_element_by_xpath("html").text
	#Replace newline char
	raw_text=raw_text.replace('\n',' ')
	#get dynamic content
	#pdb.set_trace()
	dynamic_words_list=getDynamicContentsList(raw_text)
	longest_word=findLongestWord(dynamic_words_list)
	try:
	
		assert len(longest_word)>=10,"In Dynamic texts, No word is of 10 characters length"
		print("Elam: Test1 has passed the check and found a word of 10 chars under Dynamic Text")
	except AssertionError as error:
		print("Elam: Test1 failed\n..Lets move on to Test2")

	#Execute Test2

	#get images from the webpage
	images=driver.find_elements_by_tag_name('img')
	#breakpoint()
	images_list1=[]
	for image in images:
		#images_list1+=image.get_attribute('src')
		#print(image.get_attribute('src'))
		images_list1.append(image.get_attribute('src'))

	##Check for skull image
	#print("Images list:",images_list1)
	punisher_found=0
	for img in images_list1:
		#Based on image patterns Avatar-3.jpg is the filter image we want to look for
		if 'Avatar-3.' in img:
			print("Punisher image has silhouette skull in the chest")
			punisher_found=1
			break
	try:
		assert punisher_found == 0,"Punisher images not as expected"
		print("Elam: Test2 has passed and Punisher image checks are fine\n")
		driver.close()
	except AssertionError as error:
		print("Elam:Test2 failed\nPls try running the script again\n")
		driver.close()
		
## End of Program
