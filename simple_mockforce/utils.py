import re


def parse_detail_url(path: str):
    path_end = re.sub(r"^.*?sobjects/", "", path)
    split_up = path_end.split("/")

    if len(split_up) == 2:
        sobject = split_up[-2]
        record_id = split_up[-1]
        return sobject, None, record_id
    elif len(split_up) == 3:
        sobject = split_up[-3]
        upsert_key = split_up[-2]
        record_id = split_up[-1]
        return sobject, upsert_key, record_id
    raise AssertionError(f"Unexpected path format: {path}")


def parse_create_url(url: str):
    split_up = url.split("/")
    # TODO: use pyparsing
    sobject = split_up[-2]

    return sobject


def find_object_and_index(objects: list, pk_name: str, pk: str):
    index = None
    original = None
    for idx, object_ in enumerate(objects):
        if object_[pk_name] == pk:
            index = idx
            original = object_

    assert index is not None and original, f"couldn't find anything for {pk}"
    return original, index