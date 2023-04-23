# https://www.base64encode.org/ to encode
# https://www.base64decode.org/ to decode.

x = input('encoded code: ')

print(f'Your env: {x}Your public code: import base64; x = "{x}"; exec(base64.b64decode(f"{x}"))') # put base64 then decodes

print('have fun')
