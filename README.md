# PythonVersionRustNES (IN_PROGRESS)
Recreating milestone 1 and parts of milestone 2 of the RustNES project in python

## Description
Retro chiptune music is starting to make a resurgence with the popularity of many retro indie games like Hades and Celeste. However, a majority of music produced for these games rarely use actual hardware that made the 8-bit and 16-bit music charming. The purpose of this project is to replicate a sound chip from the NES using Rust. 

## Milestones
---
### Milestone 1 (worst case scenario):
>* Basic audio generator that can produce 8-bit sound based on user's GUI input.

### Milestone 2 (expected):
>* Graphical User Interface is implemented with features such as play/pause, volume control, and MIDI import, export function.<br /><br />
>* Animation of waveforms is displayed as well when music is played (something like old Windows' winamp visualization)
We could test this function by comparing the visualization with other pre-existing services.

## Contributors
---
 [Francis German](francisgerman70)


### Resources:
>* https://www.youtube.com/playlist?list=PLHQ0utQyFw5JD2wWda50J8XuzQ2cFr8RX
>* https://www.youtube.com/watch?v=8RrQrATnXXY
>* https://www.egui.rs/
>* https://bugzmanov.github.io/nes_ebook/
>* https://docs.rs/midly/latest/midly/
>* https://docs.rs/midly/latest/rodio
>* https://github.com/RustAudio/rodio
>* https://docs.rs/basic_waves/latest/basic_waves/index.html
>* https://www.youtube.com/watch?v=gKXGDuKrCfA
>* https://github.com/crschung/RustNES
>* https://www.tutorialspoint.com/python/python_gui_programming.htm#:~:text=Tkinter%20is%20the%20standard%20GUI,Tkinter%20is%20an%20easy%20task.
>* https://www.youtube.com/watch?v=yQSEXcf6s2I&ab_channel=Codemy.com

### Programming Language: Python

### Possible Function Implemenations:
* Generating three different waveforms
* GUI

### Crates
* tkinter
* numpy

## How To Run
```
python gui.py
```