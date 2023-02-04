'''
Generate a .csv of Smartsheet workspaces in Name, ID format
'''

import smartsheet
import csv

token = [TOKEN]
smartsheet_client = smartsheet.Smartsheet(token)
smartsheet_client.errors_as_exceptions(True)

response = smartsheet_client.Workspaces.list_workspaces(include_all=True)
workspaces = response.data

with open('workspaces.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for workspace in workspaces:
        writer.writerow([workspace.name, workspace.id])

print('Complete.')