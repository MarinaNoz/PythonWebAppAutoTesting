from zeep import Client, Settings
import yaml

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)

WSDL = data["wsdl"]
print(WSDL)
settings = Settings(strict=False)
client = Client(wsdl=WSDL, settings=settings)


def check_text(word: str):
    return client.service.checkText(word)[0]["s"]


print(check_text('Сабака'))
print(check_text('Карова'))
