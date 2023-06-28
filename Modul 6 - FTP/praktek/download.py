import ftplib 
import os

def download_file(hostname, username, password, filename):     
    try: 
        #membuat objek         
        ftp = ftplib.FTP(hostname)  
        #Login ke server FTP 
        ftp.login(username, password) 
 
        #ganti directory kerja         
        ftp.cwd('') 
 
        # buka file untuk ditulis         
        with open(filename, 'wb') as file: 
            # unduh file mp4             
            ftp.retrbinary('RETR ' + filename, file.write)  
            
        # tutup koneksi FTP         
        ftp.quit() 
        print("File berhasil diunduh")
        
        # Rename file
        new_filename="result_" + filename
        os.rename(filename, new_filename)
        print("File berhasil direname menjadi", new_filename)  
    except ftplib.all_errors as e: 
        print("Terjadi kesalahan: ",e) 
 
#contoh penggunaan fungsi download_file 
hostname = '127.0.0.1' 
username = 'whisnuu' 
password = 'progjar123' 
filename = 'tes.mp4' 

download_file(hostname, username, password, filename) 
