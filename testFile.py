
"""
Created on Sun Jan 30 14:37:03 2022

@author: tejareddy
"""

import most_active_cookie
import unittest



class Test(unittest.TestCase):
    
    def testGiven1(self):
        
        result_l = most_active_cookie.most_active_cookie("tet.csv", "2018-12-08")
        correct = True
        if ("SAZuXPGUrfbcn5UA" not in result_l):
            correct = False
        if ("4sMM2LxV07bPJzwf" not in result_l):
            correct = False
        if ("fbcn5UAVanZf6UtG" not in result_l):
            correct = False
        if len(result_l) != 3:
            correct = False
        
        self.assertTrue(correct)
        
    def testGiven2(self):
        
        result_l = most_active_cookie.most_active_cookie("tet.csv", "2018-12-09")
        correct = True
        if ("AtY0laUfhglK3lC7" not in result_l):
            correct = False
        if len(result_l) != 1:
            correct = False
        
        self.assertTrue(correct)
        
    def testnoCookiesonDay(self):
        
        result_l = most_active_cookie.most_active_cookie("tet.csv", "2018-11-09")
        correct = True
        if len(result_l) != 0:
            correct = False
        
        self.assertTrue(correct)
        
    def testEmptyLog(self):
        
        result_l = most_active_cookie.most_active_cookie("tet2.csv", "2018-11-09")
        correct = True
        if len(result_l) != 0:
            correct = False
        
        self.assertTrue(correct)
        
        
if __name__ == '__main__':
    unittest.main()