import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, ttk
import threading
import os
import socket
import subprocess
import platform
from datetime import datetime
import uuid
import hashlib

class SimpleNetworkRepair:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PCPasokh Internet Repair - عیب یاب و ترمیم اینترنت پاسخگو رایانه")
        self.root.geometry("900x700")
        self.root.configure(bg='#2b2b2b')
        
        # Generate system ID
        self.system_id = self.generate_system_id()
        self.current_report = ""
        
        self.setup_ui()
        
    def generate_system_id(self):
        """Generate unique system identifier"""
        try:
            mac = hex(uuid.getnode())[2:].upper()
            identifier_string = f"{mac}-{platform.node()}"
            system_id = hashlib.md5(identifier_string.encode()).hexdigest()[:16].upper()
            return f"PC-{system_id}"
        except:
            return f"PC-{str(uuid.uuid4())[:16].upper()}"
    
    def setup_ui(self):
        """Setup user interface"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2b2b2b', height=100)
        title_frame.pack(fill='x', padx=20, pady=20)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame,
            text="PCPasokh Internet Repair\nعیب یاب و ترمیم اینترنت پاسخگو رایانه",
            font=("Arial", 16, "bold"),
            fg='white',
            bg='#2b2b2b'
        )
        title_label.pack(expand=True)
        
        system_id_label = tk.Label(
            title_frame,
            text=f"System ID: {self.system_id}",
            font=("Consolas", 10),
            fg='#888888',
            bg='#2b2b2b'
        )
        system_id_label.pack()
        
        # Main content
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Left panel
        left_panel = tk.Frame(main_frame, bg='#3b3b3b', width=300)
        left_panel.pack(side='left', fill='y', padx=(0, 10), pady=0)
        left_panel.pack_propagate(False)
        
        # Control buttons
        tk.Label(left_panel, text="کنترل پنل / Control Panel", 
                font=("Arial", 12, "bold"), fg='white', bg='#3b3b3b').pack(pady=20)
        
        self.start_btn = tk.Button(
            left_panel,
            text="🔍 شروع عیب یابی\nStart Diagnosis",
            command=self.start_diagnosis,
            height=3,
            bg='#059669',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat'
        )
        self.start_btn.pack(fill='x', padx=20, pady=(0, 10))
        
        self.repair_btn = tk.Button(
            left_panel,
            text="🔧 ترمیم مشکلات\nRepair Issues",
            command=self.repair_issues,
            height=3,
            bg='#dc2626',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            state='disabled'
        )
        self.repair_btn.pack(fill='x', padx=20, pady=(0, 10))
        
        self.reset_btn = tk.Button(
            left_panel,
            text="🔄 بازنشانی\nReset",
            command=self.reset_app,
            height=2,
            bg='#7c3aed',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat'
        )
        self.reset_btn.pack(fill='x', padx=20, pady=(0, 20))
        
        # Save button
        self.save_btn = tk.Button(
            left_panel,
            text="💾 ذخیره گزارش\nSave Report",
            command=self.save_report,
            height=2,
            bg='#1f2937',
            fg='white',
            font=("Arial", 10),
            relief='flat',
            state='disabled'
        )
        self.save_btn.pack(fill='x', padx=20, pady=(0, 10))
        
        # Contact info
        contact_frame = tk.Frame(left_panel, bg='#3b3b3b')
        contact_frame.pack(side='bottom', fill='x', padx=20, pady=20)
        
        tk.Label(contact_frame, text="ارتباط با پاسخگو رایانه", 
                font=("Arial", 10, "bold"), fg='white', bg='#3b3b3b').pack()
        tk.Label(contact_frame, text="📞 021-88888888\n📧 support@pcpasokh.ir", 
                font=("Arial", 8), fg='#cccccc', bg='#3b3b3b').pack()
        
        # Right panel
        right_panel = tk.Frame(main_frame, bg='#3b3b3b')
        right_panel.pack(side='right', fill='both', expand=True, padx=(10, 0), pady=0)
        
        # Status
        self.status_label = tk.Label(
            right_panel,
            text="🔴 آماده / Ready",
            font=("Arial", 14, "bold"),
            fg='#ef4444',
            bg='#3b3b3b'
        )
        self.status_label.pack(pady=20)
        
        # Progress
        self.progress_label = tk.Label(
            right_panel,
            text="آماده برای شروع عیب یابی... / Ready to start diagnosis...",
            font=("Arial", 10),
            fg='white',
            bg='#3b3b3b'
        )
        self.progress_label.pack(pady=(0, 10))
        
        # Results
        tk.Label(right_panel, text="📋 نتایج عیب یابی / Diagnostic Results", 
                font=("Arial", 12, "bold"), fg='white', bg='#3b3b3b').pack(pady=(20, 10))
        
        self.results_text = scrolledtext.ScrolledText(
            right_panel,
            height=25,
            font=("Consolas", 9),
            bg='#1a1a1a',
            fg='#cccccc',
            insertbackground='white'
        )
        self.results_text.pack(fill='both', expand=True, padx=20, pady=(0, 20))
    
    def update_progress(self, message):
        """Update progress display"""
        self.progress_label.configure(text=message)
        timestamp = datetime.now().strftime('%H:%M:%S')
        self.results_text.insert('end', f"[{timestamp}] {message}\n")
        self.results_text.see('end')
        self.root.update()
    
    def test_basic_connectivity(self):
        """Test basic internet connectivity"""
        try:
            # Test DNS resolution
            socket.gethostbyname('google.com')
            self.update_progress("✅ DNS Resolution: PASS - Successfully resolved google.com")
            
            # Test socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            result = sock.connect_ex(('google.com', 80))
            sock.close()
            
            if result == 0:
                self.update_progress("✅ HTTP Connectivity: PASS - Can connect to google.com")
                return True
            else:
                self.update_progress("❌ HTTP Connectivity: FAIL - Cannot connect to google.com")
                return False
                
        except socket.gaierror:
            self.update_progress("❌ DNS Resolution: FAIL - DNS resolution failed")
            return False
        except Exception as e:
            self.update_progress(f"❌ Connectivity Test: FAIL - Error: {str(e)}")
            return False
    
    def test_ping(self):
        """Test ping connectivity"""
        servers = [
            ('Google DNS', '8.8.8.8'),
            ('Cloudflare DNS', '1.1.1.1'),
            ('Shecan DNS', '178.22.122.100')
        ]
        
        for name, ip in servers:
            try:
                if platform.system() == "Windows":
                    result = subprocess.run(['ping', '-n', '4', ip], 
                                          capture_output=True, text=True, timeout=15)
                else:
                    result = subprocess.run(['ping', '-c', '4', ip], 
                                          capture_output=True, text=True, timeout=15)
                
                if result.returncode == 0:
                    self.update_progress(f"✅ Ping {name}: PASS - Successfully pinged {ip}")
                else:
                    self.update_progress(f"❌ Ping {name}: FAIL - Ping to {ip} failed")
            except Exception as e:
                self.update_progress(f"❌ Ping {name}: FAIL - Error: {str(e)}")
    
    def check_network_adapters(self):
        """Check network adapter status using system commands"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['ipconfig'], capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_progress("✅ Network Adapters: Information retrieved")
                    # Parse basic info from ipconfig
                    lines = result.stdout.split('\n')
                    adapter_count = sum(1 for line in lines if 'adapter' in line.lower())
                    self.update_progress(f"📊 Found {adapter_count} network adapters")
                else:
                    self.update_progress("❌ Network Adapters: Failed to retrieve information")
        except Exception as e:
            self.update_progress(f"❌ Network Adapters: Error - {str(e)}")
    
    def start_diagnosis(self):
        """Start network diagnosis"""
        self.start_btn.configure(state='disabled')
        self.repair_btn.configure(state='disabled')
        self.save_btn.configure(state='disabled')
        
        self.results_text.delete('1.0', 'end')
        self.status_label.configure(text="🟡 در حال عیب یابی / Diagnosing...", fg='#f59e0b')
        
        # Run diagnosis in thread
        diagnosis_thread = threading.Thread(target=self.run_diagnosis)
        diagnosis_thread.daemon = True
        diagnosis_thread.start()
    
    def run_diagnosis(self):
        """Run the actual diagnosis"""
        try:
            self.update_progress("🔍 شروع عیب یابی جامع شبکه / Starting comprehensive network diagnosis...")
            
            # Test basic connectivity
            has_internet = self.test_basic_connectivity()
            
            # Check network adapters
            self.check_network_adapters()
            
            # Test ping connectivity
            self.test_ping()
            
            # Generate report
            self.generate_report(has_internet)
            
            # Update UI on main thread
            self.root.after(0, self.diagnosis_completed, has_internet)
            
        except Exception as e:
            self.root.after(0, self.diagnosis_error, str(e))
    
    def diagnosis_completed(self, has_internet):
        """Handle diagnosis completion"""
        if has_internet:
            self.status_label.configure(text="🟢 متصل / Connected", fg='#10b981')
            self.repair_btn.configure(state='disabled')
            self.update_progress("✅ عیب یابی کامل شد - اینترنت کار می‌کند!")
        else:
            self.status_label.configure(text="🔴 مشکل شناسایی شد / Issues Detected", fg='#ef4444')
            self.repair_btn.configure(state='normal')
            self.update_progress("❌ عیب یابی کامل شد - مشکلاتی یافت شد!")
        
        self.start_btn.configure(state='normal')
        self.save_btn.configure(state='normal')
    
    def diagnosis_error(self, error):
        """Handle diagnosis error"""
        self.update_progress(f"❌ خطا در عیب یابی / Diagnosis error: {error}")
        self.status_label.configure(text="🟡 خطا / Error", fg='#f59e0b')
        self.start_btn.configure(state='normal')
    
    def repair_issues(self):
        """Repair network issues"""
        self.repair_btn.configure(state='disabled')
        self.status_label.configure(text="🔧 در حال ترمیم / Repairing...", fg='#f59e0b')
        
        repair_thread = threading.Thread(target=self.run_repair)
        repair_thread.daemon = True
        repair_thread.start()
    
    def run_repair(self):
        """Run network repair operations"""
        try:
            repairs_done = []
            
            # DNS flush
            if self.flush_dns():
                repairs_done.append("DNS Cache Flush")
            
            # IP renewal
            if self.renew_ip():
                repairs_done.append("IP Address Renewal")
            
            # Winsock reset
            if self.reset_winsock():
                repairs_done.append("Winsock Reset")
            
            self.root.after(0, self.repair_completed, repairs_done)
            
        except Exception as e:
            self.root.after(0, self.repair_error, str(e))
    
    def flush_dns(self):
        """Flush DNS cache"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['ipconfig', '/flushdns'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_progress("✅ DNS Cache Flush: SUCCESS")
                    return True
                else:
                    self.update_progress("❌ DNS Cache Flush: FAILED")
                    return False
        except Exception as e:
            self.update_progress(f"❌ DNS Cache Flush: ERROR - {str(e)}")
            return False
    
    def renew_ip(self):
        """Renew IP address"""
        try:
            if platform.system() == "Windows":
                # Release IP
                subprocess.run(['ipconfig', '/release'], capture_output=True, text=True)
                # Renew IP
                result = subprocess.run(['ipconfig', '/renew'], capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_progress("✅ IP Address Renewal: SUCCESS")
                    return True
                else:
                    self.update_progress("❌ IP Address Renewal: FAILED")
                    return False
        except Exception as e:
            self.update_progress(f"❌ IP Address Renewal: ERROR - {str(e)}")
            return False
    
    def reset_winsock(self):
        """Reset Winsock"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['netsh', 'winsock', 'reset'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_progress("✅ Winsock Reset: SUCCESS")
                    return True
                else:
                    self.update_progress("❌ Winsock Reset: FAILED")
                    return False
        except Exception as e:
            self.update_progress(f"❌ Winsock Reset: ERROR - {str(e)}")
            return False
    
    def repair_completed(self, repairs_done):
        """Handle repair completion"""
        if repairs_done:
            success_msg = f"✅ ترمیم کامل شد / Repair completed!\nاقدامات انجام شده:\n"
            for repair in repairs_done:
                success_msg += f"• {repair}\n"
            self.update_progress(success_msg)
            self.status_label.configure(text="🟢 ترمیم شد / Repaired", fg='#10b981')
            
            messagebox.showinfo("ترمیم کامل شد", 
                               "⚠️ توصیه می‌شود سیستم را مجدداً راه‌اندازی کنید")
        else:
            self.update_progress("⚠️ هیچ ترمیمی انجام نشد / No repairs were applied")
        
        self.repair_btn.configure(state='normal')
    
    def repair_error(self, error):
        """Handle repair error"""
        self.update_progress(f"❌ خطا در ترمیم / Repair error: {error}")
        self.status_label.configure(text="🔴 خطای ترمیم / Repair Error", fg='#ef4444')
        self.repair_btn.configure(state='normal')
    
    def generate_report(self, has_internet):
        """Generate diagnostic report"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        self.current_report = f"""
========================================================
    PCPasokh Internet Repair - گزارش عیب یابی اینترنت
========================================================
شناسه سیستم / System ID: {self.system_id}
تاریخ و زمان / Date & Time: {timestamp}
نام رایانه / Computer: {platform.node()}
سیستم عامل / OS: {platform.system()} {platform.release()}

وضعیت نهایی / Final Status: {'Connected' if has_internet else 'Disconnected'}

نتایج تست‌ها / Test Results:
{self.results_text.get('1.0', 'end')}

========================================================
پایان گزارش / End of Report
========================================================
        """
    
    def save_report(self):
        """Save diagnostic report"""
        if not self.current_report:
            messagebox.showwarning("هشدار", "گزارشی برای ذخیره وجود ندارد")
            return
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialvalue=f"PCPasokh_Report_{self.system_id}_{timestamp}.txt"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.current_report)
                messagebox.showinfo("موفقیت", f"گزارش ذخیره شد:\n{filename}")
                self.update_progress(f"💾 گزارش ذخیره شد: {filename}")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در ذخیره گزارش:\n{str(e)}")
    
    def reset_app(self):
        """Reset application"""
        self.results_text.delete('1.0', 'end')
        self.progress_label.configure(text="آماده برای شروع عیب یابی...")
        self.status_label.configure(text="🔴 آماده / Ready", fg='#ef4444')
        
        self.start_btn.configure(state='normal')
        self.repair_btn.configure(state='disabled')
        self.save_btn.configure(state='disabled')
        
        self.current_report = ""
        self.update_progress("🔄 برنامه بازنشانی شد / Application reset")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = SimpleNetworkRepair()
        app.run()
    except Exception as e:
        print(f"Application error: {e}")
        input("Press Enter to exit...")