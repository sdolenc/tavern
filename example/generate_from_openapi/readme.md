example script to autogenerate the travern yaml test file from a given openapi.json file

To run: 
```
pip install pipenv
pipenv install
pipenv run pub_tavern.py 
````

# 1. publish as nuget package to azure devops

# 1.1 get conversion script
```
git clone https://github.com/sdolenc/tavern.git
pushd example\generate_*\
pip install pipenv
pipenv install
```

# 1.2 conver to standalone cli binary
```
pipenv install pyinstaller
pipenv run pyinstaller pub_tavern.py
pipenv run pyinstaller --noconfirm --onefile --nowindow pub_tavern.py
```

# 1.3 create nuget package
install: Nuget Package Explorer

# 1.4 upload nuget pakcage
browser: azure devops > artifacts > "connect to feed"
