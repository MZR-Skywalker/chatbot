# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:44:01 2024

@author: lenovo
"""

import os
# import configparser
import requests

class HKBU_ChatGPT():
    #def __init__(self,config_path='./config.ini'):
    #    if type(config_path) == str:
    #        self.config = configparser.ConfigParser()
    #        self.config.read(config_path)
    #    elif type(config_path) == configparser.ConfigParser:
    #        self.config = config_path
    
    # def submit(self,message):
    def submit(message):
        conversation = [{"role": "user", "content": message}]
        
        url = (os.environ['BASICURL']) + "/deployments/" + (os.environ['MODELNAME']) + "/chat/completions/?api-version=" + (os.environ['APIVERSION'])

        headers = { 'Content-Type': 'application/json',
        'api-key': (os.environ['ACCESS_TOKEN_GPT']) }
        payload = { 'messages': conversation }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()
    
    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)