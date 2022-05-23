#Create function to test if numbers given represent an actual phone number
def isPhoneNumber(text):
    if len(text) != 12: #Checks to see if the potential number has 12 characters
        return False
    for i in range (0,3): #Looks at characters 0-3
        if not text[i].isdecimal(): #If first three charactes are numbers
            return False
    if text[3] != '-': #If a hyphen follows the first 3 characters
        return False
    for i in range(4, 7): #Repeats process for next two sets
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
print('Is 111-111-1198 a phone number?')
print(isPhoneNumber('951-751-7798'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12] #Goes through each character + next 12 to see if theres a phone number
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#Faster way of finding phone number using Regex function
from codecs import namereplace_errors
import re 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4243')
print(mo.group(1)) #415
mo.group(2) #555-4243
mo.group() #415-555-4243
mo.groups() #(415), 555-4243)
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
print('Phone number found: ' + mo.group())\


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (425) 556-4241')
print(mo.groups())

#Matching Multiple Groups with the Pip | 
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1)
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2)

#Optional Matching with the Question Mark ?
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-545-4444')
print(mo1.group())
mo2 = phoneRegex.search('My number is 444-4444')
print(mo2.group())

#Matching Zero or More with a Star *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

#Matching One or More with the Plus + 
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None) # 'wo' needs to be present to pass

#Matching Specific Repititions with Braces 
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None) #{3} 3 Ha's need to be present  can also use {3,5} for acceptance of 3 or 5 Ha's

#The finall() Method 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#Character Classes 
#   \d = Any numeric digit from 0 to 9
#   \D = Any character that is NOT a numeric digit from 0 to 9
#   \w Any letter, numeric digit, or the underscore character 
#   \W Any character that is NOT a letter, numeric digit, or the underscore character
#   \s Any space, tab, or newline character
#   \S Any character that is NOT a space, tab or newline character

#Making Your Own Character Class
vowelRegex = re.compile(r'[aeiouAEIOU]') #Adding ^ prints the rest 
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD'))

#The Wildcard Character 
atRegex = re.compile(r'.at') #Matches only the character before 
print(atRegex.findall('The cat in the hat sat on the flat mat'))

#Matching everything with Dot Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))