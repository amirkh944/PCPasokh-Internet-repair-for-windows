import customtkinter as ctk
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import threading
import os
from datetime import datetime
from network_diagnostics import NetworkDiagnostics
from email_sender import EmailSender

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NetworkTroubleshooterApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Network Troubleshooter - عیب یاب اتصال اینترنت")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Initialize components
        self.diagnostics = None
        self.email_sender = EmailSender()
        self.current_report = ""
        self.report_file_path = ""
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main title
        title_label = ctk.CTkLabel(
            self.root, 
            text="🌐 Network Troubleshooter",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(20, 10))
        
        subtitle_label = ctk.CTkLabel(
            self.root,
            text="عیب یاب و رفع کننده مشکلات اتصال اینترنت",
            font=ctk.CTkFont(size=16)
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Main frame
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Control buttons frame
        controls_frame = ctk.CTkFrame(main_frame)
        controls_frame.pack(fill="x", padx=20, pady=20)
        
        # Start diagnosis button
        self.start_btn = ctk.CTkButton(
            controls_frame,
            text="🔍 Start Diagnosis / شروع عیب یابی",
            command=self.start_diagnosis,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#2B8065",
            hover_color="#1F5F4A"
        )
        self.start_btn.pack(side="left", padx=(0, 10), fill="x", expand=True)
        
        # Email config button
        email_btn = ctk.CTkButton(
            controls_frame,
            text="📧 Email Config",
            command=self.open_email_config,
            height=50,
            font=ctk.CTkFont(size=14),
            fg_color="#1F538D",
            hover_color="#14396A"
        )
        email_btn.pack(side="left", padx=(0, 10))
        
        # Save report button
        self.save_btn = ctk.CTkButton(
            controls_frame,
            text="💾 Save Report",
            command=self.save_report,
            height=50,
            font=ctk.CTkFont(size=14),
            fg_color="#B7472A",
            hover_color="#8B3A21",
            state="disabled"
        )
        self.save_btn.pack(side="left")
        
        # Progress frame
        progress_frame = ctk.CTkFrame(main_frame)
        progress_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="Ready to start diagnosis...",
            font=ctk.CTkFont(size=14)
        )
        self.progress_label.pack(pady=10)
        
        self.progress_bar = ctk.CTkProgressBar(progress_frame)
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 10))
        self.progress_bar.set(0)
        
        # Results frame
        results_frame = ctk.CTkFrame(main_frame)
        results_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        results_label = ctk.CTkLabel(
            results_frame,
            text="📋 Diagnostic Results / نتایج عیب یابی",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        results_label.pack(pady=(15, 10))
        
        # Text area for results
        self.results_text = ctk.CTkTextbox(
            results_frame,
            height=300,
            font=ctk.CTkFont(family="Consolas", size=12)
        )
        self.results_text.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Status frame
        status_frame = ctk.CTkFrame(main_frame)
        status_frame.pack(fill="x", padx=20)
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="🔴 Status: Ready",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.status_label.pack(pady=10)
    
    def update_progress(self, message):
        """Update progress display"""
        self.progress_label.configure(text=message)
        self.results_text.insert("end", f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.results_text.see("end")
        self.root.update()
    
    def start_diagnosis(self):
        """Start network diagnosis in a separate thread"""
        self.start_btn.configure(state="disabled")
        self.save_btn.configure(state="disabled")
        self.results_text.delete("1.0", "end")
        self.progress_bar.set(0)
        self.update_progress("Initializing diagnosis...")
        
        # Start diagnosis in thread
        diagnosis_thread = threading.Thread(target=self.run_diagnosis)
        diagnosis_thread.daemon = True
        diagnosis_thread.start()
    
    def run_diagnosis(self):
        """Run the actual diagnosis"""
        try:
            self.diagnostics = NetworkDiagnostics(callback=self.update_progress)
            
            # Simulate progress
            for i in range(10):
                self.progress_bar.set(i / 10)
                self.root.update()
            
            # Run diagnosis
            results = self.diagnostics.run_full_diagnosis()
            
            # Generate report
            self.current_report = self.diagnostics.generate_report()
            
            # Update UI
            self.root.after(0, self.diagnosis_completed, results)
            
        except Exception as e:
            self.root.after(0, self.diagnosis_error, str(e))
    
    def diagnosis_completed(self, results):
        """Handle diagnosis completion"""
        self.progress_bar.set(1.0)
        self.results_text.insert("end", "\n" + "="*50 + "\n")
        self.results_text.insert("end", self.current_report)
        self.results_text.see("end")
        
        # Update status
        if results['final_status'] == 'Connected':
            self.status_label.configure(text="🟢 Status: Internet Connected")
            self.update_progress("✅ Diagnosis completed - Internet is working!")
            
            # Try to send email if configured
            self.try_send_email()
        else:
            self.status_label.configure(text="🔴 Status: Internet Issues Detected")
            self.update_progress("❌ Diagnosis completed - Issues found!")
        
        # Re-enable buttons
        self.start_btn.configure(state="normal")
        self.save_btn.configure(state="normal")
    
    def diagnosis_error(self, error):
        """Handle diagnosis error"""
        self.update_progress(f"❌ Error during diagnosis: {error}")
        self.status_label.configure(text="🟡 Status: Diagnosis Error")
        self.start_btn.configure(state="normal")
    
    def try_send_email(self):
        """Try to send email report if configured"""
        try:
            # Save report first
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            self.report_file_path = f"network_report_{timestamp}.txt"
            
            with open(self.report_file_path, 'w', encoding='utf-8') as f:
                f.write(self.current_report)
            
            # Try to send email
            success, message = self.email_sender.send_report(self.current_report, self.report_file_path)
            
            if success:
                self.update_progress("📧 Report sent via email successfully!")
            else:
                self.update_progress(f"📧 Email sending failed: {message}")
                
        except Exception as e:
            self.update_progress(f"📧 Email error: {str(e)}")
    
    def save_report(self):
        """Save report to file"""
        if not self.current_report:
            messagebox.showwarning("Warning", "No report available to save!")
            return
        
        # Ask user for file location
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Save Network Report"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.current_report)
                
                messagebox.showinfo("Success", f"Report saved to:\n{filename}")
                self.update_progress(f"💾 Report saved to: {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save report:\n{str(e)}")
    
    def open_email_config(self):
        """Open email configuration window"""
        EmailConfigWindow(self.root, self.email_sender)
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

class EmailConfigWindow:
    def __init__(self, parent, email_sender):
        self.email_sender = email_sender
        
        # Create window
        self.window = ctk.CTkToplevel(parent)
        self.window.title("Email Configuration")
        self.window.geometry("500x400")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
        self.load_current_config()
    
    def setup_ui(self):
        """Setup email config UI"""
        # Title
        title_label = ctk.CTkLabel(
            self.window,
            text="📧 Email Configuration",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.pack(pady=20)
        
        # Form frame
        form_frame = ctk.CTkFrame(self.window)
        form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # SMTP Server
        ctk.CTkLabel(form_frame, text="SMTP Server:").pack(pady=(20, 5))
        self.smtp_server_entry = ctk.CTkEntry(form_frame, width=300)
        self.smtp_server_entry.pack(pady=(0, 10))
        
        # SMTP Port
        ctk.CTkLabel(form_frame, text="SMTP Port:").pack(pady=(0, 5))
        self.smtp_port_entry = ctk.CTkEntry(form_frame, width=300)
        self.smtp_port_entry.pack(pady=(0, 10))
        
        # Email
        ctk.CTkLabel(form_frame, text="Your Email:").pack(pady=(0, 5))
        self.email_entry = ctk.CTkEntry(form_frame, width=300)
        self.email_entry.pack(pady=(0, 10))
        
        # Password
        ctk.CTkLabel(form_frame, text="Password:").pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(form_frame, width=300, show="*")
        self.password_entry.pack(pady=(0, 10))
        
        # Recipient
        ctk.CTkLabel(form_frame, text="Recipient Email:").pack(pady=(0, 5))
        self.recipient_entry = ctk.CTkEntry(form_frame, width=300)
        self.recipient_entry.pack(pady=(0, 10))
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(self.window)
        buttons_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Test button
        test_btn = ctk.CTkButton(
            buttons_frame,
            text="Test Connection",
            command=self.test_connection,
            fg_color="#B7472A",
            hover_color="#8B3A21"
        )
        test_btn.pack(side="left", padx=(20, 10), pady=20)
        
        # Save button
        save_btn = ctk.CTkButton(
            buttons_frame,
            text="Save Configuration",
            command=self.save_config,
            fg_color="#2B8065",
            hover_color="#1F5F4A"
        )
        save_btn.pack(side="left", padx=(0, 10), pady=20)
        
        # Cancel button
        cancel_btn = ctk.CTkButton(
            buttons_frame,
            text="Cancel",
            command=self.window.destroy,
            fg_color="#666666",
            hover_color="#555555"
        )
        cancel_btn.pack(side="right", padx=(0, 20), pady=20)
    
    def load_current_config(self):
        """Load current email configuration"""
        config = self.email_sender.config
        self.smtp_server_entry.insert(0, config.get("smtp_server", ""))
        self.smtp_port_entry.insert(0, str(config.get("smtp_port", "")))
        self.email_entry.insert(0, config.get("email", ""))
        self.password_entry.insert(0, config.get("password", ""))
        self.recipient_entry.insert(0, config.get("recipient", ""))
    
    def test_connection(self):
        """Test email connection"""
        # Update config temporarily
        self.email_sender.update_config(
            self.smtp_server_entry.get(),
            int(self.smtp_port_entry.get()) if self.smtp_port_entry.get().isdigit() else 587,
            self.email_entry.get(),
            self.password_entry.get(),
            self.recipient_entry.get()
        )
        
        success, message = self.email_sender.test_connection()
        
        if success:
            messagebox.showinfo("Success", "Email connection successful!")
        else:
            messagebox.showerror("Error", f"Connection failed:\n{message}")
    
    def save_config(self):
        """Save email configuration"""
        try:
            port = int(self.smtp_port_entry.get()) if self.smtp_port_entry.get().isdigit() else 587
            
            self.email_sender.update_config(
                self.smtp_server_entry.get(),
                port,
                self.email_entry.get(),
                self.password_entry.get(),
                self.recipient_entry.get()
            )
            
            messagebox.showinfo("Success", "Email configuration saved!")
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration:\n{str(e)}")

if __name__ == "__main__":
    try:
        app = NetworkTroubleshooterApp()
        app.run()
    except Exception as e:
        print(f"Application error: {e}")
        input("Press Enter to exit...")