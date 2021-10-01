import argparse
from datetime import datetime
from pathlib import PurePath
from selenium.webdriver import Chrome, ChromeOptions
from urllib.parse import urlparse, ParseResult

parser = argparse.ArgumentParser(description='Take screenshot of given URL')
parser.add_argument('-u', '--url', type=urlparse, help='URL to take screenshot of')
parser.add_argument('-t', '--target', type=PurePath, help='location where to save a screenshot')
parser.add_argument('-b', '--bin', type=PurePath, help='path to browser binary')
parser.add_argument('-d', '--driver', type=PurePath, help='path to browser driver')
parser.add_argument('-r', '--resolution', type=str, help='output screenshot resolution as comma separated str, e.g. 1920,1080')

args = parser.parse_args()

CHROMEBIN_PATH: PurePath = args.bin
CHROMEDRIVER_PATH: PurePath = args.driver
TARGET: PurePath = args.target
URL: ParseResult= args.url 
WINDOW_SIZE: str = args.resolution



def get_chrome_options(binary_location: PurePath, window_size: str) -> ChromeOptions:
    options: ChromeOptions = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(f"--window-size={window_size}")
    options.binary_location = str(CHROME_PATH)
    return options

def get_chrome_driver(driver_path: PurePath, options: ChromeOptions) -> Chrome:
    return Chrome(
        executable_path=str(driver_path), 
        chrome_options=get_options(options))

def make_screenshot(url, driver, target) -> None:
    driver.get(url)
    driver.save_screenshot(target / datetime.fromtimestamp(datetime.now()))

if __name__ == "__main__":
    make_screenshot(URL, 
                    get_chrome_driver(CHROMEDRIVER_PATH, get_chrome_options(CHROMEBIN_PATH, WINDOW_SIZE)),
                    TARGET)
