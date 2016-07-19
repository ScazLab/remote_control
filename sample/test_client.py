from remote_control import Client


with Client() as client:
    client.send_command(b'Say hello')
    print('Server said hello.')
    client.send_command(b'Say bye')
    print('Server said bye.')
