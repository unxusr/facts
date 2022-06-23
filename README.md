# Facts
API for bringing some useful information about anything

Facts is a solution for chatbots fallback; Instead of fallback on the basic answers when the user questions are not detected by the model then this request can be made from the backend and bring some facts, logical answer and some usefull data that can be used in many ways for the undetected question.


### Features
- Getting facts from conceptnet API
- Getting results from google search API
- Text processing API for sentiment analysis
- Extract colors from text
- Extract dates from text
- Extract numbers from text
- Extract currencies from text
- Get words in multiple languages
- Extract cities from text
- Extract countries from text

### Usage

Update settings_template.py by your google API key and search engine Id and rename the file to `settings.py`

```sh
cd facts
pip3 install -r requirements.txt
flask run
curl "http://127.0.0.1:5000/facts/i%20got%20a%20black%20shoe%20by%2020%20EGP%20from%20spain%20in%20june%202017"
```

### Example response

```sh
{
"Cardinals": [
"dates: [june 2017]",
"Cardinals: [20]"
],
"Colors": [
"black"
],
"Currencies": "Egyptian Pound",
"Facts": [
"a hole is for black",
"oil is related to black",
"coal is related to black",
"black is related to color",
"record is related to black",
"black is related to dark",
"A sole is part of a shoe",
"lace is a part of shoe",
"outsole is a part of shoe",
"counter is a part of shoe",
"upper is a part of shoe",
"a shoe is used for foot protection",
"shoe is related to foot",
"sock is related to shoe",
"shoe is related to footwear",
"shoe is related to feet",
"polish is related to shoe",
"Malaga is a part of Spain",
"Jerez is a part of Spain",
"San Sebastian is a part of Spain",
"Andalusia is a part of Spain",
"Majorca is a part of Spain",
"Jefferson Davis' Birthday is a part of June",
"summer solstice is a part of June",
"Midsummer Day is a part of June",
"mid-June is a part of June",
"June is a part of Gregorian calendar",
"may is related to june",
"month is related to june"
],
"Google_result": "After reading this section of the book have your opinions changed about math classes and ... and June 20 percent between July and September and 10.",
"Languages": {
"Chinese": [
0.963,
"六月"
],
"Dutch": [
0.973,
"juni"
],
"English": [
1.0,
"june"
],
"French": [
0.964,
"juins"
],
"German": [
0.983,
"junis"
],
"Italian": [
0.976,
"giugno"
],
"Japanese": [
0.967,
"水無月"
],
"Portuguese": [
0.988,
"junho"
],
"Russian": [
0.959,
"июню"
],
"Spanish": [
0.981,
"junios"
]
},
"Location": [
"Cities: []",
"Countries: ['Spain']"
],
"Sentiment": "Neutral"
}
```
More features and enhancement to be added soon, Pull requests are also welcome 

### License 

GNU
