#!/bin/bash
install_libraries()
{
    echo "==========================================="
    echo "Installing required libraries."
    echo "Make sure you have active internet connection."
    sudo apt install python3-pip
    pip3 install pyaudio
    pip3 install SpeechRecognition
    pip3 install gtts
    pip3 install playsound  
    pip3 install beautifulsoup4
    pip3 install lxml
    sudo apt install python-lxml
    echo "==========================================="
    echo "Libraries installed sucessfully."
     
}
copying_files()
{
    echo "==========================================="    
    echo "Copying required files..."
    path=$(pwd)
    echo $path
    sudo mkdir /usr/lib/voice_assist
    sudo mkdir /usr/lib/voice_assist/bin
    sudo mkdir /usr/lib/voice_assist/bin/audio
    sudo mkdir /usr/lib/voice_assist/bin/database
    sudo cp -r $path/assist.svg /usr/share/pixmaps/
    sudo cp -r $path/bin/audio/* /usr/lib/voice_assist/bin/audio/
    sudo cp -r $path/bin/database/* /usr/lib/voice_assist/bin/database/
    sudo cp -r $path/assist.py /usr/lib/voice_assist/
    sudo cp -r $path/open_app.py /usr/lib/voice_assist/
    sudo cp -r $path/close_app.py /usr/lib/voice_assist/
    sudo cp -r $path/assist.sh /usr/lib/voice_assist/
    sudo cp -r $path/assist.desktop /usr/share/applications
    echo "==========================================="
    echo "Copying finished."
}
 
echo "==========================================="
echo "Hold tight..."
echo "Installation is in progress..."
install_libraries
copying_files
echo "==========================================="
echo "Installation finished sucessfully."
echo "Now you can enjoy using Voice Assist."
