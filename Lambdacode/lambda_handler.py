import api_testing
from api_testing import function, pandas, table, json
import api_testing
import pandas as pd
import boto3
import json

# Assuming you have a DynamoDB client set up like this:
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('YourTableName')

# This is the Lambda function that contains the actual business logic
def my_lambda_function(event):
    # Define the parameters for users
    ehti_params = {"username": "ehtisham-hashmi-61a984181"}
    ali_params = {"username": "alisaqlain818"}
    zaid_params = {"username": "zaid-farooq-1b129a9b"}

    # Call the function to get posts
    post_ehti = api_testing.function(ehti_params)
    post_zaid = api_testing.function(zaid_params)
    post_ali = api_testing.function(ali_params)

    # Combine the posts and create a pandas DataFrame
    combined_post = post_ehti + post_zaid + post_ali
    Linkedin_post_tbl = pd.DataFrame(combined_post)

    # Add a Post_ID column
    Linkedin_post_tbl['Post_ID'] = Linkedin_post_tbl.index + 1

    # Fill missing values with 0
    Linkedin_post_tbl.fillna(0, inplace=True)

    # Insert data into DynamoDB
    for row, index in Linkedin_post_tbl.iterrows():
        response_data = table.put_item(
            Item={
                'Post_ID': int(row['Post_ID']),
                'Total Reactions': int(row['Total Reactions']),
                'Like Count': int(row['Like Count']),
                'Appreciation Count': int(row['Appreciation Count']),
                'Comments Count': int(row['Comments Count']),
                'Posted Date': str(row['Posted Date']),
                'Author First Name': str(row['Author First Name']),
                'Author Last Name': str(row['Author Last Name']),
                'Author Username': str(row['Author Username']),
            }
        )
        print("Inserted data:", response_data)

    return {
        'statusCode': 200,
        'body': json.dumps("Data processed successfully")
    }

# This is the Lambda handler (entry point for AWS Lambda)
def lambda_handler(event, context):
    try:
        # Call the actual Lambda function that does the processing
        return my_lambda_function(event)

    except Exception as e:
        print(f"Error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing data: {str(e)}")
        }
