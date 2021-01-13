from win10toast import ToastNotifier
import time
toaster = ToastNotifier()

toaster.show_toast('notification', 'Alert! test', threaded=True, icon_path=None, duration=4)#4 seconds
 
while toaster.notification_active():
    time.sleep(0.1)
    
