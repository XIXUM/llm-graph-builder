# (c) 2025 XIXUM.ORG
# Author: Felix Schaller
# Date: YYYY-MM-DD
# Description: This script tests the SSL connection in a Python environment
# License: MIT License
# Requirements: Python 3.x, certifi, urllib, nltk
# Usage: Run this script to verify SSL connection and download NLTK resources

import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

import urllib.request

# Test SSL connection to a known secure website
try:
    response = urllib.request.urlopen("https://www.google.com")
    print("SSL connection successful!")
except Exception as e:
    print(f"SSL connection failed: {e}")

# Ensure that the necessary NLTK resources are downloaded
import nltk
nltk.download('punkt')