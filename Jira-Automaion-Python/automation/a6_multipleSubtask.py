'''
Created on Jan. 21, 2022

@author: amitmittal
'''

import requests
from requests.auth import HTTPBasicAuth
import json
import openpyxl

#1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys="Enter here"
#2. Get the key for the Task
 
class MultipleSubtask():
    
    url = "https://freetestingapi.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("hi.amitmittal@gmail.com", "4x7NQ3XzzcKZog9t6HsXAFBC")
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    def __init__(self, issueType, parent_key, project_key):
        
        self.issueType = issueType
        self.parent_key = parent_key
        self.project_key = project_key
    
    def multiSubtask(self):
        
        #Access Excel
        wbook = openpyxl.load_workbook('Issue.xlsx') #Access the file
        shee1 = wbook['Sheet1'] #Access Sheet1
        rows = shee1.max_row #Number of rows
        
        
        for j in range (1, rows):
            payload = json.dumps( {
                
                "fields": {
                    "summary": shee1.cell(j+1,1).value,
                    "description": shee1.cell(j+1,2).value,
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
                
