from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()
        self.login_data=VendorModel()._load_vendors()

    def login(self, username, password):
        is_vendor=self.vendor_model.is_correct_vendor(username,password)


        # Add you code here after verifying the vendor data exists in the dictionary
        if is_vendor:
            self.vendor_session.login(username)
            return True
        else:
            return False



    def logout(self, username):


        # Add your code here to log out the current vendor
        is_loggedin=self.vendor_session.check_login(username)
        if is_loggedin:
            self.vendor_session.logout(username)
            print("User "+username+" logged out succesfully!")
        else:
            print("User "+username+" is not logged in")




