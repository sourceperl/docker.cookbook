# tts-redis-gw

A simple tts gateway that work with redis-srv. Just publish on redis a text message to channel "tts-channel" and the gateway immediately send it to espeak/mbrola.

Send a text message with redis-cli:

```bash
redis-cli -h redis-srv publish tts-channel "C'est rien de le dire."
```

Build and run container:

```bash
./setup.sh
```