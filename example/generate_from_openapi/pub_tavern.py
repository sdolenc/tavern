import sys
from coreapi import Client
import yaml


def generate_tavern_yaml(json_path):
    client = Client()
    d = client.get(json_path, format="openapi")

    output_yaml(d.links)
    for routes in d.data.keys():
        output_yaml(d.data[routes], routes)


def output_yaml(links, prefix=""):
    test_dict = {}
    for test_name in links.keys():
        test_dict["test_name"] = f"{prefix}/{test_name}" if prefix else test_name

        request = {
            "url": links[test_name].url,
            "method": str.upper(links[test_name].action),
        }

        if links[test_name].encoding:
            request["headers"] = {"content-type": links[test_name].encoding}

        json = get_request_placeholders(links[test_name].fields)
        if json:
            request["json"] = json

        response = {"strict": False, "status_code": 200}
        inner_dict = {"name": test_name, "request": request, "response": response}

        test_dict["stages"] = [inner_dict]
        print(test_dict)
        print(yaml.dump(test_dict, explicit_start=True, default_flow_style=False))


def get_request_placeholders(fields):
    field_dict = {}
    for field in fields:
        field_dict[field.name] = "required" if field.required else "optional"
    return field_dict


def display_help():
    print("pub_tavern.py <url to openapi.json>")
    print(
        "eg: pub_tavern.py https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v2.0/json/petstore-simple.json"
    )
    exit(-1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        display_help()
    generate_tavern_yaml(sys.argv[1])
