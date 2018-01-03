# pfss
Emit a carbonated water being opened from CLI

Sometimes, I don't have a Perrier (or equivalent) immediately next to the computer. As a result, I am unable to hear the hiss (or 'pfss') of the can being opened. I have sampled the best of a Perrier can by extensive evaluation of various cans being opened. Arguments may also specify other types of waters, including:

* Perrier
* Topo Chico (a swift turn of the cap)
* Gerolsteiner (a swift turn of the cap)  
* La Croix (including a can flick)
* San Pellegrino (a swift turn of the cap)

# Installation

## Install pyglet
```
pip install pyglet
```

## Install AVbin
```
wget https://github.com/downloads/AVbin/AVbin/avbin-darwin-x86-64-v8.1.tar.bz2
tar -xvjf avbin-darwin-x86-64-v8.1.tar.bz2  && cd avbin-darwin-x86-64-v8.1 
sudo ./install.sh
```
## Run
```
python main.py
```

## Remove annoying message (macOS)
defaults write org.python.python ApplePersistenceIgnoreState NO

