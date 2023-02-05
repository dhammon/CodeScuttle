


class Query():

    def __init__(self, Config: object, Requests: object, Time: object, Json: object):
        self.queries = Config.queries
        self.token = Config.token
        self.requests = Requests
        self.time = Time
        self.json = Json


    def query(self):
        queries = self.queries
        queried_items = {}
        i = 0
        for query_key in queries:
            rule = queries[query_key]['query']
            url = "https://api.github.com/search/code?q=" + str(rule)
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer " + self.token,
                "X-GitHub-Api-Version": "2022-11-28",
            }
            response = self.requests.get(url, headers=headers)
            if response.status_code == 403:
                response = self.handle_rate_limit(response, url, headers)
            data = self.json.loads(response.text)
            total_count = data['total_count']
            if total_count != 0:
                queried_items[i] = response.text
                i += 1
        return queried_items


    def handle_rate_limit(self, response, url, headers):
        message = self.json.loads(response.content)
        timeout = int(response.headers['X-RateLimit-Reset'])
        now = self.time.time()
        delay = timeout - now + 10
        if "You have exceeded a secondary rate limit" in message['message']:
            print("[!] INFO: GitHub API Secondary Rate Limit by exceeded. Pausing for {} seconds then retrying...".format(str(delay)))
            self.time.sleep(delay)
            response = self.requests.get(url, headers=headers)
        else:
            print("[!] INFO: Limit exceeded. {}".format(message['message']))
            self.time.sleep(delay)
            response = self.requests.get(url, headers=headers)
        return response
        
