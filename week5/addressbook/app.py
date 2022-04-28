from flask import Flask, request, render_template

import json
import addressbook
from addressbook import addressList


addressesInList = []
# addressesInList.append(addressbook.Contact(1, "Kelci", "REnee", 1234567890, "kelci@kelci.com", ":)"))


app = Flask(__name__)

@app.route("/")
def home():
    # return "Home Page!!!"
    return render_template('home.html')

@app.route("/index", methods=["GET", "POST"])
@app.route("/search", methods=["GET", "POST"])
def index():
        if request.method == "POST":
            searchStr = request.form.get("search")
            searchStr = str(searchStr)
            myList = addressList.findAllMatching(searchStr)
        else:
            myList = []
            return render_template('index.html',results = myList)


@app.route('/contacts', methods=["GET", "POST"])
def myAddresseList():
    if request.method == "POST":
        first_Name = request.form.get("fName")
        last_Name = request.form.get("lName")
        phone_number = request.form.get("phone")
        email_address = request.form.get("email")
        dig_photo = request.form.get("photo")
        
        contactInfo = f"{first_Name} {last_Name}: {phone_number}: {email_address} {dig_photo}"
        addressesInList.append(contactInfo)
        return f"{first_Name} {last_Name}: {phone_number}: {email_address} {dig_photo}"
    else:
        myList = addressList.showList()
        
        return render_template('addressBook.html', results = myList)


if __name__ == "__main__":
    app.run()
    