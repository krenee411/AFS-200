import requests
class User():

    def __init__(self,firstName,lastName, email, username, password, UUID, phone, cell, picLarge, picThumbnail):
        self.firstName= firstName 
        self.lastName= lastName 
        self.email = email
        self.username = username
        self.password = password
        self.UUID = UUID
        self.phone = phone
        self.cell = cell
        self.picLarge = picLarge
        self.picThumbnail = picThumbnail

    def setFullName(self, firstName, lastName):
       self.fullName= firstName , lastName
         
    
    def getFullName(self):
        return self.fullName

    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setLoginData(self, username, password):
        self.loginInfo = username , password
    
    def getLoginData(self):
        return self.loginInfo

    def setNumbers(self, phone, cell):
        self.contacts = phone , cell
    
    def getNumbers(self):
        return self.contacts

    def setProfilePic(self, picLarge, picThumbnail):
        self.photos = picLarge , picThumbnail
         
    
    def getProfilePic(self):
        return self.photos

    def setUUID(self, UUID):
        self.UUID = UUID
    
    def getUUID(self):
        return self.UUID
    

    def __str__(self):
        return str(self.firstName + " " + self.lastName + " (" +self.email + ")")
        

class AuthorizedUsers():

    def __init__(self):
        self.approvedUsers = []

    def userLibary(self, users):
        self.approvedUsers.append(users)

    def showUserlist(self):
        for users in self.approvedUsers:
            print(users)

def getData(nat):
    url =  "https://randomuser.me/api/?results=10&nat="+nat

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

    
myApprovedUserList = AuthorizedUsers()
jsonUserData = getData("us")



        #get users:  https://randomuser.me/api/?results=10&nat=us
        #get nationality:   https://randomuser.me/api/?nat=us
        #display only name and email:   https://randomuser.me/api/?inc=name,email
        # specify format: json is default!
for currentUser in jsonUserData["results"]:
    firstGetName = currentUser["name"]
    firstName = firstGetName['first']
    lastName = firstGetName["last"]
    email = currentUser['email']

    firstGetLogin = currentUser["login"]
    UUID = firstGetLogin["uuid"]
    username = firstGetLogin["username"]
    password = firstGetLogin["password"]

    phone = currentUser["phone"]
    cell = currentUser["cell"]

    firstGetPic = currentUser["picture"]
    picLarge = firstGetPic["large"]
    picThumbnail = firstGetPic["thumbnail"]


    newUser = User(firstName,lastName, email, username, password, UUID, phone, cell, picLarge, picThumbnail)
    myApprovedUserList.userLibary(newUser)

myApprovedUserList.showUserlist()

