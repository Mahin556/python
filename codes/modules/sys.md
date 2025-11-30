* A built-in Python module that gives access to Python interpreter internals, system information, command-line arguments, exit codes, paths, I/O streams, and more.
* No installation required.

```python
import sys
print(sys.argv)
```
```bash
$ python test.py 23
['test.py', '23']
```

---

* `sys.exit()`
```python
import sys

if len(sys.argv) < 2:
    print("Error: No argument provided")
    sys.exit(1)
    #sys.exit("Error: No argument provided")

print(sys.argv)
```
```bash
ADMIN@DESKTOP-NUAAG9F MINGW64 ~/Documents/git-repos/python/codes/modules (main)
$ python test.py 23
['test.py', '23']

ADMIN@DESKTOP-NUAAG9F MINGW64 ~/Documents/git-repos/python/codes/modules (main)
$ python test.py 
Error: No argument provided
```
```python
import sys

if len(sys.argv) < 2:
    # print("Error: No argument provided")
    # sys.exit(1)
    sys.exit("Error: No argument provided")

print(sys.argv)
```
```bash
ADMIN@DESKTOP-NUAAG9F MINGW64 ~/Documents/git-repos/python/codes/modules (main)
$ python test.py 
Error: No argument provided

ADMIN@DESKTOP-NUAAG9F MINGW64 ~/Documents/git-repos/python/codes/modules (main)
$ echo $?
1
```
```python
age = 17
if age < 18:
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
```
```python
import sys
n = len(sys.argv) # give no of command line arguments
print(f"No of command line arguments:- {n}")
print(f"Name of the script:- {sys.argv[0]}")
print(f"All arguments:- {sys.argv[1:n]}")

for i in range(n):
    print(f"Argument:- {sys.argv[i]}")

sum=0
for i in range(1,n):
    sum+=int(sys.argv[i])
print(f"Sum of all arguments:- {sum}")
```

---

* `sys.version` / `sys.version_info` / `sys.version_info.major`
```python
import sys
print(sys.version)
print()
print(sys.version_info)
print()
print(sys.version_info.major)
```
```bash
$ python test.py 
3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)]

sys.version_info(major=3, minor=13, micro=9, releaselevel='final', serial=0)

3
```

---

* `sys.path` Module paths
```python
import sys
print(sys.path)
print()
for p in sys.path:
    print(p)

#sys.path.append("/my/custom/modules") To append new search path
```
```bash
$ python test.py 
['C:\\Users\\ADMIN\\Documents\\git-repos\\python\\codes\\modules', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\python313.zip', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\DLLs', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\Lib', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0', 'C:\\Users\\ADMIN\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages', 'C:\\Users\\ADMIN\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages\\win32', 'C:\\Users\\ADMIN\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages\\win32\\lib', 'C:\\Users\\ADMIN\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages\\Pythonwin', 'C:\\Program Files\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\\Lib\\site-packages']

C:\Users\ADMIN\Documents\git-repos\python\codes\modules
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\python313.zip
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\DLLs
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0
C:\Users\ADMIN\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages
C:\Users\ADMIN\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\win32
C:\Users\ADMIN\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\win32\lib
C:\Users\ADMIN\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\Pythonwin
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\site-packages
```

---

* `sys.platform`
```python
import sys
print(sys.platform)
```
```bash
$ python test.py 
win32
```

---

* `sys.executable`
```python
import sys
print(sys.executable)
```
```bash
$ python test.py 
C:\Users\ADMIN\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe
```

---

* `sys.prefix`
```python
import sys
print(sys.prefix)
```
```bash
$ python test.py 
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0
```

---

* `sys.getwindowsversion()`
```python
import sys
print(sys.getwindowsversion())
```
```bash
$ python test.py 
sys.getwindowsversion(major=10, minor=0, build=19045, platform=2, service_pack='')
```

---

* Standard Streams — `sys.stdin`, `sys.stdout`, `sys.stderr`
```python
import sys
sys.stdout.write("Hello\n")
```
```python
import sys
data = sys.stdin.read() 
#It waits for input from user, pipe, or file.
#It keeps reading until you signal EOF.
print(data)
#Linux/Mac: CTRL + D
#Windows: CTRL + Z + Enter
```
```python
import sys
sys.stderr.write("Error message\n")
```
```python
python script.py < myfile.txt
```
```python
echo "Hello world" | python script.py
```
```python
import sys
sys.stdout.write("Loading...")
sys.stdout.flush()
```
* `flush()` forces Python to immediately write the output to the screen (stdout).
* Without flush(), Python may buffer (hold) the output in memory and print it later.
* Python uses output buffering for performance.
* That means:
  * Your output might not appear instantly.
  * Especially when printing in loops, progress bars, or real-time logs.
  * `flush()` forces the buffer to empty right now.

```python
for i in range(5):
    sys.stdout.write(f"\rProcessing {i}")
    sys.stdout.flush()
```
```python
print("Loading...", flush=True)
```

---

* Recursion Limit — `sys.getrecursionlimit()`, `sys.setrecursionlimit()`
```python
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
```
```bash
$ python test.py 
1000
2000
```

---

* Maximum Size of Integers — `sys.maxsize`
* Shows the maximum size Python ints/lists can hold (depends on architecture).
```python
import sys
print(sys.maxsize)
```

---

* Dynamic Module Loading — `sys.modules`
* Dictionary of all modules currently loaded.
* Useful for debugging imports.
```python
import sys
print(sys.modules)
print(sys.modules.keys()) #Only keys
```

---

* Full List of All Attributes in sys
```python
import sys
print(dir(sys))
```

---

* Python Implementation Details
• `sys.implementation` → CPython/PyPy version info
• `sys.byteorder` → little or big endian

```python
import sys
print(sys.implementation)
```
```bash
$ python test.py 
namespace(name='cpython', cache_tag='cpython-313', version=sys.version_info(major=3, minor=13, micro=9, releaselevel='final', serial=0), hexversion=51186160)
```

---

* System Flags — `sys.flags`
• Shows which flags were used when running Python:
  * -O optimization
  * -u unbuffered
  * -B no bytecode
```python
import sys
print(sys.flags)
```

---

* System Internals
    • sys.getsizeof(obj) → memory size of an object (in bytes)
    • sys.getrefcount(obj) → reference count of an object
    • sys.intern(string) → internal string optimizations

```python
import sys
print(sys.getsizeof("hello"))
```

---

* Exception Handling Tools
    * `sys.exc_info()` → current exception type, value, and traceback.
    * Often used inside exception blocks.

```python
import sys
try:
    1/0
except:
    print(sys.exc_info())
```
```bash
$ python test.py                                                                                              ks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'g
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001CD9F7F8980>)
```

---

* System Internals
    * `sys.getsizeof(obj)` → memory size of an object (in bytes)
    * `sys.getrefcount(obj)` → reference count of an object
    * `sys.intern(string)` → internal string optimizations

```python
import sys
print(sys.getsizeof("hello"))
```

---

* System Flags — `sys.flags`
  * Shows which flags were used when running Python:
  * -O optimization
  * -u unbuffered
  * -B no bytecode

```python
import sys
print(sys.flags)
```

---

* Check If Script is Frozen (PyInstaller)
```python
import sys
if getattr(sys, 'frozen', False):
    print("Running from EXE")
```

---

* System Encoding
```python
import sys
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
```
```bash
$ python test.py 
utf-8
utf-8
```

---

* Quiting
```python
import sys
for line in sys.stdin:
    if 'q' == line.strip():
        break
    print(f'Input : {line}')
print("Exit")
```
```python
import sys
print("Please enter you input here")
for line in sys.stdin:
    if line.lower().strip() in ['q','quit']:
        break
    print(f'Input : {line} \n Enter q/quit to exit: ')
print("Exit")
```

---

