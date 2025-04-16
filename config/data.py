import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    NAME = os.getenv("NAME")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    EMAIL = os.getenv("EMAIL")
    COMPANY_NAME = os.getenv("COMPANY_NAME")
    INFO_ABOUT_COMPANY = os.getenv("INFO_ABOUT_COMPANY")