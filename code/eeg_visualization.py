import os
import mne

def save_psd_and_raw_plots(raw):
    # Fayl papkalarini yaratish
    if not os.path.exists('results/psd_plots'):
        os.makedirs('results/psd_plots')

    if not os.path.exists('results/raw_plots'):
        os.makedirs('results/raw_plots')

    # PSD grafikasini saqlash
    fig_psd = raw.plot_psd(area_mode='range', tmax=10.0, show=False)
    fig_psd.savefig('results/psd_plots/psd_signal_4.png')

    # Raw signal grafikasi saqlash
    fig_raw = raw.plot(title="EEG Signal", show=False)
    fig_raw.savefig('results/raw_plots/raw_signal_4.png')
