import gtts
from playsound import playsound
import os
from s2t import s2t
import time 
start_timer=time.time()
start_timer_cpu=time.process_time() 

def speech(text:str,file_name:str):
    tts = gtts.gTTS(text)
    file_name=file_name+'.mp3'
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)

text=str(s2t())
file_name=str('test')
speech(text,file_name)

end_timer=time.time()
end_timer_cpu=time.process_time() 

total_time=end_timer - start_timer
total_time_cpu=end_timer_cpu - start_timer_cpu


print(f'Total time for execution of program {total_time}')
print(f'Total process time for cpu was {total_time_cpu}')