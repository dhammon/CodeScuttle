


class View():

    def __init__(self, Json):
        self.json = Json


    def view(self, filtered_result):
        if not filtered_result:
            print("[+] No code leaks found")
        else:
            for response in filtered_result.values():
                data = self.json.loads(response)
                item = data['items'][0]
                repository_full_name = item['repository']['full_name']
                html_url = item['html_url']
                print(f"[-] Match found: Name={repository_full_name} Url={html_url}")
