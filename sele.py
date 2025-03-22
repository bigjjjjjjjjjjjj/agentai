import torch
from transformers import pipeline
from huggingface_hub import login
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.parse import quote_plus

# 建立 Hugging Face 的 text-generation pipeline
pipe = pipeline(
    "text-generation",
    model="google/gemma-2b-it",
    device="cuda"
)

# 設定 Chrome 瀏覽器選項，並加入防止反爬蟲驗證的參數
def driver_config():
    options = Options()
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    
    driver = webdriver.Chrome(options=options)
    return driver

# 根據主題爬取 YouTube 上的程式設計課程
def get_courses(subject):
    # 使用 urllib.parse.quote_plus 將 subject 進行 URL 編碼
    search_query = quote_plus(f"{subject} programming courses")
    driver = driver_config()
    
    # 根據主題生成 YouTube 搜索 URL
    url = f'https://www.youtube.com/results?search_query={search_query}'
    driver.get(url)
    time.sleep(5)  # 等待頁面載入
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    videos = soup.find_all('a', {'id': 'video-title'})
    courses = []
    for video in videos:
        title = video.get('title')
        url = 'https://www.youtube.com' + video.get('href')
        courses.append((title, url))
        
    driver.quit()
    return courses

# 使用 Hugging Face 語言模型生成學習計劃的函數
def generate_study_plan(subject, courses):
    # 根據課程列表生成更具體的提示
    course_titles = "\n".join([f"Title: {title} - URL: {url}" for title, url in courses])
    
    prompt = f"""
    I am learning {subject}. Here are some courses I found that might be useful:
    
    {course_titles}
    
    Please generate a detailed 5-week study plan for learning {subject}. Include the following:
    - Suggested resources from the above courses
    - A timeline for each week
    - Specific tasks to accomplish each week
    - Learning objectives for each week
    
    The study plan should be easy to follow and ensure consistent progress.
    """
    
    # 呼叫 Hugging Face 模型生成學習計劃
    outputs = pipe(prompt, max_new_tokens=256*3)
    generated_text = outputs[0]['generated_text']
    return generated_text.strip()

# 結合爬蟲與語言模型生成計劃的整合函數
def create_study_plan_with_courses(subject):
    # 爬取可用的課程
    courses = get_courses(subject)
    # 使用語言模型生成學習計劃
    study_plan = generate_study_plan(subject, courses)
    
    # 顯示課程清單
    print("Available Courses:")
    for title, url in courses:
        print(f"Title: {title} - URL: {url}")
        
    print("\nSuggested Study Plan:")
    print(study_plan)

# 執行示範：生成針對 Python 程式設計的學習計劃
create_study_plan_with_courses("Python")  # 你可以更改這裡的主題
