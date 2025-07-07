import platform
import socket
import psutil
import uuid
import hashlib
import json
import os
import subprocess
from datetime import datetime
import winreg
import getpass

class SystemInfoCollector:
    def __init__(self):
        self.system_id = self.generate_system_id()
        self.info = {}
        
    def generate_system_id(self):
        """Generate unique system identifier based on hardware characteristics"""
        try:
            # Get MAC address
            mac = hex(uuid.getnode())[2:].upper()
            
            # Get system UUID if available (Windows)
            system_uuid = ""
            try:
                if platform.system() == "Windows":
                    result = subprocess.run(['wmic', 'csproduct', 'get', 'UUID'], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        lines = result.stdout.strip().split('\n')
                        for line in lines:
                            if line.strip() and 'UUID' not in line:
                                system_uuid = line.strip()
                                break
            except:
                pass
            
            # Create unique identifier
            identifier_string = f"{mac}-{system_uuid}-{platform.node()}"
            system_id = hashlib.md5(identifier_string.encode()).hexdigest()[:16].upper()
            
            return f"PC-{system_id}"
            
        except Exception as e:
            # Fallback to random UUID
            return f"PC-{str(uuid.uuid4())[:16].upper()}"
    
    def get_windows_version(self):
        """Get detailed Windows version information"""
        try:
            if platform.system() != "Windows":
                return f"{platform.system()} {platform.release()}"
            
            # Get Windows version from registry
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                   r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
                    product_name = winreg.QueryValueEx(key, "ProductName")[0]
                    build_number = winreg.QueryValueEx(key, "CurrentBuildNumber")[0]
                    release_id = ""
                    try:
                        release_id = winreg.QueryValueEx(key, "DisplayVersion")[0]
                    except:
                        try:
                            release_id = winreg.QueryValueEx(key, "ReleaseId")[0]
                        except:
                            pass
                    
                    version_info = f"{product_name}"
                    if release_id:
                        version_info += f" {release_id}"
                    version_info += f" (Build {build_number})"
                    
                    return version_info
            except:
                pass
            
            # Fallback to platform module
            return f"Windows {platform.release()} {platform.version()}"
            
        except Exception as e:
            return f"Windows (Unknown version): {str(e)}"
    
    def get_hardware_info(self):
        """Get hardware information"""
        hardware = {}
        
        try:
            # CPU Information
            hardware['cpu'] = {
                'name': platform.processor(),
                'architecture': platform.architecture()[0],
                'cores': psutil.cpu_count(logical=False),
                'logical_cores': psutil.cpu_count(logical=True),
                'frequency': psutil.cpu_freq().max if psutil.cpu_freq() else "Unknown"
            }
            
            # Memory Information
            memory = psutil.virtual_memory()
            hardware['memory'] = {
                'total': f"{memory.total // (1024**3)} GB",
                'available': f"{memory.available // (1024**3)} GB",
                'used_percent': f"{memory.percent}%"
            }
            
            # Disk Information
            disks = []
            for partition in psutil.disk_partitions():
                try:
                    disk_usage = psutil.disk_usage(partition.mountpoint)
                    disks.append({
                        'device': partition.device,
                        'filesystem': partition.fstype,
                        'total': f"{disk_usage.total // (1024**3)} GB",
                        'used': f"{disk_usage.used // (1024**3)} GB",
                        'free': f"{disk_usage.free // (1024**3)} GB"
                    })
                except:
                    continue
            hardware['disks'] = disks
            
        except Exception as e:
            hardware['error'] = str(e)
        
        return hardware
    
    def get_network_info(self):
        """Get detailed network information"""
        network = {}
        
        try:
            # Network Interfaces
            interfaces = []
            for interface, addresses in psutil.net_if_addrs().items():
                interface_info = {'name': interface, 'addresses': []}
                for addr in addresses:
                    if addr.family == socket.AF_INET:  # IPv4
                        interface_info['addresses'].append({
                            'type': 'IPv4',
                            'address': addr.address,
                            'netmask': addr.netmask
                        })
                    elif addr.family == socket.AF_INET6:  # IPv6
                        interface_info['addresses'].append({
                            'type': 'IPv6',
                            'address': addr.address
                        })
                if interface_info['addresses']:
                    interfaces.append(interface_info)
            
            network['interfaces'] = interfaces
            
            # Network Statistics
            net_stats = psutil.net_io_counters()
            network['statistics'] = {
                'bytes_sent': net_stats.bytes_sent,
                'bytes_recv': net_stats.bytes_recv,
                'packets_sent': net_stats.packets_sent,
                'packets_recv': net_stats.packets_recv
            }
            
            # Default Gateway
            try:
                if platform.system() == "Windows":
                    result = subprocess.run(['ipconfig'], capture_output=True, text=True)
                    # Parse default gateway from ipconfig output
                    # This is a simplified approach
                    network['ipconfig_output'] = result.stdout[:1000]  # First 1000 chars
            except:
                pass
            
        except Exception as e:
            network['error'] = str(e)
        
        return network
    
    def get_installed_software(self):
        """Get list of installed network-related software"""
        software = []
        
        try:
            if platform.system() == "Windows":
                # Check for common network software in registry
                software_keys = [
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
                ]
                
                network_keywords = ['vpn', 'proxy', 'firewall', 'antivirus', 'network', 
                                  'internet', 'wifi', 'ethernet', 'adapter']
                
                for software_key in software_keys:
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, software_key) as key:
                            for i in range(winreg.QueryInfoKey(key)[0]):
                                try:
                                    subkey_name = winreg.EnumKey(key, i)
                                    with winreg.OpenKey(key, subkey_name) as subkey:
                                        try:
                                            display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                            if any(keyword in display_name.lower() for keyword in network_keywords):
                                                software.append(display_name)
                                        except:
                                            continue
                                except:
                                    continue
                    except:
                        continue
        except Exception as e:
            software.append(f"Error scanning software: {str(e)}")
        
        return software[:20]  # Limit to 20 items
    
    def collect_all_info(self):
        """Collect comprehensive system information"""
        self.info = {
            'system_id': self.system_id,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user': getpass.getuser(),
            'computer_name': platform.node(),
            'os': {
                'name': platform.system(),
                'version': self.get_windows_version(),
                'architecture': platform.architecture()[0],
                'platform': platform.platform()
            },
            'hardware': self.get_hardware_info(),
            'network': self.get_network_info(),
            'installed_software': self.get_installed_software(),
            'python_version': platform.python_version(),
            'environment_variables': {
                'PATH': os.environ.get('PATH', ''),
                'COMPUTERNAME': os.environ.get('COMPUTERNAME', ''),
                'USERNAME': os.environ.get('USERNAME', ''),
                'USERPROFILE': os.environ.get('USERPROFILE', '')
            }
        }
        
        return self.info
    
    def generate_report_header(self):
        """Generate formatted report header with system information"""
        if not self.info:
            self.collect_all_info()
        
        header = []
        header.append("=" * 80)
        header.append("        PCPasokh Internet Repair - گزارش عیب یابی اینترنت")
        header.append("=" * 80)
        header.append(f"شناسه سیستم / System ID: {self.info['system_id']}")
        header.append(f"تاریخ و زمان / Date & Time: {self.info['timestamp']}")
        header.append(f"نام کاربر / User: {self.info['user']}")
        header.append(f"نام رایانه / Computer: {self.info['computer_name']}")
        header.append(f"سیستم عامل / OS: {self.info['os']['version']}")
        header.append(f"معماری / Architecture: {self.info['os']['architecture']}")
        header.append("")
        
        # Hardware summary
        header.append("مشخصات سخت افزار / Hardware Specifications:")
        header.append("-" * 50)
        if 'cpu' in self.info['hardware']:
            cpu = self.info['hardware']['cpu']
            header.append(f"پردازنده / CPU: {cpu.get('name', 'Unknown')}")
            header.append(f"هسته‌ها / Cores: {cpu.get('cores', 'Unknown')} physical, {cpu.get('logical_cores', 'Unknown')} logical")
        
        if 'memory' in self.info['hardware']:
            memory = self.info['hardware']['memory']
            header.append(f"حافظه / Memory: {memory.get('total', 'Unknown')} (Available: {memory.get('available', 'Unknown')})")
        
        header.append("")
        header.append("=" * 80)
        header.append("")
        
        return "\n".join(header)
    
    def save_system_info(self, filename="system_info.json"):
        """Save complete system information to JSON file"""
        try:
            if not self.info:
                self.collect_all_info()
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.info, f, indent=2, ensure_ascii=False)
            
            return True, f"System information saved to {filename}"
        except Exception as e:
            return False, f"Failed to save system info: {str(e)}"