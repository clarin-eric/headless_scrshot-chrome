import argparse
from datetime import datetime
from pathlib import PurePath
from selenium import webdriver
from time import sleep
from urllib.parse import urlparse, ParseResult

parser = argparse.ArgumentParser(description='Take screenshot of given URL')
parser.add_argument('-u', '--url', type=urlparse, help='URL to take screenshot of', required=True)
parser.add_argument('-t', '--target', type=PurePath, help='directory where to save a screenshot', required=True)

args = parser.parse_args()

TARGET: PurePath = args.target
URL: ParseResult= args.url 

def make_screenshot(url: ParseResult, target: PurePath):
    if os.path.basename(target) == '':
        target = target / (datetime.fromtimestamp(datetime.now()) + '.png')

    driver = webdriver.Chrome()
    driver.get(URL.geturl())
    sleep(1)
    
    driver.get_screenshot_as_file(target)
    driver.quit()

if __name__ == "__main__":
    make_screenshot(URL, 
                    TARGET)

