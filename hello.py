#!/usr/bin/env python3
"""Hello World Multi Language.

Exhibits the message according to the language set in the environment.

Usage:

Have the LANG variable properly configured in your environment. ex:

   export LANG=en_US

Execution:

   python3 hello.py
   or
   ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Rauan Rezende"
__license__ = "Unlicense"


import os 

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
   msg = "Olá, Mundo!"
elif current_language == "it_IT":
   msg = "Ciao, Mondo!"
   
print(msg)
