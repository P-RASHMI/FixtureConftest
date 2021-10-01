'''
@Author: Rashmi
@Date: 2021-09-30 20:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-30 20:20
@Title :Example to perform test cases using conftest concept.
'''
import pytest
@pytest.fixture
def input_value():
    '''
    Description: this is fixture which stores resource and this is 
    repeatedly used for other test cases.conftest.py extends this to use for 
    multiple files
    '''
    input = 39         #takes this resource to multiple files
    return input        #pytest -k div -v
