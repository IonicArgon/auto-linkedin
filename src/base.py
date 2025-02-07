import json
import time
import random
import requests


class MessageError(Exception):
    pass


class Base:
    def __init__(self, credentials_file: str = None, headers_file: str = None, cookies_file: str = None):
        self.headers = {}
        self.cookies = {}
        if headers_file:
            self.load_headers(headers_file)
        if cookies_file:
            self.load_cookies(cookies_file)
        if credentials_file:
            self.load_credentials(credentials_file)
        
        self.filtered_leads = []
        self.user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        ]
        self.valid_connections = []

    def load_headers(self, headers_file):
        with open(headers_file, "r", encoding="utf-8") as f:
            headers = json.load(f)
        self.headers = headers

    def load_cookies(self, cookies_file):
        with open(cookies_file, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        self.cookies = cookies
    
    def load_credentials(self, credentials_file):
        with open(credentials_file, "r", encoding="utf-8") as f:
            credentials = json.load(f)
        self.cookies = credentials.get("cookies", {})
        self.headers = credentials.get("headers", {})

    def create_message(self, message: str, name: str = None, person: str = None):
        if not message:
            return message
        name = name.split(" ")[0]
        if person is None and "{person}" in message:
            raise MessageError("Message contains {person} but no person was provided")
        if name is None and "{name}" in message:
            raise MessageError("Message contains {name} but no name was provided")

        if "{person}" not in message and "{name}" not in message:
            return message

        if "{person}" in message and "{name}" in message:
            message = message.replace("{person}", person)
            message = message.replace("{name}", name)
            return message

        if "{person}" in message:
            message = message.replace("{person}", person)
            return message

        if "{name}" in message:
            message = message.replace("{name}", name)
            return message

    def get_leads(
        self,
        url: str,
        start: int = 0,
        count: int = 25,
        end: int = 1000,
        output_file: str = "leads.json",
        time_delay_min: int = 2,
        time_delay_max: int = 5,
    ):

        pages = int(end / count)
        leads_local = []
        try:
            print("Getting leads...")
            for page in range(pages):
                self.headers["user-agent"] = random.choice(self.user_agents)
                ## replace the start and count params
                url = url.replace("start=0", f"start={start}")
                url = url.replace("count=25", f"count={count}")

                response = requests.get(url, cookies=self.cookies, headers=self.headers, timeout=10)
                if response.status_code != 200:
                    ### printing more debug information this isn't enough
                    response_headers = dict(response.headers)
                    response_cookies = dict(response.cookies)

                    print(f"Error getting leads: {response.status_code} - {response.text}\n")
                    print(f"Content headers: {json.dumps(response_headers, indent=2)}\n")
                    print(f"Content cookies: {json.dumps(response_cookies, indent=2)}\n")
                    
                    print("Request information: \n")
                    print(f"URL: {url}\n")
                    print(f"Headers: {json.dumps(self.headers, indent=2)}\n")
                    print(f"Cookies: {json.dumps(self.cookies, indent=2)}\n")
                    print(f"Occured on page: {page}")
                    
                    break
                content = response.json()

                if "elements" in content:
                    response_headers = dict(response.headers)
                    response_cookies = dict(response.cookies)
                    leads_local.extend(content["elements"])
                    print(f"Current status: {response.status_code} - {response.text}\n")
                    print(f"Content headers: {json.dumps(response_headers, indent=2)}\n")
                    print(f"Content cookies: {json.dumps(response_cookies, indent=2)}\n")
                    print(f'page: {page} - {len(content["elements"])} leads')
                else:
                    print(f"page: {page} - no leads")
                    break
                start += count
                time.sleep(random.randint(time_delay_min, time_delay_max))
            
            print(f"Total leads: {len(leads_local)}")
            print("Request information: \n")
            print(f"URL: {url}\n")
            print(f"Headers: {json.dumps(self.headers, indent=2)}\n")
            print(f"Cookies: {json.dumps(self.cookies, indent=2)}\n")

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(leads_local, f, indent=2)

        except KeyboardInterrupt:
            print("Saving leads...")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(leads_local, f, indent=2)

    def connect(self, profile_urn, message: str = ""):
        raise NotImplementedError("connect method must be implemented")
