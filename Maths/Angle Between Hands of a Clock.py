"""
Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:
Input: hour = 12, minutes = 30
Output: 165
Example 2:

Example 2:
Input: hour = 3, minutes = 30
Output: 75
Example 3:

Example 3:
Input: hour = 3, minutes = 15
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # return (30*hour - 5.5*minutes)
        hrangle = 30*hour + 0.5*minutes
        minangle = 6*minutes

        if hrangle > 360:
            hrangle = hrangle - 360
        if minangle > 360:
            minangle = minangle - 360
        
        res = abs(hrangle - minangle)
        
        if res > 180 :
            return (360 - res)
        return res
        
