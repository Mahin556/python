import subprocess

ls_Process = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(["grep", "sample"], stdin=ls_Process.stdout,stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()

print(output)
print(error)