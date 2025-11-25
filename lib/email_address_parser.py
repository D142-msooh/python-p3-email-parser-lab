# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, addresses=str):
        self.addresses = addresses

    def parse(self):
        parts = re.split(r"[,\s]+", self.addresses.strip())
        parts = [email for email in parts if email]
        valid = [email for email in parts if "@" in email]

        return sorted(set(valid))