import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "import sys; print(sys.stdin.read())"], input=b"underwater"
)

# https://www.digitalocean.com/community/tutorials/how-to-use-subprocess-to-run-external-programs-in-python-3

