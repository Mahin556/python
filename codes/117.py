def devide(n1,n2):
    try:
        result=n1/n2
    except ZeroDivisionError:
        return "Can't use zero(0) as divisor"
    except:
        return "Unknown error"
    else:
        return result


print(devide("4",1))


# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")