text = "what is the weather at 3:00"
import datetime
for i in text.split():
        if ':00' in i:
            time_hour = i.split(':')[0]
            if "PM" in text.split() and int(time_hour)<12:
                time_hour = str(int(time_hour) + 12)
            elif "AM" in text.split():
                if time_hour == '12':
                    time_hour = '0'
            elif "AM" not in text.split() and "PM" not in text.split():
                time = datetime.datetime.now()
                hour = time.hour
                if time_hour == '12':
                     x = [0,12]
                else:
                     x = [int(time_hour), int(time_hour) + 12]
                if hour < x[0]:
                     time_hour = x[0]
                elif hour > x[0] and hour < x[1]:
                     time_hour = x[1]
                elif hour > x[1]:
                     time_hour = x[0]
                else:
                     time_hour = hour
                
                    
            
print(time_hour)