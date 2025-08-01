# Automated Content Aggregator

> This project automatically pulls the latest stories from Hacker News and writes them into this README. It's a living document, updated daily by a script, showcasing a simple and practical use of automation within a GitHub repository.

## The Core Idea

This system was built to demonstrate a fundamental skill in modern software development: automation. Instead of just writing a script that runs once, this project uses GitHub Actions to create a hands-free process that keeps the repository's content fresh. It's a practical example of how to integrate data fetching, code execution, and version control into a cohesive, automated workflow.

## How It Works

The project is driven by two key components working in concert.

* **The Python Script**: At its heart is an object-oriented Python script (`aggregator.py`). It's responsible for connecting to the Hacker News API, fetching the current top stories, and then formatting them into clean markdown.

* **The GitHub Action**: A workflow file (`.github/workflows/update_readme.yml`) acts as the scheduler. It tells GitHub to run the Python script at a set time every day. After the script updates the README, the workflow automatically commits the changes and pushes them back to this repository.

## Getting Started

To use this project, you only need the three core files in a GitHub repository:

1.  `aggregator.py`
2.  `requirements.txt`
3.  `.github/workflows/update_readme.yml`

Once they are pushed to GitHub, the Action will activate and handle the rest.

## Customization

The script is designed to be easy to modify. You can change the number of stories fetched or even add new data sources (like a different API or an RSS feed) by editing the `aggregator.py` file.
