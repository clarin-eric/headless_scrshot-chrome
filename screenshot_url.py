import argparse
from datetime import datetime
import os
from pathlib import Path
from selenium import webdriver
from time import sleep, strftime
from urllib.parse import urlparse, ParseResult

parser = argparse.ArgumentParser(description='Take screenshot of given URL')
parser.add_argument('-u', '--url', type=urlparse, help='URL to take screenshot of', required=True)
parser.add_argument('-t', '--target', type=Path, help='directory where to save a screenshot', default='./output')

args = parser.parse_args()

TARGET: Path = args.target
URL: ParseResult= args.url 

def make_screenshot(url: ParseResult, target: Path):
    target = target.resolve()
        
    target = target / (strftime("%Y%m%d%H%M%S") + '.png')
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920x1080")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(URL.geturl())
    sleep(1)

    driver.get_screenshot_as_file(str(target))
    driver.quit()

if __name__ == "__main__":
    make_screenshot(URL, 
                    TARGET)

