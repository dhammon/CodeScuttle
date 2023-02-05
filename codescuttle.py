#!/usr/bin/env python3

import requests as Requests
import time as Time
import json as Json
from config.config import Config
from src.query import Query
from src.triage import Triage
from src.view import View


banner = """
                                                          0
\033[1mCode Scuttle\033[0m                                 ____         
\033[3mFind leaked source code\033[0m                     /    |        o    0
                                           /     |           o 
                                          |    o |__       0
                                          |    o |  |___   o
\033[0;34m/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~\033[0m|    o |   ___|o \033[0;34m~/\~/\~/\~/\~\033[0m
\033[0;34m/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~\033[0m|    o |  |   \033[0;34m~/\~/\~/\~/\~/\~\033[0m
\033[0;34m/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~\033[0m
\033[0;34m/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~/\~\033[0m

"""
print(banner)


if __name__ == "__main__":
    try:
        query = Query(Config(), Requests, Time, Json)
        response = query.query()
        new_triage = Triage(Config())
        filtered_result = new_triage.triage(response)
        view = View(Json)
        view.view(filtered_result)
    except Exception as e:
        print("Exception: {}".format(e))