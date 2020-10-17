import xml.etree.ElementTree as ET
def top10(name_file):
  parser=ET.XMLParser()
  tree = ET.parse(name_file,parser)
  root = tree.getroot()
  items= root.findall("channel/item")
  a=""
  for description in items:
    a=a+description.find("description").text
  a=a.split()
  s=set()
  s.update(a)
  for i in list(s):
    if len(i)<=6:
      s.remove(i)
  s=list(s)
  s1=[]
  for i in s:
    s1.append(a.count(i))
    k=0
  for i in s1[0:10]:
    maxi=s1[k]
    maxi_1=max(s1[k+1:])
    if maxi<maxi_1:
      s1[k]=maxi_1
      poz_maxi_1=s1.index(maxi_1,k+1)
      s1[poz_maxi_1]=maxi
      b=s[k]
      s[k]=s[poz_maxi_1]
      s[poz_maxi_1]=b
      k=k+1
  print(s[0:10])
top10("amp2.xml")