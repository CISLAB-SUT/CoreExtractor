import hashlib
import time
from typing import Tuple

from bs4 import BeautifulSoup

from model.main import extract_text
from setting import OK_STATUS, LEARNING_ERROR, FORMAT_ERROR, TIMEOUT_ERROR
import warnings
from logging import getLogger
import setting

logger = getLogger("extractor")


def generate_id(input_string):
    """
        Generate an 8-character unique identifier based on MD5 hash of the input string.

        This function takes an input string, generates an MD5 hash of it, and returns
        the first 8 hexadecimal characters of the hash as a unique identifier.

        Parameters:
            input_string (str): The timestamp in milliseconds to be hashed (e.g., "1634567890123").
                           Must be a string representation of the timestamp.

        Returns:
            str: An 8-character hexadecimal string derived from the MD5 hash of the input.

        """
    hash_object = hashlib.md5(input_string.encode('utf-8'))
    hashlib.md5()
    hex_dig = hash_object.hexdigest()
    return hex_dig[:10]


def content_extractor(file_path: str) -> Tuple[dict, int]:
    """
        Extract and process main content and metadata from HTML source code.

        This function performs the following operations:
        1. Validates the HTML input
        2. Extracts page content
        4. Processes the main text content
        5. Handles errors and logs the processing status

        Parameters:
            file_path (str): Path of Raw HTML source code file of the page to be processed


        Returns:
            Tuple[dict, int]:
                A tuple containing:
                - First element: Dictionary with extracted content, or None if error occurs
                - Second element: Status code (int) indicating processing result. For more information
                    refer to Code Status of setting.py file.

        Raises:
            Exception: Captures and logs any unexpected errors during processing
        """

    warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
    try:

        setting.URL_UUID = generate_id(str(time.time()))
        logger.info(f"Starting process '{setting.URL_UUID}'")
        # check if the input is html source code
        f = open(file_path, "r", encoding="utf8")
        html_source = f.read()
        soup = BeautifulSoup(html_source, 'html.parser')
        if len(soup.find_all('html')) == 0:
            return FORMAT_ERROR, None

        status, output = extract_text(html_source)

        logger.info(f"Processing completed for ID : {setting.URL_UUID}")
        return status, output
    except Exception as error:
        logger.error(f"ID : {setting.URL_UUID}, Message : {error}", exc_info=True)
        return LEARNING_ERROR, None


print(content_extractor("C:\\Users\\Mahan\'Repair\\Desktop\\test\\10.html"))
