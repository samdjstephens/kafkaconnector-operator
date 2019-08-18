import kopf


@kopf.on.create("sdjs.dev", "v1", "kafkaconnectors")
def create_fn(body, **kwargs):
    print(f"A handler is called with body: {body}")
