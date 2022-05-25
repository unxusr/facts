# Facts
API for bringing some useful information about any thing

Facts is a solution for chatbots fallback; Instead of fallback on the basic answers when the user questions are not detected by the model then this request can be made from the backend and bring some facts and logical answer for the undetected question.


### Features
- Getting facts from conceptnet API
- Getting results from google search API
- Text processing API for sentiment analysis

### Usage

Update settings_template.py by your google API key and search engine Id and rename the file to `settings.py`

```sh
cd facts
pip3 install -r requirements.txt
flask run
curl "http://127.0.0.1:5000/facts/can%20you%20cook"
```

### Example response

```sh
[
  [
    "Your phrase was:-> can you cook.", 
    "Sentiment:-> Negative"
  ], 
  "Answer: Cooking's great and I love it. Every time I saw the TV show: \"Master Chef\" I feel hungry and want to cook. I can cook yogurt cake beefsteak\u00a0...", 
  [
    "You can use a stove to cook", 
    "You can use fire to cook", 
    "You can use a baking oven to cook", 
    "You can use a kitchen to cook", 
    "You can use a machine to cook"
  ]
]
```
More features and enhancement to be added soon, Pull requests are also welcome 

### License 

GNU
