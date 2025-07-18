import subprocess
import sys
ans = subprocess.call(["python", "--version"])
if ans == 0:
    print("Command executed.")
else:
    print("Command failed.", ans)


# https://www.geeksforgeeks.org/python/python-subprocess-module/
print(sys.executable)

result = subprocess.run([sys.executable, "-c", "print('ocean')"], capture_output=True, text=True)

#Now that we can invoke an external program using subprocess.run, let’s see how we can capture output from that program. For example, this process could be useful if we wanted to use git ls-files to output all your files currently stored under version control.

print("stdout:", result.stdout)
print("stderr:", result.stderr)

result1 = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True)

print("stderr:", result1.stderr)

print(result1.check_returncode())

#We can use the check=True keyword argument to subprocess.run to have an exception raised if the external program returns a non-zero exit code:
result1 = subprocess.run([sys.executable, "-c", "raise ValueError('oops')"], capture_output=True, text=True, check=True)
print("stderr:", result1.stderr)

