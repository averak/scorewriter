#!/usr/bin/env python3
import pyaudio
import numpy as np
import pyqtgraph as pg

from core import config

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

# pyQt window app
qt_app = pg.QtGui.QApplication([])
qt_app.quitOnLastWindowClosed()
# window
qt_win = pg.QtGui.QMainWindow()
qt_win.setWindowTitle("Spectrum Analyzer")
qt_win.resize(800, 600)
qt_centralwid = pg.QtGui.QWidget()
qt_win.setCentralWidget(qt_centralwid)
# layout
qt_lay = pg.QtGui.QVBoxLayout()
qt_centralwid.setLayout(qt_lay)
# Wave figure window setting
qt_plotwid1 = pg.PlotWidget(name="wave")
qt_plotitem1 = qt_plotwid1.getPlotItem()
qt_plotitem1.setMouseEnabled(x=False, y=False)
qt_plotitem1.setYRange(-1, 1)
qt_plotitem1.setXRange(0, config.WAV_CHUNK, padding=0)
# Spectrum windows setting
qt_plotwid2 = pg.PlotWidget(name="spectrum")
qt_plotitem2 = qt_plotwid2.getPlotItem()
qt_plotitem2.setMouseEnabled(x=False, y=False)
qt_plotitem2.setYRange(0, 50)
qt_plotitem2.setXRange(0, config.WAV_RATE / 2, padding=0)
# Wave figure Axis
qt_specAxis1 = qt_plotitem1.getAxis("bottom")
qt_specAxis1.setLabel("Time [sample]")
# Spectrum Axis
qt_specAxis2 = qt_plotitem2.getAxis("bottom")
qt_specAxis2.setLabel("Frequency [Hz]")
# Plot data
qt_curve_wave = qt_plotitem1.plot()
qt_curve_spectrum = qt_plotitem2.plot()
# Widget
qt_lay.addWidget(qt_plotwid1)
qt_lay.addWidget(qt_plotwid2)


def update() -> None:
    wav = np.frombuffer(streamer.read(config.WAV_CHUNK, exception_on_overflow=False), np.float32)
    wav = wav * np.hanning(config.WAV_CHUNK)
    # amplitude spectrum
    wav_spectrum = np.fft.fft(wav)
    # power spectrum
    wav_spectrum = np.abs(wav_spectrum)

    # band-pass filter
    filter_min_freq: int = 200
    filter_max_freq: int = 1760
    wav_spectrum[:round(filter_min_freq * config.WAV_CHUNK / config.WAV_RATE)] = 0
    wav_spectrum[round(filter_max_freq * config.WAV_CHUNK / config.WAV_RATE):] = 0

    # plot
    qt_curve_wave.setData(range(config.WAV_CHUNK), wav)
    qt_curve_spectrum.setData(np.fft.fftfreq(config.WAV_CHUNK, d=1 / config.WAV_RATE), wav_spectrum)


def run_app() -> None:
    # show window
    qt_win.show()
    # set timer
    qt_timer = pg.QtCore.QTimer()
    qt_timer.timeout.connect(update)
    qt_timer.start(10)
    # run app
    pg.QtGui.QApplication.instance().exec_()


if __name__ == '__main__':
    run_app()
