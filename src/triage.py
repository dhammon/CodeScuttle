


class Triage():

    def __init__(self, Config):
        self.excludes = Config.excludes
    

    def triage(self, items):
        filtered_items = {}
        i = 0
        for item_key in items:
            item_value = items[item_key]
            exclude = self.loop_response(item_value)
            if exclude != True:
                filtered_items[i] = item_value
                i += 1
        return filtered_items


    def loop_response(self, item: str):
        exclude = False
        for exclude_item in self.excludes:
            exclude_rule = self.excludes[exclude_item]
            true_counter = 0
            element_counter = len(exclude_rule)
            for exclude_rule_key, exclude_rule_value in exclude_rule.items():
                if exclude_rule_value in str(item):
                    true_counter +=1
            if(element_counter == true_counter):
                exclude = True
        return exclude
