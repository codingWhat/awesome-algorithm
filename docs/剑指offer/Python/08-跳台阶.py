# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                tempArray[(i+1)%2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1)%2]