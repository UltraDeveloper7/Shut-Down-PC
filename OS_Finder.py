import win32com.client

def os():
    c = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    wmi = c.ConnectServer(".", "root\cimv2")
    os_results = wmi.ExecQuery(
        "SELECT Caption, Version FROM Win32_OperatingSystem")

    for os in os_results:
        os_caption = os.Caption
        os_version = os.Version
        
    return os_caption
