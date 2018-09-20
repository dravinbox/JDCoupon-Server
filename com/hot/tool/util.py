import hashlib
import os


class TokenGenerator:
    @staticmethod
    def get_token():
        return hashlib.sha1(os.urandom(24)).hexdigest()
