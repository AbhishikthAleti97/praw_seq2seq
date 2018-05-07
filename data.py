import praw
from credentials import *
import os

reddit = praw.Reddit( client_id = my_id,
client_secret = my_client_secret,
username = user_name,
password = pass_word,
user_agent = 'depressedbot'
)

subreddit = reddit.subreddit(subreddit_name)
top_depression = subreddit.top('all',limit=1000) #can set max limit to 1000

if not os.path.exists(datasets):
    os.makedirs(datasets)



def cleaned_data(data):
    data = data.replace("\n", " ").replace("\r"," ").replace('"',"'")
    return data



def data_acceptable(data):
    if len(cleaned_data(data).split(' ')) > 90 or len(cleaned_data(data))<1:
        return False
    elif len(cleaned_data(data)) > 800:
        return False
    elif data == '[deleted]' or data == '[removed]':
        return False
    else:
        return True


def write_to_file(text, more_text):
    f = open(datasets+"/data_"+subreddit_name,"a+")
    f.write(cleaned_data(text)+"\n")
    f.write(cleaned_data(more_text)+"\n")
    f.close()
    return
    #Gotta write to csv

def fetch_comments():
    for submission in top_depression:
        submission.comments.replace_more(limit=0)

        for comment1 in submission.comments:

            for comment2 in comment1.replies:
                if(comment2.ups>2 and data_acceptable(comment2.body)):
                    if(data_acceptable(comment1.body) and data_acceptable(comment2.body)):
                        print ("comment: "+cleaned_data(comment1.body)+"\nups:"+str(submission.ups))
                        print ("reply: "+cleaned_data(comment2.body))
                        write_to_file(comment1.body,comment2.body)


                for comment3 in comment2.replies:
                    if(comment3.ups>2 and data_acceptable(comment3.body)):
                        if(data_acceptable(comment3.body) and data_acceptable(comment2.body)):
                            print("reply: "+cleaned_data(comment2.body))
                            print("reply to reply: "+cleaned_data(comment3.body))
                            write_to_file(comment2.body, comment3.body)


                    for comment4 in comment3.replies:
                        if(comment4.ups>2 and data_acceptable(comment4.body)):
                            if(data_acceptable(comment4.body) and data_acceptable(comment3.body)):
                                print("reply to reply: "+cleaned_data(comment3.body))
                                print("reply to the reply of the reply: "+cleaned_data(comment4.body))
                                write_to_file(comment3.body, comment4.body)





if __name__=="__main__":
    fetch_comments()
