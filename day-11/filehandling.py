"""
file=open("new.txt","r")
data=file.read()
print(data)
file.close()
"""
"""
file=open("new.txt","w")
data=file.write("ghayal hu isiliye ghatak hu hosla aur indhan")
print(data)
file.close()
"""
"""
file=open("WIN_20250716_19_20_08_Pro.jpg","rb")
data=file.read()
print(data)
file.close()
"""

file1=open("WIN_20250716_19_20_08_Pro.jpg","rb")
content=file1.read()

file2=open("Screenshot 2025-07-30 175215.jpg","wb")
data=file2.write(content)
print(data)

file1.close()
file2.close()