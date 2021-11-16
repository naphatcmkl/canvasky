import pip

def install_wheel(path):
    pip.main(['install', path])

install_wheel('../PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
