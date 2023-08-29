import tkinter as tk
import time
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        
        self.time_label = tk.Label(root, text="Set Alarm Time (HH:MM:SS)")
        self.time_label.pack()
        
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        
        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()
        
        self.stop_button = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack()
        
        self.alarm_set = False
        
    def set_alarm(self):
        if not self.alarm_set:
            alarm_time = self.time_entry.get()
            self.alarm_hour, self.alarm_minute, self.alarm_second = map(int, alarm_time.split(":"))
            
            self.alarm_set = True
            self.set_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            
            self.check_alarm()
    
    def check_alarm(self):
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec
        
        if (
            current_hour == self.alarm_hour and
            current_minute == self.alarm_minute and
            current_second == self.alarm_second
        ):
            self.play_alarm()
        else:
            self.root.after(1000, self.check_alarm)
    
    def play_alarm(self):
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
        self.alarm_set = False
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def stop_alarm(self):
        self.alarm_set = False
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

root = tk.Tk()
alarm_clock = AlarmClock(root)
root.mainloop()
