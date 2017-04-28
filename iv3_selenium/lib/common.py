"""
Python module to test the IV3 UI using selenium.
"""

import sys
import time
import logging


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#logging.basicConfig(filename='nosetests.log',level=logging.DEBUG)
LOGGER = logging.getLogger("IntelliView")
LOGGER.setLevel(logging.DEBUG)

# create the logging file handler
fh = logging.FileHandler("iv3.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
 
# add handler to logger object
LOGGER.addHandler(fh)

class Iv3BaseClass:

    def __init__(self, iv3_url, username, password):

        self.iv3_url = iv3_url
        self.username = username
        self.password = password
	
    def login(self):
	
        """ To login into the iv3 UI with correct username and password"""
    
	self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get(self.iv3_url)
        try:
            username = self.browser.find_element_by_name("username")
            username.send_keys(self.username)
            password = self.browser.find_element_by_name("password")
            password.send_keys(self.password)
            sign_in = self.browser.find_element_by_xpath("//*[@type='button']")
            sign_in.click()

	except NoSuchElementException as err:
	    LOGGER.error("Exception while login is: %s" % str(err))
        except TimeoutException  as err:
	    LOGGER.error("Exception while login is: %s" % str(err))
	except Exception as err:
	    LOGGER.error("Exception while login is: %s" % str(err))
	else:   
	    LOGGER.info("Successfully logged into the IV3 UI")

    def navigate_to_lighting_dashboard(self):
        
        """ To navigate to the lighting dashboard of iv3"""

        WebDriverWait(self.browser,30).until(EC.visibility_of_element_located(
					(By.LINK_TEXT, "DASHBOARD")))
        lightDashboard = self.browser.find_element_by_link_text("DASHBOARD")
	builder = ActionChains(self.browser)
	lighting = self.browser.find_element_by_xpath(
			"//*[@id='App']/div[1]/div[1]/div/ul/li[1]/div/ul/li[3]/a")
	builder.move_to_element(lightDashboard).click(lighting).perform()
	time.sleep(5)

    def navigate_to_lighting_diagnostic(self):
        
        """ To navigate to the lighting diagnostic page of iv3"""

        WebDriverWait(self.browser,30).until(EC.visibility_of_element_located(
					(By.LINK_TEXT, "DIAGNOSTIC")))
        lightDiagnostic = self.browser.find_element_by_link_text("DIAGNOSTIC")
	builder = ActionChains(self.browser)
	lighting = self.browser.find_element_by_xpath(
			"//*[@id='App']/div[1]/div[1]/div/ul/li[2]/div/ul/li[3]/a")
	builder.move_to_element(lightDiagnostic).click(lighting).perform()
	time.sleep(5)

    def get_customer_list(self):
	
	""" To get the list of all the available customer under user """

 	cusElementList = self.browser.find_elements_by_xpath(
				"//*[@data-hierarchy-type='CUSTOMER']")
        time.sleep(10)
        if cusElementList:
            return cusElementList
        else:
 	    LOGGER.error("No customers are found, so exiting")
            sys.exit(0)

    def expand_and_collapse_customer_name(self, customerName):

	""" To expand and collapse the tree structure when
	required for the given customer"""

	cusElementList = self.get_customer_list()
	for cusElement in cusElementList:
	    if customerName in cusElement.text:
 		cusElementTag = cusElement.find_elements_by_tag_name("i")
 		if cusElementTag:
		    cusElementTag[1].click()
		    time.sleep(10)
 	        break
	else:
	    LOGGER.error("Customer %s is not found" % customerName)

    def get_device_list(self, customerName):

	""" To get the list of all devices under the specified customer."""
        
        # Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()	
	self.expand_and_collapse_customer_name(customerName)
	devElementList = self.browser.find_elements_by_xpath(
				"//*[@data-hierarchy-type='DEVICE']")
	actualDevList = []
        for devElement in devElementList:
            actualDevList.append(str(devElement.text).split(' ')[2])

        # Collapse the tree stucture for the specified customer
        self.expand_and_collapse_customer_name(customerName)
	LOGGER.info("Device list under customer: %s is:%s" % (
					customerName, actualDevList))
        return actualDevList
 
    def get_hierarchy_levels(self, hierarchyNames):
	
	""" To expand the hierarchy level for all the hierarchies"""

	for hierarchyName in hierarchyNames:
	    hierElementList = self.browser.find_elements_by_xpath(
					"//*[@data-hierarchy-type='HIERARCHY']")
            if hierElementList:
                for hierElement in hierElementList:
                    if hierarchyName in hierElement.text:
                        tagEle = hierElement.find_elements_by_tag_name("i")
                        tagEle[1].click()
                        time.sleep(5)

    def get_devices_under_customer_and_hierarchy(self, customerName,
					hierarchyNames, default = None):
	
	""" To get the devices available under the hierarchy"""

	# Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()
	self.expand_and_collapse_customer_name(customerName)
	
	# To expand the each hierarchy levels
	self.get_hierarchy_levels(hierarchyNames)

	devElementList = self.browser.find_elements_by_xpath(
					"//*[@data-hierarchy-type='DEVICE']")
	actualDevList = []
	for devElement in devElementList:
	    if default == "Type":
		actualDevList.append(str(devElement.text))
	    else:
	        actualDevList.append(str(devElement.text).split(' ')[2])
	# Collapse the tree stucture for the specified customer
        self.expand_and_collapse_customer_name(customerName)
	LOGGER.info("Device list under customer: '%s' and hierarchy level %s is: %s" % (
			customerName, len(hierarchyNames), actualDevList))
	return actualDevList

    def get_last_device_for_last_customer(self, customerName):
	"""
	To get the last device for the last customer.
	"""
	
	# Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()

	# get the customer list
	cusElementsList = self.get_customer_list()
	if customerName in cusElementsList[-1].text:
	    actualLastCustomer = cusElementsList[-1].text.split(' ')[0]
	    LOGGER.info("Actual last customer is: '%s' and the Expected last customer is: '%s'" % (
			actualLastCustomer, customerName))
	    tagEle = cusElementsList[-1].find_elements_by_tag_name("i")
	    tagEle[1].click()
	    time.sleep(5)
	    # Get device last to get the last customer
	    devElementList = self.browser.find_elements_by_xpath(
					"//*[@data-hierarchy-type='DEVICE']")
            if devElementList:
                actualLastDevice = str(devElementList[-1].text).split(' ')[2]
                # Collapse the tree stucture for the specified customer
                self.expand_and_collapse_customer_name(customerName)
		return actualLastDevice
	    
	else:
	    LOGGER.error("Actual last customer and the expected last customer is mismatched")
	
    def get_device_count_customer(self, customerName):
        """
        To get the device count for the required customer
        """

        # Navigate to Lighting Dashboard
        self.navigate_to_lighting_dashboard()
        cusElementList = self.get_customer_list()
        for cusElement in cusElementList:
            if customerName in cusElement.text:
                actualDeviceCount = cusElement.text.split("(")[1].split(")")[0]
                LOGGER.info("Device count for customer: '%s' is: '%s'" % (
					customerName, actualDeviceCount))
                return int(actualDeviceCount)

    def get_device_count_hierarchy(self, customerName, hierarchyNames):
        """
        To get the device count which side tree showing for each hierarchy level.
        """

	# Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()
	
	self.expand_and_collapse_customer_name(customerName)
	
	device_count_hierarchy = []
        for hierarchyName in hierarchyNames:
            hierElementList = self.browser.find_elements_by_xpath(
					"//*[@data-hierarchy-type='HIERARCHY']")
            if hierElementList:
                for hierElement in hierElementList:
                    if hierarchy_name in hierElement.text:
			count = hierElement.text.split("(")[1].split(")")[0]
			LOGGER.info("Device count for hierarchy: '%s' under customer:"
				    " '%s' is: '%s'" % (hierarchyName, customerName, count))

			device_count_hierarchy.append(int(count))
			tagEle = hierElement.find_elements_by_tag_name("i")
                        tagEle[1].click()
                        time.sleep(5)
	self.expand_and_collapse_customer_name(customerName)
	return device_count_hierarchy

    def hover_over_device_name(self, deviceName):

	""" To hove over the device name"""

	eleToHoverOver = self.browser.find_element_by_link_text(deviceName)
	hoverOver = ActionChains(self.browser).move_to_element(eleToHoverOver)
	hoverOver.perform()
	time.sleep(5)
	toolTipInfo = eleToHoverOver.get_attribute('title')
	return toolTipInfo

    def get_tool_tip_info(self, customerName, deviceName, lightingPage, hierarchyNames):
	""" 
	To get the tool tip for the given device under specified customer and hierarcy level.
	"""

	# Navigate to Lighting Dashboard
        if lightingPage == 'DASHBOARD':
	    self.navigate_to_lighting_dashboard()
	elif lightingPage == 'DIAGNOSTIC':
	    self.navigate_to_lighting_diagnostic()

	# Go to the required customer
	self.expand_and_collapse_customer_name(customerName)

	# Expand the hierarchy levels
	if hierarchyNames:
	    self.get_hierarchy_levels(hierarchyNames)    

	# Mouse over the device name
 	toolTipInfo = self.hover_over_device_name(deviceName)
	self.expand_and_collapse_customer_name(customerName)
	#print "tooltip info is", toolTipInfo
	return toolTipInfo

    def search_for_string_old(self, searchString, searchOption):
	"""
        To search for the given string in side tree.
        """

	# Navigate to Lighting Dashboard
        self.navigate_to_lighting_dashboard()

        searchElement = self.browser.find_element_by_xpath(
                        "//input[@placeholder='Search / Filter']")
        searchElement.send_keys(searchString)
        searchElement.send_keys(Keys.ENTER)
        time.sleep(5)

	if searchOption == 'DEVICE':
	    actualSearchResult = {}
	    searchDevElement = self.browser.find_elements_by_xpath(
			"//*[@data-hierarchy-type='DEVICE'][@class='selected']")
	    searchResult = searchDevElement[0].text
            actualDeviceName = searchResult.split(' ')[2]
	    actualSearchResult['DEVICE_NAME'] = str(actualDeviceName)

	    # Look for the customer name in the search result
	    cusElementList = self.get_customer_list()
	    cusName = cusElementList[0].text
	    actualCustomer = cusName.split("(")[0].strip()
	    print "cus name is", actualCustomer
	    actualSearchResult['CUSTOMER_NAME'] = str(actualCustomer)

	    # Look for the hierarchy name in the search result
	    hierElement = self.browser.find_elements_by_xpath(
                        "//*[@data-hierarchy-type='HIERARCHY']")
	    print "hierarchylist", hierElement
	    if hierElement:
	        print hierElement[0].text
	        actualSearchResult['HIERARCHY_NAMES'] = str(hierElement[0].text).split('-')[0]
            else:
		actualSearchResult['HIERARCHY_NAMES'] = hierElement

            self.browser.find_element_by_xpath(
                        "//span[@data-action='reset-search']").click()

	    print "actual search result is", actualSearchResult

	    return actualSearchResult

    def search_for_string(self, searchString, searchOption):
	"""
	To search for the given string in side tree.
	"""

	# Navigate to Lighting Dashboard
	self.navigate_to_lighting_dashboard()
	
	searchElement = self.browser.find_element_by_xpath(
			"//input[@placeholder='Search / Filter']")
	searchElement.send_keys(searchString)
	searchElement.send_keys(Keys.ENTER)
 	time.sleep(5)

	if searchOption == 'DEVICE':
	    searchDevElement = self.browser.find_elements_by_xpath(
                                  "//*[@data-hierarchy-type='DEVICE'][@class='selected']")
	    searchResult = searchDevElement[0].text
	    actualDeviceName = searchResult.split(' ')[2]
	    self.browser.find_element_by_xpath(
	    		"//span[@data-action='reset-search']").click()
	    return actualDeviceName

	else:
	    searchElement = self.browser.find_element_by_class_name('results')
	    actualSearchResult = searchElement.text
	    self.browser.find_element_by_xpath(
                        "//span[@data-action='reset-search']").click()
	    return actualSearchResult

    def logout(self):
	
	""" To logged out from th IV3 UI"""

	try:
 	    logoutElement = self.browser.find_elements_by_xpath(
				"//*[@id='App']/div[1]/div[2]/a")
	    logoutElement[0].click()
	except Exception as err:
	    LOGGER.error("Error during logout is: %s", err)
	else:
 	    LOGGER.info("Successfully logged out from IV3")		
	self.browser.quit()
