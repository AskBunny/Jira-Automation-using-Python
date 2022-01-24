'''
Created on Jan. 21, 2022

@author: amitmittal
'''
from automation import a1_createProject, a2_createEpic, a3_createTask, a4_createSubtask, a5_multipleTask, a6_multipleSubtask 

print("Please select one option: \n"
      "1. Project: \n2. EPIC: \n3. Task: \n4. Subtask: \n5. Multiple Task: \n6. Multiple Subtask: \n9. Exit: ")
num = int(input("Enter here: \n"))
print("\n")

while(num!=9):
    
    if (num == 1):
        #Project
        define_key = input("Enter the key for your project: ")
        project_name = input("Enter the name for your project: ")
        desc = input("Enter the description: ")
        
        project = a1_createProject.Project(define_key, project_name, desc)
        project.createProject()
    
    elif (num==2):
        #Epic
        print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Epic\n")
        project_key = input("Enter the project key: ")
        issueType = input("Enter the issue type id for the Epic: ")
        name = input("Enter Epic's name: ")
        summary = input("Enter the summary for the Epic: ")
        desc = input("Enter the description: ")
        
        project = a2_createEpic.Epic(name, summary, desc, issueType, project_key)
        project.createEpic()
        
    elif (num==3):
        #Task
        print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        issueType = input("Enter the issue type id for the Task: ")
        summary = input("Enter the summary for the Task: ")
        desc = input("Enter the description: ")
        
        project = a3_createTask.Task(summary, desc, issueType, project_key)
        project.createTask()

    elif (num==4):    
        #Subtask
        print("1. Get the project key and task key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        parent_key = input("Enter the parent key of the task: ")
        issueType = input("Enter the issue type id for the subtask: ")
        summary = input("Enter the summary for the subtask: ")
        desc = input("Enter the description: ")
        
        project = a4_createSubtask.Subtask(summary, desc, issueType, parent_key, project_key)
        project.createSubtask()
        
    elif (num==5):
        #Multiple Task
        print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        issueType = input("Enter the issue type id for the Task: ")
        
        project = a5_multipleTask.MultipleTask(issueType, project_key)
        project.multiTask()

    elif (num==6):
        #Subtask
        print("1. Get the project key and task key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        parent_key = input("Enter the parent key of the task: ")
        issueType = input("Enter the issue type id for the subtask: ")
        
        project = a6_multipleSubtask.MultipleSubtask(issueType, parent_key, project_key)
        project.multiSubtask()
        
    elif (num==9):
        print("Thank you, see you soon!")
        break
        
    else:
        print("Please enter a valid key.\n")
        
    print("Please select one option: \n"
      "1. Project: \n2. EPIC: \n3. Task: \n4. Subtask: \n5. MultipleTask: \n6. Multiple Subtask: \n9. Exit: ")
    num = int(input("Enter here: \n"))




#"assignee": {"accountId": "[account_id_here]" }
