# WebVTTtoSRT
A python script to convert webvtt subtitles to srt

This is a python script to convert subtitles with **WebVTT**(*.vtt*) format to **SRT**(*.srt*).
**WebVTT** and **SRT** files have two differences. First difference is that WebVTT files have a header "WEBVTT". The other one is that the time format of **SRT** contains a comma between s and ms but **WebVTT** contains a dot.

Script contains two parts:
  1. Converter
  2. File fetcher

## Converter
In this part, whole *.vtt* file is read.
At first, the header of **WebVTT** file is removed then dots between s and ms in time format are changed to commas.

## File Fetcher
File fetcher gets the ```Path``` object of a file or folder. If the object indicates that the ```Path``` object contatins the information of a **WebVTT** file, converter function is called to convert the file. If the object indicates that the ```Path``` object contains the information of file with another type, the file will be skipped. If the object file contains the information of a folder, this function will call itself recursively on subfiles/subfolders of current folder.
