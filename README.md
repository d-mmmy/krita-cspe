# Krita CSPE

A simple Krita extension that lets you toggle eraser and background/foreground color using a single shortcut, CSP style.

In Clip Studio Paint, you can go to shortcuts and set a shortcut which lets you change your active color AND switch to the alpha/eraser mode, letting you erase with your current brush, much like the E shortcut in Krita.
This extension emulates the same in Krita.

Pressing the associate shortcut key or manually accessing the script from the tools menu(not recommended) will let you switch between colors and alpha, in order -

**Primary Color -> Secondary Color -> Alpha -> Primary Color...** and so on. Looping.

![DEMO](cspe_demo.mp4)

I made this extension because I am used to having this shortcut as my pen button, and since Krita did not have an equivalent.

The default shortcut is Shift + X

**Note -** The extension won't do the switching when there is no document open.


[def]: cs