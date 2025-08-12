# Player Division Level Classifier

This is my first ever project using Pytorch to train a model.

This model is trained using the college ultimate championship player statistics to determine if they are either a division 1 player of division 3 player.

The dataset was retrieved from Kaggle from the user Maxwell:
https://data.scorenetwork.org/disc_sports/ultimate_college_championship-2024.html

Original Source: Gavin Cassidy

Note: As of 11/08/2025 I have concluded that it is more appropriate to determine the division level of a team rather than each individual player. I have created a new model that is trained to distinguish each teams divisions.

# Team Division Level Classifier

I found that my model was capped at a 60% accuracy. So I have created a new model that determines a team's division level.

This model was trained using the 2024 championship statistics and tested with the 2025 statistics that I scrapped from the USA Ultimate website:
Division 1 Data: https://play.usaultimate.org/events/2025-USA-Ultimate-College-Championships
Division 3 Data: https://play.usaultimate.org/events/2025-USA-Ultimate-D3-College-Championships

With this model I have found more success, with the Decision Tree yielding a 86% accuracy for the male database, and 72% accuracy for the female database

# Using this Notebook

To use this notebook, clone the repository and the dataset from the github, make sure to run this code to ensure you have all the dependencies to run the notebook:

```pip install -r requirements.txt```
