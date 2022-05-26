from asyncore import write


f = open("new.txt", "w")
f.write("I like how it is a readable programming language!")

f = open("new.txt", "a")
f.write("\nI plan to use this in my work soon.")
f.write("\nBy finding a company that will guide me in my python programming journey")
f.write("\n I plan to master python as soon as possible")

f = open("new.txt", "r")
f.close()