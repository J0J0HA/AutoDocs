[![pages-build-deployment](https://github.com/J0J0HA/test/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/J0J0HA/test/actions/workflows/pages/pages-build-deployment)
# AutoDocs
AutoDocs konvertiert ausgwählte .md-Dateien zu .html-Dateien und überträgt sie zusammen mit anderen ausgewählten Dateien in den /docs ordner von GitHub Pages.

## Beispiel
Dieses Repository enthält selbst den workflow. [Hier kannst du die GitHub Page sehen.](https://j0j0ha.github.io/AutoDocs/README.de) [Es gibt auch die Englische Datei online!](https://j0j0ha.github.io/AutoDocs/README.en)

## Setup
* Kopiere die Ordner /autodocs und /sources und die Datei /.github/workflows/AutoDocs.yml in dein eigenes Repository.
* Gehe in den Einstellungen deines Repositorys auf "Pages", und wähle unter "Source" "main" und "/docs" aus. Klicke anschließend auf "Save"
* Gehe nun in den Order /autodocs und bearbeite config.yml (siehe "Konfiguration" unten)

## Konfiguration
config.yml:
```
index: README.md                               # The md file to be shown at /  (optional)
style:                                         # Container for styling         (optional)
  favicon: sources/favicon-96x96.png           # Link to the favicon           (optional)
  load:                                        # list of css files to load     (optional)
    - sources/style.css                        
  themes:                                      # list of themes (name: link)   (optional)
    dark: sources/themes/dark.css
    light: sources/themes/light.css
  default theme: dark                          # default theme                 (optional)
folders:                                       # folders to create in docs     (required)
  - sources                                    # IMPORTANT: Lower level folders first
  - sources/themes
files:                                         # files to be included in /docs (required)
  - README.md                                  # You can use "*" for all files in the folder
  - README.de.md                               # or "**" for all sub folders and the files
  - README.en.md                               # tey conatin (recursive)
  - sources/**
```
