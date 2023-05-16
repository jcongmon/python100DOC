import data_parser
import json
import datetime as dt


def json_dump(data: dict):
    with open("data.json", mode="w") as fp:
        json.dump(data, fp, indent=4)


def remove_past_due(d: dict) -> dict:
    del_entry_list = []
    for idx, entry in d.items():
        if dt.datetime.strptime(entry["end_date"], '%Y-%m-%d').date() < dt.datetime.now().date():
            del_entry_list.append(idx)

    if len(del_entry_list) > 0:
        for idx in del_entry_list:
            del d[idx]

    json_dump(d)

    return d


def check_for_duplicates(curr_dict: dict, data: dict) -> list:
    del_list = []
    for cd_key, cd_value in curr_dict.items():
        cur_item = []
        for x, y in cd_value.items():
            cur_item.append(y)
        for key, value in data.items():
            compare_items = []
            for i, j in value.items():
                compare_items.append(j)
            count = 0
            for item_one, item_two in zip(cur_item, compare_items):
                if item_one == item_two:
                    count += 1
            if count > 3:
                del_list.append(cd_key)
    return del_list


def update_json(dup: list, cd: dict, data: dict) -> dict:
    for i in dup:
        del cd[i]
    if len(cd) > 0:
        data.update(cd)
        json_dump(data)
    return cd


def set_update_twitter(deals: dict):
    return False if len(deals) == 0 else True


def get_json():
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}
        json_dump(data)
    return data


def get_new_deals(data) -> dict:
    dp = data_parser.DataParser()
    data = remove_past_due(data)
    duplicates = check_for_duplicates(dp.current_deals, data)
    new_data = update_json(duplicates, dp.current_deals, data)
    data_parser.set_curr_idx(dp.curr_idx)
    return new_data


class JSONHandler:
    def __init__(self):
        self.past_deals = get_json()
        self.new_deals = get_new_deals(self.past_deals)
        self.update_twitter = set_update_twitter(self.new_deals)
