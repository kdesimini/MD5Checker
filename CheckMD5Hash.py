import os
import fileinput
import subprocess

def CheckMD5Hash():
	inputHash = input("Enter hash to check here: ")
	inputPath = input("Drag file here: ")
	
	pipe = subprocess.Popen(["md5 " + inputPath], stdout=subprocess.PIPE, shell=True)
	
	command = ""
	for line in pipe.stdout:
		command = str(line)

	
	string = r"b'MD5 ("+ inputPath + r") = " + inputHash + r"\n'"
	print(string)
	print(command)
	
	if string == command:
 		print("Success! The hash's are the same.")
	else:
		print("FAIL. The hash's are NOT the same!")
	
CheckMD5Hash()
	
	