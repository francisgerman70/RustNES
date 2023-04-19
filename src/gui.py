import tkinter as tk
import numpy as np
import pygame

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gui Player")
        self.sample_rate = 44100
        self.sound_duration = 2

        pygame.mixer.init()
        self.audio_channel = pygame.mixer.Channel(0)  # Create audio channel object

        # play and pause button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_pause)
        self.play_button.pack()

        # volume button
        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.pack()

        # Import button
        self.import_button = tk.Button(self.root, text="Import MIDI", command=self.import_button)
        self.import_button.pack()

        # export Button
        self.export_button = tk.Button(self.root, text="Export", command=self.export_button)
        self.export_button.pack()

        # Waveform selection button
        self.waveform_button = tk.Button(self.root, text="Switch Waveform", command=self.switch_waveform)
        self.waveform_button.pack()

        # Initialize waveform type and frequency
        self.waveform_type = "triangle"
        self.frequency = 440

    def play_pause(self):
        # first check if audio channel is currently playing
        if self.audio_channel.get_busy():
            # Pause audio playback
            self.audio_channel.stop()
            self.play_button.configure(text="Play")
        else:
            # generate waveforms
            waveform = self.generate_waveform(self.frequency)
  
            # Reshape waveform to be 2-dimensional for stereo mixer
            waveform = np.stack([waveform, waveform], axis=1)
            sound = pygame.sndarray.make_sound(waveform)
            
            # Set volume level and play audio
            self.audio_channel.set_volume(self.volume_slider.get() / 100)
            self.audio_channel.play(sound, loops=-1)
            
            # Update play/pause button text
            self.play_button.configure(text="Pause")

    def set_volume(self, volume):
        self.audio_channel.set_volume(float(volume) / 100)

    def import_button(self):
        
        pass

    def export_button(self):
        
        pass  

    def switch_waveform(self):
        if self.waveform_type == "triangle":
            self.waveform_type = "pulse"
        elif self.waveform_type == "pulse":
            self.waveform_type = "noise"
        else:
            self.waveform_type = "triangle"

    def run(self):
        self.root.mainloop()

    def generate_waveform(self, frequency):
        # Generate waveform samples based on waveform type and frequency
        if self.waveform_type == "triangle":
            waveform = self._generate_triangle_wave(frequency)
        elif self.waveform_type == "pulse":
            waveform = self._generate_pulse_wave(frequency)
        elif self.waveform_type == "noise":
            waveform = self._generate_noise_wave(frequency)
        else:
            raise ValueError("Invalid waveform type")

        # Normalize waveform samples to 8-bit values
        waveform = (waveform + 1) / 2 * 255
        waveform = waveform.astype(np.uint8)

        return waveform

    def _generate_triangle_wave(self, frequency):
        # Generate the time array
        t = np.linspace(0, self.sound_duration, int(self.sample_rate * self.sound_duration), endpoint=False)
        # Generate the triangle wave
        waveform = 2 * np.abs((2 * (t * frequency)) % 2 - 1) - 1
        
        return waveform
    
    def _generate_pulse_wave(self, frequency):
        # Generate the time array
        t = np.linspace(0, self.sound_duration, int(self.sample_rate * self.sound_duration), endpoint=False)
        # Generate the pulse wave
        waveform = np.where(np.mod(t * frequency, 1) < 0.5, 1, -1)
        
        return waveform

    def _generate_noise_wave(self, frequency):
        # Generate random noise with a mean of 0 and standard deviation of 1
        noise = np.random.normal(size=int(self.sample_rate * self.sound_duration))

        return noise

gui = GUI()
gui.run()