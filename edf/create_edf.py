import numpy as np
import pyedflib

# Fayl nomi
file_name = 'subject02.edf'

# Parametrlar
n_channels = 2           # Kanal soni (masalan: C3 va C4)
sampling_rate = 100      # 100 Hz
duration = 10            # 10 soniya
n_samples = sampling_rate * duration

# Sun'iy EEG signal yaratamiz
signal1 = np.sin(2 * np.pi * 10 * np.linspace(0, duration, n_samples)) * 100
signal2 = np.cos(2 * np.pi * 12 * np.linspace(0, duration, n_samples)) * 80

signals = [signal1, signal2]

# Kanal nomlari
channel_labels = ['C3', 'C4']

# Fayl yaratamiz
with pyedflib.EdfWriter(file_name, n_channels, file_type=pyedflib.FILETYPE_EDFPLUS) as f:
    channel_info = []
    for label in channel_labels:
        ch_dict = {
            'label': label,
            'dimension': 'uV',
            'sample_rate': sampling_rate,
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
