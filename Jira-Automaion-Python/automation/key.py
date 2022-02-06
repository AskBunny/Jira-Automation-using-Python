'''
Created on Feb. 3, 2022

@author: amitmittal
@description: Key class all the values which can be changed as per user profiles and issue types. Changes can be made here which are used in other classes. 
'''

class Key():
    
    def __init__(self):
        self.key = ''
        self.project_key = 'FP' #'DQA'
        self.epic_kinaxis = 'FP-19' #'DQA-729'
        self.epicIssueTypeID = '10008' #'6'
        self.storyIssueType = '10004'
        self.subtaskStoryIssueType = '10009'
        self.assign= '61e7160a38041c006854cd45'