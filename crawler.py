import requests
import sys
from urllib.parse import urlparse
import re

def is_absolute(url):
    return bool(urlparse(url).netloc)

def get_list_of_links_for_domain(url, content):
    links = []
    check_for = ["href", "src"]
    parsed_url = urlparse(url)
    for line in content.splitlines():
        if any(x in line for x in check_for):
            for part in re.split("href|src", line):
                if part.startswith("=\"") and len(part.replace("=", "").split("\"")) > 0:
                    link = part.replace("=", "").split("\"")[1]
                    if is_absolute(link) and len(parsed_url.netloc) > 0 and parsed_url.netloc.replace("www.", "") in link \
                            or not is_absolute(link):
                        links.append(link)
    print("no links: " + str(len(links)))
    return links

def parse_html_page(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return get_list_of_links_for_domain(url, r.text)
        else:
            return "Could not parse " + url + ", because of receiving HTTP status code " + str(r.status_code)
    except requests.exceptions.ConnectionError:
        return "Failed to establish a new connection with url " + url
    except requests.exceptions.MissingSchema:
        return "Invalid url " + url

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please run program with 1 argument using following command: \npython crawler.py URL")
    else:
        print(parse_html_page(sys.argv[1]))