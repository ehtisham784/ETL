import requests
import json
import pandas
import sqlite3
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LinkedinPost')


# Extract Data
url = "https://linkedin-data-api.p.rapidapi.com/get-profile-posts"

headers = {
	"x-rapidapi-key": "8956d801acmsh04f94bafff31789p172285jsnb510c8cb3aa3",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}


# dictionary = json.loads(data)

#function
def function(argument):
    response = requests.get(url, headers=headers, params=argument)
    # data = response.json()
    if response.status_code == 200:
        data = response.json()
        # df = pandas.DataFrame(data)
        # print(data)
        posts = []
        for post in data['data']:
            # text = post.get('text')
            total_reactions = post.get('totalReactionCount')
            like_count = post.get('likeCount')
            appreciation_count = post.get('appreciationCount')
            comments_count = post.get('commentsCount')
            post_url = post.get('postUrl')
            posted_date = post.get('postedDate')

            author = post.get('author', {})
            first_name = author.get('firstName')
            last_name = author.get('lastName')
            headline = author.get('headline')
            username = author.get('username')

            posts.append({
                # 'Text': text,
                'Total Reactions': total_reactions,
                'Like Count': like_count,
                'Appreciation Count': appreciation_count,
                'Comments Count': comments_count,
                # 'Post URL': post_url,
                'Posted Date': posted_date,
                'Author First Name': first_name,
                'Author Last Name': last_name,
                # 'Author Headline': headline,
                'Author Username': username,
            })

        return posts

    else:
        print("failed")




    # combine all the data

# Transform Data

# Load data
# Linkedin_post_tbl.to_csv('post.csv', index=False)





    # connection = sqlite3.connect('Linkedin_db')
    # Linkedin_post_tbl.to_sql('Linkedin_post', connection, if_exists='replace', index = False)
    # query = "SELECT * FROM Linkedin_post WHERE Post_ID = 2"
    # result = pandas.read_sql(query, connection)
    # # print(result)
    # connection.close()