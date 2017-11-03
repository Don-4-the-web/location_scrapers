import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class webScrapeAutomation():
	
	def __init__(self):
		self.driver = None

	def RunTest(self):
		self.setupSelenium()
		self.loginToSite()
		self.cleanUpBrowser()

	def setupSelenium(self):
		self.driver = webdriver.Chrome('./chromedriver')

	def loginToSite(self):
		zipCodeSearch = [90045, 91010]
		location = "https://www.mcdonalds.com/us/en-us/restaurant-locator.html?submit=true&radiusSelected=5&searchText="
		listviewString = "#rl-listView"
		time.sleep(1)

		try:
			for eachZip in zipCodeSearch:
				stringZip = str(eachZip)
	
				self.driver.get(location + stringZip)
				self.stopAdDrop()
				self.goToListView()
				self.getNumberNearYou()
				self.findElements()
				self.printOutList()
		except:
			pass


		#print('Selenium works')

	def stopAdDrop(self):
		try:
			self.alertGreeting = self.driver.find_element_by_xpath('//a[@class="close"]')
			self.alertGreeting.click()
		except: 
			pass

	def goToListView(self):

		self.listView = self.driver.find_element_by_id('tab-rl-listView')

		try:
			self.listView.click()
		except: 
			pass

	def getNumberNearYou(self):
		self.results = self.driver.find_element_by_class_name('results')
		self.locationNumber = (self.results.text).split()
		self.locNum2Num = self.locationNumber[0]
		self.resultsNum = int(self.locNum2Num)
		self.itemsInSegment = 5
		self.loadMoreTimes = math.ceil(self.resultsNum/self.itemsInSegment)
		print(self.loadMoreTimes)

		n = self.loadMoreTimes
		try:
			for counter in range(1, n):
				self.driver.find_element_by_class_name('load-more-btn').click()
		except:
			pass	

	def findElements(self):
		self.rowDataH3 = self.driver.find_elements_by_class_name('restaurant-location__title')
		self.rowDataH4 = self.driver.find_elements_by_class_name('restaurant-location__address')


	def printOutList(self):

		self.numItems = len(self.rowDataH3)

		try:
			for i in range(self.numItems):
				print(self.rowDataH3[i].text + ", " + self.rowDataH4[i].text)
		except:
			pass

	def cleanUpBrowser(self):
		self.driver.close()

if __name__ == "__main__":
	taskmaster = webScrapeAutomation()
	taskmaster.RunTest()# 


