import kopf
import requests


@kopf.on.create("sdjs.dev", "v1", "kafkaconnectors")
def create_fn(body, spec, **kwargs):
    print(f"Create handler called with body: {body}")
    create_or_update(body, spec)


@kopf.on.update("sdjs.dev", "v1", "kafkaconnectors")
def update_fn(body, spec, **kwargs):
    print(f"Update handler called with body: {body}")
    create_or_update(body, spec)


def create_or_update(body, spec):
    connector_name = body['metadata']['name']
    resp = requests.put(f"http://localhost:8083/connectors/{connector_name}/config",
                        json=convert_config_params(spec['config']))
    print(f"{resp.status_code}: {resp.content}")


def convert_config_params(config):
    return {key.replace("_", "."): val for key, val in config.items()}


@kopf.on.delete("sdjs.dev", "v1", "kafkaconnectors")
def delete_fn(body, **kwargs):
    print(f"Delete handler called with body: {body}")
    connector_name = body['metadata']['name']
    resp = requests.delete(f"http://localhost:8083/connectors/{connector_name}")
    print(f"{resp.status_code}: {resp.content}")
