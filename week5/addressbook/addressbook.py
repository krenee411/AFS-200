
import requests
import itertools


class Contact():
    id_iter = itertools.count(1)

    def __init__(self, id, firstName, lastName, phone, email, photo):
        self.id = next(self.id_iter)
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email
        self.photo = photo

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getFirstName(self):
        return self.firstName

    def setName(self, firstName):
        self.firstName = firstName
        
    def getLastName(self):
            return self.lastName

    def setLastName(self, lastName):
        self.firstName = lastName
        

    def getPhone(self):
            return self.phone

    def setPhone(self, phone):
        self.phone = phone

    def getEmail(self):
            return self.email

    def setEmail(self, email):
        self.email = email

    def getPhoto(self):
        return self.photo

    def setPhoto(self, photo):
        self.photo = photo

    def __str__(self):
        return str(self.firstName +" "+ self.lastName +  " ( " + self.email + " )")

    def __repr__(self):
         return str(self.firstName +" "+ self.lastName +  " ( " + self.email + " )")  

        
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses

    ##what i have added
    def showList(self):
        results = []
        for address in self.addresses:
            results.append(address)
            # print(address)
        return results
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            # print(address)
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)  
                     
        return results
    
def getData(nat):
    url =  "https://randomuser.me/api/?results=25&nat="+nat

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

addressList = AddressBook()
jsonAddressData = getData("us")

for currentUser in jsonAddressData["results"]:
    firstGetName = currentUser["name"]
    firstName = firstGetName['first']
    lastName = firstGetName["last"]
    email = currentUser['email']

    firstGetLogin = currentUser["login"]
    id = firstGetLogin["uuid"]
    
    phone = currentUser["phone"]
    

    firstGetPic = currentUser["picture"]
    photo = firstGetPic["large"]
   


    newPerson = Contact(id, firstName, lastName, phone, email, photo)
    addressList.addAddress(newPerson)

# addressList



