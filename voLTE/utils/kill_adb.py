import psutil

def kill_adb():
    process_name = "adb.exe"
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                pid = process.info['pid']
                p = psutil.Process(pid)
                try:
                    p.terminate()
                except:
                    p.kill()  # to forcefully terminate
                print(f"Process {process_name} (PID {pid}) terminated.")
            except psutil.NoSuchProcess as e:
                print(f"Error terminating process: {e}")

def kill_adb_with_pid(pid):
    process_name = "adb.exe"
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['pid'] == pid:
            try:
                p = psutil.Process(pid)
                try:
                    p.terminate()
                except:
                    p.kill()  # to forcefully terminate
                print(f"Process {process_name} (PID {pid}) terminated.")
            except psutil.NoSuchProcess as e:
                print(f"Error terminating process: {e}")


def kill_media_player():
    process_name = "Microsoft.Media.Player.exe"
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                pid = process.info['pid']
                p = psutil.Process(pid)
                try:
                    p.terminate()
                except:
                    p.kill()  # to forcefully terminate
                print(f"Process {process_name} (PID {pid}) terminated.")
            except psutil.NoSuchProcess as e:
                print(f"Error terminating process: {e}")