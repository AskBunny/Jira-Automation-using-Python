# Jira-Automation-using-Python
This repository helps to automate basic Jira's operations using python
- Project with a template (depending on the requirement)
- Epic under a project
- Task to assign a particular project
- Subtask for any project
- Can also create multiple tasks if required; for that, add the details
like title and description in the excel sheet, and python will take care
of it.

Note: User has to define the key in key file to access the personal account to run the code.

There are couple of things to access the API
- Access token key 
- User key of (Avialable in user profile's web address)
  - Reportee's code (Who runs the code)
  - Assignee's key (Who complete the task)
  -  
Note: The user will be able to perform actions on the API as per permission level, if for example, user doesn't have  permissions to create new projects in JIRA, he will be not able to do it using the API token too. This means that in some cases he will need to ask someone to provide the API token with more access — depends on the integration.
