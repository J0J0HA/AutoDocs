import gh_md_to_html.core_converter
import requests
import yaml
import os
import glob

try:
    os.mkdir("../docs")
except FileExistsError:
    for file in glob.glob("../docs"):
        os.remove(file)

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

with open("template.html", "r") as file:
    template = file.read()

for file in config["files"]:
    if file.endswith(".md"):
        raw = requests.get("https://raw.githubusercontent.com/" + config["name"] + "/main/" + file).text
        html = gh_md_to_html.core_converter.markdown(raw)
        with open("../docs/" + file + ".html", "w") as file:
            file.write(
                template
                    .replace("%title%", str(config["name"]) + "/" + str(file))
                    .replace("%content%", html)
            )
    else:
        raw = requests.get("https://raw.githubusercontent.com/" + config["name"] + "/main/" + file).text
        with open("../docs/" + file, "w") as file:
            file.write(raw)
