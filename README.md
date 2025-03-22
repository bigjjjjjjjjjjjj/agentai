# agentai
Reflexive Web Agent for Automated Study Plan Generation
Overview
This project implements a Reflexive Web Agent that automates the generation of a 5-week study plan for programming courses. The agent uses Selenium to scrape YouTube for relevant programming courses based on a user-defined subject and leverages a large language model (LLM) from Hugging Face to create a detailed, personalized study plan. This tool is designed to assist learners by providing a structured learning path with weekly tasks, objectives, and resources.

Features
Web Scraping: Scrapes YouTube for programming course videos using Selenium.
Natural Language Processing: Generates study plans using the Hugging Face text-generation pipeline with the google/gemma-2b-it model.
Automation: Automates browser interactions with anti-bot detection avoidance.
Setup Instructions
Prerequisites
Python: Version 3.8 or higher
Google Chrome: Installed on your system
ChromeDriver: Must match your Chrome version
CUDA-enabled GPU (optional): For faster model inference with the LLM
Installation
Clone the Repository:
bash

Collapse

Wrap

Copy
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Python Dependencies:
bash

Collapse

Wrap

Copy
pip install selenium transformers torch huggingface_hub beautifulsoup4
Install ChromeDriver:
Download ChromeDriver from the official site.
Ensure the version matches your installed Google Chrome version.
Add chromedriver to your system’s PATH or specify its path in the webdriver.Chrome() call in the code.
Hugging Face Authentication:
Obtain a Hugging Face API token from Hugging Face.
Replace the placeholder token "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" in the code with your own token.
Usage
Run the Script:
bash

Collapse

Wrap

Copy
python study_plan_generator.py
By default, it generates a study plan for "Python". Modify the subject in the create_study_plan_with_courses() call to change it.
Customize the Subject:
Edit the script to generate a plan for a different subject, e.g., "JavaScript":
python

Collapse

Wrap

Copy
create_study_plan_with_courses("JavaScript")
Output:
The script outputs:
A list of YouTube courses (titles and URLs).
A 5-week study plan with weekly tasks, objectives, and suggested resources.
Implementation Details
1. Web Scraping with Selenium
Function: get_courses(subject)
Purpose: Fetches a list of programming courses from YouTube based on the subject.
Details:
Uses Selenium with a headless Chrome browser to navigate to https://www.youtube.com/results?search_query={subject}+programming+courses.
Waits 5 seconds (time.sleep(5)) for the page to load.
Parses the HTML with BeautifulSoup to extract video titles and URLs from <a id="video-title"> tags.
Returns a list of tuples: (title, url).
2. Study Plan Generation with Hugging Face LLM
Function: generate_study_plan(subject, courses)
Purpose: Creates a 5-week study plan using the scraped courses and the LLM.
Details:
Constructs a prompt with the subject and a formatted list of course titles and URLs.
Uses the text-generation pipeline with the google/gemma-2b-it model, running on CUDA if available.
Limits output to 768 tokens (max_new_tokens=256*3) for detailed yet concise plans.
Returns the generated text stripped of excess whitespace.
3. Integration
Function: create_study_plan_with_courses(subject)
Purpose: Combines web scraping and LLM generation into a single workflow.
Details:
Calls get_courses(subject) to retrieve courses.
Passes the results to generate_study_plan(subject, courses) to create the study plan.
Prints the available courses and the generated study plan.
4. ChromeDriver Configuration
Function: driver_config()
Purpose: Sets up Selenium’s ChromeDriver with anti-detection and performance options.
Details:
Options:
disable-blink-features=AutomationControlled: Prevents bot detection.
--headless: Runs without a visible browser window.
--disable-gpu, --disable-extensions, --disable-infobars: Optimizes performance.
Proxy settings: Ensures direct connection without interference.
Returns a configured webdriver.Chrome instance.
Code Structure
python

Collapse

Wrap

Copy
import torch
from transformers import pipeline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus

# LLM Pipeline
pipe = pipeline("text-generation", model="google/gemma-2b-it", token="your_token_here", device="cuda")

# ChromeDriver Setup
def driver_config(): ...

# YouTube Scraping
def get_courses(subject): ...

# Study Plan Generation
def generate_study_plan(subject, courses): ...

# Main Workflow
def create_study_plan_with_courses(subject): ...

# Run Example
create_study_plan_with_courses("Python")
Example Output
For the subject "Python":

text

Collapse

Wrap

Copy
Available Courses:
Title: Python for Beginners - URL: https://www.youtube.com/watch?v=abc123
Title: Advanced Python Programming - URL: https://www.youtube.com/watch?v=def456

Suggested Study Plan:
Week 1: Introduction to Python
- Watch "Python for Beginners" (URL: https://www.youtube.com/watch?v=abc123)
- Tasks: Learn basic syntax, variables, and data types.
- Objective: Build a foundation in Python.

Week 2: Intermediate Concepts
- Watch "Advanced Python Programming" (URL: https://www.youtube.com/watch?v=def456)
- Tasks: Explore functions and modules.
- Objective: Understand code organization.
...
Notes
Model Limitations: The google/gemma-2b-it model may produce inconsistent results. Consider upgrading to a larger model for better quality.
Scraping Reliability: YouTube’s layout may change, requiring updates to the BeautifulSoup parsing logic.
Performance: Adjust time.sleep(5) if dynamic content fails to load in headless mode.
License
This project is licensed under the MIT License.

This README.md provides a comprehensive guide to setting up and understanding your code, tailored to the provided implementation. Save it as README.md in your project directory.
