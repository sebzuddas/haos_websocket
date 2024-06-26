import unittest
import numpy as np
import pandas as pd

from control.SignalProcessing import SignalProcessing
from peripherals.Sensor import Sensor

# Unit Tests
class TestSignalProcessing(unittest.TestCase):

    def setUp(self):
        np.random.seed(0)
        # self.sample_signal1 = Sensor(virtual=True)
        # self.sample_signal2 = Sensor(virtual=True)
        
        # self.sample_signal1 = self.sample_signal1.generate_virtual_data(sample_rate=1, amplitude=2, frequency=50, phase=40, noise_level=2, randomise=False)
        # self.sample_signal2 = self.sample_signal2.generate_virtual_data(sample_rate=0.5, amplitude=1, frequency=20, phase=30, noise_level=1, randomise=False)
    
    # def test_detrend(self):
    #     detrended_signal = SignalProcessing.detrend(self.sample_signal1, plot=False)
    #     self.assertIsInstance(detrended_signal, np.ndarray)
    #     #TODO: more asserts

    # def test_fourier_transform_no_plot(self):
    #     result = SignalProcessing.fourier_transform(self.sample_signal1, plot=False)
    #     self.assertIsInstance(result, np.ndarray)
    #     self.assertEqual(result.shape[0], 5)

    # def test_power_spectral_density_no_plot(self):
    #     f, Pxx_den = SignalProcessing.power_spectral_density(self.sample_signal1, plot=False)
    #     self.assertIsInstance(f, np.ndarray)
    #     self.assertIsInstance(Pxx_den, np.ndarray)
    #     self.assertEqual(len(f), len(Pxx_den))

    # def test_auto_correlation_no_plot(self):
    #     result = SignalProcessing.auto_correlation(self.sample_signal1, lags=10, plot=False)
    #     self.assertIsInstance(result, np.ndarray)
    #     self.assertEqual(len(result), 10)

    # def test_stationarity_white_noise(self):
    #     white_noise = np.random.normal(size=1000)
    #     sensor = Sensor(
    #         friendly_name="White Noise Sensor",
    #         device_class="random",
    #         unit_of_measurement="units",
    #         timeseries_data=pd.DataFrame({'time': np.arange(1000), 'state': white_noise}),
    #         numpy_data=white_noise
    #     )
    #     result = SignalProcessing.stationarity(sensor)
    #     self.assertLess(result['p-value'], 0.05, "White noise should be stationary")

    def test_stationarity_sine_wave(self):
        sensor = Sensor(virtual=True)
        sensor.generate_virtual_data(amplitude=1, frequency=1, noise_level=0, phase=0, randomise=False)
        result = SignalProcessing.stationarity(sensor)
        self.assertLess(result['p-value'], 0.05, "Sine wave should be stationary")

    # def test_cross_correlation(self):
    #     # Sanity check with synthetic data
    #     # Create two sine waves with a known phase shift

    #     t1 = Sensor(virtual=True)
    #     t1.generate_virtual_data(sample_rate=1, amplitude=1, frequency=5, phase=0, noise_level=0, randomise=False)
        
    #     t2 = Sensor(virtual=True)
    #     t2.generate_virtual_data(sample_rate=1, amplitude=1, frequency=5, phase=45, noise_level=0, randomise=False)

    #     # Get the cross-correlation result
    #     cross_corr_result = SignalProcessing.cross_correlation(t1, t2, lags_percentage=50, plot=False)

    #     self.assertIsInstance(cross_corr_result, np.ndarray)
    #     self.assertEqual(cross_corr_result.shape, (2 * 50 + 1,))

    #     # Assuming a known phase shift results in an expected lag
    #     expected_lag_index = 50  # Adjust this based on your calculated expected lag in samples
    #     max_lag_index = np.argmax(cross_corr_result)
    #     self.assertEqual(max_lag_index, expected_lag_index)



if __name__ == '__main__':
    unittest.main()