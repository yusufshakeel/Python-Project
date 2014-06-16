#File: moduleCase2.py
#Description:
#This is a module containing functions to change case of a string
#
#Date: 16-06-2014 monday
#Author: Yusuf Shakeel
#
#youtube.com/yusufshakeel
#plus.google.com/+YusufShakeel
#https://github.com/yusufshakeel/Python-Project
#
#The MIT License (MIT)
#
#Copyright (c) 2014 Yusuf Shakeel
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#function definition
#check alphabet
def isAlpha(ch):
    if ('a'<= ch <= 'z') or ('A' <= ch <= 'Z'):
        return True
    return False

#check lower case
def isLower(ch):
    if 'a'<= ch <='z':
        return True
    return False

#check upper case
def isUpper(ch):
    if 'A' <= ch <= 'Z':
        return True
    return False

#convert to lower case
#param ch - upper case character
def toLower(ch):
    i = ord(ch)         #this will return the ascii value
    return chr(i+32)    #return lowercase character

#convert to upper case
#param ch - lower case character
def toUpper(ch):
    i = ord(ch)         #this will return the ascii value
    return chr(i-32)    #return uppercase character

#convert to lower case - string
#param s - string s to convert to lower case
#note! string are immutable so we cannot change them directly
def toLowerCase(s):
    slen = len(s)               #length of the string s
    lowstr = ''                 #lower case string that will be returned
    for index in range(slen):   #loop from index 0 to slen-1
        if isAlpha(s[index]) and isUpper(s[index]):
            lowstr += toLower(s[index])
        else:
            lowstr += s[index]
    return lowstr

#convert to upper case - string
#param s - string s to convert to upper case
#note! string are immutable so we cannot change them directly
def toUpperCase(s):
    slen = len(s)               #length of the string s
    upstr = ''                  #upper case string that will be returned
    for index in range(slen):   #loop from index 0 to slen-1
        if isAlpha(s[index]) and isLower(s[index]):
            upstr += toUpper(s[index])
        else:
            upstr += s[index]
    return upstr
