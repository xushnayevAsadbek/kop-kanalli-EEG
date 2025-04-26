# 5 ta EEG signalini yaratish va saqlash
# import numpy as np
# import pyedflib

# file_name = 'subject03.edf'
# n_channels = 5           # Kanal soni
# sampling_rate = 100      # 100 Hz
# duration = 10            # 10 soniya
# n_samples = sampling_rate * duration

# # 5 ta sun'iy EEG signal yaratamiz
# signals = []
# for freq in [10, 12, 8, 15, 20]:  # Har bir signal uchun turli chastotalar
#     signal = np.sin(2 * np.pi * freq * np.linspace(0, duration, n_samples)) * 100
#     signals.append(signal)

# # Kanal nomlari
# channel_labels = ['C3', 'C4', 'P3', 'P4', 'O1']

# with pyedflib.EdfWriter(file_name, n_channels, file_type=pyedflib.FILETYPE_EDFPLUS) as f:
#     channel_info = []
#     for label in channel_labels:
#         ch_dict = {
#             'label': label,
#             'dimension': 'uV',
#             'sample_frequency': sampling_rate,  # sample_rate o‘rniga sample_frequency
#             'physical_min': -500.0,
#             'physical_max': 500.0,
#             'digital_min': -32768,
#             'digital_max': 32767,
#             'transducer': '',
#             'prefilter': ''
#         }
#         channel_info.append(ch_dict)

#     f.setSignalHeaders(channel_info)
#     f.writeSamples(signals)

# print(f"{file_name} muvaffaqiyatli yaratildi ✅")



#10 ta EEG signalini yaratish va saqlash

import numpy as np
import pyedflib

file_name = 'D:\\EEG\\data\\subject04.edf' 

n_channels = 10           # 10 ta kanal
sampling_rate = 100       # 100 Hz
duration = 10             # 10 soniya
n_samples = sampling_rate * duration

# 10 ta sun'iy EEG signal yaratamiz
signals = []
for freq in [10, 12, 8, 15, 20, 10, 25, 30, 5, 18]:  # Har bir signal uchun turli chastotalar
    signal = np.sin(2 * np.pi * freq * np.linspace(0, duration, n_samples)) * 100
    signals.append(signal)

# Kanal nomlari
channel_labels = ['C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F3', 'F4', 'T3', 'T4']

# Fayl yaratamiz
with pyedflib.EdfWriter(file_name, n_channels, file_type=pyedflib.FILETYPE_EDFPLUS) as f:
    channel_info = []
    for label in channel_labels:
        ch_dict = {
            'label': label,
            'dimension': 'uV',
            'sample_frequency': sampling_rate,  # sample_rate o‘rniga sample_frequency
            'physical_min': -500.0,
            'physical_max': 500.0,
            'digital_min': -32768,
            'digital_max': 32767,
            'transducer': '',
            'prefilter': ''
        }
        channel_info.append(ch_dict)

    f.setSignalHeaders(channel_info)
    f.writeSamples(signals)

print(f"{file_name} muvaffaqiyatli yaratildi ✅")
