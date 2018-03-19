# Twitter Sentiment Analysis Using Python 
Before I tell you to run this project , this project i learn from this link.. https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-

## How to Run This Project ?

1. Create Twitter App , I learn it from this site https://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/
2. Change the file **TwitterConfig.example.py** to **TwitterConfig.py** and fill the blank with your key and access token.
3. install all libraries with pip  
```
    pip install -r requirements.txt 
```
4. Fill the query that will you analyze in parameter q on  **SentimentAnalysis.py** files , like this example.. i'll analyze twit that contains 'muslim'
```
 tweets = extractor.search(q="Muslim",lang="en",count="200")
```
6. Run the project and you're done...
