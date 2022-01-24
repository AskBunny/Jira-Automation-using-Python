'''
Created on Jan. 21, 2022

@author: amitmittal
'''

import requests
from requests.auth import HTTPBasicAuth
import json


#1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys="Enter here"
#2. Get the key for the Subtask
 
class Subtask():
    
    url = "https://freetestingapi.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("hi.amitmittal@gmail.com", "4x7NQ3XzzcKZog9t6HsXAFBC")
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    def __init__(self, summary, desc, issueType, parent_key, project_key):
        
        self.summary = summary
        self.desc = desc
        self.issueType = issueType
        self.parent_key = parent_key
        self.project_key = project_key
    
    def createSubtask(self):
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
                    }           
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
        
        #print(response.text)
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
            
