import gh_md_to_html.core_converter
import requests
import yaml
import os
import glob

def emptydir(dir):
    "Deletes the contents of a directory."
    for file in glob.glob(dir + "/*"):
        try:
            os.remove(file)
        except IsADirectoryError:
            emptydir(file)
            os.rmdir(file)

# Ensure empty docs folder
try:
    os.mkdir("../docs")
except FileExistsError:
    emptydir("../docs")

# load config
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

# load template
with open("template.html", "r") as file:
    template = file.read()

# create required folders
for folder in config["folders"]:
    os.mkdir("../docs/" + folder)

# transfer files
for path in config["files"]:
    for filen in glob.glob("../" + path):
        if filen.endswith(".md"):
            # .md files get converted to html and saved in docs
            with open(filen, "r") as file:
                raw = file.read()
            html = gh_md_to_html.core_converter.markdown(raw)
            with open("../docs/" + filen.removeprefix("../").removesuffix(".md") + ".html", "w") as file:
                file.write(
                    template
                        .replace("%title%", filen)
                        .replace("%content%", html)
                )
        else:
            # other files are stored directly in the docs folder
            with open(filen, "rb") as file:
                raw = file.read()
            with open("../docs/" + filen.removeprefix("../"), "wb") as file:
                file.write(raw)

# creating an optional index page
if "index" in config:
    with open("../" + config["index"], "r") as file:
        raw = file.read()
    html = gh_md_to_html.core_converter.markdown(raw)
    with open("../docs/index.html", "w") as file:
        file.write(
            template
                .replace("%title%", config["index"])
                .replace("%content%", html)
        )
