"""A simple example of how to access the Google Analytics API."""

import argparse

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

import pandas

import urllib2



def get_service(api_name, api_version, scope, key_file_location,
                service_account_email):
  """Get a service that communicates to a Google API.

  Args:
    api_name: The name of the api to connect to.
    api_version: The api version to connect to.
    scope: A list auth scopes to authorize for the application.
    key_file_location: The path to a valid service account p12 key file.
    service_account_email: The service account email address.

  Returns:
    A service that is connected to the specified API.
  """

  f = open(key_file_location, 'rb')
  key = f.read()
  f.close()

  credentials = SignedJwtAssertionCredentials(service_account_email, key,
    scope=scope)

  http = credentials.authorize(httplib2.Http())

  # Build the service object.
  service = build(api_name, api_version, http=http)

  return service

def get_emails()  :
    # Get a list of emails to add:
  f = open ('emails.txt', 'r')
  emails = f.read()
  f.close()
  return emails

def add_user(service) :
 
  f = open('emails.txt', 'rb')
  for email in f:  
   
  
    
    try:
        email = email.rstrip()
        profile_links = service.management().profileUserLinks().insert(
           
            accountId='00000000',
            webPropertyId='UA-00000000-1',
            profileId='000000000',
            body={
            'permissions': {
                  'local': [
                      'READ_AND_ANALYZE'#,
                  #not 'READ_AND_ANALYSE'
                 ]
            },
            'userRef': {
                  'email': email
            }
        }  
                  
        ).execute()
        continue
        return profile_links

    except TypeError, error:
    # Handle errors in constructing a query.
        print 'There was an error in constructing your query : %s' % error
        
    #except HttpError, error:
   #  Handle API errors.
        #print ('There was an API error : %s : %s' %
           #(error.resp.status, error.resp.reason))
        continue
           


def main():
  # Define the auth scopes to request.
  scope = ['https://www.googleapis.com/auth/analytics.manage.users']

  # Use the developer console and replace the values with your
  # service account email and relative location of your key file.
  service_account_email = 'your_service_account_email'
  key_file_location = 'client_secrets.p12'

  # Authenticate and construct service.
  service = get_service('analytics', 'v3', scope, key_file_location,
    service_account_email)
  #profile = get_first_profile_id(service)
  #print_results(get_results(service, profile))
  user = add_user(service)
  print "All done"
  
  
  
 
    

# Note: This code assumes you have an authorized Analytics service object.
# See the User Permissions Developer Guide for details.


         
         
if __name__ == '__main__':
  main()
