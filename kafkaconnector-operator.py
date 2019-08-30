import kopf
import requests


@kopf.on.create("sdjs.dev", "v1", "kafkaconnectors")
def create_fn(body, spec, **kwargs):
    print(f"A handler is called with body: {body}")
    connector_name = body['metadata']['name']
    resp = requests.put(f"http://localhost:8083/connectors/{connector_name}/config",
                        data=convert_config_params(spec['config']),
                        headers={"Content-Type": "application/json"})
    print(f"{resp.status_code}: {resp.content}")


def convert_config_params(config):
    return {key.replace("_", "."): val for key, val in config.items()}


@kopf.on.delete("sdjs.dev", "v1", "kafkaconnectors")
def delete_fn(body, **kwargs):
    connector_name = body['metadata']['name']
    resp = requests.delete(f"http://localhost:8083/connectors/{connector_name}")
    print(f"{resp.status_code}: {resp.content}")