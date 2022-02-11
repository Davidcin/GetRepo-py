from colorama import Fore, init
from getrepo import get_data
import logging
import json

init(autoreset=True)
logging.basicConfig(filename='log/getrepo.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

print(Fore.LIGHTWHITE_EX + "Github API /", Fore.LIGHTBLACK_EX + "Search Repository by it's name!\n")

q = input("Search repo: ")
while q == "":
    print(Fore.RED + "Repository name is required argument!")
    q = input("Search repo: ")
logging.info("New Search: {}".format(q))
language = input("Programming language: ")
sort = input("Sort by stars, forks, help-wanted-issues, updated: ")
order = input("Which order (asc or desc): ")
per_page = int(input("How many results: ") or 5)
ignore = input("Ignore: ")

json_data = get_data(q, language, sort, order, per_page)

if ignore != "":
    json_data["items"] = [item for item in json_data["items"] if ignore not in item.get("name")]
    json_data['total_count'] = len(json_data["items"])

if bool(json_data["items"]):
    for repo in json_data["items"]:
        print(Fore.RED + "#########################################")
        print(Fore.GREEN + "Owner:", repo["owner"]["login"], Fore.GREEN + "\nRepo name:", repo["name"], Fore.GREEN + "\nRepo URL:", repo["svn_url"], Fore.GREEN + "\nRepo API URL", repo["url"])
        logging.info("Found Repo: {}".format(repo["url"]))
    print(Fore.RED + "#########################################")
    ans = input("Do you want to save json file? (Y/N): ")
    if ans.upper() == "Y":
        with open('SavedJSON/saved.json', 'w') as f:
            json.dump(json_data, f, indent=2)
            print(Fore.GREEN + "New JSON data is saved in SavedJSON folder!")
            logging.info("New JSON data is saved in SavedJSON folder!")
else:
    print(Fore.RED + "Your search did not match any repos!")
    logging.error("Couldn't find any results!")
