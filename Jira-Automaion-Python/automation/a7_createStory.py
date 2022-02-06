'''
Created on Jan. 26, 2022

@author: amitmittal
@description: Story class creates story in Jira using python
It accepts the variable from the test file
'''

import requests
from requests.auth import HTTPBasicAuth
from automation import key
import json

 
class Story():
    
    url = "https://freetestingapi.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("hi.amitmittal@gmail.com", key.Key().key)
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    def __init__(self, summary, desc, issueType, project_key, parent_key, word):
        
        self.summary = summary
        self.desc = desc
        self.issueType = issueType
        self.project_key = project_key
        self.parent_key = parent_key
        self.word = word
    
    def createStory(self):
        
        payload = json.dumps( {
            
            "fields": {
                "summary": self.summary,
                "description": self.desc,
                "issuetype": {
                    "id": self.issueType,
                    },
                "parent":{
                    "key": self.parent_key
                    },
                "project":{
                    "key": self.project_key
                    },
                "assignee": {
                    "id": key.Key().assign
                    },
                "labels":self.word
                }
            }
        )
        
        response = requests.request(
           "POST",
           self.url,
           data=payload,
           headers=self.headers,
           auth=self.auth,
           )
        
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))