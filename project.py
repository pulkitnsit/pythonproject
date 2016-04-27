import Nsound as ns
import pyaudio
#x = ns.AudioStream('sing.wav')
'''
print x.getNChannels()
sr = x.getSampleRate()
print sr
# x.plot("Nsound")

y = ns.AudioStream('rs100000.wav')
sr = y.getSampleRate()
print sr
y.plot("rs")

x = ns.AudioStream('rs1000.wav')
sr = x.getSampleRate()
x.plot("rs2")
print sr
ns.Plotter.show()
'''
#lpf = ns.FilterLowPassFIR(sr, 128, 1000.0)
#y = lpf.filter(x)
#print "s"
#x >> "or.wav"
#y >> "fl.wav"
'''
x.resample2(100000.0)
x >> "rs100000.wav"
x.resample2(1000.0)
x >> "rs1000.wav"
print "Done"
'''
f1 = ns.FilterLowPassFIR(500.0, 64, 100.0)
f2 = ns.FilterHighPassFIR(500.0, 64, 100.0)
f3 = ns.FilterBandPassFIR(500.0, 64, 100.0, 200.0)
f4 = ns.FilterBandRejectFIR(500.0, 64, 100.0, 200.0)
'''
bf = ns.Buffer("sing.wav")
f1 = f1*bf
f1 >> "lp.wav"
'''
