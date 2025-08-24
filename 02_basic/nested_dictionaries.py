# nested dictionaries
phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5
    }
}   
print(phones["Area1"]["y"])
print(phones["Area2"]["c"])
