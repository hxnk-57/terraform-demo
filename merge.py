import os
import json
import sys

def merge_json_files(directory : str, output_file: str, key: str):

    output_file_path = os.path.join(directory, output_file)

    with open(output_file_path, 'r') as f:
        data = json.load(f)
    
    for filename in os.listdir(directory):
        if filename.endswith('.json') and filename != output_file:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                item = json.load(f)
                data[key].append(item)
            
            os.remove(file_path)
            print(f"deleted file {file_path}")

    
    with open(output_file_path, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    directory = sys.argv[1]
    
    match directory:
        case "topic":
            merge_json_files("topic", "topics.json", "topics")
        case "service_account":
            merge_json_files("service_account", "service_accounts.json", "service_accounts")
        case _:
            print("")