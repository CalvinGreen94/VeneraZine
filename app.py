# import numpy as np
from flask import Flask, session, abort, request, jsonify, render_template, redirect, url_for, flash, redirect
# import pyttsx3
# import datetime
# import wolframalpha
import os
# import wikipedia
import datetime
import hashlib
import json
from urllib.parse import urlparse
# from uuid import uuid4
from flask_cors import CORS
# from faunadb import query as q
# from faunadb.client import FaunaClient
# from faunadb.objects import Ref
# from faunadb.errors import BadRequest, NotFound
# Part 1 - Building a Blockchain
# from web3 import Web3
# from web3 import middleware
# from web3.middleware import geth_poa_middleware
# from tronpy import Tron, Contract
# from tronpy.keys import PrivateKey
# import pickle
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler as mini
# import os
# import stripe
# import time
# # import datetime
# import bs4
# import urllib.request
import requests
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup
# import random
import asyncio
# from twilio.base.exceptions import TwilioRestException
# from authy.api import AuthyApiClient
from flask_bootstrap import Bootstrap
import openai
# import shutil
# from twilio.rest import Client
# from clint.textui import progress
# from ecapture import ecapture as ec
# from espeakng import ESpeakNG
# import wave
# import json
# import pyaudio
# import StringIO
import os
# from os.path import join, dirname
# from dotenv import load_dotenv

# dotenv_path = '.env'
# load_dotenv(dotenv_path)

import pandas as pd
import numpy as np
import datetime as dt
# import cbpro
# import matplotlib.pyplot as plt 
import time
# from web3.middleware import geth_poa_middleware
# from web3.gas_strategies.time_based import medium_gas_price_strategy
# # from eth_account.messages import encode_defunct

# from web3 import Web3
import json
# import librosa


# from web3 import Web3
# from web3 import middleware
# from web3.middleware import geth_poa_middleware
# from web3.auto import w3
# infura_url = "https://mainnet.infura.io/v3/5c9cb0b35a2742659dec6fc7680c16c4"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# web3.middleware_onion.inject(geth_poa_middleware, layer=0)


# from coinbase.wallet.client import Client
import json
import pandas as pd 
# Before implementation, set environmental variables with the names API_KEY and API_SECRET
# from web3.auto import w3
from uuid import *
# client = Tron()
import braintree

from werkzeug.security import generate_password_hash, check_password_hash
from faunadb import query as q
from faunadb.client import FaunaClient
from faunadb.objects import Ref
from faunadb.errors import BadRequest, NotFound

import requests

import urllib.request

import shutil


app = Flask(__name__)
# bootstrap = Bootstrap(app)
# Fclient = FaunaClient(secret="fnAEflNSoFAAQ0DqKRR3lLxOKA53IcVSdw2WL8un",domain="db.us.fauna.com")

# cors = CORS(app, resources={r"/*": {"origins": ["http://yappolafranc.herokuapp.com/yappchat_gpt","http://yappolafranc.herokuapp.com/image_bot"]}})
# cors = CORS(infura_url, resources={r"/*": {"origins": "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"}})

# app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'  # default to 'secondary'
# app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'lumen'
app.secret_key = 'regurgitationA maximation'

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

TIMEOUT_SECONDS = 2


def worker(ws, loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ws.start())

@app.route('/')
def home():
    return render_template('index.html')

usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}


if __name__ == "__main__":
    # debug=True,host="0.0.0.0",port=50000
    app.run(debug=True, host="0.0.0.0", port=5000)