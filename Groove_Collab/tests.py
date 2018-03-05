import data
import storeFinder
import json
import unittest



class CLITests(unittest.TestCase):
    #Check for data in the store-locations.csv file
    def test_get_data_from_csv(self):
        result=data.get_data_from_csv('store-locations.csv')
        self.assertNotEqual(0,result)
    #Check for expected distance between two geocodes
    def test_compare_lat_lng(self):
        result1=data.get_lat_lng('261 University Ave, Palo Alto, CA 94301')
        result2=data.get_lat_lng('660 Stanford Shopping Center, Palo Alto, CA 94304')
        distance=data.compare_lat_lng(result1[0],result1[1],result2[0],result2[1])
        expected=0.986673289578851
        self.assertAlmostEqual(expected,distance)
    #positive unit test for checking output format
    def test_find_closest_store_output_positive(self):
        dict_list=result=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='mi','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            json.loads(output)
            result=True
        except ValueError as error:
            result=False
        expected=True
        self.assertEqual(expected,result)
    #negative unit test for checking out format where argument['output'] is json
    def test_find_closest_store_output_negative(self):
        dict_list=result=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='mi','text','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            json.loads(output)
            result=True
        except ValueError as error:
            result=False
        expected=False
        self.assertEqual(expected,result)
    #postive test case for argument['unit'] is specified as miles
    def test_find_closest_store_units_miles_positive(self):
        dict_list=result=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='mi','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Distance']
        except ValueError as error:
            result=0.0
        expected=1.614

        self.assertAlmostEqual(expected,result)
    #negative test case for argument['unit'] is specified as miles
    def test_find_closest_store_units_miles_negative(self):
        dict_list=result=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='mi','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Distance']
        except ValueError as error:
            result=0.0
        expected=2.597

        self.assertNotEqual(expected,result)
    #postive test case for argument['unit'] is specified as km
    def test_find_closest_store_units_km_positive(self):
        dict_list=result=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='km','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Distance']
        except ValueError as error:
            result=0.0
        expected=2.597

        self.assertAlmostEqual(expected,result)
    #negative test case for argument['unit'] is specified as km
    def test_find_closest_store_units_km_negative(self):
        dict_list=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='km','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Distance']
        except ValueError as error:
            result=0.0
        expected=1.614
        self.assertNotEqual(expected,result)
    #positive test case to find the closest store to a specified address
    def test_find_closest_store_output_address_positive(self):
        dict_list=data.get_data_from_csv('store-locations.csv')
        val='1455 Market St, San Francisco, CA 94103'
        units,output,addr_zip='mi','json','address'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Store_Name']
        except:
            result='Error'
        expected='San Francisco Central'
        self.assertEqual(expected,result)
    #positive test case to find the closest store to a specified zipcode
    def test_find_closest_store_output_zip_code_positive(self):
        dict_list=data.get_data_from_csv('store-locations.csv')
        val='93065'
        units,output,addr_zip='mi','json','zipcode'
        output=data.find_closest_store(dict_list,val,units,output,addr_zip)
        try:
            result=json.loads(output)
            result=result['Store_Name']
        except:
            result='Error'
        expected='Simi Valley West'
        self.assertEqual(expected,result)


def main():
    unittest.main(warnings='ignore')

if __name__ == '__main__':
    main()
