from bcloud import util

light = '-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwfczbrS0ZW5r+yParkgkxOrPGcpQnZ2Th4HzDXwoH/9O/fw7Hsr459QlEuhK6iro2e1a7OD+Si1Lq+gYr7DZ2g3WR6XKUBnwNgXn6aflOLpqawgrVH/j8JENvsgnwzVGbCY8vLaEgC9fRJyK5AcH9X5OOfPnnHmxbfoS6uBpcCwIDAQAB-----END PUBLIC KEY-----'
light2 = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCwfczbrS0ZW5r+yParkgkxOrPG\ncpQnZ2Th4HzDXwoH/9O/fw7Hsr459QlEuhK6iro2e1a7OD+Si1Lq+gYr7DZ2g3WR\n6XKUBnwNgXn6aflOLpqawgrVH/j8JENvsgnwzVGbCY8vLaEgC9fRJyK5AcH9X5OO\nfPnnHmxbfoS6uBpcCwIDAQAB\n-----END PUBLIC KEY-----'
dark = util.RSA_encrypt(light2, '410015216')

print(dark)
