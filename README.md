# StackState Agent v2 secrets example

Tested on StackState Agent 2.7.0 and Python 2/3.


## Secrets executable

```
chmod u+x ./secrets.py
chmod go-r ./secrets.py
```

Test:

```
sudo -u stackstate-agent -- echo '{"version": "1.0", "secrets": ["secret1", "secret2"]}' | ./secrets.py
```

## Enable secrets backend

Edit `/etc/stackstate-agent/stackstate.yaml`

Add:

```
secret_backend_command: /path/to/secrets.py
```

Restart the StackState Agent service, e.g. `systemctl restart stackstate-agent`


## Example check


`/etc/stackstate-agent/checks.d/hello.py`

`/etc/stackstate-agent/conf.d/hello.yaml`


`sudo -u stackstate-agent -- stackstate-agent check hello -l INFO`

```
2020-10-06 12:46:57 UTC | INFO | (src/github.com/StackVista/stackstate-agent/pkg/collector/py/datadog_agent.go:150 in LogMessage) | (hello.py:7) | {'secret2': 'decrypted_secret2', 'secret1': 'decrypted_secret1'}
=========
Collector
=========

  Running Checks
  ==============

    hello (1.0.0)
    -------------
      Instance ID: hello:17af12e826a642f5 [OK]
      Total Runs: 1
      Metric Samples: Last Run: 0, Total: 0
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
```

Test:

```
sudo -u stackstate-agent -- stackstate-agent secret
```