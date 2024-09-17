# import ctypes
# import os
#
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
#
# if __name__ == "__main__":
#     if is_admin():
#         os.startfile(u"C:\\Program Files (x86)\\Accuver\\XCAL-M\\XCAL-M.exe")
#     else:
#         ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", "script_to_XCAL_function.py", None, 1)
#
#