'''
@Author: Rashmi
@Date: 2021-09-30 20:17
@Last Modified by: Rashmi
@Last Modified time: 2021-09-30 20:20
@Title :Example to perform conftest concept to extension to use resource for 
multiple files
'''
import pytest
def test_div_13(input_value):
    '''
    Description: this takes value from fixture
    '''
    assert input_value % 13 == 0

def test_div_3(input_value):
    '''
    Description: this takes value from fixture
    '''
    assert input_value % 3 == 0
