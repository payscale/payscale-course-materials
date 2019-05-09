"""Write class to make the code below work."""


# implement class here
# hint: class Programmer: ...
class Programmer:

    def __init__(self, language):
        self.language = language
    
    def hello_world(self):
        if self.language == "python":
            return 'print("hello world")'
        elif self.language == "bash":
            return "echo 'hello world'"
        else:
            return f"ack! I don'k know {self.language}"


# try to make the following code work
programmer = Programmer(language="python")
hello_world_program = programmer.hello_world()
print(hello_world_program, '<should be> `print("hello world")`')

programmer = Programmer(language="bash")
hello_world_program = programmer.hello_world()
print(hello_world_program, "<should be> `echo 'hello world'`")

programmer = Programmer(language="Java")
hello_world_program = programmer.hello_world()
print(hello_world_program, "<should be> `ack! I don't know Java!`")

programmer = Programmer(language="C++")
hello_world_program = programmer.hello_world()
print(hello_world_program, "<should be> `ack! I don't know C++!`")
