import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import threading
import os
from datetime import datetime
from network_diagnostics import NetworkDiagnostics
from ftp_uploader import FTPUploader
from system_info import SystemInfoCollector
import webbrowser

# Configure appearance and fix Persian text display
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PCPasokhInternetRepair:
    def __init__(self):
        self.root = ctk.CTk()
        self.setup_window()
        
        # Initialize components
        self.diagnostics = None
        self.ftp_uploader = FTPUploader()
        self.system_info = SystemInfoCollector()
        self.current_report = ""
        self.last_diagnosis_results = None
        
        # Persian text fix - Use a font that supports Persian
        self.persian_font = ("Tahoma", 11)
        self.persian_font_large = ("Tahoma", 16, "bold")
        self.persian_font_small = ("Tahoma", 9)
        
        self.setup_ui()
        
    def setup_window(self):
        """Configure main window"""
        self.root.title("PCPasokh Internet Repair - عیب یاب و ترمیم اینترنت پاسخگو رایانه")
        self.root.geometry("1100x800")
        self.root.resizable(True, True)
        
        # Set window icon (if available)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
    
    def setup_ui(self):
        """Setup the modern user interface"""
        # Header Section with Logo and Title
        self.create_header()
        
        # Main Content Area
        main_container = ctk.CTkFrame(self.root)
        main_container.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Left Panel - Controls
        left_panel = ctk.CTkFrame(main_container, width=300)
        left_panel.pack(side="left", fill="y", padx=(20, 10), pady=20)
        left_panel.pack_propagate(False)
        
        # Right Panel - Results
        right_panel = ctk.CTkFrame(main_container)
        right_panel.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)
        
        self.setup_left_panel(left_panel)
        self.setup_right_panel(right_panel)
        
        # Footer
        self.create_footer()
    
    def create_header(self):
        """Create header with logo and title"""
        header_frame = ctk.CTkFrame(self.root, height=120, corner_radius=15)
        header_frame.pack(fill="x", padx=20, pady=20)
        header_frame.pack_propagate(False)
        
        # Logo section (placeholder - you can add actual logo image)
        logo_frame = ctk.CTkFrame(header_frame, width=100, height=80, 
                                 fg_color="#1e3a8a", corner_radius=10)
        logo_frame.pack(side="left", padx=20, pady=20)
        logo_frame.pack_propagate(False)
        
        logo_label = ctk.CTkLabel(logo_frame, text="🌐\nPC", 
                                 font=("Arial", 16, "bold"), 
                                 text_color="white")
        logo_label.pack(expand=True)
        
        # Title section
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        # English title
        english_title = ctk.CTkLabel(title_frame, 
                                   text="PCPasokh Internet Repair",
                                   font=("Arial", 24, "bold"),
                                   text_color="#2563eb")
        english_title.pack(anchor="w")
        
        # Persian title with proper text direction
        persian_title = ctk.CTkLabel(title_frame,
                                   text="عیب یاب و ترمیم اینترنت پاسخگو رایانه",
                                   font=self.persian_font_large,
                                   text_color="#059669")
        persian_title.pack(anchor="w", pady=(5, 0))
        
        # System ID display
        system_id_label = ctk.CTkLabel(title_frame,
                                     text=f"System ID: {self.system_info.system_id}",
                                     font=("Consolas", 12),
                                     text_color="#6b7280")
        system_id_label.pack(anchor="w", pady=(10, 0))
    
    def setup_left_panel(self, parent):
        """Setup left control panel"""
        # Panel title
        panel_title = ctk.CTkLabel(parent, text="کنترل پنل / Control Panel", 
                                  font=self.persian_font_large)
        panel_title.pack(pady=(20, 30))
        
        # Main action buttons
        self.start_button = ctk.CTkButton(
            parent,
            text="🔍 شروع عیب یابی\nStart Diagnosis",
            command=self.start_diagnosis,
            height=60,
            font=self.persian_font,
            fg_color="#059669",
            hover_color="#047857",
            corner_radius=12
        )
        self.start_button.pack(fill="x", padx=20, pady=(0, 15))
        
        self.repair_button = ctk.CTkButton(
            parent,
            text="🔧 ترمیم مشکلات\nRepair Issues",
            command=self.repair_issues,
            height=60,
            font=self.persian_font,
            fg_color="#dc2626",
            hover_color="#b91c1c",
            corner_radius=12,
            state="disabled"
        )
        self.repair_button.pack(fill="x", padx=20, pady=(0, 15))
        
        self.reset_button = ctk.CTkButton(
            parent,
            text="🔄 بازنشانی\nReset",
            command=self.reset_application,
            height=50,
            font=self.persian_font,
            fg_color="#7c3aed",
            hover_color="#6d28d9",
            corner_radius=12
        )
        self.reset_button.pack(fill="x", padx=20, pady=(0, 15))
        
        # Separator
        separator = ctk.CTkFrame(parent, height=2, fg_color="#374151")
        separator.pack(fill="x", padx=20, pady=20)
        
        # Report buttons
        report_label = ctk.CTkLabel(parent, text="گزارش‌ها / Reports", 
                                   font=self.persian_font)
        report_label.pack(pady=(0, 15))
        
        self.save_button = ctk.CTkButton(
            parent,
            text="💾 ذخیره گزارش\nSave Report",
            command=self.save_report,
            height=50,
            font=self.persian_font_small,
            fg_color="#1f2937",
            hover_color="#374151",
            corner_radius=10,
            state="disabled"
        )
        self.save_button.pack(fill="x", padx=20, pady=(0, 10))
        
        self.upload_button = ctk.CTkButton(
            parent,
            text="📤 ارسال گزارش\nSend to PCPasokh",
            command=self.upload_report,
            height=50,
            font=self.persian_font_small,
            fg_color="#ea580c",
            hover_color="#c2410c",
            corner_radius=10,
            state="disabled"
        )
        self.upload_button.pack(fill="x", padx=20, pady=(0, 15))
        
        # System info button
        system_info_button = ctk.CTkButton(
            parent,
            text="📊 اطلاعات سیستم\nSystem Info",
            command=self.show_system_info,
            height=40,
            font=self.persian_font_small,
            fg_color="#6b7280",
            hover_color="#4b5563",
            corner_radius=10
        )
        system_info_button.pack(fill="x", padx=20, pady=(0, 10))
        
        # Settings button
        settings_button = ctk.CTkButton(
            parent,
            text="⚙️ تنظیمات\nSettings",
            command=self.open_settings,
            height=40,
            font=self.persian_font_small,
            fg_color="#6b7280",
            hover_color="#4b5563",
            corner_radius=10
        )
        settings_button.pack(fill="x", padx=20)
    
    def setup_right_panel(self, parent):
        """Setup right results panel"""
        # Status section
        status_frame = ctk.CTkFrame(parent, height=80)
        status_frame.pack(fill="x", padx=20, pady=(20, 10))
        status_frame.pack_propagate(False)
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="🔴 آماده / Ready",
            font=self.persian_font_large,
            text_color="#ef4444"
        )
        self.status_label.pack(pady=20)
        
        # Progress section
        progress_frame = ctk.CTkFrame(parent, height=100)
        progress_frame.pack(fill="x", padx=20, pady=(0, 10))
        progress_frame.pack_propagate(False)
        
        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="آماده برای شروع عیب یابی... / Ready to start diagnosis...",
            font=self.persian_font,
            wraplength=400
        )
        self.progress_label.pack(pady=(15, 5))
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame, width=400)
        self.progress_bar.pack(pady=(0, 15))
        self.progress_bar.set(0)
        
        # Results section
        results_frame = ctk.CTkFrame(parent)
        results_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        results_title = ctk.CTkLabel(
            results_frame,
            text="📋 نتایج عیب یابی / Diagnostic Results",
            font=self.persian_font_large
        )
        results_title.pack(pady=(20, 10))
        
        # Text area for results with custom scrollbar
        self.results_text = ctk.CTkTextbox(
            results_frame,
            height=300,
            font=("Consolas", 11),
            corner_radius=10,
            border_width=2
        )
        self.results_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
    
    def create_footer(self):
        """Create footer with contact information"""
        footer_frame = ctk.CTkFrame(self.root, height=80, corner_radius=10)
        footer_frame.pack(fill="x", padx=20, pady=(0, 20))
        footer_frame.pack_propagate(False)
        
        # Contact info
        contact_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
        contact_frame.pack(side="left", fill="both", expand=True, padx=20, pady=15)
        
        contact_title = ctk.CTkLabel(contact_frame,
                                   text="ارتباط با پاسخگو رایانه / Contact PCPasokh",
                                   font=self.persian_font)
        contact_title.pack(anchor="w")
        
        contact_info = ctk.CTkLabel(contact_frame,
                                  text="📞 021-88888888 | 📧 support@pcpasokh.ir | 🌐 www.pcpasokh.ir",
                                  font=("Arial", 10),
                                  text_color="#6b7280")
        contact_info.pack(anchor="w", pady=(5, 0))
        
        # Website button
        website_button = ctk.CTkButton(
            footer_frame,
            text="🌐 وب‌سایت\nWebsite",
            command=lambda: webbrowser.open("https://www.pcpasokh.ir"),
            width=100,
            height=50,
            font=self.persian_font_small,
            fg_color="#1f2937",
            hover_color="#374151"
        )
        website_button.pack(side="right", padx=20, pady=15)
    
    def update_progress(self, message):
        """Update progress display with proper Persian text handling"""
        # Handle text direction for mixed Persian/English text
        if any(ord(char) > 127 for char in message):  # Contains non-ASCII (Persian) characters
            display_text = message
        else:
            display_text = message
        
        self.progress_label.configure(text=display_text)
        self.results_text.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.results_text.see("end")
        self.root.update()
    
    def start_diagnosis(self):
        """Start comprehensive network diagnosis"""
        self.start_button.configure(state="disabled")
        self.repair_button.configure(state="disabled")
        self.save_button.configure(state="disabled")
        self.upload_button.configure(state="disabled")
        
        self.results_text.delete("1.0", "end")
        self.progress_bar.set(0)
        self.status_label.configure(text="🟡 در حال عیب یابی / Diagnosing...", text_color="#f59e0b")
        
        # Start diagnosis in thread
        diagnosis_thread = threading.Thread(target=self.run_diagnosis)
        diagnosis_thread.daemon = True
        diagnosis_thread.start()
    
    def run_diagnosis(self):
        """Run comprehensive diagnosis"""
        try:
            self.diagnostics = NetworkDiagnostics(callback=self.update_progress)
            
            # Simulate progress updates
            for i in range(1, 11):
                self.progress_bar.set(i / 10)
                self.root.update()
                
            # Run comprehensive diagnosis
            self.last_diagnosis_results = self.diagnostics.run_comprehensive_diagnosis()
            
            # Generate report
            self.current_report = self.diagnostics.generate_report()
            
            # Update UI on main thread
            self.root.after(0, self.diagnosis_completed)
            
        except Exception as e:
            self.root.after(0, self.diagnosis_error, str(e))
    
    def diagnosis_completed(self):
        """Handle diagnosis completion"""
        self.progress_bar.set(1.0)
        self.results_text.insert("end", "\n" + "="*60 + "\n")
        self.results_text.insert("end", self.current_report)
        self.results_text.see("end")
        
        # Update status based on results
        if self.last_diagnosis_results and self.last_diagnosis_results['final_status'] == 'Connected':
            self.status_label.configure(text="🟢 متصل / Connected", text_color="#10b981")
            self.repair_button.configure(state="disabled")
        else:
            self.status_label.configure(text="🔴 مشکل شناسایی شد / Issues Detected", text_color="#ef4444")
            self.repair_button.configure(state="normal")
        
        # Enable buttons
        self.start_button.configure(state="normal")
        self.save_button.configure(state="normal")
        self.upload_button.configure(state="normal")
        
        self.update_progress("✅ عیب یابی کامل شد / Diagnosis completed!")
    
    def diagnosis_error(self, error):
        """Handle diagnosis error"""
        self.update_progress(f"❌ خطا در عیب یابی / Diagnosis error: {error}")
        self.status_label.configure(text="🟡 خطا / Error", text_color="#f59e0b")
        self.start_button.configure(state="normal")
    
    def repair_issues(self):
        """Repair network issues"""
        if not self.diagnostics:
            messagebox.showwarning("هشدار / Warning", 
                                 "ابتدا عیب یابی را انجام دهید\nPlease run diagnosis first")
            return
        
        self.repair_button.configure(state="disabled")
        self.status_label.configure(text="🔧 در حال ترمیم / Repairing...", text_color="#f59e0b")
        
        # Run repair in thread
        repair_thread = threading.Thread(target=self.run_repair)
        repair_thread.daemon = True
        repair_thread.start()
    
    def run_repair(self):
        """Run network repair operations"""
        try:
            repair_results = self.diagnostics.repair_network_issues()
            
            # Update UI on main thread
            self.root.after(0, self.repair_completed, repair_results)
            
        except Exception as e:
            self.root.after(0, self.repair_error, str(e))
    
    def repair_completed(self, repair_results):
        """Handle repair completion"""
        if repair_results:
            success_msg = f"✅ ترمیم کامل شد / Repair completed!\nاقدامات انجام شده / Actions taken:\n"
            for repair in repair_results:
                success_msg += f"• {repair}\n"
            
            self.update_progress(success_msg)
            self.status_label.configure(text="🟢 ترمیم شد / Repaired", text_color="#10b981")
            
            # Show restart recommendation
            restart_msg = ("⚠️ توصیه می‌شود سیستم را مجدداً راه‌اندازی کنید\n"
                          "It is recommended to restart your system")
            messagebox.showinfo("ترمیم کامل شد / Repair Complete", restart_msg)
        else:
            self.update_progress("⚠️ هیچ ترمیمی انجام نشد / No repairs were applied")
        
        self.repair_button.configure(state="normal")
        
        # Regenerate report with repair results
        if self.diagnostics:
            self.current_report = self.diagnostics.generate_report()
    
    def repair_error(self, error):
        """Handle repair error"""
        self.update_progress(f"❌ خطا در ترمیم / Repair error: {error}")
        self.status_label.configure(text="🔴 خطای ترمیم / Repair Error", text_color="#ef4444")
        self.repair_button.configure(state="normal")
    
    def reset_application(self):
        """Reset application state"""
        self.results_text.delete("1.0", "end")
        self.progress_bar.set(0)
        self.progress_label.configure(text="آماده برای شروع عیب یابی... / Ready to start diagnosis...")
        self.status_label.configure(text="🔴 آماده / Ready", text_color="#ef4444")
        
        # Reset buttons
        self.start_button.configure(state="normal")
        self.repair_button.configure(state="disabled")
        self.save_button.configure(state="disabled")
        self.upload_button.configure(state="disabled")
        
        # Clear data
        self.current_report = ""
        self.last_diagnosis_results = None
        self.diagnostics = None
        
        self.update_progress("🔄 برنامه بازنشانی شد / Application reset")
    
    def save_report(self):
        """Save diagnostic report to file"""
        if not self.current_report:
            messagebox.showwarning("هشدار / Warning", 
                                 "گزارشی برای ذخیره وجود ندارد\nNo report available to save")
            return
        
        # Generate filename with system ID and timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        default_filename = f"PCPasokh_Report_{self.system_info.system_id}_{timestamp}.txt"
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="ذخیره گزارش / Save Report",
            initialvalue=default_filename
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.current_report)
                
                success_msg = f"✅ گزارش ذخیره شد / Report saved:\n{filename}"
                messagebox.showinfo("موفقیت / Success", success_msg)
                self.update_progress(f"💾 گزارش ذخیره شد / Report saved to: {filename}")
                
            except Exception as e:
                error_msg = f"❌ خطا در ذخیره / Save error:\n{str(e)}"
                messagebox.showerror("خطا / Error", error_msg)
    
    def upload_report(self):
        """Upload report to PCPasokh server via FTP"""
        if not self.current_report:
            messagebox.showwarning("هشدار / Warning", 
                                 "گزارشی برای ارسال وجود ندارد\nNo report available to upload")
            return
        
        self.upload_button.configure(state="disabled")
        self.update_progress("📤 در حال ارسال گزارش به سرور پاسخگو رایانه...")
        
        # Upload in thread to prevent UI freeze
        upload_thread = threading.Thread(target=self.run_upload)
        upload_thread.daemon = True
        upload_thread.start()
    
    def run_upload(self):
        """Run FTP upload"""
        try:
            success, message, filename = self.ftp_uploader.upload_report(
                self.current_report, 
                self.system_info.system_id,
                "diagnostic"
            )
            
            self.root.after(0, self.upload_completed, success, message, filename)
            
        except Exception as e:
            self.root.after(0, self.upload_error, str(e))
    
    def upload_completed(self, success, message, filename):
        """Handle upload completion"""
        if success:
            success_msg = f"✅ {message}"
            messagebox.showinfo("ارسال موفق / Upload Successful", success_msg)
            self.update_progress(f"📤 {message}")
        else:
            error_msg = f"❌ {message}"
            messagebox.showerror("خطای ارسال / Upload Error", error_msg)
            self.update_progress(f"📤 خطا در ارسال / Upload error: {message}")
        
        self.upload_button.configure(state="normal")
    
    def upload_error(self, error):
        """Handle upload error"""
        error_msg = f"❌ خطا در ارسال / Upload error: {error}"
        messagebox.showerror("خطا / Error", error_msg)
        self.update_progress(error_msg)
        self.upload_button.configure(state="normal")
    
    def show_system_info(self):
        """Show detailed system information"""
        SystemInfoWindow(self.root, self.system_info)
    
    def open_settings(self):
        """Open settings window"""
        SettingsWindow(self.root, self.ftp_uploader)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

class SystemInfoWindow:
    def __init__(self, parent, system_info):
        self.system_info = system_info
        
        # Create window
        self.window = ctk.CTkToplevel(parent)
        self.window.title("System Information - اطلاعات سیستم")
        self.window.geometry("700x600")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
        self.load_system_info()
    
    def setup_ui(self):
        """Setup system info UI"""
        title_label = ctk.CTkLabel(
            self.window,
            text="📊 System Information - اطلاعات سیستم",
            font=("Tahoma", 18, "bold")
        )
        title_label.pack(pady=20)
        
        # Info text area
        self.info_text = ctk.CTkTextbox(
            self.window,
            font=("Consolas", 10)
        )
        self.info_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Buttons
        button_frame = ctk.CTkFrame(self.window)
        button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        refresh_btn = ctk.CTkButton(
            button_frame,
            text="🔄 Refresh",
            command=self.load_system_info,
            width=100
        )
        refresh_btn.pack(side="left", padx=20, pady=20)
        
        save_btn = ctk.CTkButton(
            button_frame,
            text="💾 Save Info",
            command=self.save_system_info,
            width=100
        )
        save_btn.pack(side="left", padx=(0, 20), pady=20)
        
        close_btn = ctk.CTkButton(
            button_frame,
            text="❌ Close",
            command=self.window.destroy,
            width=100,
            fg_color="#666666"
        )
        close_btn.pack(side="right", padx=20, pady=20)
    
    def load_system_info(self):
        """Load and display system information"""
        self.info_text.delete("1.0", "end")
        
        try:
            info = self.system_info.collect_all_info()
            
            # Format and display information
            info_text = f"""
System ID: {info['system_id']}
Timestamp: {info['timestamp']}
User: {info['user']}
Computer Name: {info['computer_name']}

Operating System:
- Name: {info['os']['name']}
- Version: {info['os']['version']}
- Architecture: {info['os']['architecture']}

Hardware:
- CPU: {info['hardware'].get('cpu', {}).get('name', 'Unknown')}
- Cores: {info['hardware'].get('cpu', {}).get('cores', 'Unknown')} physical, {info['hardware'].get('cpu', {}).get('logical_cores', 'Unknown')} logical
- Memory: {info['hardware'].get('memory', {}).get('total', 'Unknown')}

Network Interfaces:
"""
            
            for interface in info['network'].get('interfaces', []):
                info_text += f"- {interface['name']}:\n"
                for addr in interface['addresses']:
                    info_text += f"  {addr['type']}: {addr['address']}\n"
            
            if info.get('installed_software'):
                info_text += "\nNetwork-related Software:\n"
                for software in info['installed_software']:
                    info_text += f"- {software}\n"
            
            self.info_text.insert("1.0", info_text)
            
        except Exception as e:
            self.info_text.insert("1.0", f"Error loading system information: {str(e)}")
    
    def save_system_info(self):
        """Save system information to file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")],
            title="Save System Information"
        )
        
        if filename:
            try:
                success, message = self.system_info.save_system_info(filename)
                if success:
                    messagebox.showinfo("Success", message)
                else:
                    messagebox.showerror("Error", message)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")

class SettingsWindow:
    def __init__(self, parent, ftp_uploader):
        self.ftp_uploader = ftp_uploader
        
        # Create window
        self.window = ctk.CTkToplevel(parent)
        self.window.title("Settings - تنظیمات")
        self.window.geometry("600x500")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
        self.load_current_config()
    
    def setup_ui(self):
        """Setup settings UI"""
        title_label = ctk.CTkLabel(
            self.window,
            text="⚙️ Settings - تنظیمات FTP سرور پاسخگو رایانه",
            font=("Tahoma", 16, "bold")
        )
        title_label.pack(pady=20)
        
        # Form frame
        form_frame = ctk.CTkFrame(self.window)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # FTP Server settings
        ctk.CTkLabel(form_frame, text="آدرس سرور / FTP Server:", font=("Tahoma", 12)).pack(pady=(20, 5))
        self.host_entry = ctk.CTkEntry(form_frame, width=400, placeholder_text="ftp.pcpasokh.ir")
        self.host_entry.pack(pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="پورت / Port:", font=("Tahoma", 12)).pack(pady=(0, 5))
        self.port_entry = ctk.CTkEntry(form_frame, width=400, placeholder_text="21")
        self.port_entry.pack(pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="نام کاربری / Username:", font=("Tahoma", 12)).pack(pady=(0, 5))
        self.username_entry = ctk.CTkEntry(form_frame, width=400, placeholder_text="reports_user")
        self.username_entry.pack(pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="رمز عبور / Password:", font=("Tahoma", 12)).pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(form_frame, width=400, show="*", placeholder_text="Password")
        self.password_entry.pack(pady=(0, 10))
        
        ctk.CTkLabel(form_frame, text="پوشه گزارشات / Reports Directory:", font=("Tahoma", 12)).pack(pady=(0, 5))
        self.directory_entry = ctk.CTkEntry(form_frame, width=400, placeholder_text="/network_reports/")
        self.directory_entry.pack(pady=(0, 20))
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(self.window)
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        test_btn = ctk.CTkButton(
            buttons_frame,
            text="🔍 Test Connection",
            command=self.test_connection,
            fg_color="#dc2626",
            hover_color="#b91c1c"
        )
        test_btn.pack(side="left", padx=20, pady=20)
        
        save_btn = ctk.CTkButton(
            buttons_frame,
            text="💾 Save Settings",
            command=self.save_settings,
            fg_color="#059669",
            hover_color="#047857"
        )
        save_btn.pack(side="left", padx=(0, 20), pady=20)
        
        cancel_btn = ctk.CTkButton(
            buttons_frame,
            text="❌ Cancel",
            command=self.window.destroy,
            fg_color="#6b7280",
            hover_color="#4b5563"
        )
        cancel_btn.pack(side="right", padx=20, pady=20)
    
    def load_current_config(self):
        """Load current FTP configuration"""
        config = self.ftp_uploader.ftp_config
        self.host_entry.insert(0, config.get("host", ""))
        self.port_entry.insert(0, str(config.get("port", "")))
        self.username_entry.insert(0, config.get("username", ""))
        self.password_entry.insert(0, config.get("password", ""))
        self.directory_entry.insert(0, config.get("remote_directory", ""))
    
    def test_connection(self):
        """Test FTP connection"""
        # Update config temporarily
        self.ftp_uploader.update_config(
            self.host_entry.get(),
            int(self.port_entry.get()) if self.port_entry.get().isdigit() else 21,
            self.username_entry.get(),
            self.password_entry.get(),
            self.directory_entry.get()
        )
        
        success, message = self.ftp_uploader.test_connection()
        
        if success:
            messagebox.showinfo("✅ موفقیت / Success", message)
        else:
            messagebox.showerror("❌ خطا / Error", message)
    
    def save_settings(self):
        """Save FTP settings"""
        try:
            port = int(self.port_entry.get()) if self.port_entry.get().isdigit() else 21
            
            self.ftp_uploader.update_config(
                self.host_entry.get(),
                port,
                self.username_entry.get(),
                self.password_entry.get(),
                self.directory_entry.get()
            )
            
            messagebox.showinfo("✅ موفقیت / Success", "تنظیمات ذخیره شد / Settings saved!")
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("❌ خطا / Error", f"خطا در ذخیره / Save error:\n{str(e)}")

if __name__ == "__main__":
    try:
        app = PCPasokhInternetRepair()
        app.run()
    except Exception as e:
        print(f"Application error: {e}")
        input("Press Enter to exit...")