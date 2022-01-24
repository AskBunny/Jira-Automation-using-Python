'''
Created on Jan. 20, 2022

@author: amitmittal
'''

import requests
from requests.auth import HTTPBasicAuth
import json

#To check the projects and key
# https://freetestingapi.atlassian.net/rest/agile/latest/board/

# projectTemplateKey(s): 
#https://confluence.atlassian.com/jirakb/creating-projects-via-rest-api-in-jira-963651978.html
# Scrum: "com.pyxis.greenhopper.jira:gh-scrum-template"
# Kanban: "com.pyxis.greenhopper.jira:gh-kanban-template"
# Basic: "com.pyxis.greenhopper.jira:basic-software-development-template"
 #business: com.atlassian.jira-core-project-templates:jira-core-simplified-project-management
 
class Project():
    
    url = "https://freetestingapi.atlassian.net/rest/api/3/project"
    auth = HTTPBasicAuth("hi.amitmittal@gmail.com", "4x7NQ3XzzcKZog9t6HsXAFBC")
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    #user 'admin@domain.com:A1b2345CdEfgHIJkLMn67O8Q'
    }

    def __init__(self, define_key, project_name, desc):
        self.define_key = define_key
        self.project_name = project_name
        self.desc = desc
    
    def createProject(self):
        payload = json.dumps( {

            "key": self.define_key,
            "name": self.project_name,
            "projectTypeKey": "software",
            "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-kanban-template",
            "description": self.desc,
            "assigneeType": "PROJECT_LEAD", #Role
            "leadAccountId":"61e6f63884311c00691fab2a",
            "avatarId": 10200 #Display Picture
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
            
