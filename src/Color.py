'''
Created on Mar 13, 2016

@author: Tim
'''

class Color:
    '''
    This class classifies the HSV values that are used in the neopixel and the fastLed library
    '''

    def __init__(self, hue = 0, sat = 0, val = 0):
        '''
        constructs the hsv value
        '''
        self.hue = hue
        self.sat = sat
        self.val = val
    
    def set(self, hue, sat, val):
        '''
        sets all three values through one single method
        '''
        self.hue=hue
        self.sat=sat
        self.val=val
    
    def __str__(self):
        return "Hue: %d Saturation: %d Value %d" %(self.hue, self.sat, self.val)
        
c1 = Color(255,255,255)
c1.set(23, 123, 31)
print(c1)
    
    