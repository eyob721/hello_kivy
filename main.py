#!/usr/bin/python3
"""A simple exercise application"""
import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require("2.3.0")


class SimpleApp(App):
    def build(self):
        return Label(text="Hello World")


if __name__ == "__main__":
    SimpleApp().run()
