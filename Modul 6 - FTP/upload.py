import ftplib 


def upload_file(hostname, username, password, filename):     
    try: 
        #membuat objek FTP 
        ftp = ftplib.FTP(hostname)  
        #login ke server FTP 
        ftp.login(username, password) 
 
        #buka file untuk dibaca         
        with open(filename, 'rb') as file: 
            #unggah file mp4             
            ftp.storbinary('STOR ' + filename, file)  
            #tutup koneksi ftp         
            ftp.quit() 
            print("File berhasil diunggah")     
    except ftplib.all_errors as e: 
        print("Terjadi kesalahan: ", e) 
 
#contoh penggunaan fungsi upload_file 
hostname = '127.0.0.1' 
username = 'whisnuu' 
password = 'progjar123' 
filename = 'mantoi.jpg' 

upload_file(hostname, username, password, filename) 
