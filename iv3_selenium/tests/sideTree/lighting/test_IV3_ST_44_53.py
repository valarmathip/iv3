from test_common import *


class TestSideTreeSearchFilterClass(TestIv3CommonClass):

    
    def oldtest_search_with_device_name(self):
	"""
	Test Case ID: IV-ST-SRCH-44
	Description:  Side Tree-Lighting Dashboard -Search
		      Search for a "Device Name" in various hierarchies
	Expected Output: IV 3.0 should Point to & Highlight the first occurrence
	                 of the Device Entry from the Search Result.
	"""

	# Search with device name in customer level	
        #CUSTOMER_NAME = 'QA-AUTO-01'
	SEARCH_OPTION = 'DEVICE'
	EXPECTED_SEARCH_RESULT = {
			'CUSTOMER_NAME': 'QA-AUTO-01',
		        'HIERARCHY_NAMES': ['NONE'],
			'DEVICE_NAME': 'SLC-DEVICE0003'}
	self.verify_search_result(EXPECTED_SEARCH_RESULT['DEVICE_NAME'],
		EXPECTED_SEARCH_RESULT, SEARCH_OPTION)

	# Search for device name in hierarchy level 1
	EXPECTED_SEARCH_RESULT = {
                        'CUSTOMER_NAME': 'QA-AUTO-02',
			'HIERARCHY_NAMES': ['PETRAINDIA'],
			'DEVICE_NAME': 'SLC-DEVICE0007'}
	self.verify_search_result(EXPECTED_SEARCH_RESULT['DEVICE_NAME'],
                EXPECTED_SEARCH_RESULT, SEARCH_OPTION)

 	# Search for device name in hierarchy level 2
	EXPECTED_SEARCH_RESULT = {
                        'CUSTOMER_NAME': 'QA-AUTO-03',
			'HIERARCHY_NAMES': ['PETRACH', 'PETRAMP'],
			'DEVICE_NAME': 'SLC-DEVICE0014'}
	self.verify_search_result(EXPECTED_SEARCH_RESULT['DEVICE_NAME'],
                EXPECTED_SEARCH_RESULT, SEARCH_OPTION)

	# Search for device name in hierarchy level 3
	EXPECTED_SEARCH_RESULT = {
                        'CUSTOMER_NAME': 'QA-AUTO-04',
			'HIERARCHY_NAMES': ['PETRAUS', 'PETRACA', 'PETRASANJOSE'],
			'DEVICE_NAME': 'SLC-DEVICE0032'}
	self.verify_search_result(EXPECTED_SEARCH_RESULT['DEVICE_NAME'],
                EXPECTED_SEARCH_RESULT, SEARCH_OPTION)

    def test_search_with_device_name(self):
	"""
	Test Case ID: IV-ST-SRCH-44
	Description:  Side Tree-Lighting Dashboard -Search
		      Search for a "Device Name" in various hierarchies
	Expected Output: IV 3.0 should Point to & Highlight the first occurrence
	                 of the Device Entry from the Search Result.
	"""

	SEARCH_OPTION = 'DEVICE'

	# Search for device name in customer level 1	
	EXPECTED_DEVICE_NAME = SEARCH_STRING = 'SLC-DEVICE0003'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device name in hierarchy level 1	
	EXPECTED_DEVICE_NAME = SEARCH_STRING = 'SLC-DEVICE0007'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device name in hierarchy level 2
	EXPECTED_DEVICE_NAME = SEARCH_STRING = 'SLC-DEVICE0014'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device name in hierarchy level 3	
	EXPECTED_DEVICE_NAME = SEARCH_STRING = 'SLC-DEVICE0033'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

    def test_seach_device_with_serial_number(self):
	"""
	Test case ID: IV-ST-SRCH-47
	Description:  Side Tree- Lighting Dashboard - Search
		      Search for a "Serial Number" in various hierarchies
	Expeted Output: IV 3.0 should Point to & Highlight the first occurrence
			of the Device Entry from the Search Result
	"""

	SEARCH_OPTION = 'DEVICE'
	
	# Search for device using serial number under customer level
	SEARCH_STRING = '700F6F5552579A43'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0004'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
			SEARCH_OPTION)
	
	# Search for device using serial number under hierarchy level 1
	SEARCH_STRING = '700F7G5552579A48'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0009'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device using serial number under hierarchy level 2
	SEARCH_STRING = '700F6F6662579A54'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0015'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)
	
	# Search for device using serial number under hierarchy level 3
	SEARCH_STRING = '700F6F5552579A72'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0033'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

    def test_seach_device_with_plc_node_id(self):
	"""
	Test case ID: IV-ST-SRCH-48
	Description:  Side Tree- Lighting Dashboard - Search
		      Search for a "PLC node ID" in various hierarchies
	Expeted Output: IV 3.0 should Point to & Highlight the first occurrence
			of the Device Entry from the Search Result
	"""

	SEARCH_OPTION = 'DEVICE'
	
	# Search for device using plc node id under customer level
	SEARCH_STRING = '0101010177778888000F6F0002579B10'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0002'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
			SEARCH_OPTION)
	
	# Search for device using PLC node id under hierarchy level 1
	SEARCH_STRING = '0101010199998888000F6F0002579B16'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0008'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device using PLC node id under hierarchy level 2
	SEARCH_STRING = '0101010177778888111F6F0002579B23'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0015'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)
	
	# Search for device using PLC node id  under hierarchy level 3
	SEARCH_STRING = '0101010177778888000F6F0002579B40'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0032'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

    def test_seach_device_with_tcc_id(self):
	"""
	Test case ID: IV-ST-SRCH-49
	Description:  Side Tree- Lighting Dashboard - Search
		      Search for a "TCC ID" in various hierarchies
	Expeted Output: IV 3.0 should Point to & Highlight the first occurrence
			of the Device Entry from the Search Result
	"""

	SEARCH_OPTION = 'DEVICE'
	
	# Search for device using TCC id under customer level
	SEARCH_STRING = '10020B32'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0002'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
			SEARCH_OPTION)
	
	# Search for device using TCC id under hierarchy level 1
	SEARCH_STRING = '10030B39'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0009'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

	# Search for device using TCC id under hierarchy level 2
	SEARCH_STRING = '10020B45'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0015'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)
	
	# Search for device using PLC node id  under hierarchy level 3
	SEARCH_STRING = '11020B61'
	EXPECTED_DEVICE_NAME = 'SLC-DEVICE0031'
	self.verify_search_result(SEARCH_STRING, EXPECTED_DEVICE_NAME,
                        SEARCH_OPTION)

    def test_search_for_invalid_device(self):
	"""
	Test Case ID: IV-ST-SRCH-52
	Description:  Side Tree- Lighting Dashboard - Search
		      Search for a invalid device in various hierarchies
	Expected Output: IV 3.0 Should Display "NO RESULTS FOUND".
	"""

	SEARCH_OPTION = 'INVALID'
	SEARCH_STRING = 'SLC-DEVICE0001000'
	EXPECTED_SEARCH_RESULT = 'NO RESULTS FOUND'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

    def test_search_for_multiple_matches(self):
	"""
	Test Case ID:  IV-ST-SRCH-53
	Description:   Side Tree- Lighting Dashboard - Search
		       search with a pattern such that it matches multiple
		       devices (for various customers)
	Expected Output: IV 3.0 should Point to & Highlight the first occurrence of
                         the Device Entry from the Search Result
	"""

	SEARCH_OPTION = 'DEVICE'

	# Search for device name with search patter based on device name
	SEARCH_STRING = 'SLC-DEVICE000*'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

        SEARCH_STRING = 'DEVICE'
        EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	# Search based on different search pattern with serial number
	SEARCH_STRING = '700F6F5552579A4*'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '700F6F55'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '700F7G55'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '700F6F66'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	# Search based on different search pattern with PLC node ID
	SEARCH_STRING = '0101010177778888000F6F0002579B2*'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '0101010177778888'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)
        
	SEARCH_STRING = '0101010199998888'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)
        
	SEARCH_STRING = '0101010177778888111'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)
        
        # Search based on different search pattern with TCC ID
	SEARCH_STRING = '10020B3*'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
	self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '1002'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	SEARCH_STRING = '1003'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0020'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)

	
	SEARCH_STRING = '1102'
	EXPECTED_SEARCH_RESULT = 'SLC-DEVICE0030'
        self.verify_search_result(SEARCH_STRING, EXPECTED_SEARCH_RESULT,
                        SEARCH_OPTION)
