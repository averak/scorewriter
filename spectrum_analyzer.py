#!/usr/bin/env python3
import pyaudio
import numpy as np
import pyqtgraph as pg


# pyaudio streamer
pa = pyaudio.PyAudio()
streamer = pa.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=16000,
    input=True,
    output=False,
    frames_per_buffer=1024,
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
qt_plotitem1.setXRange(0, 1024, padding=0)
# Spectrum windows setting
qt_plotwid2 = pg.PlotWidget(name="spectrum")
qt_plotitem2 = qt_plotwid2.getPlotItem()
qt_plotitem2.setMouseEnabled(x=False, y=False)
qt_plotitem2.setYRange(0, 50)
qt_plotitem2.setXRange(0, 16000 / 2, padding=0)
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
# Show plot window
qt_win.show()


def update() -> None:
    wav = np.frombuffer(streamer.read(1024, exception_on_overflow=False), np.float32)
    wav = wav * np.hanning(1024)
    # amplitude spectrum
    wav_spectrum = np.fft.fft(wav)
    # power spectrum
    wav_spectrum = np.abs(wav_spectrum)

    # plot
    qt_curve_wave.setData(range(1024), wav)
    qt_curve_spectrum.setData(np.fft.fftfreq(1024, d=1 / 16000), wav_spectrum)


if __name__ == '__main__':
    qt_timer = pg.QtCore.QTimer()
    qt_timer.timeout.connect(update)
    qt_timer.start(10)
    pg.QtGui.QApplication.instance().exec_()
