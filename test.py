from pyjsonio.jsonio import JsonIO

json_test = JsonIO("testfile.json")

print("Dict: ", json_test.dict())
print("Json: ", json_test.json())
print("Element position zero: ", json_test[0])