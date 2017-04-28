import re
import time
import logging

from iv3_selenium.lib.common import Iv3BaseClass, LOGGER
from nose.tools import eq_, assert_in


IV3_URL = 'http://10.6.3.56'
#IV3_URL = 'http://a8af04780297a11e7aec506cfb63a5af-414812701.us-west-2.elb.amazonaws.com/'
USERNAME = 'jamaica'
PASSWORD = 'superuser'
BASE_CLASS = Iv3BaseClass(IV3_URL, USERNAME, PASSWORD)


class TestIv3CommonClass:
    """
    def __init__(self):

        iv3_url = 'http://10.6.3.56'
        #iv3_url = 'http://a9fb19f1b235111e7aec506cfb63a5af-1794047128.us-west-2.elb.amazonaws.com/'
        username = 'jamaica'
        password = 'superuser'
        self.base_class = Iv3BaseClass(iv3_url, username, password)
    """
    @classmethod
    def setup_class(cls):
	"""
	Setup module before each test suite run
	"""
	
	BASE_CLASS.login()

    @classmethod
    def teardown_class(cls):
  	"""
	Tear down module after each test suite completed.
	"""

	BASE_CLASS.logout()

    def verify_device_names(self, customerName, expectedDevList, actualDevList):
	"""
	To verify whether the Expected devices are available under
	the specified customer.
	"""

        # Get the list of available devices under the specified customer

        if type(actualDevList) == list: 
	    actualDevList.sort()
	eq_(expectedDevList, actualDevList,
		"Actual device list is not matched with the expected "
		"device list for customer: %s" % customerName)
 
    def verify_device_count(self, name, expectedDevCount, actualDevCount, option = None):
	"""
	To verify whether the expected number of devices are 
	avaiable under specified customer.
	"""
 		
	eq_(expectedDevCount, actualDevCount, "Actaul device count is not matched with the"
			"Expected device count for %s: %s" % (option, name))

    def verify_device_type(self, customerName, hierarchyNames, expectedDevType):
	"""
	To verify whether the device type matches with the expected device type.
	"""
	
	actualDeviceList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
                                            customerName, hierarchyNames, default = 'Type')
	for device in actualDeviceList:
	    assert_in(expectedDevType, device,
		"Device type for device '%s' is not as expected" % device)

    def verify_tool_tip_info(self, customerName, deviceName, expectedToolTipInfo,
		hierarchyNames = None, option = None):
	"""
	To verify the actual tool information with the expected information.
	"""
        lightingPage = 'DASHBOARD'
	actualToolTipInfo = BASE_CLASS.get_tool_tip_info(customerName, deviceName,
				lightingPage, hierarchyNames)
	actualToolTipDict = {}
	keyList = ['Serial Number', 'PLC Node ID', 'TCC ID', 'Product Family', 'Dim Level',
		   'Latitude', 'Longitude', 'Location', 'Zip Code', 'Pole ID']
	
	for key in keyList:
	    for line in actualToolTipInfo.splitlines():
	    	if key in line:
		    actualToolTipDict[key] = str(line.split(':')[1].lstrip())
	
	if option == expectedToolTipInfo:
	    if expectedToolTipInfo not in actualToolTipDict.keys():
		LOGGER.info("TCC ID not found for device: '%s' as expected" % deviceName)
		return
	    else:
		raise Exception("'%s' should not displayed in the device "
				"info for device: '%s'" % (expectedToolTipInfo, deviceName))
	for k, v in actualToolTipDict.iteritems():
	    eq_(expectedToolTipInfo[k], actualToolTipDict[k],
		"Device info mismatches for: %s for device: %s" % (k, deviceName))

    def verify_uninstall_date(self, customerName, deviceName, expectedUninstallDate,
				hierarchyNames = None):
	"""
	To get the validate the last transaction time for the uninstalled device.
	"""

        lightingPage = 'DIAGNOSTIC'
	actualToolTipInfo = BASE_CLASS.get_tool_tip_info(customerName, deviceName,
                                lightingPage, hierarchyNames)
	for line in actualToolTipInfo.splitlines():
            if 'Last Transaction Time' in line:
		remat = re.match(r'.*\S+:\s(.*)', line)
		if remat:
                    actualLastTransTime = remat.group(1)
                    eq_(expectedUninstallDate, actualLastTransTime,
				"Expected and Actual last transaction date"
                                                "mismatched for device: '%s'" % deviceName)

    def verify_search_result(self, searchString, expectedResult, searchOption):
	"""
	To verify the search result with the expected result.
	"""

	actaulSearchResult = BASE_CLASS.search_for_string(searchString, searchOption)
	eq_(expectedResult, actaulSearchResult, "Expected output not shown in the search result")	
