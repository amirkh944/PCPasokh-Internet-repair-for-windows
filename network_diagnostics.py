import socket
import subprocess
import platform
import requests
import psutil
from ping3 import ping
import speedtest
import time
import json
from datetime import datetime

class NetworkDiagnostics:
    def __init__(self, callback=None):
        self.callback = callback
        self.results = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tests': [],
            'fixes_applied': [],
            'final_status': 'Unknown'
        }
    
    def log_result(self, test_name, status, details="", fix_applied=None):
        """Log test results"""
        result = {
            'test': test_name,
            'status': status,
            'details': details,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }
        self.results['tests'].append(result)
        
        if fix_applied:
            self.results['fixes_applied'].append(fix_applied)
        
        if self.callback:
            self.callback(f"{test_name}: {status}")
    
    def test_basic_connectivity(self):
        """Test basic internet connectivity"""
        try:
            # Test DNS resolution
            socket.gethostbyname('google.com')
            self.log_result("DNS Resolution", "✅ PASS", "Successfully resolved google.com")
            
            # Test HTTP connectivity
            response = requests.get('http://www.google.com', timeout=10)
            if response.status_code == 200:
                self.log_result("HTTP Connectivity", "✅ PASS", f"Status code: {response.status_code}")
                return True
            else:
                self.log_result("HTTP Connectivity", "❌ FAIL", f"Status code: {response.status_code}")
                return False
                
        except socket.gaierror:
            self.log_result("DNS Resolution", "❌ FAIL", "DNS resolution failed")
            return False
        except requests.exceptions.RequestException as e:
            self.log_result("HTTP Connectivity", "❌ FAIL", f"Request failed: {str(e)}")
            return False
    
    def test_ping_connectivity(self):
        """Test ping connectivity to major servers"""
        servers = [
            ('Google DNS', '8.8.8.8'),
            ('Cloudflare DNS', '1.1.1.1'),
            ('Google', 'google.com')
        ]
        
        ping_results = []
        for name, host in servers:
            try:
                result = ping(host, timeout=5)
                if result:
                    ping_results.append(f"{name}: {result*1000:.2f}ms")
                    self.log_result(f"Ping {name}", "✅ PASS", f"Response time: {result*1000:.2f}ms")
                else:
                    ping_results.append(f"{name}: Timeout")
                    self.log_result(f"Ping {name}", "❌ FAIL", "Request timeout")
            except Exception as e:
                ping_results.append(f"{name}: Error")
                self.log_result(f"Ping {name}", "❌ FAIL", f"Error: {str(e)}")
        
        return ping_results
    
    def test_speed(self):
        """Test internet speed"""
        try:
            if self.callback:
                self.callback("Testing internet speed...")
            
            st = speedtest.Speedtest()
            st.download()
            st.upload()
            results = st.results.dict()
            
            download_speed = results['download'] / 1000000  # Convert to Mbps
            upload_speed = results['upload'] / 1000000
            ping_ms = results['ping']
            
            speed_info = f"Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps, Ping: {ping_ms:.2f} ms"
            self.log_result("Speed Test", "✅ PASS", speed_info)
            
            return {
                'download': download_speed,
                'upload': upload_speed,
                'ping': ping_ms
            }
        except Exception as e:
            self.log_result("Speed Test", "❌ FAIL", f"Error: {str(e)}")
            return None
    
    def check_network_adapters(self):
        """Check network adapter status"""
        adapters = psutil.net_if_stats()
        active_adapters = []
        
        for adapter, stats in adapters.items():
            if stats.isup:
                active_adapters.append(adapter)
                self.log_result(f"Network Adapter {adapter}", "✅ ACTIVE", "Adapter is up and running")
            else:
                self.log_result(f"Network Adapter {adapter}", "❌ INACTIVE", "Adapter is down")
        
        return active_adapters
    
    def flush_dns(self):
        """Flush DNS cache"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['ipconfig', '/flushdns'], 
                                      capture_output=True, text=True, check=True)
                self.log_result("DNS Flush", "✅ SUCCESS", "DNS cache flushed successfully")
                self.results['fixes_applied'].append("DNS cache flushed")
                return True
            else:
                self.log_result("DNS Flush", "⚠️ SKIP", "Not supported on this OS")
                return False
        except subprocess.CalledProcessError as e:
            self.log_result("DNS Flush", "❌ FAIL", f"Error: {str(e)}")
            return False
    
    def reset_network_stack(self):
        """Reset network stack (Windows only)"""
        try:
            if platform.system() == "Windows":
                commands = [
                    ['netsh', 'winsock', 'reset'],
                    ['netsh', 'int', 'ip', 'reset']
                ]
                
                for cmd in commands:
                    subprocess.run(cmd, capture_output=True, text=True, check=True)
                
                self.log_result("Network Stack Reset", "✅ SUCCESS", "Network stack reset completed")
                self.results['fixes_applied'].append("Network stack reset")
                return True
            else:
                self.log_result("Network Stack Reset", "⚠️ SKIP", "Not supported on this OS")
                return False
        except subprocess.CalledProcessError as e:
            self.log_result("Network Stack Reset", "❌ FAIL", f"Error: {str(e)}")
            return False
    
    def renew_ip_address(self):
        """Release and renew IP address"""
        try:
            if platform.system() == "Windows":
                # Release IP
                subprocess.run(['ipconfig', '/release'], 
                             capture_output=True, text=True, check=True)
                time.sleep(2)
                
                # Renew IP
                subprocess.run(['ipconfig', '/renew'], 
                             capture_output=True, text=True, check=True)
                
                self.log_result("IP Address Renewal", "✅ SUCCESS", "IP address renewed successfully")
                self.results['fixes_applied'].append("IP address renewed")
                return True
            else:
                self.log_result("IP Address Renewal", "⚠️ SKIP", "Not supported on this OS")
                return False
        except subprocess.CalledProcessError as e:
            self.log_result("IP Address Renewal", "❌ FAIL", f"Error: {str(e)}")
            return False
    
    def run_full_diagnosis(self):
        """Run complete network diagnosis"""
        if self.callback:
            self.callback("Starting network diagnosis...")
        
        # Test basic connectivity first
        has_internet = self.test_basic_connectivity()
        
        # Check network adapters
        self.check_network_adapters()
        
        # Test ping connectivity
        self.test_ping_connectivity()
        
        # If no internet, try fixes
        if not has_internet:
            if self.callback:
                self.callback("No internet detected. Attempting fixes...")
            
            # Try DNS flush
            self.flush_dns()
            time.sleep(2)
            
            # Test again
            has_internet = self.test_basic_connectivity()
            
            if not has_internet:
                # Try IP renewal
                self.renew_ip_address()
                time.sleep(5)
                
                # Test again
                has_internet = self.test_basic_connectivity()
            
            if not has_internet:
                # Try network stack reset as last resort
                self.reset_network_stack()
                if self.callback:
                    self.callback("Network stack reset completed. Please restart your computer.")
        
        # If we have internet, test speed
        if has_internet:
            self.test_speed()
            self.results['final_status'] = 'Connected'
        else:
            self.results['final_status'] = 'Disconnected'
        
        if self.callback:
            self.callback("Diagnosis completed!")
        
        return self.results
    
    def generate_report(self):
        """Generate a detailed text report"""
        report = []
        report.append("=" * 60)
        report.append("          NETWORK DIAGNOSTIC REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {self.results['timestamp']}")
        report.append(f"Final Status: {self.results['final_status']}")
        report.append("")
        
        report.append("DIAGNOSTIC TESTS:")
        report.append("-" * 30)
        for test in self.results['tests']:
            report.append(f"[{test['timestamp']}] {test['test']}: {test['status']}")
            if test['details']:
                report.append(f"    Details: {test['details']}")
        
        if self.results['fixes_applied']:
            report.append("")
            report.append("FIXES APPLIED:")
            report.append("-" * 30)
            for fix in self.results['fixes_applied']:
                report.append(f"✓ {fix}")
        
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)