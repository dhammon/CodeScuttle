# CodeScuttle
*Find leaked source code*
```
                                                          0
                                             ____         
                                            /    |        o    0
                                           /     |           o 
                                          |    o |__       0
                                          |    o |  |___   o
/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~|    o |   ___|o ~/\~/\~/\~/\~
/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~|    o |  |   ~/\~/\~/\~/\~/\~
/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~
/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~
```
> Warning! This minimally viable product/project is in an alpha stage, use at your own discretion and check back for updates

# Purpose
Sometimes an organization's private source code is pushed onto GitHub as public repositories.  The purpose of this project is to give organizations an opensource tool to search GitHub for public repositories that match their source code's fingerprint.

# How it works
CodeScuttle searches GitHub public repositories using your configured queries and exclusions.  Utilizing GitHub's authenticated API, you can quickly and systematically identify when source code is leaked.

> Warning! Sometimes GitHub API fails to return results due to their indexing and search service.

> Warning! GitHub subjects users to API rate limits.  We've added logic to pause and retry when these limits are hit.  We are not responsible for your use of this software and any violations against GitHub's use policies.


# Installation
```
git clone https://github.com/dhammon/CodeScuttle
pip install -r requirements.txt
```

# Configuration
1. Rename `config.py.example` to `config.py`
2. Insert your GitHub API token as the `token` value in `config.py`
3. Insert your search parameters as `queries` in `config.py`.
4. Optional: Insert any exclude parameters as `excludes` in `config.py`

> Warning! GitHub doesn't search partial strings.  Example, if you are tring to find "ThisExampleString" and search "ThisExample" GitHub won't return results with "ThisExampleString".  GitHub search also doesn't allow for wildcards - so "ThisExample*" won't work either.

# Use
```
./codescuttle.py
```

# Use Cases
> Warning! CodeScuttle only returns 30 GitHub API results per query in the `queries` section of `config.py`.  This includes results that may later be excluded using `excludes` settings in the `config.py` file.

## Source Code
Include source code strings in double quotes with spaces between them and use as entries in the `config.py` file's `queries` section.  For example, your source code file has `someDescriptiveFunctionName` and `someDescriptiveVariableName`.  A query entry in `config.py` would look something like this:
```
    queries = {
        "mySearch": {
            "description": "Searching for my secret source code",
            "query": '"someDescriptiveFunctionName" "someDescriptiveVariableName"'
        },
```

## Canary Tokens
Consider generating a long random token (canary) and insert as a comment in files you wish to monitor.  Then add this token value as a entry in the `config.py` file's `queries` section.  A query entry in the `config.py` might look something like this:
```
    queries = {
        "canary": {
            "description": "Searching for my canary token",
            "query": '"9edab40c7c70577cbc307c6d5894fe77"'
        },
```


## Secrets (or maybe not)
You 'could' use secret values as search parameters, but consider the following:
1. Storing secrets in the config file isn't great
2. Search parameters in GitHub's API are via GET method and could be logged by intermediaries and/or GitHub


## Exclude Results
There could be false positives that you'll want to remove from the output of CodeScuttle.  You can ignore such results by writing and `excludes` entry in the `config.py` file.  For example, say you wanted to ignore any GitHub search results that included the string `dhammon`, an exclude entry might look something like this:
```
    excludes = {
        "allowList": {
            "username": "dhammon",
        },
```
Or perhaps you want to exclude all results that include `dhammon` and the term `CodeScuttle`, an entry might then look like the following:
```
    excludes = {
        "allowList": {
            "username": "dhammon",
            "project": "CodeScuttle"
        },
```

---
Thank you for checking out CodeScuttle and happy hunting! -Daniel