#!/usr/bin/env python3.5
import sys
import mimetypes

import kivy
kivy.require('1.9.1')
from kivy.config import Config
Config.set('kivy', 'desktop', 1)
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty

from editorcontainer.editorcontainer import EditorContainer
from menubar.menubar import MenuBar
from footer.footer import Footer
from kivyloader import load_all_kv_files


class Container(BoxLayout):

    menu_bar = ObjectProperty(None)
    editor_container = ObjectProperty(None)
    footer = ObjectProperty(None)
    
    def build_text_editor(self):
             
        # Send editorcontainer to menubar and from there propapagate it
        self.menu_bar.propagate_editor_container(self.editor_container)
        # Send editorcontainer to footer and from there propapagate it
        self.footer.propagate_editor_container(self.editor_container)
        

class AzaharTEAApp(App):
 
    columns = NumericProperty(10)
    rows = NumericProperty(1)   
    
    mime_type = None
    
    def build(self):
        
        load_all_kv_files()
        
        container = Container()
        container.build_text_editor()

        return container

if __name__ == '__main__':

    app = AzaharTEAApp()
    
    # See if a file was opened directly to get the mime type and open 
    # it with the correct lexer
    if len(sys.argv) > 1:
        mime_type, encoding = mimetypes.guess_type(sys.argv[1])
        app.mime_type = mime_type
        print(mime_type, encoding)
        
    app.run()

