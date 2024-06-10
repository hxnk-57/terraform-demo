import os
import json

def merge_json_files():

    SERVICE_ACCOUNT_PATH = "service_account/service_accounts.json"
    TOPIC_PATH = "topic/topics.json"

    with open(SERVICE_ACCOUNT_PATH, 'r') as f:
        service_accounts = json.load(f)
    
    for filename in os.listdir("service_account"):
        if filename.endswith('.json') and filename != "service_accounts.json" :
            file_path = os.path.join("service_account", filename)
            with open(file_path, 'r') as f:
                item = json.load(f)
                service_accounts["service_accounts"].append(item)
            os.remove(file_path)
    
    with open(SERVICE_ACCOUNT_PATH, 'w') as f:
        json.dump(service_accounts, f, indent=2)    
    
    with open(TOPIC_PATH, 'r') as f:
        topics = json.load(f)
    
    for filename in os.listdir("topic"):
        if filename.endswith('.json') and filename != "topics.json" :
            file_path = os.path.join("topic", filename)
            with open(file_path, 'r') as f:
                item = json.load(f)
                topics["topics"].append(item)
            os.remove(file_path)
    
    with open(TOPIC_PATH, 'w') as f:
        json.dump(topics, f, indent=2)


if __name__ == "__main__":
    merge_json_files()