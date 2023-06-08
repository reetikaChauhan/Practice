import sys
xml = "".join(input() for _ in range(int(input())))
import xml.etree.ElementTree as etree
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(root.attrib)
for i in root.iter(): # root.iter() gives all the child and subchild
    print(i)
def countatrib(root):
     return(sum([len(i.attrib) for i in root.iter()]))
    

        
#countatrib(root)     

