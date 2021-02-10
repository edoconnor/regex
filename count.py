import re

# pattern = re.compile(r"\w+") 
# string = "regex is awesome!"
# result = pattern.match(string)

# print(result.group()) 

# with open('scarlet.txt', 'r') as f:
#     text = f.read()
#     words = text.split() 
#     #print(len(words))
#     print(res)

with open('scarlet.txt', 'r') as f:
    for line in f:
        print(line.strip())

# myfile = open("scarlet.txt", "rt") 
# contents = myfile.read()         
# myfile.close()                   
# print(contents)  

##---------------------------------
#Count word occurence in txt file:

# text = open("scarlet.txt", "r") 

# d = dict() 
  
# for line in text: 
#     line = line.strip() 
#     line = line.lower() 
#     words = line.split(" ") 
  
#     for word in words: 
#         if word in d: 
#             d[word] = d[word] + 1
#         else: 
#             d[word] = 1
  
# for key in list(d.keys()): 
#     print(key, ":", d[key]) 