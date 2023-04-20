from matplotlib import pyplot as plt
import numpy as np


orig_file = "JHW_P1.txt"
refine_file = "refined.txt"
ch1 = "channel_1.txt"
ch2 = "channel_2.txt"
plot_signal = 50

stereo = [ch1, ch2]


for ch in stereo :
  with open(ch, 'r', encoding='latin_1') as ch_read :
        all_sig = np.array([])
        cnt_line = 1
        while True : 
            line = ch_read.readline()
            line = line.strip()
            if not line : break
            signal = np.array(line.split(','))
            signal = signal.astype(np.float32)
            #print(signal)
            all_sig = np.append(all_sig, signal)
            #all_sig = np.append(all_sig, signal)
            #print("line numer : %d, count_data : %s '\n" %(cnt_line, signal.size))
            cnt_line += 1
      
  rms = np.sqrt(np.mean(all_sig**2))       
  x = np.arange(0.0E-5, 11.2, 2.0833334E-5)

  if ch == ch1 :
    ch_lbl = 'Right VEMP Data'
    color = 'red'
    plot_seq = 211
  else : 
    ch_lbl = 'Left VEMP Data'
    color = 'blue'
    plot_seq = 212

  plt.subplot(plot_seq)
  plt.subplots_adjust(hspace=0.4)
  plt.plot(x, all_sig, 'b', label=ch_lbl, color=color, lw=1) 
  plt.title(ch_lbl)
  plt.xlabel('Time(Sec)')
  plt.ylabel('Amplitude(uV)')
  plt.grid(True)
  plt.legend(["{0} = {1}".format(ch_lbl, rms)])
  

#plt.tight_layout()
plt.show()
