import pyaudio
import numpy as np
import scipy.signal

from . import config

# pyaudio streamer
pa = pyaudio.PyAudio()
streamer = pa.open(
    format=pyaudio.paFloat32,
    channels=config.WAV_N_CHANNELS,
    rate=config.WAV_RATE,
    input=True,
    output=False,
    frames_per_buffer=config.WAV_CHUNK,
)


def detect_peak(AC):
    peak = []
    for i in range(AC.shape[0] - 2):
        if AC[i] < AC[i + 1] and AC[i + 1] > AC[i + 2]:
            peak.append([i + 1, AC[i + 1]])
    return np.array(peak)


past_spec_sum: float = 0.0
past_key_states: list = [0] * config.N_MUSICAL_SCALE


def get_key_states() -> list:
    global past_spec_sum
    global past_key_states

    wav = np.frombuffer(streamer.read(config.WAV_CHUNK, exception_on_overflow=False), np.float32)
    wav = wav * np.hanning(config.WAV_CHUNK)
    # amplitude spectrum
    wav_spectrum = np.fft.fft(wav)
    # power spectrum
    wav_spectrum = np.abs(wav_spectrum)
    # logarithmic spectrum
    wav_spectrum = 20 * np.log10(wav_spectrum)

    # band-pass filter
    filter_min_freq: int = 200
    filter_max_freq: int = 1760
    wav_spectrum[:round(filter_min_freq * config.WAV_CHUNK / config.WAV_RATE)] = 0
    wav_spectrum[round(filter_max_freq * config.WAV_CHUNK / config.WAV_RATE):] = 0

    # detect key push
    spectrum_peak = np.where(wav_spectrum > 15)[0]
    if spectrum_peak != []:

        current_spec_sum = np.abs(np.sum(wav_spectrum))

        if past_spec_sum > current_spec_sum:
            # continuous sound
            past_spec_sum = current_spec_sum
            return past_key_states
        else:
            result: list = [0] * config.N_MUSICAL_SCALE
            key_index: int = round((spectrum_peak[0] - 10) / 50 * config.N_MUSICAL_SCALE)
            if key_index > config.N_MUSICAL_SCALE:
                key_index = config.N_MUSICAL_SCALE - 1
            if key_index < 0:
                key_index = 0
            result[key_index] = 1
            return result

    return [0] * config.N_MUSICAL_SCALE
