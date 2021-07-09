#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Question 1
a = 0#given a variable value
def b():  #defined function 'b'
 global a #made  a global value
 a = c(a) #variable 'a' calls function 'c' by passing down a parameter 'a'
def c(a):#defines a function called 'c' with a parameter value 'a'
 return a + 2 #returns the summation


# In[6]:


b()


# In[7]:


b()


# In[8]:


b()


# In[9]:


a


# In[ ]:


# Q2
def filelength(filename):#function defined
    try:
    
        file = open(filename)#opens the file contents
        contents = file.read()#reads the content from files
        file.close()
        print(len(contents))
    
    except FileNotFoundError:
        print('File'+filename+'not found')
        


# In[19]:


filelength('Assignment2.ipynb')#function called


# In[20]:


filelength('midterm.py')


# In[21]:


#Question 3
class Marsupial:                  #Create a class named Marsupial
    def __init__(self):      
         self.lst=[]              #Create an empty list in the init method
    def put_in_pouch(self,pouch): #Create a method to add the elements
        self.lst.append(pouch)
    def pouch_contents(self):
        return self.lst           #Return the list
m = Marsupial() 
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()


# In[1]:


class Marsupial(object):
    def __init__(self):
        self.myList = []
    def put_in_pouch(self,item):
        self.myList.append(item)
    def pouch_contents(self):
        return self.myList

class Kangaroo(Marsupial):
    def __init__(self,x,y):
        Marsupial.__init__(self)
        self.x = x
        self.y = y
    def jump(self,ax,ay):
        self.x += ax
        self.y += ay
    def __str__(self):
        return "I am a Kangaroo located at co-ordinates ({},{})".format(self.x,self.y)
    
my = Marsupial()
my.put_in_pouch('doll')
my.put_in_pouch('firetruck')
my.put_in_pouch('kitten')
my.pouch_contents()

kg = Kangaroo(0,0)

print(kg)

kg.put_in_pouch('doll')
kg.put_in_pouch('firetruck')
kg.put_in_pouch('kitten')
kg.pouch_contents()
kg.jump(1,0)
kg.jump(1,0)
kg.jump(1,0)
print(kg)


# In[2]:


#Question 4
def collatz(number):
    if number !=1:
        if number % 2 == 0:
            number = number/2
            (print(int(number)))
            collatz(number)
        else:
            number = (3*number+1)
            (print(int(number)))
            collatz(number)


# In[3]:


print(10)
collatz(10)


# In[4]:


print(1)
collatz(1)


# In[10]:


#question 5
def binary(n):
    if n > 1:
        binary(n//2)
    print(n % 2,end = '')


# In[11]:


binary(0)


# In[12]:


binary(1)


# In[13]:


binary(3)


# In[14]:


binary(9)


# # Question 6
# 
# from urllib.request import urlopen
# 
# def getSource(url): #search for the webpages response = urlopen(url) html = response.read() return html.decode()
# 
# def feedParser (self): # read the page infile = open('w3c.html') content = infile.read() infile.close()
# 
# from html.parser import HTMLParser parser = HTMLParser() parser.feed(content) #feed the strings of the page into parser
# 
# class HeadingParser(HTMLParser):
# 
# def__init__(self):
# 
#     HTMLParser.__init__(self)
#     self.indent=0
# 
# def handler_starttag(self,tag,attrs):
# 
#     for tag not in {'br','p'}: # p is the paraghraph element, br is the line break element. IF a tag is not a paraghraph element, tag is a header
# 
#         print('/n{}{}start'.format(self.indetn*' ',tag))
#         self.indent+=4

# # Question 7
# 
# class Crawler: def init(self): self.visited = set()
# 
# def webdir(self, url, depth, indent):
#     links = analyze(url)
#     sekf.visited.add(url)
# 
#     for link in links:
#         if link not in self.visited:
#             try:
#                 if depth >= 0:
# 
#                     indent = 0
# 
#                     for click in depth: 
# 
#                         self.webdir(link, depth, indent)
#                         print(url)
#                         self.indent =+1
# 
#                 else:
#                     pass
#             except:
#                 pass
# 
# webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)

# # Question 8
# 
# con = sqlite3.connect('web.db')
# 
# cur = con.cursor()
# 
# cur.execute("CREATE TABLE Weather (City text, Country text, Season text, Temperature(C) real,Rainfall(mm) real)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India', 'Winter', 24.8, 5.9)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India', 'Spring', 28.4, 16.2)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India', 'Summer', 27.9 1549.4)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Mumbai', 'India', 'Fall', 27.6, 346.0)")
# 
# cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom', 'Winter', 4.2, 207.7)")
# 
# cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom', 'Spring',8.3 , 169.6)")
# 
# cur.execute("INSERT INTO Weather VALUES ('London', 'United Kingdom', 'Summer', 15.7 , 157.0)")
# 
# cur.execute("INSERT INTO Weather VALUES ('London', 'United', 'Kingdom', 'Fall', 10.4 , 218.5)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt', 'Winter', 13.6, 16.5)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt', 'Spring', 20.7, 6.5)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt', 'Summer', 27.7, 0.1)")
# 
# cur.execute("INSERT INTO Weather VALUES ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)")
# 
# # Question a: All the temperature data.
# 
# SELECT Temperature FROM Weather
# 
# # Question b: All the cities, but without repetition.
# 
# SELECT DISTINCT City FROM Weather 
# 
# # question c: All the records for India.
# 
# SELECT * FROM Weather 
# WHERE Country = 'India'
# 
# # question d: All the Fall records.
# 
# SELECT * FROM Weather 
# WHERE Season = 'Fall'
# 
# # question e: The city, country, and season for which the average rainfall is between 200
# and 400 millimeters.
# 
# SELECT City, Country, Season 
# FROM Weather 
# WHERE Rainfall BETWEEN 200 and 400
# 
# # question f: The city and country for which the average Fall temperature is above 20
# degrees, in increasing temperature order.
# 
# SELECT City, Country FROM Weather 
# WHERE Season = 'Fall' and Temperature > 20 
# ORDER BY Temperature ASC
# 
# # question g: The total annual rainfall for Cairo.
# 
# SELECT SUM(Rainfall) FROM Weather 
# Where Country = 'Cairo'
# 
# # question h: The total rainfall for each season.
# 
# SELECT SUM(Rainfall) FROM Weather 
# GROUP BY Season

# In[23]:


# Question 9

#a
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [element.upper()for element in words];words


# In[24]:


#b
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
words = [element.lower()for element in words];words


# In[26]:


#c
[len(words) for words in ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']]


# In[27]:


#d
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']
newList=[]
for word in words:
    newList.append(word.upper())
    newList.append(word.lower())
    newList.append(len(word))

print(newList)


# In[28]:


#e
words=['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']
newList = [i for i in words if len(i) >= 4]
newList


# In[ ]:




