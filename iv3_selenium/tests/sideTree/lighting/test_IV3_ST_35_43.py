from test_common import *


class TestSideTreeDeviceInfoClass(TestIv3CommonClass):


    def test_tool_tip_for_device_customer_level(self):
        """
        Test Case ID:    IV-ST-TT-35
        Description:     Side Tree- Lighting Dashboard -  ToolTip - device under customer level
        Expected Output: Actual Device Information should be matched with the expected dvice
			 Information.
        """

        CUSTOMER_NAME = 'QA-AUTO-01'
        DEVICE_NAME = 'SLC - SLC-DEVICE0002'
        EXPECTED_DEVICE_INFO = {'Serial Number': '700F6F5552579A41',
				'PLC Node ID': '0101010177778888000F6F0002579B10',
				'TCC ID': '10020B32',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '13.07901211',
				'Longitude': '80.17121232',
				'Location': 'Mount Road, Chennai',
				'Zip Code': '600001',
				'Pole ID': 'Pole 6001'}
        self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_DEVICE_INFO)

    def test_tool_tip_for_device_customer_hierarchy_level1(self):
        """
        Test Case ID:    IV-ST-TT-36
	Description:     Side Tree- Lighting Dashboard -ToolTip -Customer-Hierarchy Level 1
        Expected Output: Actual Device Information should be matched with the expected dvice
                         Information.
        """

        CUSTOMER_NAME = 'QA-AUTO-02'
        DEVICE_NAME = 'SLC - SLC-DEVICE0009'
        HIERARCHY_NAMES = ['PETRAINDIA']
        EXPECTED_DEVICE_INFO = {'Serial Number': '700F7G5552579A48',
				'PLC Node ID': '0101010199998888000F6F0002579B17',
				'TCC ID': '10030B39',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '13.07857468',
				'Longitude': '80.67099887',
				'Location': 'Mount Road, Chennai',
				'Zip Code': '600001',
				'Pole ID': 'Pole 6001'}

        self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME,
                EXPECTED_DEVICE_INFO, hierarchyNames = HIERARCHY_NAMES)

    def test_tool_tip_for_device_customer_hierarchy_level2(self):
        """
        Test Case ID:    IV-ST-TT-37
	Description:     Side Tree- Lighting Dashboard -ToolTip -Customer-Hierarchy Level 2
        Expected Output: Actual Device Information should be matched with the expected dvice
                         Information.
        """

        CUSTOMER_NAME = 'QA-AUTO-03'
        DEVICE_NAME = 'SLC - SLC-DEVICE0012'
	HIERARCHY_NAMES = ['PETRACH', 'PETRAMP']
	EXPECTED_DEVICE_INFO ={'Serial Number': '700F6F6662579A51',
			       'PLC Node ID': '0101010177778888111F6F0002579B20',
			       'TCC ID': '10020B42',
		               'Product Family': 'Smart Light Controller 2.0',
			       #'Dim Level': '50%',
 			       'Latitude': '13.07859468',
                               'Longitude': '80.87099887',
                               'Location': 'Mount Road, Chennai',
                               'Zip Code': '600001',
                               'Pole ID': 'Pole 6001'}

	self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME,
                EXPECTED_DEVICE_INFO, hierarchyNames = HIERARCHY_NAMES)
	
    def test_tool_tip_for_device_customer_hierarchy_level3(self):
        """
        Test Case ID:    IV-ST-TT-38
	Description:     Side Tree- Lighting Dashboard -ToolTip -Customer-Hierarchy Level 3
        Expected Output: Actual Device Information should be matched with the expected dvice
                         Information.
        """

        CUSTOMER_NAME = 'QA-AUTO-04'
        DEVICE_NAME = 'SLC - SLC-DEVICE0034'
	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']

	EXPECTED_DEVICE_INFO = {'Serial Number': '700F6F5552579A73',
				'PLC Node ID': '0101010177778888000F6F0002579B42',
				'TCC ID': '11020B64',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '37.32918983',
				'Longitude': '121.9561785',
				'Location': 'MCGINNESS AVE, San Jose',
				'Zip Code': '95127',
				'Pole ID': 'Pole 5136'}

	self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME,
                EXPECTED_DEVICE_INFO, hierarchyNames = HIERARCHY_NAMES)

    def test_tool_tip_for_device_under_diff_cus_hier_level(self):
        """
        Test Case ID:    IV-ST-TT-39
        Description:     Side Tree- Lighting Dashboard -  ToolTip - device under different customer and
			 hierarchy level
        Expected Output: Actual Device Information should be matched with the expected dvice
			 Information.
        """
	# check device info for the first device in the side tree
        CUSTOMER_NAME = 'QA-AUTO-01'
        DEVICE_NAME = 'SLC - SLC-DEVICE0001'
        EXPECTED_DEVICE_INFO = {'Serial Number': '700F6F5552579A40',
				'PLC Node ID': '0101010177778888000F6F0002579B99',
				'TCC ID': '10020B31',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '13.08506522',
				'Longitude': '80.27330658',
				'Location': 'Mount Road, Chennai',
				'Zip Code': '600001',
				'Pole ID': 'Pole 6001'}
				#'Last Transaction Time': 'Thursday, April 20 2017 5:35 PM'}
        self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_DEVICE_INFO)
	
	# check the device info for the middle device in the side tree
	CUSTOMER_NAME = 'QA-AUTO-03'
	DEVICE_NAME = 'SLC - SLC-DEVICE0015'
	HIERARCHY_NAMES = ['PETRACH', 'PETRAMP']
        EXPECTED_DEVICE_INFO = {'Serial Number': '700F6F6662579A54',
				'PLC Node ID': '0101010177778888111F6F0002579B23',
				'TCC ID': '10020B45',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '13.07859468',
				'Longitude': '80.87099887',
				'Location': 'Mount Road, Chennai',
				'Zip Code': '600001',
				'Pole ID': 'Pole 6001'}

	self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_DEVICE_INFO,
					hierarchyNames = HIERARCHY_NAMES)

	# Check the device info for the last device in the side tree
	CUSTOMER_NAME = 'QA-AUTO-04'
	DEVICE_NAME = 'SLC - SLC-DEVICE0020'
	HIERARCHY_NAMES = ['PETRAUS', 'PETRACA', 'PETRASANJOSE']
        EXPECTED_DEVICE_INFO = {'Serial Number': '700F6F5552579A59',
				'PLC Node ID': '0101010177778888000F6F0002579B28',
				'TCC ID': '10020B50',
				'Product Family': 'Smart Light Controller 2.0',
				#'Dim Level': '50%',
				'Latitude': '37.3228479',
				'Longitude': '121.9581247',
				'Location': 'MCGINNESS AVE, San Jose',
				'Zip Code': '95127',
				'Pole ID': 'Pole 5136'}
	self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_DEVICE_INFO,
		hierarchyNames = HIERARCHY_NAMES)

    def test_tool_tip_omitting_values(self):
	"""
	Test case ID:    IV-ST-TT-40
	Description :    Side Tree Validation- Lighting Dashboard -  ToolTip - Omitting Values
	EXpected Output: Omitted value should not displayed in the device tool tip.
	"""

	CUSTOMER_NAME = 'QA-AUTO-01'
	DEVICE_NAME = 'SLC - SLC-DEVICE0004'
	EXPECTED_OUTPUT = 'TCC ID'
	self.verify_tool_tip_info(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_OUTPUT,
				option = EXPECTED_OUTPUT) 

    def noest_tool_tip_changing_dim_level(self):
        """
        Test Case ID: IV-ST-TT-41
	Description: Side Tree Validation- Lighting Dashboard -  ToolTip - Changing Dim Level
	Expected Output: Dimming level in the device tool tip should be updated as per our change.
	"""
        # To DO
	CUSTOMER_NAME = ''

    def test_tool_tip_last_transaction_date(self):
	"""
	Test Case ID:    IV-ST-TT-43
	Description:     Side Tree Validation- Lighting Dashboard -
                         ToolTip - Last Transaction Date
	Expected Output: Last Transaction date should display the actual uninstalled date
                         as specified in the Installation Master Data source file.
	"""

 	CUSTOMER_NAME = "QA-AUTO-01"
	DEVICE_NAME = "SLC - SLC-DEVICE0002"
	EXPECTED_UNINSTALLED_DATE = 'Saturday, December 17 2016 10:30 AM'
	
	self.verify_uninstall_date(CUSTOMER_NAME, DEVICE_NAME, EXPECTED_UNINSTALLED_DATE)
