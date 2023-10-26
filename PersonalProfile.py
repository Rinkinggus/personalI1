# src/PAIEA/PersonalProfile.py

class PersonalProfile:
    def __init__(self):
        self.profile = {}

    def add_profile_details(self, details):
        """
        Add profile details to the profile dictionary.
        :param details: A dictionary containing profile details.
        """
        self.profile.update(details)

    def update_profile_details(self, details):
        """
        Update profile details in the profile dictionary.
        :param details: A dictionary containing profile details to be updated.
        """
        self.profile.update(details)

    def retrieve_profile_details(self):
        """
        Retrieve all profile details.
        :return: A dictionary containing all profile details.
        """
        return self.profile
