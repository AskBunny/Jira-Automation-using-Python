'''
Created on Jan. 21, 2022

@author: amitmittal
'''
from automation import a1_createProject, a2_createEpic, a3_createTask, a4_createSubtask, a5_multipleTask, a6_multipleSubtask, a7_createStory 

print("Please select one option: \n"
      "1. Project: \n2. EPIC: \n3. Story: \n4. Task: \n5. Subtask: \n6. Multiple Task: \n7. Multiple Subtask: \n9. Exit: ")
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
    
    # elif (num==2):
    #     #Epic
    #     print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Epic\n")
    #     project_key = input("Enter the project key: ")
    #     issueType = input("Enter the issue type id for the Epic: ")
    #     name = input("Enter Epic's name: ")
    #     summary = input("Enter the summary for the Epic: ")
    #     desc = input("Enter the description: ")
    #
    #     project = a2_createEpic.Epic(name, summary, desc, issueType, project_key)
    #     project.createEpic()
        
    
    elif (num==2):
        #Epic
        
        led = int(input("Please enter '1' if this is Kinaxis led project \nor else '2'"))
        if (led == 1):
            cust = input("Please enter the customer name: ")
            partner = input("Please enter the partner's name: ")
            ename = cust + " " + partner + " Deployment"
            summary = cust + " " + partner + " led project"
            print("Epic name is {} & summary is {}".format(ename, summary))
            print("\n1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Epic\n")

            project_key = input("Enter the project key: ")
            issueType = input("Enter the issue type id for the Epic: ")
        
        
        
        desc = input("Enter the description: ")
        
        project = a2_createEpic.Epic(ename, summary, desc, issueType, project_key)
        project.createEpic() 
        
    elif (num==3):    
        #Story
        print("1. Get the project key and EPIC key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Story\n")
        project_key = input("Enter the project key: ")
        parent_key = input("Enter the parent key (EPIC/Story/Task): ")
        issueType = input("Enter the issue type id for the story: ")
        summary = input("Enter the summary for the story: ")
        desc = input("Enter the description: ")
        
        project = a7_createStory.Story(summary, desc, issueType, project_key, parent_key)
        project.createStory()
        
    elif (num==4):
        #Task
        print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        issueType = input("Enter the issue type id for the Task: ")
        summary = input("Enter the summary for the Task: ")
        desc = input("Enter the description: ")
        
        project = a3_createTask.Task(summary, desc, issueType, project_key)
        project.createTask()

    elif (num==5):    
        #Subtask
        print("1. Get the project key and task key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        parent_key = input("Enter the parent key (EPIC/Story/Task): ")
        issueType = input("Enter the issue type id for the subtask: ")
        summary = input("Enter the summary for the subtask: ")
        desc = input("Enter the description: ")
        
        project = a4_createSubtask.Subtask(summary, desc, issueType, parent_key, project_key)
        project.createSubtask()
        
    elif (num==6):
        #Multiple Task
        print("1. Get the project key from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        issueType = input("Enter the issue type id for the Task: ")
        
        project = a5_multipleTask.MultipleTask(issueType, project_key)
        project.multiTask()

    elif (num==7):
        #Subtask
        print("1. Get the project key and task key (Parent id) from the dashboard and go to the link: https://freetestingapi.atlassian.net/rest/api/latest/issue/createmeta?projecyKeys=\"Enter here\"\n2. Get the issue type id for the Task\n")
        project_key = input("Enter the project key: ")
        parent_key = input("Enter the parent key (EPIC/Story/Task): ")
        issueType = input("Enter the issue type id for the subtask: ")
        
        project = a6_multipleSubtask.MultipleSubtask(issueType, parent_key, project_key)
        project.multiSubtask()
        
    elif (num==9):
        break
        
    else:
        print("Please enter a valid key.\n")
        
    print("Please select one option: \n"
      "1. Project: \n2. EPIC: \n3. Story: \n4. Task: \n5. Subtask: \n6. Multiple Task: \n7. Multiple Subtask: \n9. Exit: ")
    num = int(input("Enter here: \n"))

print("Thank you, see you soon!")



#"assignee": {"accountId": "[account_id_here]" }
