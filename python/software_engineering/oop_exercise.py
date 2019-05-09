"""Write class to make the code below work."""


# implement class here
# hint: class Programmer: ...


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
