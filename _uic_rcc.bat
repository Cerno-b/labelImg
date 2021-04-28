@echo off

echo running uic...
pyuic5 -o main_window_ui.py ui\main_window.ui

echo running rcc...
pyrcc5 -o resources_rc.py resources.qrc

echo.
pause