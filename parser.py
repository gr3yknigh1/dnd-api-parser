from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypeVar
    from typing import Any
    K = TypeVar("K")
    V = TypeVar("V")
import requests
import pprint
import json
import shutil
import os.path


data_path = "api-data.json"

if not os.path.exists(data_path):
    with


data = {}
api_url = "https://www.dnd5eapi.co"


def get_dict_value_from_path(dct: dict[K, V], path: str, path_sep="/") -> V | None:
    path_items: list[str] = path.split(path_sep)
    current_dict: dict = dct
    current_item: Any
    for index, path_item in enumerate(path_items):
        current_item = current_dict[path_item]
        if type(current_item) == dict:
            current_dict = current_item
        else:
            if index + 1 != len(path_items):
                print(path_item)
                err_path = path_sep.join(path_items[index:])
                raise Exception(f"Can't follow path: '{err_path}'")
    return current_item


def get_resource(index: str) -> dict:
    if index[0] != "/":
        index = "/" + index
    return requests.get(f"{api_url}{index}").json()

data = get_resource("/api")

for key, value in data.copy().items():
    data[key] = get_resource(value) 


