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
from system_info import SystemInfoCollector

class NetworkDiagnostics:
    def __init__(self, callback=None):
        self.callback = callback
        self.system_info = SystemInfoCollector()
        self.results = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'system_id': self.system_info.system_id,
            'tests': [],
            'fixes_applied': [],
            'final_status': 'Unknown',
            'repair_recommendations': []
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
    
    def test_dns_servers(self):
        """Test multiple DNS servers"""
        dns_servers = [
            ('Shecan DNS', '178.22.122.100'),
            ('403 DNS', '10.202.10.202'),
            ('Google DNS', '8.8.8.8'),
            ('Cloudflare DNS', '1.1.1.1'),
            ('OpenDNS', '208.67.222.222')
        ]
        
        working_dns = []
        for name, dns_ip in dns_servers:
            try:
                # Test DNS resolution using specific DNS server
                import dns.resolver
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [dns_ip]
                resolver.timeout = 5
                
                result = resolver.resolve('google.com', 'A')
                if result:
                    working_dns.append(name)
                    self.log_result(f"DNS Test {name}", "✅ PASS", f"Server {dns_ip} working")
                else:
                    self.log_result(f"DNS Test {name}", "❌ FAIL", f"Server {dns_ip} not responding")
                    
            except Exception as e:
                self.log_result(f"DNS Test {name}", "❌ FAIL", f"Server {dns_ip} error: {str(e)}")
        
        return working_dns
    
    def test_proxy_settings(self):
        """Check for proxy configuration issues"""
        try:
            if platform.system() == "Windows":
                # Check Windows proxy settings
                result = subprocess.run(['reg', 'query', 
                                       'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings',
                                       '/v', 'ProxyEnable'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0 and '0x1' in result.stdout:
                    self.log_result("Proxy Check", "⚠️ WARNING", "Proxy is enabled - may affect connectivity")
                    self.results['repair_recommendations'].append("Check proxy settings in Internet Options")
                    return True
                else:
                    self.log_result("Proxy Check", "✅ PASS", "No proxy configured")
                    return False
                    
        except Exception as e:
            self.log_result("Proxy Check", "❌ FAIL", f"Error checking proxy: {str(e)}")
        
        return False
    
    def test_firewall_status(self):
        """Check Windows Firewall status"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    if 'State                                 ON' in result.stdout:
                        self.log_result("Firewall Check", "✅ ACTIVE", "Windows Firewall is enabled")
                        return True
                    else:
                        self.log_result("Firewall Check", "⚠️ WARNING", "Windows Firewall may be disabled")
                        self.results['repair_recommendations'].append("Enable Windows Firewall for security")
                        return False
                        
        except Exception as e:
            self.log_result("Firewall Check", "❌ FAIL", f"Error checking firewall: {str(e)}")
        
        return False
    
    def test_network_drivers(self):
        """Check network adapter drivers"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['wmic', 'path', 'win32_networkadapter', 'where', 
                                       'netconnectionstatus=2', 'get', 'name,driverversion'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.log_result("Network Drivers", "✅ PASS", "Network drivers information collected")
                    return result.stdout
                else:
                    self.log_result("Network Drivers", "❌ FAIL", "Could not retrieve driver information")
                    
        except Exception as e:
            self.log_result("Network Drivers", "❌ FAIL", f"Error checking drivers: {str(e)}")
        
        return None
    
    def repair_network_issues(self):
        """Comprehensive network repair function"""
        repair_success = []
        
        if self.callback:
            self.callback("🔧 شروع ترمیم مشکلات شبکه / Starting network repairs...")
        
        # 1. Reset TCP/IP Stack
        if self.reset_tcpip_stack():
            repair_success.append("TCP/IP Stack Reset")
        
        # 2. Flush DNS
        if self.flush_dns():
            repair_success.append("DNS Cache Flush")
        
        # 3. Reset Winsock
        if self.reset_winsock():
            repair_success.append("Winsock Reset")
        
        # 4. Renew IP Address
        if self.renew_ip_address():
            repair_success.append("IP Address Renewal")
        
        # 5. Reset Network Adapters
        if self.reset_network_adapters():
            repair_success.append("Network Adapters Reset")
        
        # 6. Clear ARP Cache
        if self.clear_arp_cache():
            repair_success.append("ARP Cache Clear")
        
        # 7. Reset Internet Explorer Settings (affects some network components)
        if self.reset_ie_settings():
            repair_success.append("Internet Explorer Settings Reset")
        
        return repair_success
    
    def reset_tcpip_stack(self):
        """Reset TCP/IP Stack"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['netsh', 'int', 'ip', 'reset'], 
                                      capture_output=True, text=True, check=True)
                self.log_result("TCP/IP Stack Reset", "✅ SUCCESS", "TCP/IP stack reset completed")
                self.results['fixes_applied'].append("TCP/IP stack reset")
                return True
        except subprocess.CalledProcessError as e:
            self.log_result("TCP/IP Stack Reset", "❌ FAIL", f"Error: {str(e)}")
        return False
    
    def reset_winsock(self):
        """Reset Winsock"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['netsh', 'winsock', 'reset'], 
                                      capture_output=True, text=True, check=True)
                self.log_result("Winsock Reset", "✅ SUCCESS", "Winsock reset completed")
                self.results['fixes_applied'].append("Winsock reset")
                return True
        except subprocess.CalledProcessError as e:
            self.log_result("Winsock Reset", "❌ FAIL", f"Error: {str(e)}")
        return False
    
    def reset_network_adapters(self):
        """Reset all network adapters"""
        try:
            if platform.system() == "Windows":
                # Disable and enable network adapters
                result1 = subprocess.run(['wmic', 'path', 'win32_networkadapter', 'where', 
                                        'netconnectionstatus=2', 'call', 'disable'], 
                                       capture_output=True, text=True)
                time.sleep(3)
                result2 = subprocess.run(['wmic', 'path', 'win32_networkadapter', 'where', 
                                        'netconnectionstatus=0', 'call', 'enable'], 
                                       capture_output=True, text=True)
                
                self.log_result("Network Adapters Reset", "✅ SUCCESS", "Network adapters reset completed")
                self.results['fixes_applied'].append("Network adapters reset")
                return True
        except Exception as e:
            self.log_result("Network Adapters Reset", "❌ FAIL", f"Error: {str(e)}")
        return False
    
    def clear_arp_cache(self):
        """Clear ARP cache"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['arp', '-d', '*'], 
                                      capture_output=True, text=True)
                self.log_result("ARP Cache Clear", "✅ SUCCESS", "ARP cache cleared")
                self.results['fixes_applied'].append("ARP cache cleared")
                return True
        except Exception as e:
            self.log_result("ARP Cache Clear", "❌ FAIL", f"Error: {str(e)}")
        return False
    
    def reset_ie_settings(self):
        """Reset Internet Explorer settings"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(['rundll32.exe', 'inetcpl.cpl,ClearMyTracksByProcess', '255'], 
                                      capture_output=True, text=True)
                self.log_result("IE Settings Reset", "✅ SUCCESS", "Internet Explorer settings reset")
                self.results['fixes_applied'].append("Internet Explorer settings reset")
                return True
        except Exception as e:
            self.log_result("IE Settings Reset", "❌ FAIL", f"Error: {str(e)}")
        return False
    
    def run_comprehensive_diagnosis(self):
        """Run comprehensive network diagnosis with all tests"""
        if self.callback:
            self.callback("🔍 شروع عیب یابی جامع شبکه / Starting comprehensive network diagnosis...")
        
        # Collect system information
        self.system_info.collect_all_info()
        
        # Test basic connectivity
        has_internet = self.test_basic_connectivity()
        
        # Test DNS servers
        working_dns = self.test_dns_servers()
        
        # Check network adapters
        self.check_network_adapters()
        
        # Test ping connectivity
        self.test_ping_connectivity()
        
        # Check proxy settings
        self.test_proxy_settings()
        
        # Check firewall status
        self.test_firewall_status()
        
        # Check network drivers
        self.test_network_drivers()
        
        # If we have internet, test speed
        if has_internet:
            self.test_speed()
            self.results['final_status'] = 'Connected'
        else:
            self.results['final_status'] = 'Disconnected'
            self.results['repair_recommendations'].append("Run network repair to fix connectivity issues")
        
        if self.callback:
            self.callback("✅ عیب یابی جامع تکمیل شد / Comprehensive diagnosis completed!")
        
        return self.results
    
    def generate_report(self):
        """Generate a detailed text report with system information"""
        # Get system info header
        header = self.system_info.generate_report_header()
        
        report = []
        report.append(header)
        
        report.append("نتایج عیب یابی شبکه / NETWORK DIAGNOSTIC RESULTS:")
        report.append("=" * 80)
        report.append(f"وضعیت نهایی / Final Status: {self.results['final_status']}")
        report.append("")
        
        report.append("تست‌های انجام شده / DIAGNOSTIC TESTS:")
        report.append("-" * 50)
        for test in self.results['tests']:
            report.append(f"[{test['timestamp']}] {test['test']}: {test['status']}")
            if test['details']:
                report.append(f"    جزئیات / Details: {test['details']}")
        
        if self.results['fixes_applied']:
            report.append("")
            report.append("اقدامات ترمیمی انجام شده / FIXES APPLIED:")
            report.append("-" * 50)
            for fix in self.results['fixes_applied']:
                report.append(f"✓ {fix}")
        
        if self.results['repair_recommendations']:
            report.append("")
            report.append("توصیه‌های ترمیم / REPAIR RECOMMENDATIONS:")
            report.append("-" * 50)
            for recommendation in self.results['repair_recommendations']:
                report.append(f"• {recommendation}")
        
        report.append("")
        report.append("=" * 80)
        report.append("پایان گزارش / End of Report")
        report.append("=" * 80)
        
        return "\n".join(report)