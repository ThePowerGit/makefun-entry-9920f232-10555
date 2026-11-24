# Make the AI Judge Laugh: the Office Joke Open

The entry:

> The meeting that could have been an email has been moved to 4pm, when it will be an email.

90 characters, well under the 200-character cap.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies the exact bytes of `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt`,
defaulting to `/output`.
