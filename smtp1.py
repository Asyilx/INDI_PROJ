from getpass import getpass
from socket import *
from base64 import *
import ssl

YOUR_EMAIL = input("Enter Your Email Address : ")
YOUR_PASSWORD = getpass("Enter Your Email Password : ")
YOUR_DESTINATION_EMAIL = input("Enter Email Destination : ")
YOUR_SUBJECT_EMAIL = input("Enter Subject : ")
YOUR_BODY_EMAIL = input("Enter Message : ")

msg = '{}. \r\n\nThis Purpose Is For Individual Project ITT440 Sir Azizi'.format(YOUR_BODY_EMAIL)
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
#Fill in end

recv = clientSocket.recv(1024)
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'.encode()
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')

# Account Authentication
# Fill in start
strtlscmd = "STARTTLS\r\n".encode()
clientSocket.send(strtlscmd)
recv2 = clientSocket.recv(1024)

sslClientSocket = ssl.wrap_socket(clientSocket)

EMAIL_ADDRESS = b64encode(YOUR_EMAIL.encode())
EMAIL_PASSWORD = b64encode(YOUR_PASSWORD.encode())

authorizationcmd = "AUTH LOGIN\r\n"

sslClientSocket.send(authorizationcmd.encode())
recv2 = sslClientSocket.recv(1024)
print(recv2)

sslClientSocket.send(EMAIL_ADDRESS + "\r\n".encode())
recv3 = sslClientSocket.recv(1024)
print(recv3)

sslClientSocket.send(EMAIL_PASSWORD + "\r\n".encode())
recv4 = sslClientSocket.recv(1024)
print(recv4)
# Fill in end    
	
# Send MAIL FROM command and print server response.
# Fill in start
mailfrom = "MAIL FROM: <{}>\r\n".format(YOUR_EMAIL)
sslClientSocket.send(mailfrom.encode())
recv5 = sslClientSocket.recv(1024)
print(recv5)
# Fill in end    

# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT TO: <{}>\r\n".format(YOUR_DESTINATION_EMAIL)
sslClientSocket.send(rcptto.encode())
recv6 = sslClientSocket.recv(1024)
# Fill in end

# Send DATA command and print server response. 
# Fill in start
data = 'DATA\r\n'
sslClientSocket.send(data.encode())
recv7 = sslClientSocket.recv(1024)
print(recv7)
# Fill in end    

# Send message data.
# Fill in start
sslClientSocket.send("Subject: {}\n\n{}".format(YOUR_SUBJECT_EMAIL, msg).encode())
# Fill in end

# Message ends with a single period.
# Fill in start
sslClientSocket.send(endmsg.encode())
recv8 = sslClientSocket.recv(1024)
print(recv8)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcommand = 'QUIT\r\n'
sslClientSocket.send(quitcommand.encode())
recv9 = sslClientSocket.recv(1024)
print(recv9)

sslClientSocket.close()
print('Was successful!')
# Fill in end
