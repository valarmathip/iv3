import logging

from test_common import *

class TestSideTreeDevicesClass(TestIv3CommonClass):


    def test_device_list_customer_level(self):
	"""
	Test Case ID:    IV-ST-DL-1
	Description:     Side Tree Validation - Lighting Dashboard - Device List - Customer Level
	Expected Output: Side Tree should display the following 4 devices under the customer "QA-AUTO-01"
			 SLC-DEVICE0001, SLC-DEVICE0002,SLC-DEVICE0003,SLC-DEVICE0004
 	"""
	
	CUSTOMER_NAME = 'QA-AUTO-01'
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0001', 'SLC-DEVICE0002', 'SLC-DEVICE0003', 'SLC-DEVICE0004']
	
        #actualDevList =	self.base_class.get_device_list(CUSTOMER_NAME)
        actualDevList =	BASE_CLASS.get_device_list(CUSTOMER_NAME)
        self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)
	
    def test_device_list_hierarchy_level1(self):
	"""
	Test Case ID:   IV-ST-DL-02
	Description:    Side Tree Validation - Lighting Dashboard - Device List - Hierarchy 1 Level
	Expected Ouput: Side Tree should display the following 5 devices under the customer "QA-AUTO-02" and
                        Hierarchy level 1 "PETRAINDIA"
                        SLC-DEVICE0005, SLC-DEVICE0006,SLC-DEVICE0007,SLC-DEVICE0008,SLC-DEVICE0009
        """
	
	CUSTOMER_NAME = 'QA-AUTO-02'
	HIERARCHY_NAMES = ['PETRAINDIA']
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0005', 'SLC-DEVICE0006', 'SLC-DEVICE0007',
				'SLC-DEVICE0008', 'SLC-DEVICE0009']
        
	actualDevList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
					CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)
 
    def test_device_list_hierarchy_level2(self):
	"""
	Test Case ID:   IV-ST-DL-03
	Description:    Side Tree Validation - Lighting Dashboard - Device List - Hierarchy 2 Level
	Expected Ouput: Side Tree should display the following 5 devices under the customer "QA-AUTO-03" and
                        Hierarchy level 2 "PETRACH" and "PETRAMP"
                        SLC-DEVICE00010, SLC-DEVICE00011, SLC-DEVICE00012, SLC-DEVICE00013,SLC-DEVICE00014,
			SLC-DEVICE00015.

        """
	
	CUSTOMER_NAME = 'QA-AUTO-03'
	HIERARCHY_NAMES = ['PETRACH', 'PETRAMP']
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0010', 'SLC-DEVICE0011', 'SLC-DEVICE0012',
				'SLC-DEVICE0013', 'SLC-DEVICE0014', 'SLC-DEVICE0015']
        
	actualDevList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
					CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)
 
    def test_device_list_hierarchy_level3(self):
	"""
	Test Case ID:   IV-ST-DL-04
	Description:    Side Tree Validation - Lighting Dashboard - Device List - 
			Hierarchy 3 Level under the Customer
	Expected Ouput: Side Tree should display the following 20 devices under the customer "QA-AUTO-04" and
                        Hierarchy level 3 "PETRAUS" and "PETRACA" and "PETRASANJOSE".
                        SLC-DEVICE0016, SLC-DEVICE0017, SLC-DEVICE0018, SLC-DEVICE0019,SLC-DEVICE0020,
                        SLC-DEVICE0021, SLC-DEVICE0022, SLC-DEVICE0023, SLC-DEVICE0024,SLC-DEVICE0025,
                        SLC-DEVICE0026, SLC-DEVICE0027, SLC-DEVICE0028, SLC-DEVICE0029,SLC-DEVICE0030,
                        SLC-DEVICE0031, SLC-DEVICE0032, SLC-DEVICE0033, SLC-DEVICE0034,SLC-DEVICE0035,

        """
	
	CUSTOMER_NAME = 'QA-AUTO-04'
	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0016', 'SLC-DEVICE0017', 'SLC-DEVICE0018', 'SLC-DEVICE0019',
				'SLC-DEVICE0020', 'SLC-DEVICE0021', 'SLC-DEVICE0022', 'SLC-DEVICE0023',
				'SLC-DEVICE0024', 'SLC-DEVICE0025', 'SLC-DEVICE0026', 'SLC-DEVICE0027',
				'SLC-DEVICE0028', 'SLC-DEVICE0029', 'SLC-DEVICE0030', 'SLC-DEVICE0031',
				'SLC-DEVICE0032', 'SLC-DEVICE0033', 'SLC-DEVICE0034', 'SLC-DEVICE0035']
	        
	actualDevList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
					CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)

    def test_device_list_for_two_customers(self):
	
	"""
	Test Case ID:   IV-ST-DL-06
	Description:    Side Tree Validation - Lighting Dashboard - Device List -  2 customers 
		   	(with 1 customer have all 3 hierarchy levels and another with 1 hierarchy levels)
	Expected Ouput: Side Tree should display 20 devices under the customer "QA-AUTO-04" and
                        Hierarchy level 3 "PETRAUS" and "PETRACA" and "PETRASANJOSE".
			and 4 devices under customer 'QA-AUTO-02' and hierachy level 1 "PETRAINDIA". 
        """
	
	CUSTOMER_NAME = 'QA-AUTO-04'
	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0016', 'SLC-DEVICE0017', 'SLC-DEVICE0018', 'SLC-DEVICE0019',
				'SLC-DEVICE0020', 'SLC-DEVICE0021', 'SLC-DEVICE0022', 'SLC-DEVICE0023',
				'SLC-DEVICE0024', 'SLC-DEVICE0025', 'SLC-DEVICE0026', 'SLC-DEVICE0027',
				'SLC-DEVICE0028', 'SLC-DEVICE0029', 'SLC-DEVICE0030', 'SLC-DEVICE0031',
				'SLC-DEVICE0032', 'SLC-DEVICE0033', 'SLC-DEVICE0034', 'SLC-DEVICE0035']
	        
	actualDevList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
					CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)

	CUSTOMER_NAME = 'QA-AUTO-02'
	HIERARCHY_NAMES = ['PETRAINDIA']
	EXPECTED_DEVICE_LIST = ['SLC-DEVICE0005', 'SLC-DEVICE0006', 'SLC-DEVICE0007',
				'SLC-DEVICE0008', 'SLC-DEVICE0009']
        
	actualDevList = BASE_CLASS.get_devices_under_customer_and_hierarchy(
					CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE_LIST, actualDevList)

    def test_check_device_list_for_last_customer(self):
	"""
        Test Case ID:    IV-ST-DL-07
	Description:     Side Tree Validation - Lighting Dashboard -Check the device list for the last customer 
			 (and verify last device in that customer)
	Expected Output: Side Tree should display the following 1 device under the last customer "QA-AUTO-04"
			 "SLC-DEVICE0020"
	"""

	CUSTOMER_NAME = 'QA-AUTO-04'
	EXPECTED_DEVICE = 'SLC-DEVICE0020'
        actaulLastDevice = BASE_CLASS.get_last_device_for_last_customer(CUSTOMER_NAME)
	self.verify_device_names(CUSTOMER_NAME, EXPECTED_DEVICE, actaulLastDevice)	

    def test_device_count_customer_level(self):
	"""
	Test Case ID:    IV-ST-DL-08
	Description:     Side Tree Validation - Lighting Dashboard - Device Count - Customer Level
	Expected Output: Side Tree should display Device Count 4 for the Customer "QA-AUTO-01".
	"""
	
	CUSTOMER_NAME = 'QA-AUTO-01'
	EXPECTED_DEVICE_COUNT = 4
	actualDeviceCount = BASE_CLASS.get_device_count_customer(CUSTOMER_NAME)
	self.verify_device_count(CUSTOMER_NAME, EXPECTED_DEVICE_COUNT, actualDeviceCount, option="customer")

    def test_device_count_customer_with_hierarchy_level1(self):
	"""
	Test Case ID:    IV-ST-DL-09
	Description:     Side Tree Validation - Lighting Dashboard - Device Count - Hierarchy 1 Level 
	Expected Output: Side Tree should display Device Count 5 for the Customer "QA-AUTO-02".
                         and Device Count 3 Hierarchy Level 1 "PetraIndia"

	"""

	CUSTOMER_NAME = 'QA-AUTO-02'
	EXPECTED_DEVICE_COUNT = 5
	actualDeviceCount = BASE_CLASS.get_device_count_customer(CUSTOMER_NAME)
	self.verify_device_count(CUSTOMER_NAME, EXPECTED_DEVICE_COUNT, actualDeviceCount, option="customer")

	HIERARCHY_NAMES = ['PETRAINDIA']
	EXPECTED_DEVICE_COUNT_HIERARCHY = 3
	actualDeviceCountHierarchy = BASE_CLASS.get_device_count_hierarchy(CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_count(HIERARCHY_NAMES[0], EXPECTED_DEVICE_COUNT_HIERARCHY,
				actualDeviceCountHierarchy[0], option="hierarchy")

    def test_device_count_customer_with_hierarchy_level2(self):
	"""
	Test Case ID:    IV-ST-DL-10
	Description:     Side Tree Validation - Lighting Dashboard - Device Count - Hierarchy 2 Level 
	Expected Output: Side Tree should display Device Count 6 for the Customer "QA-AUTO-03", 
			 Device Count 4 Hierarchy Level 1 "PETRCH", Device Count 2 Hierarchy Level 2
			 "PETRAMP".
	"""
	  
	CUSTOMER_NAME = 'QA-AUTO-03'
	EXPECTED_DEVICE_COUNT = 6
	actualDeviceCount = BASE_CLASS.get_device_count_customer(CUSTOMER_NAME)
	self.verify_device_count(CUSTOMER_NAME, EXPECTED_DEVICE_COUNT, actualDeviceCount, option="customer")

	HIERARCHY_NAMES = ['PETRACH', 'PETRAMP']
	EXPECTED_DEVICE_COUNT_HIERARCHY1 = 4
	EXPECTED_DEVICE_COUNT_HIERARCHY2 = 2
	actualDeviceCountHierarchy = BASE_CLASS.get_device_count_hierarchy(CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_count(HIERARCHY_NAMES[0], EXPECTED_DEVICE_COUNT_HIERARCHY1,
				actualDeviceCountHierarchy[0], option="hierarchy")
	self.verify_device_count(HIERARCHY_NAMES[1], EXPECTED_DEVICE_COUNT_HIERARCHY2,
				actualDeviceCountHierarchy[1], option="hierarchy")

    def test_device_count_customer_with_hierarchy_level3(self):
	"""
	Test Case ID:    IV-ST-DL-11
	Description:     Side Tree Validation - Lighting Dashboard - Device Count - Hierarchy 3 Level 
	Expected Output: Side Tree should display Device Count 20 for the Customer "QA-AUTO-04", 
			 Device Count 15 Hierarchy Level 1 "PETRAUS", Device Count 10 Hierarchy Level 2
			 "PETRACA" and Device Count 5 for Hierarchy level 3 "PETRASANJOSE".
	
	"""
	  
	CUSTOMER_NAME = 'QA-AUTO-04'
	EXPECTED_DEVICE_COUNT = 20
	actualDeviceCount = BASE_CLASS.get_device_count_customer(CUSTOMER_NAME)
	self.verify_device_count(CUSTOMER_NAME, EXPECTED_DEVICE_COUNT, actualDeviceCount, option="customer")

	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']
	EXPECTED_DEVICE_COUNT_HIERARCHY1 = 15
	EXPECTED_DEVICE_COUNT_HIERARCHY2 = 10
	EXPECTED_DEVICE_COUNT_HIERARCHY3 = 5
	actualDeviceCountHierarchy = BASE_CLASS.get_device_count_hierarchy(CUSTOMER_NAME, HIERARCHY_NAMES)
	self.verify_device_count(HIERARCHY_NAMES[0], EXPECTED_DEVICE_COUNT_HIERARCHY1,
				actualDeviceCountHierarchy[0], option="hierarchy")
	self.verify_device_count(HIERARCHY_NAMES[1], EXPECTED_DEVICE_COUNT_HIERARCHY2,
				actualDeviceCountHierarchy[1], option="hierarchy")
	self.verify_device_count(HIERARCHY_NAMES[2], EXPECTED_DEVICE_COUNT_HIERARCHY3,
				actualDeviceCountHierarchy[2], option="hierarchy")

    def test_device_type_customer_hierarchy_level(self):
	"""
	Test Case ID:	 IV-ST-DT-17
	Description:	 Side Tree Validation - Lighting Dashboard - Device Type-Customer-Hierarchy Levels
	Expected Output: Side Tree should display device type as "SLC - SLC-DEVICE000*" for Customer "QA-AUTO-04"
			 at Hierarchy Level 1&2&3 "PetraUS"&"PetraCA"&"PetraSanJose".
	"""

	CUSTOMER_NAME = 'QA-AUTO-04'
	EXPECTED_DEV_TYPE = 'SLC - SLC-DEVICE'
	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']
	
	self.verify_device_type(CUSTOMER_NAME, HIERARCHY_NAMES, EXPECTED_DEV_TYPE)
