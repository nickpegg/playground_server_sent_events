import json
import threading
import random
import time
from typing import Iterator

from flask import Flask, render_template, stream_with_context, Response

OUTPUT_FILE = "service.log"


def main() -> None:
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        """
        Just serve up the HTML page
        """
        return render_template("index.html")

    @app.route("/read")
    def read() -> Response:
        """
        Read the log file forever, returning Server-Sent Events for each additional bit
        that was read.
        """

        def generate() -> Iterator[bytes]:
            with open(OUTPUT_FILE) as f:
                while True:
                    text = f.read().strip()
                    if text != "":
                        yield make_event(text)
                    time.sleep(0.25)

        return Response(generate(), mimetype="text/event-stream")

    print("Starting threads")
    threading.Thread(target=producer).start()
    threading.Thread(target=app.run).start()


def make_event(log_text: str) -> bytes:
    """
    Build and return a Javascript server-sent event
    """
    event = b"event: logLine\n"
    for line in log_text.splitlines():
        line = line.strip()
        if line != "":
            event += f"data: {line}\n".encode()
    event += b"data: \n"
    event += b"\n"
    return event


def producer() -> None:
    """
    Producer thread which writes lines to a log file forever
    """
    # truncate the file
    with open(OUTPUT_FILE, "w"):
        pass

    print("producer running")
    while True:
        num = random.randint(1, 100)
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"jawn {num}\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
