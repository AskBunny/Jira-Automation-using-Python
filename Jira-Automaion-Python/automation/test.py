'''
Created on Jan. 21, 2022

@author: amitmittal
@description: This is the main file which calls all the other classes as per their task.
'''
import requests
import base64
import json
from automation import a1_createProject, a2_createEpic, a3_createTask, a4_createSubtask, a5_multipleTask, a6_multipleSubtask, a7_createStory, key 

'''
@description: label function takes the input from user and split into label which is stored in the Jira's epic
'''

def labelForEpic():
    text = input("Please enter free text with a space for the label: ")
    labels = text.split()
    return labels

'''
@description: label function checks if parent has the label and if not then it takes the input from user and split into label which is stored in 
the Jira's EPIC(for partner)/story/subtask.
'''

def label(parentKey):
    parent_key = parentKey

    REQUEST_URL = 'https://freetestingapi.atlassian.net/rest/api/3/issue/'+parent_key+'/?fields=labels'
    login = 'hi.amitmittal@gmail.com'
    password = key.Key().key
    response = requests.get(REQUEST_URL, auth=(login, password))

    json_data = response.text.encode('utf-8', 'ignore')
    data = json.loads(json_data)
    
    data_label = data['fields']['labels']
    
    if not data_label:
        text = input("Please enter free text with a space for the label: ")
        labels = text.split()
        return labels
    else:
        #labels = ""
        labels = []
        for l in data_label:  
            labels.append(l)  
        #    labels += (l+" ")
        return labels
    
'''
@description: dep_check method asks user if it is Initial deployment or Rollout so that the input can be used in the summary for task creation. 
    It is solely to use while naming the task.
'''

def dep_check(): #Deployment check
    
    print("Is this 'Initial Deployment (Press 1) or 'Roll out (Press 2)?")
    
    dep_type = int(input("Enter here: \n"))
    
    if (dep_type == 1):
        dep_value = "Initial Deployment"
        return dep_value
    elif(dep_type == 2): 
        dep_value = "Rollout"
        return dep_value
    else:
        print("Try again\n")
        dep_check()

dep_value = dep_check()

'''
@description: featursWithoutEpic method is used to create story, subtask and multiple subtasks for Kinaxis led projects
It accepts the input from user and accordingly performs the task.
'''

def featursWithoutEpic(): #Kinaxis led

    print("Please select one option: \n"
          "1. Story: \n2. Subtask: \n3. Multiple Subtask: \n8. Main menu: \n9. Exit: ")
    num = int(input("Enter here: \n"))
    print("\n")
    
    global dep_value
    
    partner = "Kinaxis led"
    
    while(num!=9):
            
        if (num==1):    
            #Story
            cust = input("Please enter the customer name: ")
            summary = cust +" "+ dep_value +" ("+ partner +")" 
            desc = ""
            word = labelForEpic()
            
            project = a7_createStory.Story(summary, desc, key.Key().storyIssueType, key.Key().project_key, key.Key().epic_kinaxis, word)
            project.createStory()
            
        elif (num==2):    
            #Subtask
            print("Get the parent key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n")
            parent_key = input("Enter the parent key (Story): ")
            summary = input("Enter the summary for the subtask: ")
            word = label(parent_key)
            desc = ""
            
            project = a4_createSubtask.Subtask(summary, desc, key.Key().subtaskStoryIssueType, parent_key, key.Key().project_key, word)
            project.createSubtask()
    
        elif (num==3):
            #MultipleSubtask
            print("Get the parent key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n")
            parent_key = input("Enter the parent key (Story): ")
            value = project_type()
            
            project = a6_multipleSubtask.MultipleSubtask(key.Key().subtaskStoryIssueType, parent_key, key.Key().project_key, value)
            project.multiSubtask(dep_value)
            
        elif (num==8):
            #Main menu
            dep_value = dep_check()
            project_led()
            
        elif (num==9):
            break
            
        else:
            print("Please enter a valid key.\n")
            
        print("Please select one option: \n"
          "1. Story: \n2. Subtask: \n3. Multiple Subtask: \n8. Main menu: \n9. Exit: ")
        num = int(input("Enter here: \n"))
    
    print("Thank you, see you soon!")

'''
@description: featursWithEpic method is used to create epic, story, subtask and multiple subtasks for partner led projects
It accepts the input from user and accordingly performs the task.
'''

def featursWithEpic(): #Partner led

    print("Please select one option: \n"
          "1. EPIC: \n2. Story: \n3. Subtask: \n4. Multiple Subtask: \n8. Main menu: \n9. Exit: ")
    num = int(input("Enter here: \n"))
    print("\n")
    
    global dep_value
    
    while(num!=9):
        
        if (num==1):
            #Epic
            partner = input("Please enter the partner's name: ")
            cust = input("Please enter the customer name: ")
            
            summary = cust + " (" + partner + " led)"
            print("Epic name is: {}".format(summary))
            desc = ""
            word = labelForEpic()
            
            project = a2_createEpic.Epic(summary, desc, key.Key().epicIssueTypeID, key.Key().project_key, word)
            project.createEpic() 
            
        elif (num==2):    
            #Story
            partner = input("Please enter the partner's name: ")
            cust = input("Please enter the customer name: ")
            
            print("Get the parent key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n")
            parent_key = input("Enter the parent key (EPIC): ")
            summary = cust + " " + dep_value + " (" + partner + ")" 
            desc = ""
            word = label(parent_key)
            
            project = a7_createStory.Story(summary, desc, key.Key().storyIssueType, key.Key().project_key, parent_key, word)
            project.createStory()
    
        elif (num==3):    
            #Subtask
            print("Get the parent key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n")
            parent_key = input("Enter the parent key (Story): ") #Enter the value in this case
            summary = input("Enter the summary for the subtask: ")
            desc = ""
            word = label(parent_key)
            
            project = a4_createSubtask.Subtask(summary, desc, key.Key().subtaskStoryIssueType, parent_key, key.Key().project_key, word)
            project.createSubtask()
                
        elif (num==4):
            #MultipleSubtask
            print("1. Get the project key and task key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n")
            parent_key = input("Enter the parent key (EPIC/Story/Task): ")
            value = project_type()
                        
            project = a6_multipleSubtask.MultipleSubtask(key.Key().subtaskStoryIssueType, parent_key, key.Key().project_key, value)
            project.multiSubtask(dep_value)
            
        elif (num==8):
            #Main Menu
            dep_value = dep_check()
            project_led()
        
        elif (num==9):
            break
            
        else:
            print("Please enter a valid key.\n")
            
        print("Please select one option: \n"
          "1. EPIC: \n2. Story: \n3. Subtask: \n4. Multiple Subtask: \n8. Main menu: \n9. Exit: ") 
        num = int(input("Enter here: \n"))
    
    print("Thank you, see you soon!")

'''
@description: It checks whether issue is Kinaxis led or partner led and passes the input to either featursWithoutEpic or featursWithEpic as per input
'''

def project_led():
    
    print("\nPlease enter '1' if this is Kinaxis led project or else '2'")
    
    led = int(input("Enter here: \n"))
    
    if (led == 1):
        featursWithoutEpic()

    elif (led == 2):
        featursWithEpic()
    
    else:
        print("Try again\n")
        project_led()

'''
@description: It checks whether issue is RapidStart or RapidResponse (if dep_check is Initial Deployment) and returns the input which is further used to while creating multiple subtasks.
'''

def project_type():
    
    if (dep_value == "Initial Deployment"):
        print("Is project RapidStart (Press 1) or RapidResponse (Press 2): ")
        val = int(input("Enter here: \n"))
        if (val == 1):
            val = "RapidStart"
            return val
        else: 
            val = "RapidResponse"
            return val
    
    else:
        val = "Rollout"
        return val

project_led()
