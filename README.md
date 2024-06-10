# [Diplomatic Data](https://github.com/PaoloLanaro/diplomatic-data)
<img src="https://i.imgur.com/wN5KZOb.png" align="right" alt="diplomatic data logo by copilot image generator" width="84" height="84">

by [Paolo Lanaro](https://github.com/PaoloLanaro), [Sydney Schulz](https://github.com/sydneygschulz), [Nia Quinn](https://github.com/niaquinn), and [Milo Margolis](https://github.com/MiloMargolis)

## About
This project was created over the course of Northeastern University's Summer 2024 Dialouge of Civilizations to Leuven, Belgium focused on the intersection of software development and AI in the context of international policy and regulation. Targeted at understanding the relationships between various news sources and their influences on global sentiments, this app highlights how different users may be able to analyze countries of interests. They can predict sentiment scores of articles, track articles, and more! We invite you to explore and find how the Diplomatic Data team can help serve your purposes.

## Uses
When opening the app, the user can enter as three different personas, in addition to a system admin. The first of which, Anton Müller, is a foreign policy advisor at the EU. When entering as Anton, one can explore adding an article to the database and view articles that have been recently interacted with, as well as predict source countries of articles!

Another persona can enter as is Katerina Stepanov, a PR specialist at Gasprom Oil in Russia. As Katerina, you can calculate an article's sentiment score based off of various attributes about the article. Additionally, you can view articles in the database to then save, share, and like them for later viewing. 

Finally, one can enter as Monika José, a young traveller. As Monika, one can configure their preferences and search for different articles within the database.

## Structure
Below you can find the general structure of the project. The `api` directory contains the majority of the routes connecting each component of the various Docker containers. Within the   `api/backend/ml_models` directory, you can find the backend renferences for the main logic of the two machine learning models. 

From the `app` directory, one can find the main contents of the front end. The `app\src\pages` folder contains each of the pages a user can interact with. Inside of the `pages` folder, one can see each of the pages labeled with the first two digits of each page representing its location within the app. For example, all of the pages a user acting as Anton can view begin with `0X`. 

Finally, the other main component of the project structure is the `database` folder which contains all of the information allowing for users to interact with articles and training data for the two machine learning models, amongst other features.

```
└───diplomatic-data
    ├───api
    │   └───backend
    │       ├───activity
    │       ├───article_data
    │       ├───assets
    │       │   ├───utils
    │       ├───customers
    │       ├───db_connection
    │       ├───ml_models
    │       ├───models
    │       ├───products
    │       ├───social
    ├───app
    │   └───src
    │       ├───assets
    │       ├───modules
    │       └───pages
    ├───database
    └───fake_data
```

## Improvements To Make & Current Limitations
For future iterations of this app, there can be improvements upon the validity and accuracy of the ML models in terms of both the capacity of training data and general span.
