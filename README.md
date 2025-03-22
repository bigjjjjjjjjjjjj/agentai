Sure! Here's the content formatted in markdown for use on GitHub:

markdown


# Reflexive Web Agent for Automated Study Plan Generation

## Overview
This project implements a Reflexive Web Agent that automates the creation of a 5-week study plan for programming courses. The agent uses Selenium to scrape YouTube for relevant programming course videos based on a user-defined subject and integrates a large language model (LLM) from Hugging Face to generate a detailed, personalized study plan. This tool aims to assist learners by providing a structured learning path with weekly tasks, objectives, and resources.

## Features
- **Web Scraping:** Uses Selenium to fetch programming course videos from YouTube.
- **Natural Language Processing:** Employs the Hugging Face text-generation pipeline with the `google/gemma-2b-it` model to create study plans.
- **Automation:** Handles browser interactions with anti-bot detection measures.

## Setup Instructions

### Prerequisites
- **Python:** Version 3.8 or higher
- **Google Chrome:** Installed on your system
- **ChromeDriver:** Must match your Chrome version
- **CUDA-enabled GPU (optional):** For accelerated LLM inference

### Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
Install Python Dependencies:




pip install selenium transformers torch huggingface_hub beautifulsoup4
Install ChromeDriver:

Download ChromeDriver from the official site.
Ensure it matches your Google Chrome version.
Add chromedriver to your system PATH or specify its location in the webdriver.Chrome() call.
Hugging Face Authentication:

Get an API token from Hugging Face.
Replace "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" in the code with your token.
Usage
Run the Script:




python study_plan_generator.py
By default, it generates a plan for "Python". Modify the subject in create_study_plan_with_courses() to customize it.

Customize the Subject: Change the subject in the script, e.g., for "JavaScript":




create_study_plan_with_courses("JavaScript")
Output:
The script produces:

A list of YouTube course titles and URLs.
A 5-week study plan with tasks, objectives, and resources.
Implementation Details
1. Web Scraping with Selenium
Function: get_courses(subject)
Purpose: Retrieves programming courses from YouTube based on the subject.

Details:

Navigates to https://www.youtube.com/results?search_query={subject}+programming+courses using a headless Chrome browser.
Waits 5 seconds (time.sleep(5)) for content to load.
Parses HTML with BeautifulSoup to extract video titles and URLs from <a id="video-title"> tags.
Returns a list of (title, url) tuples.
2. Study Plan Generation with Hugging Face LLM
Function: generate_study_plan(subject, courses)
Purpose: Generates a 5-week study plan using scraped courses and the LLM.

Details:

Builds a prompt with the subject and course list.
Uses the google/gemma-2b-it model via the text-generation pipeline, leveraging CUDA if available.
Limits output to 768 tokens (max_new_tokens=256*3) for concise yet detailed plans.
3. Integration
Function: create_study_plan_with_courses(subject)
Purpose: Combines scraping and plan generation into one workflow.

Details:

Calls get_courses(subject) to fetch courses.
Passes results to generate_study_plan(subject, courses) for plan creation.
Displays courses and the study plan.
4. ChromeDriver Configuration
Function: driver_config()
Purpose: Configures Selenium’s ChromeDriver for optimal performance and stealth.

Details:

Options:
disable-blink-features=AutomationControlled: Avoids bot detection.
--headless: Runs browser in the background.
--disable-gpu, --disable-extensions, --disable-infobars: Enhances efficiency.
Code Structure
python


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
Week 1:

Introduction to Python

Setting up the Python environment

Basic syntax and data types

Variables and operators

Input and output

Resources:

Title: Python Full Course for Beginners

Title: Learn Python - Full Course for Beginners [Tutorial]

Timeline:

Week 1: 5 hours

Task 1: Create a Python environment and practice basic commands.

Task 2: Learn about variables and data types.

Task 3: Practice using variables and operators.

Learning Objectives:

Understand the basics of Python programming.

Use variables and operators to store and manipulate data.

Week 2:

Control flow statements

If statements

While loops

Practice using control flow statements.

Resources:

Title: Python Full Course for Beginners

Title: Learn Python With 5 Projects - From Beginner to Advanced

Timeline:

