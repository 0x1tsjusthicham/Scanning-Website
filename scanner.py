import requests, re, urllib.parse
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url, block_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.avoid_block_links = []
    
    def get_links(self,url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))
    
    def crawl(self,url=None):

        if url == None:
            url = self.target_url

        href_links = self.get_links(url)
        for link in href_links:
            link = urllib.parse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]

            if url in link not in self.target_links and link not in self.avoid_block_links:
                self.target_links.append(link)
                print(link)
                self.crawl(url)
    
    def get_forms(self,url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content.decode(errors="ignore"), "html.parser")
        return parsed_html.findAll("form")
    
    def submit_forms(self, form, value, url):
        action = form.get("action")
        post_url = urllib.parse.urljoin(url,action)
        method = form.get("method")

        input_list = form.findAll("input")

        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")

            if input_type == "text":
                input_value = "this is me"
            
            post_data[input_name] = input_value

        if method == "get":
            return self.session.post(post_url, data=post_data)
        
        return self.session.get(post_url, params=post_data)
    
    def test_xss_form(self, form, url):
        javascript_script = "<sCript>alert('hacked')</sCript>"
        response = self.submit_forms(form, javascript_script, url)
        return javascript_script in response.content.decode()

    
    def test_xss_links(self, url):
        javascript_script = "<sCript>alert('hacked')</sCript>"
        url = url.replace("=", "=" + javascript_script)
        response = self.session.get(url)
        return javascript_script in response.content.decode()
    
    def run_scanner(self):
        for link in self.target_links:
            forms = self.get_forms(link)
            for form in forms:
                print("[+] Testing form in " + link)
                is_vulnerable_to_xss = self.test_xss_form(form, link)
                if is_vulnerable_to_xss:
                    print("\n\n[*******] XSS found in link " + link + "in the following form")
                    print(form)
            
            if "=" in link:
                print("[+] Testing link: " + link)
                is_vulnerable_to_xss = self.test_xss_links(link)
                if is_vulnerable_to_xss:
                    print("\n\n[*******] XSS found in link " + link)
                    print(form)
