import sys
xml = "".join(input() for _ in range(int(input())))
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(root.attrib)
maxdepth = 0
def depth(root,level):
    global maxdepth
    if maxdepth==level:
        maxdepth=maxdepth+1
    for child in root:
        depth(root,level+1) 
    return maxdepth

depth(root,-1)           
    

         

  

     




        
print(depth(root,-1))    

