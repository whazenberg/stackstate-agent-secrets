#!/usr/bin/python3
import sys, json;

data = json.load(sys.stdin)

version = data.get('version', 'no version found')
if version != "1.0":
    raise Exception("Secret request version is not 1.0, got: %s" % version)

secrets = data.get('secrets', [])
response = { secret: {'value': 'decrypted_%s' % secret, 'error': None} for secret in secrets}

print(json.dumps(response, separators=(',',':')))
