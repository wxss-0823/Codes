# $language = "python"
# $interface = "1.0"

# This script shows how to read in a file, and it demonstrates how to
# perform some preprocessing on data (splitting the file data into
# separate strings) before sending it to a server.


def checkReturn(echo: str, wait_time: int, error_handle: list) -> bool:
	if not crt.Screen.WaitForStrings(echo, wait_time):
		if error_handle == "Stuck Dead"
			crt.Session.Disconnect
		crt.Screen.Send("Error" + "\r")
		for cmd in error_handle:
			crt.Screen.Send(cmd + "\r")
			crt.Sleep(100)
			checkReturn("OK", 15, "Stuck Dead"):
		return False
	return True
	

def main() -> None:
	crt.Screen.Synchronous = False
	error_handle = [
		"carr_inactivate 0", "carr_inactivate 1",
		"carr_inactivate 2", "carr_inactivate 3"
	]
	
	echo = [
		"OK", "done"
	]
	
	wait_time = 15
	
	dir = "D:\\Users\\ProjectFiles\\Codes\\PycharmProjects\\Projects\\20250808\\SecureCRTScript\\N28CarrierConfig.txt"
	
	while 1:
		for line in open(dir, "r"):
			crt.Screen.Send(line)
			crt.Sleep(100)
			if not checkReturn(echo, wait_time, error_handle):
				break
			
		crt.Sleep(30000)
			
main()