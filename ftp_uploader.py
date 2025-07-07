import ftplib
import os
import json
from datetime import datetime
import socket

class FTPUploader:
    def __init__(self):
        # PCPasokh Server Configuration - به روزرسانی با اطلاعات واقعی سرور
        self.ftp_config = {
            "host": "ftp.pcpasokh.ir",  # آدرس سرور پاسخگو رایانه
            "port": 21,
            "username": "reports_user",  # نام کاربری FTP
            "password": "PCPasokh2024!",  # رمز عبور FTP
            "remote_directory": "/network_reports/",  # پوشه گزارشات
            "timeout": 30
        }
        self.config_file = "ftp_config.json"
        self.load_config()
    
    def load_config(self):
        """Load FTP configuration from file if exists"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    saved_config = json.load(f)
                    self.ftp_config.update(saved_config)
            except Exception as e:
                print(f"Error loading FTP config: {e}")
    
    def save_config(self):
        """Save FTP configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.ftp_config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving FTP config: {e}")
    
    def update_config(self, host, port, username, password, remote_directory):
        """Update FTP configuration"""
        self.ftp_config.update({
            "host": host,
            "port": port,
            "username": username,
            "password": password,
            "remote_directory": remote_directory
        })
        self.save_config()
    
    def test_connection(self):
        """Test FTP connection to PCPasokh server"""
        try:
            # Create FTP connection
            ftp = ftplib.FTP()
            ftp.connect(self.ftp_config["host"], self.ftp_config["port"], self.ftp_config["timeout"])
            ftp.login(self.ftp_config["username"], self.ftp_config["password"])
            
            # Test directory access
            try:
                ftp.cwd(self.ftp_config["remote_directory"])
            except ftplib.error_perm:
                # Directory might not exist, try to create it
                try:
                    ftp.mkd(self.ftp_config["remote_directory"])
                    ftp.cwd(self.ftp_config["remote_directory"])
                except:
                    pass
            
            # Get server welcome message
            welcome_msg = ftp.getwelcome()
            ftp.quit()
            
            return True, f"✅ اتصال موفق به سرور پاسخگو رایانه\nConnection successful to PCPasokh server\nWelcome: {welcome_msg}"
            
        except socket.timeout:
            return False, "❌ خطا: زمان اتصال به پایان رسید\nError: Connection timeout"
        except socket.gaierror:
            return False, "❌ خطا: آدرس سرور یافت نشد\nError: Server address not found"
        except ftplib.error_perm as e:
            return False, f"❌ خطا: دسترسی مجاز نیست\nError: Permission denied - {str(e)}"
        except Exception as e:
            return False, f"❌ خطا در اتصال: {str(e)}\nConnection error: {str(e)}"
    
    def upload_report(self, report_content, system_id, report_type="diagnostic"):
        """Upload diagnostic report to PCPasokh server"""
        try:
            # Generate unique filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{system_id}_{report_type}_{timestamp}.txt"
            local_filepath = filename
            
            # Save report locally first
            with open(local_filepath, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            # Upload to FTP server
            success, message = self._upload_file(local_filepath, filename)
            
            # Clean up local file after upload
            try:
                os.remove(local_filepath)
            except:
                pass
            
            if success:
                return True, f"✅ گزارش با موفقیت ارسال شد\nReport uploaded successfully\nFilename: {filename}", filename
            else:
                return False, message, None
                
        except Exception as e:
            return False, f"❌ خطا در آماده‌سازی گزارش: {str(e)}\nError preparing report: {str(e)}", None
    
    def _upload_file(self, local_filepath, remote_filename):
        """Internal method to upload file to FTP server"""
        try:
            # Connect to FTP server
            ftp = ftplib.FTP()
            ftp.connect(self.ftp_config["host"], self.ftp_config["port"], self.ftp_config["timeout"])
            ftp.login(self.ftp_config["username"], self.ftp_config["password"])
            
            # Change to remote directory
            try:
                ftp.cwd(self.ftp_config["remote_directory"])
            except ftplib.error_perm:
                # Try to create directory if it doesn't exist
                try:
                    ftp.mkd(self.ftp_config["remote_directory"])
                    ftp.cwd(self.ftp_config["remote_directory"])
                except:
                    pass
            
            # Upload file in binary mode
            with open(local_filepath, 'rb') as file:
                ftp.storbinary(f'STOR {remote_filename}', file)
            
            ftp.quit()
            return True, "فایل با موفقیت آپلود شد / File uploaded successfully"
            
        except ftplib.error_perm as e:
            return False, f"خطا: عدم دسترسی FTP / FTP Permission error: {str(e)}"
        except socket.timeout:
            return False, "خطا: زمان اتصال به پایان رسید / Connection timeout"
        except Exception as e:
            return False, f"خطا در آپلود: {str(e)} / Upload error: {str(e)}"
    
    def get_uploaded_reports(self, system_id=None):
        """Get list of uploaded reports for a system"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self.ftp_config["host"], self.ftp_config["port"], self.ftp_config["timeout"])
            ftp.login(self.ftp_config["username"], self.ftp_config["password"])
            
            ftp.cwd(self.ftp_config["remote_directory"])
            
            # Get list of files
            files = ftp.nlst()
            
            # Filter by system ID if provided
            if system_id:
                files = [f for f in files if f.startswith(system_id)]
            
            ftp.quit()
            return True, files
            
        except Exception as e:
            return False, f"Error retrieving file list: {str(e)}"
    
    def download_report(self, remote_filename, local_filepath):
        """Download a report from the server"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self.ftp_config["host"], self.ftp_config["port"], self.ftp_config["timeout"])
            ftp.login(self.ftp_config["username"], self.ftp_config["password"])
            
            ftp.cwd(self.ftp_config["remote_directory"])
            
            with open(local_filepath, 'wb') as file:
                ftp.retrbinary(f'RETR {remote_filename}', file.write)
            
            ftp.quit()
            return True, f"Report downloaded to {local_filepath}"
            
        except Exception as e:
            return False, f"Download error: {str(e)}"
    
    def delete_old_reports(self, days_old=30):
        """Delete reports older than specified days (admin function)"""
        try:
            from datetime import timedelta
            
            ftp = ftplib.FTP()
            ftp.connect(self.ftp_config["host"], self.ftp_config["port"], self.ftp_config["timeout"])
            ftp.login(self.ftp_config["username"], self.ftp_config["password"])
            
            ftp.cwd(self.ftp_config["remote_directory"])
            
            files = ftp.nlst()
            cutoff_date = datetime.now() - timedelta(days=days_old)
            deleted_count = 0
            
            for filename in files:
                try:
                    # Extract date from filename (format: SYSTEMID_TYPE_YYYYMMDD_HHMMSS.txt)
                    parts = filename.split('_')
                    if len(parts) >= 4:
                        date_str = parts[2]  # YYYYMMDD part
                        file_date = datetime.strptime(date_str, '%Y%m%d')
                        
                        if file_date < cutoff_date:
                            ftp.delete(filename)
                            deleted_count += 1
                except:
                    continue
            
            ftp.quit()
            return True, f"Deleted {deleted_count} old reports"
            
        except Exception as e:
            return False, f"Error deleting old reports: {str(e)}"