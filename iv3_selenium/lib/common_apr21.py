"""
Python module to test the IV3 UI using selenium.
"""

import sys
import time
import logging


from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get(self.iv3_url)
        time.sleep(3)

    def login(self):
	
        """ To login into the iv3 UI with correct username and password"""
        
        try:
            username = self.browser.find_element_by_name("username")
            username.send_keys(self.username)
            password = self.browser.find_element_by_name("password")
            password.send_keys(self.password)
            sign_in = self.browser.find_element_by_xpath("//*[@type='button']")
            sign_in.click()
	except NoSuchElementException:
	    LOGGER.error("No such an element exception")
        except Exception as err:
            LOGGER.error("Exception while login is:" % err)
	else:        
	    LOGGER.info("Successfully logged into the IV3 UI")

    def navigate_to_lighting_dashboard(self):
        
        """ To navigate to the lighting dashboard of iv3"""

        #try: 
        WebDriverWait(self.browser,30).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='App']/div[1]/div[1]/div/ul/li[1]/a")))
        lightDashboard = self.browser.find_element_by_xpath("//*[@id='App']/div[1]/div[1]/div/ul/li[1]/a")
	builder = ActionChains(self.browser)
	lighting = self.browser.find_element_by_xpath("//*[@id='App']/div[1]/div[1]/div/ul/li[1]/div/ul/li[3]/a")
	builder.move_to_element(lightDashboard).click(lighting).perform()
	time.sleep(5)

    def get_customer_list(self):
	
	""" To get the list of all the available customer under user """

 	cusElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='CUSTOMER']")
        time.sleep(10)
        #print "Customer elements are", cusElementList
        if cusElementList:
            return cusElementList
        else:
 	    LOGGER.error("No customers are found, so exiting")
            sys.exit(0)

    def expand_and_collapse_customer_name(self, customer_name):

	""" To expand and collapse the tree structure when required for the given customer"""

	cusElementList = self.get_customer_list()
	for cusElement in cusElementList:
	    if customer_name in cusElement.text:
 		cusElementTag = cusElement.find_elements_by_tag_name("i")
 		if cusElementTag:
		    cusElementTag[1].click()
		    time.sleep(10)
 	        break
	else:
	    LOGGER.warning("Customer %s is not found" % customer_name)

    def get_device_list(self, customer_name):

	""" To get the list of all devices under the specified customer."""
        
        # Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()	
        """
	cusElementList = self.get_customer_list()
        for cusElement in cusElementList:
	    if customer_name in cusElement.text:
		cusElementTag = cusElement.find_elements_by_tag_name("i")
                if cusElementTag:
                    # Expand the tree structure for the specified customer
		    cusElementTag[1].click()
                    time.sleep(10)
                    devElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='DEVICE']")
 		    actualDevList = []
                    for devElement in devElementList:
           		actualDevList.append(str(devElement.text))

                    # Collapse the tree stucture for the specified customer
		    # To do
                    print "Actual Device list is", actualDevList
	            return actualDevList	    
        else:
            print "Customer %s is not found" % customer_name
	"""
	self.expand_and_collapse_customer_name(customer_name)
	devElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='DEVICE']")
	actualDevList = []
        for devElement in devElementList:
            actualDevList.append(str(devElement.text).split(' ')[2])

        # Collapse the tree stucture for the specified customer
        self.expand_and_collapse_customer_name(customer_name)
        #print "Actual Device list is", actualDevList
	LOGGER.info("Device list under customer: %s is:%s" % (customer_name, actualDevList))
        return actualDevList

	    	 
    def get_devices_under_customer_and_hierarchy(self, customer_name, hierarchy_names, level = None):
	
	""" To get the devices available under the hierarchy"""

	# Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()
	self.expand_and_collapse_customer_name(customer_name)
	if len(hierarchy_names) == 1:
	    hierarchy_name1 = hierarchy_names[0]
	    hierElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='HIERARCHY']")
	    if hierElementList:
		for hierElement in hierElementList:
	            if hierarchy_name1 in hierElement.text:
			tagEle = hierElement.find_elements_by_tag_name("i")
			tagEle[1].click()
			time.sleep(5)
			break
	elif len(hierarchy_names) == 2:
	    hierarchy_name1 = hierarchy_names[0]
	    hierarchy_name2 = hierarchy_names[1]
	    hierElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='HIERARCHY']")
	    if hierElementList:
		for hierElement in hierElementList:
		    if hierarchy_name1 in hierElement.text:
			tagEle = hierElement.find_elements_by_tag_name("i")
			tagEle[1].click()
			time.sleep(5)
			hierElementList1 = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='HIERARCHY']")
			if hierElementList1:
			    for hierElement in hierElementList1:
				if hierarchy_name2 in hierElement.text:
				    tagEle1 = hierElement.find_elements_by_tag_name("i")
			            tagEle1[1].click()
        	                    time.sleep(5)
	                            break
	elif len(hierarchy_names) == 3:
	    hierarchy_name1 = hierarchy_names[0]
            hierarchy_name2 = hierarchy_names[1]
            hierarchy_name3 = hierarchy_names[2]
	    hierElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='HIERARCHY']")
	    if hierElementList:
		for hierElement in hierElementList:
		    if hierarchy_name1 in hierElement.text:
			tagEle = hierElement.find_elements_by_tag_name("i")
			tagEle[1].click()
			time.sleep(5)
			hierElementList1 = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='HIERARCHY']")
			if hierElementList1:
			    for hierElement1 in hierElementList1:
				if hierarchy_name2 in hierElement1.text:
				    tagEle1 = hierElement1.find_elements_by_tag_name("i")
			            tagEle1[1].click()
        	                    time.sleep(5)
				    hierElementList2 = self.browser.find_elements_by_xpath(
							"//*[@data-hierarchy-type='HIERARCHY']")
				    if hierElementList2:
					for hierElement2 in hierElementList2: 
					    if hierarchy_name3 in hierElement2.text:
					 	tagEle2 = hierElement2.find_elements_by_tag_name("i")
						tagEle2[1].click()
	                                        time.sleep(5)

	else:
	    LOGGER.warning("Hierarchy level is not specified")

	devElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='DEVICE']")
	actualDevList = []
	for devElement in devElementList:
	    actualDevList.append(str(devElement.text).split(' ')[2])
	# Collapse the tree stucture for the specified customer
        self.expand_and_collapse_customer_name(customer_name)
	LOGGER.info("Device list under customer: '%s' and hierarchy level %s is: %s" % (
			customer_name, len(hierarchy_names), actualDevList))
	return actualDevList

    def get_last_device_for_last_customer(self, customer_name):
	"""
	To get the last device for the last customer.
	"""
	
	# Navigate to the Lighting Dashboard
        self.navigate_to_lighting_dashboard()

	# get the customer list
	cusElementsList = self.get_customer_list()
	if customer_name in cusElementsList[-1].text:
	    actualLastCustomer = cusElementsList[-1].text.split(' ')[0]
	    LOGGER.info("Actual last customer is: '%s' and the Expected last customer is: '%s'" % (
			actualLastCustomer, customer_name))
	    tagEle = cusElementsList[-1].find_elements_by_tag_name("i")
	    tagEle[1].click()
	    time.sleep(5)
	    # Get device last to get the last customer
	    devElementList = self.browser.find_elements_by_xpath("//*[@data-hierarchy-type='DEVICE']")
            if devElementList:
                actualLastDevice = str(devElementList[-1].text).split(' ')[2]
                # Collapse the tree stucture for the specified customer
                self.expand_and_collapse_customer_name(customer_name)
		return actualLastDevice
	    
	else:
	    LOGGER.error("Actual last customer and the expected last customer is not matched")
	
			
        #self.expand_and_collapse_customer_name(customer_name)
	

    def logout(self):
	
	""" To logged out from th IV3 UI"""

	if self.browser:
	    try:
 	        logoutElement = self.browser.find_elements_by_xpath("//*[@id='App']/div[1]/div[2]/a")
	        logoutElement[0].click()
	    except Exception as err:
	        LOGGER.error("Error during logout is: %s", err)
	    else:
 	        LOGGER.info("Successfully logged out from IV3")		
