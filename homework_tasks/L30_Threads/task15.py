'''
Prosty web crawler
Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki do
odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę
odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i
zbioru (set) do przechowywania już odwiedzonych linków.
'''


import threading
from queue import Queue
import requests
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup

### Definitions and variables ###
MAX_PAGES = 50
NUM_THREADS = 5 # (MAX_PAGES//10)+1  # limit to 10 threads

visited = set()
visited_lock = threading.Lock()

queue = Queue()

rb = RobotFileParser()


def is_same_domain(base_url, new_url):
    return urlparse(base_url).netloc == urlparse(new_url).netloc


def worker(base_url):
    while True:
        # Get the next URL from the queue
        url = queue.get()

        if url is None:
            queue.task_done()
            break

        try:
            response = requests.get(url, timeout=(5, 5))  # 5 to connect, 5 to read
            html = response.text
        except Exception:
            queue.task_done()
            continue  # Skip to the next URL in the queue
        
        # Parse the HTML
        soup = BeautifulSoup(html, "html.parser")

        for link in soup.find_all("a", href=True):
            # Get the full URL of the link, making it internal by checking if it starts with the base URL
            full_url = urljoin(url, link["href"])

            # Check if the link is internal
            if not is_same_domain(base_url, full_url):
                continue  # Skip to the next URL in the page

            # Check if the link is allowed by robots.txt
            if not rb.can_fetch("*", full_url):
                continue

            with visited_lock:
                if len(visited) >= MAX_PAGES:
                    break 

                if full_url not in visited:
                    visited.add(full_url)
                    queue.put(full_url)

        # Print the current URL
        print(f"Visited: {url}")

        queue.task_done()


if __name__ == "__main__":
    start_url = "https://www.mosir.zgora.pl/" # Hard URL for testing
    #start_url = input("Podaj URL startowy: ")

    start_url = start_url if start_url[-1] == '/' else start_url + '/'

    # Read robots.txt
    rb.set_url(start_url + 'robots.txt')
    rb.read()

    visited.add(start_url)
    queue.put(start_url)

    threads = []

    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(start_url,))
        t.start()
        threads.append(t)

    queue.join()

    
    for _ in threads:
        queue.put(None)

    for t in threads:
        t.join()

    print(f"Visited: {len(visited)} pages\n Thanks for your hospitality, host!")
