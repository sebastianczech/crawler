import requests
import sys
from urllib.parse import urlparse

def is_absolute(url):
    return bool(urlparse(url).netloc)

def get_list_of_links_for_domain(url, content):
    links = []
    check_for = ["href", "src"]
    parsed_url = urlparse(url)
    for line in content.splitlines():
        if any(x in line for x in check_for):

            # if len(line.replace(" =", "=").split("href=")) > 0:
            # if parsed_url.netloc.replace("www.", "") in line
            links.append(line)
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