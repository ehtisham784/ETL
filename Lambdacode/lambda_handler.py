import api_testing
from api_testing import function, pandas, table, json
def lambda_handler():
    # define the values for our parameters
    ehti_params = {"username": "ehtisham-hashmi-61a984181"}
    ali_params = {"username": "alisaqlain818"}
    zaid_params = {"username": "zaid-farooq-1b129a9b"}

    # call the function
    post_ehti = function(ehti_params)
    post_zaid = function(zaid_params)
    post_ali = function(ali_params)

    combined_post = post_ehti + post_zaid + post_ali
    Linkedin_post_tbl = pandas.DataFrame(combined_post)

    Linkedin_post_tbl['Post_ID'] = Linkedin_post_tbl.index+1
    Linkedin_post_tbl.fillna(0, inplace=True)

    # print(Linkedin_post_tbl)
    # insert transformed data into dynamodb
    #dynamo works with row and index
    for row, index in Linkedin_post_tbl.iterrows():
        response_data = table.put_item(
            item={
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
        print("Inserted data")

    return{
        'statusCode': 200,
        'body': json.dumps("Data processed")
    }