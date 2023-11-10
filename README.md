# DreamyBird
A open source project aimed to creating the first python DreamBerd interpreter.
If you don't know DreamBerd see this repo: https://github.com/TodePond/DreamBerd

## Contribute
If you want to help, feel free to contribute to this project, by making pull requests, raising issues you encounter, etc. <3

## State of Dev
Since this project is completly new, we have a lot to do!
Until now, the .db3 Script in /data/db3code/ is read and I started by trying to parse every line to a lineHandler in /interpreter/LineHandler.py.
In the current commit, the lineHandler should detect empty lines, recognise var declarations and count the exclamation marks at the line ending.
Especially the exclamation mark count will need a lot of work, since it isn't really efficiant not can it handle exclamation marks in strings with double qoutes...
So even the little things I already have, will need a huge rework.
I hope together we will be able to achive more, and start coding in the best programming language ever build...

### TODO
So I wwould suggest:
-reworking the current methods
-replacing ; with the not operator
-running interpreted codelines
-error handling
-functions
-classes
-kivy.md interface for writing code
-with the custom IDE interface we should be able to encode emojis and numbers so that they can be used as var names
-detecting plain text after var declaration as string var
-arrays
Feel free to add more, break up points and/or order them, ... 

## Ownership
Since this project does not have the name DreamBerd3 in its title, I guess it's owned by the DreamBerd 3 Foundation haha
