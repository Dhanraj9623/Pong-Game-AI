# Pong-Game-AI
You will need to install the necessary dependenies

Just type 

> pip install -r requirements.txt


Also install Android Debug Bridge (ADB) Client for making the connection between your android mobile and computer.

You will also need a android phone with pong game installed from playstore.

## Installation

To run the app flawlessly, satisfy the requirements

<button id="copyButton" onclick="copyToClipboard()">Copy to Clipboard</button>



<script>
  function copyToClipboard() {
    const textToCopy = "This is the text you want to copy.";

    const textArea = document.createElement("textarea");
    textArea.value = textToCopy;

    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);

    alert("Copied to clipboard: " + textToCopy);
  }
</script>

