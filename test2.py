import coreapi

# Initialize a client & load the schema document
client = coreapi.Client()
schema = client.get("https://etro.gg/api/docs/")

# Interact with the API endpoint
action = ["auth", "discord > login > create"]
params = {
    "access_token": ...,
    "code": ...,
    "id_token": ...,
}
result = client.action(schema, action, params=params)