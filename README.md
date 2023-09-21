# Footy-Players

Welcome to the Footy Players Data Management repository! This project consists of a set of Python scripts that automate the collection, enhancement, and storage of football player data. Whether you're a football enthusiast or just interested in learning about web scraping, JSON manipulation, and MongoDB integration, this repository has something for you.

## Overview

In this project, I've created two Python scripts:

1. **crawler.py**: This script fetches JSON objects from a JSON bin and uses web scraping techniques to find and update each player's image url by searching Google and copying the link. The updated data is then saved to another JSON bin.

2. **populater.py**: This script reads the updated JSON objects from the JSON bin and populates a MongoDB collection with this enriched player data.

## Feature

- **Automating the boring stuff**: There was no need to manually searching for player images and copy the respective image links! The script harnesses the power of web scraping to fetch and update player images automatically. Also, the updated players' data was populated to a MongoDB collection effortlessly!.


## Getting Started

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/{your-username}/Footy-Players.git
   ```
2. Install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```
3. Configure your JSON bin API endpoints and MongoDB connection details in the respective scripts. [npoint](https://npoint.io) is recommended
4. Run the scripts:
    ```shell
    python crawler.py
    python populater.py
    ```

## Contributions

 Feel free to submit bug reports, feature requests, or even pull requests to help make this mini-project even better.