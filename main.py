#Try to use a crash script like the following

#spec file should include txt files
# (list) Source files to include (let empty to include all the files)
#source.include_exts = txt,jpeg,py,png
if_error_use_this_script="""
from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDScreen:
    MDBoxLayout:
        padding: dp(10)
        orientation: "vertical"
        MDLabel:
            text: "AAAA"
'''
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
Test().run()
"""
try:
    exec(open("main.txt").read())
    
except Exception as e:
    exec(if_error_use_this_script.replace("AAAA",str(e)))

#In case something fails the script will say the error without crashing the app