# import ftplib

# from ftplib import FTP
# ftp = FTP('ftp.us.debian.org')  # connect to host, default port
# x=(ftp.login())   
# print(x)   #login status               

# lst=ftp.retrlines('LIST')           # list directory contents

# ===========================================

# listing files from an ftp server
 
# ftp = ftplib.FTP("ftp.nluug.nl")
# ftp.login("anonymous", "ftplib-example-1") #connects to the FTP server at ftp.nluug.nl.

# data = []
 
# ftp.dir(data.append) #current directory on the FTP server and appends each line of the directory listing to the data 
 
# ftp.quit()
 
# for dat in data:
#     print (dat)
