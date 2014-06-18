#dictionaries - key-value pair

#create dictionary
e2h = {}            #english to hindi

#add key-value in the dictionary
e2h['one'] = 'ek'
e2h['two'] = 'do'

#print content of dictionary
print e2h

#another way to create dictionary
e2h = {'one':'ek', 'two':'do', 'three':'teen'}

#print dictionary
print e2h

#look up value using key in dictionary
print e2h['two']

#dictionary operations
#create dictionary
inventory = {'apple':100,
             'orange':200,
             'banana':300
             }
print inventory

#delete banana
del inventory['banana']
print inventory

#add mango
inventory['mango'] = 300
print inventory

#update mango quantity
inventory['mango'] = 100
print inventory

#print no. of keys in inventory
print len(inventory)


#dictionary methods
print e2h.keys()        #this will return the list of keys
print e2h.values()      #thsi will return the list of values

#to get the key-value pair as tuple we use items()
print e2h.items()

#to check if a key exists in a dictionary
print e2h.has_key('one')        #return True or False


#alias and copy
#dictionaries are mutable
os = {'win':8.1,
      'osx':10.9,
      'ubuntu':14.04,
      'fedora':20
      }
print os

alias = os          #alias refer to same object os
copyOS = os.copy()  #this will create a fresh copy of object os

#any change in object os will be reflected back in object alias
#but copyOS will remain unchanged
os['ubuntu']='14.04 LTS'    #update value
print os
print alias
print copyOS

