import pandas as pd
import os

orig_file = "JHW_P1.txt"
refine_file = "refined.txt"
ch1 = "channel_1.txt"
ch2 = "channel_2.txt"

if os.path.exists(refine_file) :
  os.remove(refine_file)
if os.path.exists(ch1) :
  os.remove(ch1)
if os.path.exists(ch2) :
  os.remove(ch2)    
  
with open(refine_file, "a+", encoding='latin_1') as file_write :
    with open(orig_file, 'r', encoding='latin_1') as file_read:
      while True :
          line = file_read.readline()

          if not line : break  # 마지막 줄이면 파일 정리 마침
          if line.find("Channel Number=") >= 0 :  # Channel Number 가 포함된 줄
              file_write.write(line)              # 정리파일에 추가
          elif line.find("<960>=") >= 0 :    # <960>= 가 포함된 줄
              print(line.find("<960>="))
              file_write.write(line[28:])   # 해당 중의 24번째 문자부터 끝까지 추가
              
# Right Channel(Channel Numer = 1) channel_1.txt에 분리저장
with open(ch1, "a+", encoding='latin_1') as ch1_write :
    with open(refine_file, 'r', encoding='latin_1') as ref_read:
        while True :
            line = ref_read.readline()
            if line.find("Channel Number=2") >= 0 or (not line) : break
            if line.find("Channel Number=1") >= 0 : continue
            ch1_write.write(line)

# Left Channel(Channel Numer = 2) channel_2.txt에 분리저장
with open(ch2, "a+", encoding='latin_1') as ch2_write :
    with open(refine_file, 'r', encoding='latin_1') as ref_read:
        while True :
            line = ref_read.readline()
            if line.find("Channel Number=2") >= 0 : break
        while True :
            line = ref_read.readline()
            if  not line : break
            ch2_write.write(line)            
            
                            
with open(ch1, "r", encoding='latin_1') as ch1_read :
    print("Channel 1 : 데이터 수 => ", len(ch1_read.readlines()))
    
with open(ch2, "r", encoding='latin_1') as ch2_read :
    print("Channel 2 : 데이터 수 => ", len(ch2_read.readlines()))    
