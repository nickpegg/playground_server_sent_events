# Server-Sent Events Playground

After reading [Julia Evans's blog post on server-sent
events](https://jvns.ca/blog/2021/01/12/day-36--server-sent-events-are-cool--and-a-fun-bug/),
I wanted to mess around with them! This is a little playground repo for that.

## log_tailer
This is a simple program which has one thread writing lines to a log file, and
another thread serving up a Flask app which has a /read endpoint that will send
server-sent events of new logfile contents.

The javascript here handles the events and appends the new lines to the
displayed log, and even has the option to auto-scroll the log like `tail -F`!

To see this in action, run `make run` in a terminal and then open
https://localhost:5000/ in a web browser.


## log_tailer_htmx

Same thing as the original log tailer, but using the [htmx](https://htmx.org) framework.
