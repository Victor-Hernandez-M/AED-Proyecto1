# -*- coding:utf-8 -*-

class Convert:

    def __init__(self):
        pass

    def convertTime(self,string):
        
        content = string.split(":")
        if (len(content)==3):
            seg = 0
            seg += int(content[0])*3600
            seg += int(content[1])*60
            seg += int(content[2])
        else:
            return False
        # print(seg)
        return seg

# a = Convert()
# con = "04:34:52"
# a.convertTime(con)
