from pyjsonio.jsonio import JsonIO

json_test = JsonIO("testfile.json")


print("Basic test:")
print("Dict: ", json_test.dict())
print("Json: ", json_test.json())
print("Element position zero: ", json_test[0])


print("Change value in element position zero:")
print("Before: ", json_test[0])
json_test[0]["name"] = "Doo"
print("After: ", json_test[0])


print("Write modified json to new file: ")
json_test.write("testfile2.json")
print("ok")


print("Read new file: ")
json_test.read("testfile2.json")
print("Dict: ", json_test.dict())


print("test string: ", json_test)


print("Delete object: ")
del json_test
try:
    print(json_test)
except NameError:
    print("ok")