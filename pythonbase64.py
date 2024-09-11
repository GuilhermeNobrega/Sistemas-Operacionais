import base64

name = "picanha"
name_encoded = base64.b64encode(name.encode('utf-8'))
print(f"Nome codificado: {name_encoded}")

namedecoded = base64.b64decode(name_encoded).decode('utf-8')
print(f"Nome decodificado: {namedecoded}")
