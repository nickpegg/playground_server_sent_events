function main() {
    logContents = "-- log start --\n";

    console.log("Tailer starting");
    document.querySelector("#log").textContent = logContents;

    // Set to true if log scroll was done automatically
    wasAutoScroll = false;

    // Should we auto-scroll the log?
    followLog = false;

    // Element containing the log
    logEl = document.querySelector("#log")

    // Set auto-scrolling if the Follow checkbox is checked
    document.querySelector("#follow").onchange = function(ev) {
        followLog = ev.srcElement.checked;
        if (followLog) {
            logEl.scrollTo(0, logEl.scrollHeight);
        }
    };

    // Adjust auto-scroll depending on where the log gets scrolled to. If it goes to the
    // end, then start auto-scrolling. Otherwise, stop it.
    logEl.onscroll = function(ev) {
        followLog = (logEl.scrollHeight - Math.abs(logEl.scrollTop) === logEl.clientHeight);
        document.querySelector("#follow").checked = followLog;
    }

    // Set up the event source to read the log
    evtSource = new EventSource("/read");
    evtSource.onerror = function(err) {
        console.log("Got error: ", err);
    }
    evtSource.addEventListener("text", function(event) {
        // event data JSON format: {"logText": "<new text to show>"}
        logContents += JSON.parse(event.data).logText;
        logEl.textContent = logContents;

        if (followLog) {
            logEl.scrollTo(0, logEl.scrollHeight);
        }
    });
}

document.addEventListener('DOMContentLoaded', main);
