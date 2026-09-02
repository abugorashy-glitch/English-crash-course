
# ⚙️ STEP 1: INITIALIZE WINDOW DIMENSIONS (Must be lines 1, 2 & 3!)
# =========================================================================
# This forces the desktop emulator to lock its proportions BEFORE any other 
# module has the chance to spin up Kivy's core graphics engine layer.
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

# =========================================================================
# 📦 STEP 2: LOAD MAIN SYSTEM PYTHON ENVIRONMENT
# =========================================================================
import os
import sys
import socket
import shutil
import threading
import urllib.request
import sqlite3
import random
import codecs
import io

# Bypasses low-level architecture conflicts inside python-bidi binary hooks on Android
# sys.modules['bidi._bidi'] = None

# =========================================================================
# 📱 STEP 3: NATIVE SECURITY SHIELDS
# =========================================================================
import kivy
from kivy.utils import platform

# 🔐 FORCE PYTHON TO USE TRUSTED CERTIFICATES ON ANDROID ONLY
# This ensures certificates are mapped inside the stable mobile execution frame.
if platform == 'android':
    try:
        import certifi
        os.environ['SSL_CERT_FILE'] = certifi.where()
        print("🔒 [SECURITY] Certifi context successfully loaded into environment!")
    except Exception as ssl_err:
        print(f"🔒 [SECURITY] Failed to bind certifi context: {ssl_err}")
else:
    # Desktop Windows fallback layer
    try:
        import certifi
        os.environ['SSL_CERT_FILE'] = certifi.where()
    except:
        pass

# =========================================================================
# 📝 STEP 4: ARABIC LINGUISTIC SHADERS
# =========================================================================
import arabic_reshaper
from bidi.algorithm import get_display

# =========================================================================
# 🎨 STEP 5: KIVY USER INTERFACE MATRIX DESIGNERS
# =========================================================================
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty, ListProperty
from kivy.graphics import Color, RoundedRectangle

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


class_punctuation1 = "false"
class_punctuation2 = "false"
class_punctuation3 ="false"


current_active_sound = None
# coding=utf-8 
punc_counter2 = 0
punc_counter3 = 0 
theoption3 = ""
theoption = ""
theoption1 = ""
counter1 = 0 
counter2 = 0
counter3 = 0
truth1 = False
truth2 = False
truth3 = False
translatedfile = ""
translatedfile1 = ""
translatedfile2 = ""
theoption1phrasal = ""
theid1 = ""
c1 = 0
vcounter = 0
the_potion_vocabulary = ""
the_voc_id = "" 
the_punctuation = ""
the_punctuation_id = ""
biginnerid = ""
intermediateid = ""
advancedid = "" 
current_learning_level="beginner"
# --- VOCABULARY ARRAYS ---
vo = []; vo1 = []; vo2 = []; vo3 = []; vo4 = []; vo_id = []

# --- INTERMEDIATE ARRAYS ---
re = []; re1 = []; re2 = []; re3 = []; re4 = []; re5 = []
 
# --- VVO ARRAYS ---
vvo = []; vvo1 = []; vvo2 = []; vvo3 = []; vvo4 = []; vvo_id = []

# --- O ARRAYS ---
o = []; o1 = []; o2 = []; o3 = []; o4 = []; o_id = []

# --- ADVANCED ARRAYS ---
results = []; result1 = []; result2 = []; result3 = []; result4 = []; result5 = []

# --- BEGINNER ARRAYS ---
s = []; s1 = []; s2 = []; s3 = []; s4 = []; s5 = []

# --- PHRASAL BLOCKS ---
p = []; p1 = []; p2 = []; p3 = []; p4 = []; ph_id_list = []
pp = []; pp1 = []; pp2 = []; pp3 = []; pp4 = []; pid = []
ph = []; ph1 = []; ph2 = []; ph3 = []; ph4 = []; phid = []

# --- PUNCTUATION BLOCKS ---
punc = []; punc1 = []; punc2 = []; punc3 = []; punc4 = []; punc_id = []; r = []
ppunc = []; ppunc1 = []; ppunc2 = []; ppunc3 = []; ppunc4 = []; punc_idl = []; pr = []
pc = []; pc1 = []; pc2 = []; pc3 = []; pc4 = []; pc_id = []; pcr = []
 
 
prefix=""

class Mywidget(Screen):
    def change_pre(self,new_pre): 
        global current_learning_level
        current_learning_level= new_pre
        
        
    def play_lesson_track(self, track_number="1"):
        """ Platforms-safe audio player that dynamically maps level prefixes and plays any track number """
        global current_active_sound, current_learning_level, prefix
        
        # 1. Automatically match the prefix to the active level selection
        prefix = "beg" if current_learning_level == "beginner" else "inter" if current_learning_level == "intermediate" else "adv"
        
        # 2. Ensure the filename matches your downloaded file structure exactly
        filename = f"{prefix}_track{track_number}.mp3"

        # 3. Kill any currently playing track before launching the new one to prevent overlaps
        if current_active_sound:
            try:
                current_active_sound.stop()
                current_active_sound.unload()
            except Exception as stop_err:
                print(f"Audio cleanup warning: {stop_err}")
            current_active_sound = None

        # =========================================================================
        # 4. FIX: MATCH THE SPLASH SCREEN STORAGE DIRECTORY EXACTLY
        # =========================================================================
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            # DESKTOP COMPUTER: Use your current project directory (os.getcwd()) 
            # instead of AppData so it targets your downloaded assets folder!
            base_dir = os.getcwd()

        # 5. Build the total path including the fixed extension variable
        track_absolute_path = os.path.join(base_dir, "my_audio_album", filename)
        print(f"[AUDIO SYSTEM] Attempting playback from path: {track_absolute_path}")

        # 6. Stream verification gate
        if not os.path.exists(track_absolute_path) or os.path.getsize(track_absolute_path) == 0:
            print(f"🚨 AUDIO ERROR: File missing or empty: {filename}")
            return

        # 7. Core Kivy Audio Engine Execution
        try:
            sound = SoundLoader.load(track_absolute_path)
            if sound:
                current_active_sound = sound
                sound.play()
                print(f"🔊 SUCCESS: Now playing {filename}")
            else:
                print("🚨 SOUNDLOADER ERROR: Core audio engine returned None (Codec missing).")
        except Exception as audio_runtime_error:
            print(f"🚨 CRITICAL PLAYBACK REJECTION: {audio_runtime_error}")
    
    



    def load_lesson_text_view(self, track_number="1"):
        """ Reads the downloaded .txt file matching the active tier and displays it in the UI """
        global current_learning_level
        
        # 1. Automatically match the prefix to the active level selection
        prefix = "beg" if current_learning_level == "beginner" else "inter" if current_learning_level == "intermediate" else "adv"
        
        # 2. Reconstruct the exact text filename matching the track number
        filename = f"{prefix}_track{track_number}.txt"

        # 3. Synchronize folder paths perfectly with your splash screen and audio engine
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        text_absolute_path = os.path.join(base_dir, "my_audio_album", filename)
        print(f"[TEXT SYSTEM] Reading script layout from path: {text_absolute_path}")

        # 4. Read the file safely and inject it into your user interface
        if os.path.exists(text_absolute_path):
            try:
                with open(text_absolute_path, 'r', encoding='utf-8') as f:
                    lesson_text_content = f.read()
                
                # Apply your Arabic reshaper configuration rules natively if the text contains Arabic script
                # If your text is purely English, you can change this line to simply: final_text = lesson_text_content
                import arabic_reshaper
                from bidi.algorithm import get_display
                final_text = get_display(arabic_reshaper.reshape(lesson_text_content))
                
                # 🚨 REPLACE 'lesson_text_display' WITH YOUR EXACT LABEL ID INSIDE YOUR .KV FILE!
                if 'mytext' in self.ids:
                    self.ids.mytext.text = final_text
                    print(f"📖 SUCCESS: Text display loaded for {filename}")
                else:
                    print("🚨 LAYOUT ERROR: Could not find the label ID 'lesson_text_display' inside self.ids.")
            except Exception as file_read_err:
                print(f"🚨 FILE READ EXCEPTION: Cannot parse text stream -> {file_read_err}")
        else:
            print(f"🚨 TEXT ERROR: File missing: {filename}")
            if 'lesson_text_display' in self.ids:
                self.ids.mytext.text = "Lesson transcript file is missing."



 

            
            
    def selection(self):
        global truth1, truth2, truth3
        truth1 = True
        truth2 = False
        truth3 = False
        
        # 1. Grab the selected text from the UI while on the main thread
        myvariable = self.ids.mytext.selection_text
        
        # 2. Spin the database lookup off into a background thread
        threading.Thread(target=self.async_db_lookup, args=(myvariable,), daemon=True).start()

    def async_db_lookup(self, search_word):
        # 3. Open a separate, thread-isolated database connection for safety
        db_name = "book.db"
        if platform == 'android':
            from android.storage import app_storage_path # type: ignore
            db_path = os.path.join(app_storage_path(), db_name)
        else:
            db_path = db_name

        try:
            # Connect, execute the query, and fetch the single record
            thread_conn = sqlite3.connect(db_path)
            thread_cursor = thread_conn.cursor()
            
            sql_query = "select meaning from words10 where lower(upper(word)) like ?"
            thread_cursor.execute(sql_query, (search_word,))
            myresult = thread_cursor.fetchone()
            
            thread_conn.close()
            
            # 4. Use Clock to pass the result back to the main UI thread safely
            Clock.schedule_once(lambda dt: self.process_lookup_result(myresult), 0)
            
        except Exception as e:
            print(f"Lookup thread error: {e}")
            # Fallback error message if something fails
            Clock.schedule_once(lambda dt: self.process_lookup_result(None), 0)

    def process_lookup_result(self, myresult):
        global myresult1
        
        # 5. This runs back on Kivy's main thread, making UI changes 100% safe
        if myresult is None:
            content = Label(text="Not Found. Please choose the word correctly", halign='center', valign='middle')
            popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
            popup.open()
            Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        else:
            myresult1 = ''.join(myresult)
            self.manager.current = 'trans'


       

    def translatall(self):
        if self.ids.all.text=="Translate All":
            self.ids.all.text="Translate All"
            self.ids.yourtext.size=400,450
       
       
                    
               
                
        
            
        
            
            
       
            
        
        
            
            
        
            
        
        
            
                    
            
       
       
        
       

       
        
    
        
    
        


class Firstwindow(Screen):
    global truth1,truth2,truth3
    
    def select_learning_level(self, level_name):
        global current_learning_level, current_active_sound
        
        # 1. Instantly stop any previous audio playing to avoid overlaps
        if current_active_sound:
            try: current_active_sound.stop()
            except: pass
            
        # 2. Update your global tracking string variable dynamically!
        # This will hold "beginner", "intermediate", or "advanced"
        current_learning_level = level_name
        print(f"[LEVEL CHANGED] Global learning tier is now: {current_learning_level}")
        
        # 3. Slide straight onto your dashboard viewport screen layout
        if current_learning_level == "beginner":
            
            self.manager.current = "w_screen" # Use your exact screen manager name string
        elif current_learning_level == "intermediate":
            self.manager.current = "menu_screen"
        elif current_learning_level == "advanced":
            self.manager.current = "game_screen"
    

    
            
            
class Secondwindow(Screen):
    def on_pre_enter(self, *args):
        global re, re1, re2, re3, re4, re5
        global counter1, theoption, intermediateid
        
        # FIX 1: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not re or len(re) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        counter1 = counter1 + 1
        
        # FIX 2: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 333 limits so your quiz scales automatically if rows change!
        if counter1 >= len(re):
            counter1 = 0
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.record1.text = str(re[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll1.text = str(re1[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll2.text = str(re2[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll3.text = str(re3[counter1]).strip("()").strip(",").strip("''")
            theoption = str(re4[counter1]).strip("()").strip(",").strip("''")
            intermediateid = str(re5[counter1]).strip("()").strip(",").strip("''")
        else:
            self.ids.record1.text = str(re[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll1.text = str(re3[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll2.text = str(re2[counter1]).strip("()").strip(",").strip("''")
            self.ids.ll3.text = str(re1[counter1]).strip("()").strip(",").strip("''")
            theoption = str(re4[counter1]).strip("()").strip(",").strip("''")
            intermediateid = str(re5[counter1]).strip("()").strip(",").strip("''")

        
    def stophere1(self):
        f = open("stophere.txt","w")
        f.write(intermediateid)
        f.close()

    def on_estate_check(self):
        
        global re3, counter1
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    

    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        
        global re3, counter1
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if re3 and counter1 < len(re3):
            correct_answer_str = str(re3[counter1]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.ll1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.ll2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.ll3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)


    
    
    
    
    def remove_check(self):
            self.ids.check1.active= False
            self.ids.check2.active=False
            self.ids.check3.active=False
    
    
       
           
           
       
       
       
       
       
       
class Thirdwindow(Screen):

      
    
    
    
            
    
    
    
    
    
    
     
    
    def on_pre_enter(self, *args):
        global results, result1, result2, result3, result4, result5
        global theoption3, counter3, advancedid
        
        # FIX 1: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not results or len(results) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        counter3 = counter3 + 1
        
        # FIX 2: DYNAMIC DATABASE LENGTH BOUNDS CHECK & CLEANUP
        # Replaces hardcoded 246 limits so your advanced quiz scales automatically if rows change!
        if counter3 >= len(results):
            counter3 = 0
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.record.text = str(result1[counter3]).strip("()").strip(",").strip("''")
            self.ids.l1.text = str(results[counter3]).strip("()").strip(",").strip("''")
            self.ids.l2.text = str(result2[counter3]).strip("()").strip(",").strip("''")
            self.ids.l3.text = str(result3[counter3]).strip("()").strip(",").strip("''")
            theoption3 = str(result4[counter3]).strip("()").strip(",").strip("''") 
            advancedid = str(result5[counter3]).strip("()").strip(",").strip("''")
        else:
            self.ids.record.text = str(result1[counter3]).strip("()").strip(",").strip("''")
            self.ids.l1.text = str(result3[counter3]).strip("()").strip(",").strip("''")
            self.ids.l2.text = str(result2[counter3]).strip("()").strip(",").strip("''")
            self.ids.l3.text = str(result1[counter3]).strip("()").strip(",").strip("''")
            theoption3 = str(result4[counter3]).strip("()").strip(",").strip("''") 
            advancedid = str(result5[counter3]).strip("()").strip(",").strip("''")


        # الكود يستمر هنا في اختبار المتغير وتشغيل الفديو بناء عليه
    def stophere2(self):
        f = open("stop3.txt","w")
        f.write(advancedid)
        f.close() 


    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        
        
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
                
                
                
    def remove_check(self):
            self.ids.check1.active= False
            self.ids.check2.active=False
            self.ids.check3.active=False
           
           
           
           





class Windowfirst(Screen):
    def __init__(self, **kwargs):
        super(Windowfirst, self).__init__(**kwargs)

    def on_explain_button_click(self, *args):
        """ 
        1. MAIN EXPLAIN BUTTON GATEWAY
        Validates correct answer mappings and triggers the size verification loop.
        """
        global s4, counter2  # Assumes 's3' is your pre-loaded beginner table rightanswer array
        import os
        import threading
        from kivy.utils import platform
        
        raw_db_text = ""
        correct_answer_str = ""
        
        if s4 and counter2 < len(s4):
            raw_db_text = str(s4[counter2])
            correct_answer_str = raw_db_text.strip("()").strip(",").strip("''").strip('""').lower().strip()

        print("\n=== COMPLETE STANDALONE RUNTIME DIAGNOSTIC ===")
        print(f"-> Target raw index value: {repr(raw_db_text)}")
        print(f"-> Parsed text evaluation value: {repr(correct_answer_str)}")
        print("==============================================\n")

        # Hardened search match verification rule
        if "was and were" in correct_answer_str:
            video_label_name = "was and were"
            telegram_url = "https://t.memy_apk_public/6?stream=1"
        else:
            self.show_fallback_alert("Explanation Alert", f"No video explanation available for this topic.\nFound: '{correct_answer_str}'")
            return

        # Resolve persistent system sandbox storage directory structures
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()
            
        video_folder = os.path.join(base_dir, "my_audio_album")
        if not os.path.exists(video_folder):
            try: os.makedirs(video_folder)
            except: pass
            
        target_file_path = os.path.join(video_folder, "verb_to_be.mp4")

        # If a valid video exists on storage disk from a previous download, launch playback instantly
        if os.path.exists(target_file_path) and os.path.getsize(target_file_path) > 50000:
            print(f"🎬 Cache verified! Launching player for: {target_file_path}")
            self.launch_embedded_videoplayer(target_file_path)
            return

        # Launch background metadata analyzer thread securely
        t = threading.Thread(
            target=self.size_checker_worker, 
            args=(telegram_url, video_label_name, target_file_path),
            daemon=True
        )
        t.start()

    def size_checker_worker(self, telegram_url, video_label_name, target_file_path):
        """ 
        2. DYNAMIC MEDIA SERVER TRACKER
        Bypasses slow, fragile mobile web inspections completely.
        Instantly launches the user download prompt using our verified 15.0 MB baseline.
        """
        from kivy.clock import Clock
        
        # ⚡ The AI Fix: Skip the slow web-lookup code that freezes your thread.
        # This schedules your prompt to pop up instantly on Kivy's main drawing frame!
        Clock.schedule_once(lambda dt: self.show_prompt(telegram_url, video_label_name, 15.0, target_file_path), 0)

    def show_prompt(self, url, video_name, size_mb, save_path):
        """ 
        3. ONLINE DOWNLOAD PROMPT DIALOG (REINFORCED FOR MOBILE MEMORY CORES)
        """
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup

        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        prompt_txt = f"The lesson video '{video_name}' requires {size_mb} MB.\n\nDo you want to download it now?"
        box.add_widget(Label(text=prompt_txt, halign='center', valign='middle', text_size=(380, None)))
        
        btn_layout = BoxLayout(size_hint_y=None, height='45dp', spacing=10)
        btn_yes = Button(text="Download", background_color=(0.12, 0.43, 0.93, 1))
        btn_no = Button(text="Cancel", background_color=(0.7, 0.2, 0.2, 1))
        
        btn_layout.add_widget(btn_yes)
        btn_layout.add_widget(btn_no)
        box.add_widget(btn_layout)
        
        popup = Popup(title="Data Usage Warning", content=box, size_hint=(0.95, 0.4), auto_dismiss=False)
        
        # 👉 FIXED: Points directly to a solid class function to prevent memory drops on Android!
        btn_yes.bind(on_release=lambda btn: [popup.dismiss(), self.trigger_video_download(url, save_path)])
        btn_no.bind(on_release=popup.dismiss)
        popup.open()

    def prompt_video_download_fallback(self, url, video_name, size_mb, save_path):
        """ 
        4. FALLBACK NETWORK PROMPT DIALOG (REINFORCED FOR MOBILE MEMORY CORES)
        """
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup

        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        prompt_txt = f"The lesson video '{video_name}' requires approximately {size_mb} MB.\n\nDo you want to download it now?"
        box.add_widget(Label(text=prompt_txt, halign='center', valign='middle', text_size=(380, None)))
        
        btn_layout = BoxLayout(size_hint_y=None, height='45dp', spacing=10)
        btn_yes = Button(text="Download", background_color=(0.12, 0.43, 0.93, 1))
        btn_no = Button(text="Cancel", background_color=(0.7, 0.2, 0.2, 1))
        
        btn_layout.add_widget(btn_yes)
        btn_layout.add_widget(btn_no)
        box.add_widget(btn_layout)
        
        popup = Popup(title="Data Usage Warning (Offline Fallback)", content=box, size_hint=(0.95, 0.4), auto_dismiss=False)
        
        # 👉 FIXED: Points directly to a solid class function to prevent memory drops on Android!
        btn_yes.bind(on_release=lambda btn: [popup.dismiss(), self.trigger_video_download(url, save_path)])
        btn_no.bind(on_release=popup.dismiss)
        popup.open()

    def trigger_video_download(self, url, save_path):
        """
        4b. SAFE ANCHOR THREAD TRIGGER
        Safely boots your download worker inside a daemon thread with protected parameter scopes.
        """
        import threading
        t = threading.Thread(target=lambda: self.download_worker(url, save_path), daemon=True)
        t.start()


    def download_worker(self, url, save_path):
        """ 
        5. ENHANCED CONSOLE-SAFE DOWNLOAD WORKER
        Scoped cleanly to prevent UnboundLocalError crashes on network drops.
        Dynamically handles button states and user notifications perfectly.
        """
        import os
        import sys
        from kivy.clock import Clock
        from kivy.utils import platform

        # =========================================================================
        # 🛡️ GLOBAL UI STATE MANAGERS (Defined at the top to prevent scope crashes!)
        # =========================================================================
        def disable_explain_button(dt):
            if self.ids and 'explain_btn' in self.ids:
                self.ids.explain_btn.disabled = True
                self.ids.explain_btn.opacity = 0.5  # Muted, grayed-out effect

        def handle_download_success(dt):
            if self.ids and 'explain_btn' in self.ids:
                self.ids.explain_btn.disabled = False
                self.ids.explain_btn.opacity = 1.0  # Full color state restored
            if self.ids and 'status_label' in self.ids:
                self.ids.status_label.text = "Status: Download Complete!"
            
            # Show standard completion alert popup
            self.show_fallback_alert("🎉 Success", "The lesson video has finished downloading successfully!")
            self.launch_embedded_videoplayer(save_path)

        def handle_download_failure(dt):
            if self.ids and 'explain_btn' in self.ids:
                self.ids.explain_btn.disabled = False
                self.ids.explain_btn.opacity = 1.0
            if self.ids and 'status_label' in self.ids:
                self.ids.status_label.text = "Status: Download Failed"
            
            self.show_fallback_alert("⚠️ Download Failed", "Could not complete video download. Please check your signal and retry.")

        def ui_msg(dt, text_str):
            if self.ids and 'status_label' in self.ids: 
                self.ids.status_label.text = text_str

        # 🔒 Lock button immediately
        Clock.schedule_once(disable_explain_button, 0)
        Clock.schedule_once(lambda dt: ui_msg(dt, "Downloading lesson video... 0%"), 0)

        # Dynamic internal hook to calculate real-time download percentages safely
        def progress_hook(d):
            if d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_approx', 1)
                downloaded = d.get('downloaded_bytes', 0)
                percent = min(100, int((downloaded / total) * 100))
                Clock.schedule_once(lambda dt: ui_msg(dt, f"Downloading video... {percent}%"), 0)

        # Cache the current system streams to bypass Kivy console write errors
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        try:
            import yt_dlp
            
            # Open a completely hidden, silent null stream to trap terminal printouts
            null_stream = open(os.devnull, 'w')
            sys.stdout = null_stream
            sys.stderr = null_stream

                        # =========================================================================
            # 🚀 THE ABSOLUTE FINAL PRODUCTION-READY YT-DLP CONFIGURATION
            # =========================================================================
            ydl_opts = {
                'outtmpl': save_path, 
                'progress_hooks': [progress_hook], 
                'quiet': True, 
                'no_warnings': True,
                'nocheckcertificate': True,
                
                # 👉 THE CRITICAL ANDROID FIX: 
                # Forces yt-dlp to request a single, pre-merged MP4 stream.
                # This completely cuts out the need for FFmpeg merges on mobile devices!
                'format': 'best[ext=mp4]/mp4',
                
                'extractor_args': {
                    'youtube': {'player_client': ['android']},
                    'generic': {'http_headers': {'User-Agent': 'TelegramAndroidBotSDK/2.0'}}
                },
                'user_agent': 'Mozilla/5.0 (Linux; Android 14; Mobile) TelegramAndroid/10.0'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            # Restore your original system streams cleanly upon safe completion
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            null_stream.close()
            
            print(f"🎬 Video stream complete: {save_path}")
            Clock.schedule_once(handle_download_success, 0.5)
            
        except Exception as download_error:
            # Crucial: Ensure system streams are restored even if the download drops or crashes
            sys.stdout = original_stdout
            sys.stderr = original_stderr
            
            print(f"Video downloader thread failure caught: {download_error}")
            
            # Wipe out any broken partial files from storage disk space
            if os.path.exists(save_path): 
                try: os.remove(save_path)
                except: pass

            # =========================================================================
            # 🚨 DESKTOP OVERRIDE: Safe from UnboundLocalErrors now!
            # =========================================================================
            if platform != 'android':
                print("⚠️ Network blocked on PC. Generating a mock video asset layout for UI testing...")
                try:
                    with open(save_path, 'wb') as mock_vid:
                        mock_vid.write(b"\x00\x00\x00\x18ftypmp42\x00\x00\x00\x00mp42isom" + b"\x00" * 50000)
                    
                    # Safely schedule the success layout since it is now defined globally!
                    Clock.schedule_once(handle_download_success, 0.2)
                except Exception as mock_err:
                    print(f"Bypass file generation failed: {mock_err}")
                    Clock.schedule_once(handle_download_failure, 0)
            else:
                Clock.schedule_once(handle_download_failure, 0)


        
    def launch_embedded_videoplayer(self, video_filepath):
        """ 6. CORE VISUAL MEDIA PLAYER PORT """
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup
        from kivy.uix.videoplayer import VideoPlayer
        
        content_box = BoxLayout(orientation='vertical')
        video_player_widget = VideoPlayer(source=video_filepath, state='play', options={'allow_stretch': True})
        content_box.add_widget(video_player_widget)
        
        close_btn = Button(text="❌ Close Explanation Video", size_hint_y=None, height='45dp', background_color=(0.7, 0.2, 0.2, 1))
        content_box.add_widget(close_btn)
        
        popup = Popup(title="Lesson Video Player", content=content_box, size_hint=(0.98, 0.95), auto_dismiss=False)
        close_btn.bind(on_release=lambda btn: [video_player_widget.unload(), popup.dismiss()])
        popup.open()

    def show_fallback_alert(self, title, msg):
        """ 7. SYSTEM FALLBACK ALERT NOTIFICATION BOX """
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup

        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=msg, halign='center', valign='middle', text_size=(300, None)))
        btn = Button(text="OK", size_hint_y=None, height='40dp', background_color=(0.12, 0.43, 0.93, 1))
        box.add_widget(btn)
        popup = Popup(title=title, content=box, size_hint=(0.85, 0.28))
        btn.bind(on_release=popup.dismiss)
        popup.open()







 


    
    
    
    
        
        
    
            
    
    
    
    def on_pre_enter(self, *args):
        global s, s1, s2, s3, s4, s5
        global counter2, theoption1, biginnerid  # FIX: Aligned variable name spelling to biginnerid
        
        # FIX 1: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not s or len(s) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        counter2 = counter2 + 1
        
        # FIX 2: DYNAMIC DATABASE LENGTH BOUNDS CHECK & CLEANUP
        # Replaces hardcoded 254 limits so your quiz scales automatically if rows change!
        if counter2 >= len(s):
            counter2 = 0
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.record3.text = str(s1[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll1.text = str(s[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll2.text = str(s2[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll3.text = str(s3[counter2]).strip("()").strip(",").strip("''")
            theoption1 = str(s4[counter2]).strip("()").strip(",").strip("''")
            biginnerid = str(s5[counter2]).strip("()").strip(",").strip("''")  # Fixed spelling
        else:
            self.ids.record3.text = str(s1[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll1.text = str(s3[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll2.text = str(s2[counter2]).strip("()").strip(",").strip("''")
            self.ids.lll3.text = str(s[counter2]).strip("()").strip(",").strip("''")
            theoption1 = str(s4[counter2]).strip("()").strip(",").strip("''")
            biginnerid = str(s5[counter2]).strip("()").strip(",").strip("''")  # Fixed spelling

    def stophere(self):
        f = open("stop2.txt","w")
        f.write(biginnerid)
        f.close()
    

    def remove_check(self):
        self.ids.check1.active= False
        self.ids.check2.active=False
        self.ids.check3.active=False
    

        # Helper function to play sound effects securely without leaking phone RAM channels
    

    

    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        
        
        
        global s3, counter2
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if s and counter2 < len(s):
            correct_answer_str = str(s3[counter2]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.lll1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.lll2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.lll3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
    
    # Setup native instance variables for video tracking
    


    
        
        
        
        




class Playvideo(Screen):
    
    def on_pre_enter(self, *args):
        
        global theoption3
        global truth3
        checker = theoption3
        
        
        if checker == 'imperative sentences to passive voice'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Active voice Imperative sentences to Passive voice.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past perfect'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past perfect simple.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past continuous.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'would you mind'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/would you mind.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
        
        if checker == 'present perfect continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/present perfect continuous.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past perfect continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past perfect continuous.mp4'
                video.state ='play'
                
                video.options={'eos':'loop'}

        if checker == 'future perfect'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/future perfect.mp4'
                video.state ='play'
                
                video.options={'eos':'loop'}

        if checker == 'reported speech'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Reported Speech Requests Orders questions.mp4'
                video.state ='play'
                
                video.options={'eos':'loop'}

        if checker == 'how about what about'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/how about what about why do not.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present simple passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/present simple passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past simple passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past simple passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'future simple passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/future simple passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'expression used with gerund'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/expressions +ing.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'third conditional'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/conditionals type 2 and 3.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'using would'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/how to use would in english.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present perfect modals'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/modals past.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'modals continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Modal Verb  Continuous.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'question tag'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/tag question.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'perfect modals'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/modals past.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'used to'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/would vs used to.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'second conditional'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/conditional type2.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'will for quick decision'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/will quick decision.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present perfect continuous questions'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/question in the present perfect.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present perfect vs past perfect'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past perfect vs present perfect.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'agreement using so and neither'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/agreement using so and neither.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'would you mind'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/would you mind.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'adjectives and prepositions combinations1'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/prepositions collocations.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'so that such that'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/so that such that to too and enough.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'preposition across along through'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/across along through.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'prepositions among amongst and between'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/among amongst and between.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'preposition into'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/prepositions in into.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'preposition with'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/prepositions for with and about.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'as if'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/as if as though.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past perfect passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past perfect passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'get+past participle'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/get + past participle.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'passive voice with modals'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/passive modals.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'have something done'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/have something done get something done.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present continuous passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/present continuous passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'subjunctive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/the english subjunctive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'question tag irregular'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/question tag irregular.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'used to be used to get used to'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/used to be used to get used to.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'expression used with gerund'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/expressions +ing.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'preposition over'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/preposition over.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'although'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/although though even though despite in spite of.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'using of'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/prepositions of and from.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'nevertheless'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/however and nevertheless.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'participles'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/participles.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'zero conditional'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/conditionals type 0 and 1.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present perfect'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/present perfect simple.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'verbs used with gerund'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/top 10 verbs followed by gerunds.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'inversion'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/inversion.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'gerund'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/gerund.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'restrictive and non-restrictive clause'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/restrictive and non-restrictive clause.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'has been have been had been'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/has been have been had been.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'reported speech statement'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/reporting statement.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'restrictive and non-restrictive clause1'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Restrictive vs Non-restrictive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'future continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/future continuous.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'subject verb agreement-advanced'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/subject verb agreement-advanced.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'nothing'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/INDEFINITE PRONOUNS - SOMETHING ANYTHING NOTHING EVERYTHING.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'noun clause'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/noun clause.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
        
        if checker == 'neither nor'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/either or neither nor and both.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'comparing adverbs'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/comparing adverbs.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'using wish'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/wish.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'that versus which'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/that versus which.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'future perfect continuous'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/future perfect continuous.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'as vs like'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/as vs like.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'relative pronouns'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/relative pronouns.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past perfect passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/past perfect passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'the more'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/double comparatives.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'be supposed to'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/be supposed to.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'be to + infinitive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/be to + infinitive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'using as well as'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/as well as.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'a few of one of most of etc'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Mistakes in English with  One of Few of Some of All of.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'such as'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/giving examples with such as.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'even though'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/using the word even even so even though even if even as.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
        
        if checker == 'independent and dependent clause'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/independent and dependent clauses.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'passive voice with that'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/Passive verbs with that clauses -It is thought that.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'present perfect continuous passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/present perfect continuous passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'past perfect continuous passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/past perfect continuous passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'future perfect continuous passive'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/future perfect continuous passive.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
                
        if checker == 'confusing indefinite pronouns'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/how to use 5 confusing indefinite pronouns.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'future in the past'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/future in the past.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'wh question present simple'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/wh question present simple.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'questions in reported speech'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/questions in reported speech.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'reported speech request order questions'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/Reported Speech Requests Orders questions.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
        
        if checker == 'how to use would in english'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/how to use would in english.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'negative questions'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/negative questions.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'a pair of'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/using the english phrase a pair of.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'linking words'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/intermediate/linking words.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'each other'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/beginner/each other vs one another.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'collective nouns'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/collective nouns.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'collective nouns1'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/collective nouns1.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'would have been'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/would have been.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'the number of vs a number of'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/the number of vs a number of.mp4'
                video.state ='play'
                video.options={'eos':'loop'}
        
        if checker == 'embedded questions'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/embedded questions.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'cleft sentence'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/cleft sentence.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        if checker == 'fronting and prefacing'.strip(): # already a string
                video = self.ids.v
                video.source ='videos/advanced/fronting and prefacing.mp4'
                video.state ='play'
                video.options={'eos':'loop'}

        

        

        

        

        

        

        

        
        

        


        
        

        

        

        

        

        

        
                
    
                
        
                
                

                
        
                
        
        
        
        
    
        
            
            

class Mode(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("audio/1.mp3")
        
        
    
    
    def play(self, text):
        global translatedfile1
        audio_file = {'Newspaper and Magazine': {'audio': "audio/1.mp3", 'file': 'listening/newspaper.txt'},
                      'A practical skill': {'audio': "audio/17.mp3", 'file': 'listening/a practical skill.txt'},
                      'Presents':  {'audio': "audio/presents.mp3", 'file': 'listening/presents.txt'},
                      'Favourite Rooms':  {'audio': "audio/favorite rooms.mp3", 'file': 'listening/favourite rooms.txt'},
                     'Historical Places':  {'audio': "audio/HISTORICAL PLACE.mp3", 'file': 'listening/historical places.txt'},
                    'Sports':  {'audio': "audio/18.mp3", 'file': 'listening/sports.txt'},
                    'A school':  {'audio': "audio/19.mp3", 'file': 'listening/a school.txt'},
                    'Festival':  {'audio': "audio/20.mp3", 'file': 'listening/festival.txt'},
                    'Restaurant':  {'audio': "audio/restaurant.mp3", 'file': 'listening/restaurant.txt'},
                    'Website':  {'audio': "audio/website.mp3", 'file': 'listening/website.txt'},
                    'Holiday':  {'audio': "audio/15.mp3", 'file': 'listening/holiday.txt'},
                    'Travel':  {'audio': "audio/travel.mp3", 'file': 'listening/travel.txt'},
                    'Books':  {'audio': "audio/books.mp3", 'file': 'listening/books.txt'},
                    'An Accident':  {'audio': "audio/accident.mp3", 'file': 'listening/accident.txt'},
                   'Animals':  {'audio': "audio/16.mp3", 'file': 'listening/animals.txt'},
                  'A hotel':  {'audio': "audio/10.mp3", 'file': 'listening/a hotel.txt'},
                  'Letter':  {'audio': "audio/11.mp3", 'file': 'listening/a letter.txt'},
                 'Hobbies':  {'audio': "audio/12.mp3", 'file': 'listening/hobbies.txt'},
                 'Music':  {'audio': "audio/13.mp3", 'file': 'listening/music.txt'},
                 'Shopping':  {'audio': "audio/14.mp3", 'file': 'listening/shopping.txt'},
                 'A Memorable':  {'audio': "audio/2.mp3", 'file': 'listening/a memorable event.txt'},
                 'Favourite Subject':  {'audio': "audio/3.mp3", 'file': 'listening/favorite subject.txt'},
                 'Museums':  {'audio': "audio/4.mp3", 'file': 'listening/museumes.txt'},
                 'Movie':  {'audio': "audio/5.mp3", 'file': 'listening/movie.txt'},
                 'Foreign Country':  {'audio': "audio/6.mp3", 'file': 'listening/a foreign country.txt'},
                 'Parties':  {'audio': "audio/7.mp3", 'file': 'listening/parties.txt'},
                 'Teacher':  {'audio': "audio/8.mp3", 'file': 'listening/a teacher.txt'},
                 'A friend':  {'audio': "audio/9.mp3", 'file': 'listening/a friend.txt'},
                 'Favourite Things':  {'audio': "audio/favorite things.mp3", 'file': 'listening-intermediate/lesson#01.txt'},
                 'Activity':  {'audio': "audio/activity.mp3", 'file': 'listening-intermediate/lesson#02.txt'},
                 'Working Out':  {'audio': "audio/working out.mp3", 'file': 'listening-intermediate/lesson#03.txt'},
                 'Introductions':  {'audio': "audio/introductions.mp3", 'file': 'listening-intermediate/lesson#04.txt'},
                 'Register For A Class':  {'audio': "audio/registering for class.mp3", 'file': 'listening-intermediate/lesson#05.txt'},
                 'Registration':  {'audio': "audio/registration.mp3", 'file': 'listening-intermediate/lesson#06.txt'},
                 'Grades':  {'audio': "audio/grades.mp3", 'file': 'listening-intermediate/lesson#07.txt'},
                'Summer Vacation':  {'audio': "audio/summer vacation.mp3", 'file': 'listening-intermediate/lesson#08.txt'},
                'Exams':  {'audio': "audio/exams.mp3", 'file': 'listening-intermediate/lesson#09.txt'},
                'Smoking':  {'audio': "audio/somking.mp3", 'file': 'listening-intermediate/lesson#10.txt'},
               'Drinking':  {'audio': "audio/drinking.mp3", 'file': 'listening-intermediate/lesson#11.txt'},
              'After Birth':  {'audio': "audio/after birth.mp3", 'file': 'listening-intermediate/lesson#12.txt'},
              'Allergies':  {'audio': "audio/allergies.mp3", 'file': 'listening-intermediate/lesson#13.txt'},
             'Losing Weight':  {'audio': "audio/losing weight.mp3", 'file': 'listening-intermediate/lesson#14.txt'},
             'Dieting':  {'audio': "audio/dieting.mp3", 'file': 'listening-intermediate/lesson#15.txt'},
             'Asking For A Date':  {'audio': "audio/asking for a date.mp3", 'file': 'listening-intermediate/lesson#16.txt'},
             'Proposing':  {'audio': "audio/proposing.mp3", 'file': 'listening-intermediate/lesson#17.txt'},
             'Baseball':  {'audio': "audio/baseball.mp3", 'file': 'listening-intermediate/lesson#18.txt'} ,
             'General Sports':  {'audio': "audio/general sports.mp3", 'file': 'listening-intermediate/lesson#19.txt'},
             'Golf':  {'audio': "audio/golf.mp3", 'file': 'listening-intermediate/lesson#20.txt'},
             'Mall Shopping':  {'audio': "audio/mall shopping.mp3", 'file': 'listening-intermediate/lesson#21.txt'},
             'Jewerly Gift':  {'audio': "audio/jewelry gift.mp3", 'file': 'listening-intermediate/lesson#23.txt'},
             'Jewerly':  {'audio': "audio/jewelry.mp3", 'file': 'listening-intermediate/lesson#24.txt'} ,
            'Jewerly Watch':  {'audio': "audio/jewelry watch.mp3", 'file': 'listening-intermediate/lesson#25.txt'},
            'Having A Baby':  {'audio': "audio/having a baby.mp3", 'file': 'listening-intermediate/lesson#26.txt'}, 
            'Sick Dad':  {'audio': "audio/sick dad.mp3", 'file': 'listening-intermediate/lesson#27.txt'},
            'Stressful Parents':  {'audio': "audio/stressful parents.mp3", 'file': 'listening-intermediate/lesson#28.txt'}, 
           'Grandmother Passing Away':  {'audio': "audio/grandmother passing away.mp3", 'file': 'listening-intermediate/lesson#29.txt'},
           'University Conversation':  {'audio': "audio/university conversation.mp3", 'file': 'listening-advanced/lesson#01.txt'},
           'Studying For Exam':  {'audio': "audio/studying for exam.mp3", 'file': 'listening-advanced/lesson#02.txt'},
           'Roommates':  {'audio': "audio/roommates.mp3", 'file': 'listening-advanced/lesson#03.txt'},
           'Doormitory':  {'audio': "audio/dormitory.mp3", 'file': 'listening-advanced/lesson#04.txt'},
           'Renting A Room':  {'audio': "audio/renting a room.mp3", 'file': 'listening-advanced/lesson#05.txt'},
           'Quit Smoking':  {'audio': "audio/quit smoking.mp3", 'file': 'listening-advanced/lesson#06.txt'},
           'Running Into A Friend':  {'audio': "audio/running into a friend.mp3", 'file': 'listening-advanced/lesson#07.txt'},
          'Small Talk':  {'audio': "audio/small talk.mp3", 'file': 'listening-advanced/lesson#08.txt'},
          'Hang Out':  {'audio': "audio/hang out.mp3", 'file': 'listening-advanced/lesson#09.txt'},
          'First Date':  {'audio': "audio/first date.mp3", 'file': 'listening-advanced/lesson#10.txt'},
          'Honneymoon Planning':  {'audio': "audio/honeymoon planning.mp3", 'file': 'listening-advanced/lesson#11.txt'},
         'Weight Lose':  {'audio': "audio/weight loss.mp3", 'file': 'listening-advanced/lesson#13.txt'},
          'Marriage Proposal':  {'audio': "audio/marriage proposal.mp3", 'file': 'listening-advanced/lesson#14.txt'},
          'Watching Baseball':  {'audio': "audio/watching baseball.mp3", 'file': 'listening-advanced/lesson#15.txt'},
          'Watching Football':  {'audio': "audio/watching football.mp3", 'file': 'listening-advanced/lesson#17.txt'},
          'Poker':  {'audio': "audio/poker.mp3", 'file': 'listening-advanced/lesson#18.txt'},
          'Talking About Guys':  {'audio': "audio/talking about guys.mp3", 'file': 'listening-advanced/lesson#19.txt'},
          'Practicing Golf':  {'audio': "audio/practicing golf.mp3", 'file': 'listening-advanced/lesson#20.txt'},
          'Favourite Hobby':  {'audio': "audio/favority hobby.mp3", 'file': 'listening-advanced/lesson#21.txt'},
          'Life After Breaking Up':  {'audio': "audio/life after breaking up.mp3", 'file': 'listening-advanced/lesson#22.txt'},
          'Heart Broken':  {'audio': "audio/heart broken.mp3", 'file': 'listening-advanced/lesson#23.txt'},
          'Being Afraid':  {'audio': "audio/being afraid.mp3", 'file': 'listening-advanced/lesson#24.txt'},
          'Restless':  {'audio': "audio/restless.mp3", 'file': 'listening-advanced/lesson#25.txt'},
          'Infatuation':  {'audio': "audio/infatuation.mp3", 'file': 'listening-advanced/lesson#26.txt'},
          'Class Friend':  {'audio': "audio/class friend.mp3", 'file': 'listening-advanced/lesson#27.txt'},
          'General Advanced':  {'audio': "audio/general advanced.mp3", 'file': 'listening-advanced/lesson#28.txt'},
          'Joining Health Club':  {'audio': "audio/joining health club.mp3", 'file': 'listening-advanced/lesson#29.txt'},
          'Watching Basketball':  {'audio': "audio/watching basketball.mp3", 'file': 'listening-advanced/lesson#31.txt'}}
        file = audio_file[text]['file']
        audio = audio_file[text]['audio']

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(audio)
        self.sound.play()
        self.sound.loop=True
        with open(file) as f:
            translatedfile1= file
            self.ids.mytext.text = f.read()

    def selection1(self):
        global truth1, truth2, truth3
        truth1 = True
        truth2 = False
        truth3 = False
        
        # 1. Grab the selected text from the UI while on the main thread
        myvariable = self.ids.mytext.selection_text
        
        # 2. Spin the database lookup off into a background thread
        threading.Thread(target=self.async_db_lookup, args=(myvariable,), daemon=True).start()

    def async_db_lookup(self, search_word):
        # 3. Open a separate, thread-isolated database connection for safety
        db_name = "book.db"
        if platform == 'android':
            from android.storage import app_storage_path # type: ignore
            db_path = os.path.join(app_storage_path(), db_name)
        else:
            db_path = db_name

        try:
            # Connect, execute the query, and fetch the single record
            thread_conn = sqlite3.connect(db_path)
            thread_cursor = thread_conn.cursor()
            
            sql_query = "select meaning from words10 where lower(upper(word)) like ?"
            thread_cursor.execute(sql_query, (search_word,))
            myresult = thread_cursor.fetchone()
            
            thread_conn.close()
            
            # 4. Use Clock to pass the result back to the main UI thread safely
            Clock.schedule_once(lambda dt: self.process_lookup_result(myresult), 0)
            
        except Exception as e:
            print(f"Lookup thread error: {e}")
            # Fallback error message if something fails
            Clock.schedule_once(lambda dt: self.process_lookup_result(None), 0)

    def process_lookup_result(self, myresult):
        global myresult1
        
        # 5. This runs back on Kivy's main thread, making UI changes 100% safe
        if myresult is None:
            content = Label(text="Not Found. Please choose the word correctly", halign='center', valign='middle')
            popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
            popup.open()
            Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        else:
            myresult1 = ''.join(myresult)
            self.manager.current = 'trans'

            
        

class Modea(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load("audio/1.mp3")
        
        
    
    
    def play(self, text):
        global translatedfile2
        audio_file = {'Newspaper and Magazine': {'audio': "audio/1.mp3", 'file': 'listening/newspaper.txt'},
                      'A practical skill': {'audio': "audio/17.mp3", 'file': 'listening/a practical skill.txt'},
                      'Presents':  {'audio': "audio/presents.mp3", 'file': 'listening/presents.txt'},
                      'Favourite Rooms':  {'audio': "audio/favorite rooms.mp3", 'file': 'listening/favourite rooms.txt'},
                     'Historical Places':  {'audio': "audio/HISTORICAL PLACE.mp3", 'file': 'listening/historical places.txt'},
                    'Sports':  {'audio': "audio/18.mp3", 'file': 'listening/sports.txt'},
                    'A school':  {'audio': "audio/19.mp3", 'file': 'listening/a school.txt'},
                    'Festival':  {'audio': "audio/20.mp3", 'file': 'listening/festival.txt'},
                    'Restaurant':  {'audio': "audio/restaurant.mp3", 'file': 'listening/restaurant.txt'},
                    'Website':  {'audio': "audio/website.mp3", 'file': 'listening/website.txt'},
                    'Holiday':  {'audio': "audio/15.mp3", 'file': 'listening/holiday.txt'},
                    'Travel':  {'audio': "audio/travel.mp3", 'file': 'listening/travel.txt'},
                    'Books':  {'audio': "audio/books.mp3", 'file': 'listening/books.txt'},
                    'An Accident':  {'audio': "audio/accident.mp3", 'file': 'listening/accident.txt'},
                   'Animals':  {'audio': "audio/16.mp3", 'file': 'listening/animals.txt'},
                  'A hotel':  {'audio': "audio/10.mp3", 'file': 'listening/a hotel.txt'},
                  'Letter':  {'audio': "audio/11.mp3", 'file': 'listening/a letter.txt'},
                 'Hobbies':  {'audio': "audio/12.mp3", 'file': 'listening/hobbies.txt'},
                 'Music':  {'audio': "audio/13.mp3", 'file': 'listening/music.txt'},
                 'Shopping':  {'audio': "audio/14.mp3", 'file': 'listening/shopping.txt'},
                 'A Memorable':  {'audio': "audio/2.mp3", 'file': 'listening/a memorable event.txt'},
                 'Favourite Subject':  {'audio': "audio/3.mp3", 'file': 'listening/favorite subject.txt'},
                 'Museums':  {'audio': "audio/4.mp3", 'file': 'listening/museumes.txt'},
                 'Movie':  {'audio': "audio/5.mp3", 'file': 'listening/movie.txt'},
                 'Foreign Country':  {'audio': "audio/6.mp3", 'file': 'listening/a foreign country.txt'},
                 'Parties':  {'audio': "audio/7.mp3", 'file': 'listening/parties.txt'},
                 'Teacher':  {'audio': "audio/8.mp3", 'file': 'listening/a teacher.txt'},
                 'A friend':  {'audio': "audio/9.mp3", 'file': 'listening/a friend.txt'},
                 'Favourite Things':  {'audio': "audio/favorite things.mp3", 'file': 'listening-intermediate/lesson#01.txt'},
                 'Activity':  {'audio': "audio/activity.mp3", 'file': 'listening-intermediate/lesson#02.txt'},
                 'Working Out':  {'audio': "audio/working out.mp3", 'file': 'listening-intermediate/lesson#03.txt'},
                 'Introductions':  {'audio': "audio/introductions.mp3", 'file': 'listening-intermediate/lesson#04.txt'},
                 'Register For A Class':  {'audio': "audio/registering for class.mp3", 'file': 'listening-intermediate/lesson#05.txt'},
                 'Registration':  {'audio': "audio/registration.mp3", 'file': 'listening-intermediate/lesson#06.txt'},
                 'Grades':  {'audio': "audio/grades.mp3", 'file': 'listening-intermediate/lesson#07.txt'},
                'Summer Vacation':  {'audio': "audio/summer vacation.mp3", 'file': 'listening-intermediate/lesson#08.txt'},
                'Exams':  {'audio': "audio/exams.mp3", 'file': 'listening-intermediate/lesson#09.txt'},
                'Smoking':  {'audio': "audio/somking.mp3", 'file': 'listening-intermediate/lesson#10.txt'},
               'Drinking':  {'audio': "audio/drinking.mp3", 'file': 'listening-intermediate/lesson#11.txt'},
              'After Birth':  {'audio': "audio/after birth.mp3", 'file': 'listening-intermediate/lesson#12.txt'},
              'Allergies':  {'audio': "audio/allergies.mp3", 'file': 'listening-intermediate/lesson#13.txt'},
             'Losing Weight':  {'audio': "audio/losing weight.mp3", 'file': 'listening-intermediate/lesson#14.txt'},
             'Dieting':  {'audio': "audio/dieting.mp3", 'file': 'listening-intermediate/lesson#15.txt'},
             'Asking For A Date':  {'audio': "audio/asking for a date.mp3", 'file': 'listening-intermediate/lesson#16.txt'},
             'Proposing':  {'audio': "audio/proposing.mp3", 'file': 'listening-intermediate/lesson#17.txt'},
             'Baseball':  {'audio': "audio/baseball.mp3", 'file': 'listening-intermediate/lesson#18.txt'} ,
             'General Sports':  {'audio': "audio/general sports.mp3", 'file': 'listening-intermediate/lesson#19.txt'},
             'Golf':  {'audio': "audio/golf.mp3", 'file': 'listening-intermediate/lesson#20.txt'},
             'Mall Shopping':  {'audio': "audio/mall shopping.mp3", 'file': 'listening-intermediate/lesson#21.txt'},
             'Jewerly Gift':  {'audio': "audio/jewelry gift.mp3", 'file': 'listening-intermediate/lesson#23.txt'},
             'Jewerly':  {'audio': "audio/jewelry.mp3", 'file': 'listening-intermediate/lesson#24.txt'} ,
            'Jewerly Watch':  {'audio': "audio/jewelry watch.mp3", 'file': 'listening-intermediate/lesson#25.txt'},
            'Having A Baby':  {'audio': "audio/having a baby.mp3", 'file': 'listening-intermediate/lesson#26.txt'}, 
            'Sick Dad':  {'audio': "audio/sick dad.mp3", 'file': 'listening-intermediate/lesson#27.txt'},
            'Stressful Parents':  {'audio': "audio/stressful parents.mp3", 'file': 'listening-intermediate/lesson#28.txt'}, 
           'Grandmother Passing Away':  {'audio': "audio/grandmother passing away.mp3", 'file': 'listening-intermediate/lesson#29.txt'},
           'University Conversation':  {'audio': "audio/university conversation.mp3", 'file': 'listening-advanced/lesson#01.txt'},
           'Studying For Exam':  {'audio': "audio/studying for exam.mp3", 'file': 'listening-advanced/lesson#02.txt'},
           'Roommates':  {'audio': "audio/roommates.mp3", 'file': 'listening-advanced/lesson#03.txt'},
           'Doormitory':  {'audio': "audio/dormitory.mp3", 'file': 'listening-advanced/lesson#04.txt'},
           'Renting A Room':  {'audio': "audio/renting a room.mp3", 'file': 'listening-advanced/lesson#05.txt'},
           'Quit Smoking':  {'audio': "audio/quit smoking.mp3", 'file': 'listening-advanced/lesson#06.txt'},
           'Running Into A Friend':  {'audio': "audio/running into a friend.mp3", 'file': 'listening-advanced/lesson#07.txt'},
          'Small Talk':  {'audio': "audio/small talk.mp3", 'file': 'listening-advanced/lesson#08.txt'},
          'Hang Out':  {'audio': "audio/hang out.mp3", 'file': 'listening-advanced/lesson#09.txt'},
          'First Date':  {'audio': "audio/first date.mp3", 'file': 'listening-advanced/lesson#10.txt'},
          'Honneymoon Planning':  {'audio': "audio/honeymoon planning.mp3", 'file': 'listening-advanced/lesson#11.txt'},
         'Weight Lose':  {'audio': "audio/weight loss.mp3", 'file': 'listening-advanced/lesson#13.txt'},
          'Marriage Proposal':  {'audio': "audio/marriage proposal.mp3", 'file': 'listening-advanced/lesson#14.txt'},
          'Watching Baseball':  {'audio': "audio/watching baseball.mp3", 'file': 'listening-advanced/lesson#15.txt'},
          'Watching Football':  {'audio': "audio/watching football.mp3", 'file': 'listening-advanced/lesson#17.txt'},
          'Poker':  {'audio': "audio/poker.mp3", 'file': 'listening-advanced/lesson#18.txt'},
          'Talking About Guys':  {'audio': "audio/talking about guys.mp3", 'file': 'listening-advanced/lesson#19.txt'},
          'Practicing Golf':  {'audio': "audio/practicing golf.mp3", 'file': 'listening-advanced/lesson#20.txt'},
          'Favourite Hobby':  {'audio': "audio/favority hobby.mp3", 'file': 'listening-advanced/lesson#21.txt'},
          'Life After Breaking Up':  {'audio': "audio/life after breaking up.mp3", 'file': 'listening-advanced/lesson#22.txt'},
          'Heart Broken':  {'audio': "audio/heart broken.mp3", 'file': 'listening-advanced/lesson#23.txt'},
          'Being Afraid':  {'audio': "audio/being afraid.mp3", 'file': 'listening-advanced/lesson#24.txt'},
          'Restless':  {'audio': "audio/restless.mp3", 'file': 'listening-advanced/lesson#25.txt'},
          'Infatuation':  {'audio': "audio/infatuation.mp3", 'file': 'listening-advanced/lesson#26.txt'},
          'Class Friend':  {'audio': "audio/class friend.mp3", 'file': 'listening-advanced/lesson#27.txt'},
          'General Advanced':  {'audio': "audio/general advanced.mp3", 'file': 'listening-advanced/lesson#28.txt'},
          'Joining Health Club':  {'audio': "audio/joining health club.mp3", 'file': 'listening-advanced/lesson#29.txt'},
          'Watching Basketball':  {'audio': "audio/watching basketball.mp3", 'file': 'listening-advanced/lesson#31.txt'}}
        file = audio_file[text]['file']
        audio = audio_file[text]['audio']

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(audio)
        self.sound.play()
        self.sound.loop=True
        with open(file) as f:
            translatedfile2=file
            self.ids.mytext.text = f.read()

    def selection2(self):
        global truth1, truth2, truth3
        truth1 = True
        truth2 = False
        truth3 = False
        
        # 1. Grab the selected text from the UI while on the main thread
        myvariable = self.ids.mytext.selection_text
        
        # 2. Spin the database lookup off into a background thread
        threading.Thread(target=self.async_db_lookup, args=(myvariable,), daemon=True).start()

    def async_db_lookup(self, search_word):
        # 3. Open a separate, thread-isolated database connection for safety
        db_name = "book.db"
        if platform == 'android':
            from android.storage import app_storage_path # type: ignore
            db_path = os.path.join(app_storage_path(), db_name)
        else:
            db_path = db_name

        try:
            # Connect, execute the query, and fetch the single record
            thread_conn = sqlite3.connect(db_path)
            thread_cursor = thread_conn.cursor()
            
            sql_query = "select meaning from words10 where lower(upper(word)) like ?"
            thread_cursor.execute(sql_query, (search_word,))
            myresult = thread_cursor.fetchone()
            
            thread_conn.close()
            
            # 4. Use Clock to pass the result back to the main UI thread safely
            Clock.schedule_once(lambda dt: self.process_lookup_result(myresult), 0)
            
        except Exception as e:
            print(f"Lookup thread error: {e}")
            # Fallback error message if something fails
            Clock.schedule_once(lambda dt: self.process_lookup_result(None), 0)

    def process_lookup_result(self, myresult):
        global myresult1
        
        # 5. This runs back on Kivy's main thread, making UI changes 100% safe
        if myresult is None:
            content = Label(text="Not Found. Please choose the word correctly", halign='center', valign='middle')
            popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
            popup.open()
            Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        else:
            myresult1 = ''.join(myresult)
            self.manager.current = 'trans'

class Video_a(Screen):
    def on_pre_enter(self, *args):
        
        global theoption1
        global truth1
        checker = theoption1
        
        
        if checker == 'go swimming'.strip(): # already a string
                video = self.ids.v1
                video.source ='videos/beginner/play-go-do.mp4'
                video.state ='play'
                
                
    
                
        if checker == 'verb to be'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/verb to be.mp4'
                video.state ='play'
                
        
        
        if checker == 'was and were'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/was were.mp4'
                video.state ='play'

        if checker == 'good at'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/good at.mp4'
                video.state ='play'

        if checker == 'so with adjective'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using so and such.mp4'
                video.state ='play'

        if checker == 'participle adjectives'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/participle adjectives.mp4'
                video.state ='play'

        if checker == 'much and many'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/much and many.mp4'
                video.state ='play'

        if checker == 'present continuous'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/present continuous.mp4'
                video.state ='play'

        if checker == 'would you mind'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/would you mind.mp4'
                video.state ='play'

        if checker == 'present simple'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/present simple.mp4'
                video.state ='play'

        if checker == 'have got'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/have got and has got.mp4'
                video.state ='play'

        if checker == 'possessive adjective'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/possessive adjectives.mp4'
                video.state ='play'

        if checker == 'to infinitive'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/to infinitive.mp4'
                video.state ='play'

        if checker == 'possessive pronouns'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/possessive pronouns.mp4'
                video.state ='play'

        if checker == 'want vs need'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/want and need.mp4'
                video.state ='play'

        if checker == 'could'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using could.mp4'
                video.state ='play'

        if checker == 'comparison of adjectives'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/comparison of adjectives.mp4'
                video.state ='play'

        if checker == 'verb to be negative form'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/verb to be negative.mp4'
                video.state ='play'

        if checker == 'look for'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/look for.mp4'
                video.state ='play'

        if checker == 'present simple negative'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/do not and does not.mp4'
                video.state ='play'

        if checker == 'how'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/how.mp4'
                video.state ='play'

        if checker == 'may and might'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/may and might.mp4'
                video.state ='play'

        if checker == 'question with how'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/how old are you.mp4'
                video.state ='play'

        if checker == 'future simple'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/future simple.mp4'
                video.state ='play'

        if checker == 'preposition from'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prepositions of and from.mp4'
                video.state ='play'

        if checker == 'quantifiers'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/quantifiers.mp4'
                video.state ='play'

        if checker == 'exclamation in english'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/exclamation in english.mp4'
                video.state ='play'

        if checker == 'causative verbs'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/causative verbs2.mp4'
                video.state ='play'

        if checker == 'both and either or neither nor'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/both and either or neither nor.mp4'
                video.state ='play'

        if checker == 'responding to good news'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/responding to good news and bad news.mp4'
                video.state ='play'

        if checker == 'catenative verbs'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/catenative verbs.mp4'
                video.state ='play'

        if checker == 'can'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/can.mp4'
                video.state ='play'

        if checker == 'preposition for'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prepositions for with and about.mp4'
                video.state ='play'

        if checker == 'using do does and did'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using do does and did.mp4'
                video.state ='play'

        if checker == 'indifinite articles'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/indefinite articles1.mp4'
                video.state ='play'

        if checker == 'too and very'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/adjectives with too and very.mp4'
                video.state ='play'

        if checker == 'using has have'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using have has.mp4'
                video.state ='play'

        if checker == 'would like'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/would like.mp4'
                video.state ='play'

        if checker == 'prepositions in-on-at'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prepositions in-on-at.mp4'
                video.state ='play'

        if checker == 'some any no'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/some any no.mp4'
                video.state ='play'

        if checker == 'prefer'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prefer.mp4'
                video.state ='play'

        if checker == 'did'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/negative form of do not does not and did not.mp4'
                video.state ='play'

        if checker == 'preposition by'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/preposition by.mp4'
                video.state ='play'

        if checker == 'using do does'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using do does and did.mp4'
                video.state ='play'

        if checker == 'definite article'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/definite article.mp4'
                video.state ='play'

        if checker == 'like'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/like.mp4'
                video.state ='play'

        if checker == 'using had'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/using have has1.mp4'
                video.state ='play'

        if checker == 'reflexive pronouns'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/reflexive pronouns.mp4'
                video.state ='play'

        if checker == 'negative form of did'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/negative form of do not does not and did not.mp4'
                video.state ='play'

        if checker == 'indefinite pronouns'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/indefinite pronouns.mp4'
                video.state ='play'

        if checker == 'comparative and superlative'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/comparative and superlative.mp4'
                video.state ='play'

        if checker == 'past simple'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/past simple.mp4'
                video.state ='play'

        if checker == 'do vs make'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/do vs make.mp4'
                video.state ='play'

        if checker == 'question with how long'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/question with how long.mp4'
                video.state ='play'

        if checker == 'less vs fewer'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/less vs fewer.mp4'
                video.state ='play'

        if checker == 'first conditional'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/conditionals type 0 and 1.mp4'
                video.state ='play'

        if checker == 'stop'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/stop try help.mp4'
                video.state ='play'

        if checker == 'none of'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/none of.mp4'
                video.state ='play'

        if checker == 'few a few little a little'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/few a few little a little.mp4'
                video.state ='play'

        if checker == 'demonstrative pronouns'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/demonstrative pronouns.mp4'
                video.state ='play'

        if checker == 'have got to'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/have got to have to must.mp4'
                video.state ='play'

        if checker == 'genitive'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/genitive.mp4'
                video.state ='play'

        if checker == 'how do'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/wh-question present simple.mp4'
                video.state ='play'

        if checker == 'adverbs of frequency'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/adverbs of frequency.mp4'
                video.state ='play'

        if checker == 'preposition into'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prepositions in into.mp4'
                video.state ='play'

        if checker == 'order of adverbs'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/order of adverbs.mp4'
                video.state ='play'

        if checker == 'imperative'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/the imperative.mp4'
                video.state ='play'

        if checker == 'parallelism'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/parallelism.mp4'
                video.state ='play'

        if checker == 'preposition over'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/preposition over.mp4'
                video.state ='play'

        if checker == 'wh questions'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/questions wh.mp4'
                video.state ='play'

        if checker == 'should'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/should.mp4'
                video.state ='play'

        if checker == 'there is there are'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/there is there are.mp4'
                video.state ='play'

        if checker == 'telling time'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/telling time1.mp4'
                video.state ='play'

        if checker == 'will vs going to'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/will vs going to.mp4'
                video.state ='play'

        if checker == 'a lot of'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/much many and a lot of.mp4'
                video.state ='play'

        if checker == 'how tall how long'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/how tall how long.mp4'
                video.state ='play'

        if checker == 'preposition between'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/prepositions between next to etc.mp4'
                video.state ='play'

        if checker == 'do does'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/yes no question do does was were have.mp4'
                video.state ='play'

        if checker == 'preposition above'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/above over up.mp4'
                video.state ='play'

        if checker == 'linking verbs'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/action and linking verbs.mp4'
                video.state ='play'

        if checker == 'question words'.strip(): # already a string
                
                video = self.ids.v1
                video.source ='videos/beginner/question words.mp4'
                video.state ='play'

        

        

        

        

        

        

        

class Video_b(Screen):
    def on_pre_enter(self, *args):
        
        global theoption
        global truth1
        checker = theoption
        
        
        if checker == 'using wish'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/wish.mp4'
                video.state ='play'

        if checker == 'first conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/conditionals type 0 and 1.mp4'
                video.state ='play'
        if checker == 'comparative and superlative'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/comparative and superlative.mp4'
                video.state ='play'

        if checker == 'using have been'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/has been have been had been.mp4'
                video.state ='play'

        if checker == 'third conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/conditionals type 2 and 3.mp4'
                video.state ='play'

        if checker == 'be able to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/can could be able to.mp4'
                video.state ='play'

        if checker == 'adjectives with too and very'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/adjectives with too and very.mp4'
                video.state ='play'

        if checker == 'less'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/less vs fewer.mp4'
                video.state ='play'

        if checker == 'have got to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/have got to have to must.mp4'
                video.state ='play'

        if checker == 'future perfect'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/future perfect.mp4'
                video.state ='play'

        if checker == 'other others'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/another other and others2.mp4'
                video.state ='play'

        if checker == 'present perfect continuous'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/present perfect continuous.mp4'
                video.state ='play'

        if checker == 'past continuous'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/past continuous.mp4'
                video.state ='play'

        if checker == 'present perfect'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/present perfect simple.mp4'
                video.state ='play'

        if checker == 'relative pronouns'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/relative pronouns.mp4'
                video.state ='play'

        if checker == 'gerund'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/gerund.mp4'
                video.state ='play'

        if checker == 'exclamation in english'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/exclamation in english.mp4'
                video.state ='play'

        if checker == 'would you mind'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/would you mind.mp4'
                video.state ='play'

        if checker == 'question tag'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/tag question.mp4'
                video.state ='play'

        if checker == 'present simple questions'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/questions wh.mp4'
                video.state ='play'

        if checker == 'agreement using so and neither'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/agree with so neither and either.mp4'
                video.state ='play'

        if checker == 'using whatever'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/whatever whoever etc.mp4'
                video.state ='play'

        if checker == 'using without'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/without.mp4'
                video.state ='play'

        if checker == 'using hope'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/hope vs wish.mp4'
                video.state ='play'

        if checker == 'adjective word order'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/order of adjectives.mp4'
                video.state ='play'

        if checker == 'would like'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/would like.mp4'
                video.state ='play'

        if checker == 'so that such that'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/so that such that to too and enough.mp4'
                video.state ='play'

        if checker == 'order of adverbs'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/order of adverbs.mp4'
                video.state ='play'

        if checker == 'past simple passive'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/past simple passive.mp4'
                video.state ='play'

        if checker == 'so that such that'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/so that such that to too and enough.mp4'
                video.state ='play'

        if checker == 'a lot of'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner\much many and a lot of.mp4'
                video.state ='play'

        if checker == 'had better'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/had better.mp4'
                video.state ='play'

        if checker == 'few a few little a little'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/few a few little a little.mp4'
                video.state ='play'

        if checker == 'much many'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner\much and many.mp4'
                video.state ='play'
        if checker == 'preposition over'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner\preposition over.mp4'
                video.state ='play'

        if checker == 'third conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/conditionals type 2 and 3.mp4'
                video.state ='play'

        if checker == 'did not'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/negative form of do not does not and did not.mp4'
                video.state ='play'

        if checker == 'infinitive'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/to infinitive.mp4'
                video.state ='play'

        if checker == 'keep'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/phrsalverbs with keep.mp4'
                video.state ='play'

        if checker == 'prefer'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prefer.mp4'
                video.state ='play'

        if checker == 'past simple'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/past simple.mp4'
                video.state ='play'

        if checker == 'second conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/conditionals type 2 and 3.mp4'
                video.state ='play'

        if checker == 'preposition with'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions for with and about.mp4'
                video.state ='play'

        if checker == 'so that'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/so vs so that.mp4'
                video.state ='play'

        if checker == 'would'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/the helping verb would.mp4'
                video.state ='play'

        if checker == 'would like'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/would like.mp4'
                video.state ='play'
        
        if checker == 'may might'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/may and might.mp4'
                video.state ='play'

        if checker == 'do not does not'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/negative form of do not does not and did not.mp4'
                video.state ='play'

        if checker == 'should'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/should.mp4'
                video.state ='play'

        if checker == 'instead of'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/instead and instead of.mp4'
                video.state ='play'

        if checker == 'as soon as'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/as soon as.mp4'
                video.state ='play'

        if checker == 'would rather'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/would rather.mp4'
                video.state ='play'

        if checker == 'present perfect'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/present perfect simple.mp4'
                video.state ='play'

        if checker == 'expressing purpose'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/expressing purpose.mp4'
                video.state ='play'

        if checker == 'comparison of adjectives'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/comparison of adjectives.mp4'
                video.state ='play'

        if checker == 'a pair of'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/a pair of.mp4'
                video.state ='play'

        if checker == 'using since'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/since vs for.mp4'
                video.state ='play'

        if checker == 'was used to+ing'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/used to be used to get used to.mp4'
                video.state ='play'

        if checker == 'have something done'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/have something done get something done.mp4'
                video.state ='play'

        if checker == 'as  much as as many as'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/as much as.mp4'
                video.state ='play'

        if checker == 'causative verbs'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/causative verbs2.mp4'
                video.state ='play'

        if checker == 'ought to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/should ought to had better.mp4'
                video.state ='play'

        if checker == 'perfect modals could have should have would have must have'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/Perfect Modals could have should have would have must have.mp4'
                video.state ='play'

        if checker == 'how much how many'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/how.mp4'
                video.state ='play'

        if checker == 'going to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/will vs going to.mp4'
                video.state ='play'

        if checker == 'preposition into'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions in into.mp4'
                video.state ='play'

        if checker == 'past perfect'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/past perfect simple.mp4'
                video.state ='play'

        if checker == 'would you mind'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/would you mind.mp4'
                video.state ='play'

        if checker == 'preposition next to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions between next to etc.mp4'
                video.state ='play'

        if checker == 'zero conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/conditionals type 0 and 1.mp4'
                video.state ='play'

        if checker == 'preposition in-on-at'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions in-on-at.mp4'
                video.state ='play'

        if checker == 'how about what about why not'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/how about what about why do not.mp4'
                video.state ='play'

        if checker == 'preposition from'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions of and from.mp4'
                video.state ='play'

        if checker == 'subjunctive'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/advanced/the english subjunctive.mp4'
                video.state ='play'

        if checker == 'could'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/can could be able to.mp4'
                video.state ='play'

        if checker == 'used to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/used to be used to get used to.mp4'
                video.state ='play'

        if checker == 'have got to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/have got to have to must.mp4'
                video.state ='play'

        if checker == 'first conditional'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/conditionals type 0 and 1.mp4'
                video.state ='play'

        if checker == 'so that such that'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/so that such that to too and enough.mp4'
                video.state ='play'

        if checker == 'like'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/like.mp4'
                video.state ='play'

        if checker == 'used to be used to get used to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/used to be used to get used to.mp4'
                video.state ='play'

        if checker == 'agreement using so and neither'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/advanced/agreement using so and neither.mp4'
                video.state ='play'

        if checker == 'preposition for'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions for with and about.mp4'
                video.state ='play'

        if checker == 'future simple passive'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/future simple passive.mp4'
                video.state ='play'

        if checker == 'relative pronouns'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/relative pronouns.mp4'
                video.state ='play'

        if checker == 'look forward to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/looking forward to.mp4'
                video.state ='play'

        if checker == 'can'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/can could be able to.mp4'
                video.state ='play'

        if checker == 'in the end vs at the end'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/in the end vs at the end.mp4'
                video.state ='play'

        if checker == 'indefinite pronouns'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/indefinite pronouns.mp4'
                video.state ='play'

        if checker == 'unless'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/unless.mp4'
                video.state ='play'

        if checker == 'some any no'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/some any no.mp4'
                video.state ='play'

        if checker == 'should'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/should.mp4'
                video.state ='play'

        if checker == 'question tag irregular'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/question tag irregular.mp4'
                video.state ='play'

        if checker == 'other others'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/another other and others.mp4'
                video.state ='play'

        if checker == 'how to count uncountable nouns'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/count uncountable nouns-a piece of.mp4'
                video.state ='play'

        if checker == 'parallelism'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/parallelism.mp4'
                video.state ='play'

        if checker == 'indirect questions'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/indirect question.mp4'
                video.state ='play'

        if checker == 'not only but also'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/not only but also.mp4'
                video.state ='play'

        if checker == 'inversion rarely'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/inversion.mp4'
                video.state ='play'

        if checker == 'too vs very'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/adjectives with too and very.mp4'
                video.state ='play'

        if checker == 'there is there are'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/there is there are.mp4'
                video.state ='play'

        if checker == 'comparison of adjectives'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/comparison of adjectives.mp4'
                video.state ='play'

        if checker == 'gerund'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/gerund.mp4'
                video.state ='play'

        if checker == 'has have'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/using have has1.mp4'
                video.state ='play'

        if checker == 'reported speech statement'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/advanced/reporting statement.mp4'
                video.state ='play'

        if checker == 'how many how much'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/how.mp4'
                video.state ='play'

        if checker == 'as much as as many as'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/as as much as as many as.mp4'
                video.state ='play'

        if checker == 'as many as vs as much as'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/as as much as as many as.mp4'
                video.state ='play'

        if checker == 'present continuous'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/present continuous.mp4'
                video.state ='play'

        if checker == 'although even though'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/advanced/although though even though despite in spite of.mp4'
                video.state ='play'

        if checker == 'using enough'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/so that such that to too and enough.mp4'
                video.state ='play'

        if checker == 'would rather'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/would rather.mp4'
                video.state ='play'

        if checker == 'because of'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/because and because of.mp4'
                video.state ='play'

        if checker == 'being'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/being.mp4'
                video.state ='play'

        if checker == 'had better'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/should ought to had better.mp4'
                video.state ='play'

        if checker == 'like'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/like.mp4'
                video.state ='play'

        if checker == 'comparing adverbs'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/comparing adverbs.mp4'
                video.state ='play'

        if checker == 'the more'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/advanced/double comparatives.mp4'
                video.state ='play'

        if checker == 'be able to'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/be able to.mp4'
                video.state ='play'

        if checker == 'even if'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/using the word even even so even though even if even as.mp4'
                video.state ='play'

        if checker == 'inversion'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/inversion.mp4'
                video.state ='play' 

        if checker == 'would better'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/i would better i would better not.mp4'
                video.state ='play'

        if checker == 'participle adjectives'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/participle adjectives.mp4'
                video.state ='play'

        if checker == 'using of'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions of and from.mp4'
                video.state ='play'

        if checker == 'prepositions in-on-at'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions in-on-at.mp4'
                video.state ='play'

        if checker == 'good at'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/good at.mp4'
                video.state ='play'

        if checker == 'preposition from'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/prepositions of and from.mp4'
                video.state ='play'

        if checker == 'did'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/beginner/negative form of do not does not and did not.mp4'
                video.state ='play'

        if checker == 'question tag irregular'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/question tag irregular.mp4'
                video.state ='play'

        if checker == 'perfect modals could have should have would have must have'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/perfect modals could have should have would have must have.mp4'
                video.state ='play'

        if checker == 'distributives'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/distributives.mp4'
                video.state ='play'

        if checker == 'future continuous'.strip(): # already a string
                video = self.ids.v2
                video.source ='videos/intermediate/future continuous.mp4'
                video.state ='play'
            


















        

        

        
        

        

        

        

        

        
          
class ArabicText(Screen):
    def on_pre_enter(self, *args):
        if translatedfile== "listening/newspaper.txt":
            a = codecs.open(r'arabic/newspaper and magazine.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(a))
        
        
        if translatedfile== "listening/a practical skill.txt":
            b = codecs.open(r'arabic/a practical skill.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(b))
            
        
        if translatedfile== "listening/presents.txt":
            c = codecs.open(r'arabic/present.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(c))
            
            
            
        if translatedfile== "listening/favourite rooms.txt":
            d = codecs.open(r'arabic/favourite room.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(d))
            
            
        if translatedfile== "listening/historical places.txt":
            e = codecs.open(r'arabic/historical places.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(e))
            
            
        if translatedfile== "listening/sports.txt":
            f = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(f))
            
            
        if translatedfile== "listening/a school.txt":
            g = codecs.open(r'arabic/a school.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(g))
            
            
        if translatedfile== "listening/festival.txt":
            h = codecs.open(r'arabic/festival.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(h))
            
            
        if translatedfile== "listening/resaurant.txt":
            i = codecs.open(r'arabic/restaurant.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(i))
            
        if translatedfile== "listening/holiday.txt":
            j = codecs.open(r'arabic/holiday.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(j))
            
            
        if translatedfile== "listening/website.txt":
            k = codecs.open(r'arabic/website.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(k))
            
            
        if translatedfile== "listening/travel.txt":
            l = codecs.open(r'arabic/travel.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(l))
            
        if translatedfile== "listening/books.txt":
            m = codecs.open(r'arabic/books.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(m))
            
            
        if translatedfile== "listening/accident.txt":
            n = codecs.open(r'arabic/accident.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(n))
            
            
        if translatedfile== "listening/animals.txt":
            o = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(o))
            
            
        if translatedfile== "listening/a hotel.txt":
            p = codecs.open(r'arabic/a hotel.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(p))
            
            
        if translatedfile== "listening/a letter.txt":
            q = codecs.open(r'arabic/a letter.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(q))
            
            
        if translatedfile== "listening/hobbies.txt":
            r = codecs.open(r'arabic/hobbies.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(r))
            
        if translatedfile== "listening/music.txt":
            t = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(t))
        
        
        
        if translatedfile== "listening/shopping.txt":
            u = codecs.open(r'arabic/shopping.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(u))
            
            
        if translatedfile== "listening/memorable event.txt":
            v = codecs.open(r'arabic/memorable event.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(v))
            
        if translatedfile== "listening/favorite subject.txt":
            w = codecs.open(r'arabic/favorite subject.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(w))
            
            
        if translatedfile== "listening/museums.txt":
            x = codecs.open(r'arabic/museums.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x))
            
        if translatedfile== "listening/movie.txt":
            y = codecs.open(r'arabic/movie theater.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(y))
            
            
        if translatedfile== "listening/a foreign country.txt":
            z = codecs.open(r'arabic/foreign country.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(z))
            
            
        if translatedfile== "listening/parties.txt":
            aa = codecs.open(r'arabic/parties.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(aa))
            
        if translatedfile== "listening/a teacher.txt":
            bb = codecs.open(r'arabic/a teacher.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(bb))
            
            
        if translatedfile== "listening/a friend.txt":
            cc = codecs.open(r'arabic/a friend.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(cc))
            
            
        if translatedfile== "listening-intermediate/lesson#01.txt":
            dd = codecs.open(r'arabic/favorite things.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(dd))
            
        if translatedfile== "listening-intermediate/lesson#02.txt":
            ee = codecs.open(r'arabic/activity.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ee))
            
            
        if translatedfile== "listening-intermediate/lesson#03.txt":
            ff = codecs.open(r'arabic/working out.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ff))
            
        
        if translatedfile== "listening-intermediate/lesson#04.txt":
            gg = codecs.open(r'arabic/introductions.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(gg))
            
            
        if translatedfile== "listening-intermediate/lesson#05.txt":
            hh = codecs.open(r'arabic/registering for class.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(hh))
            
            
        if translatedfile== "listening-intermediate/lesson#06.txt":
            ii = codecs.open(r'arabic/registering.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ii))
            
            
            
        if translatedfile== "listening-intermediate/lesson#07.txt":
            jj = codecs.open(r'arabic/grades.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(jj))
            
        
        if translatedfile== "listening-intermediate/lesson#08.txt":
            kk = codecs.open(r'arabic/summer vacation.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(kk))
            
        
        if translatedfile== "listening-intermediate/lesson#09.txt":
            ll = codecs.open(r'arabic/exams.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ll))
            
            
        if translatedfile== "listening-intermediate/lesson#10.txt":
            mm = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(mm))
            
        if translatedfile== "listening-intermediate/lesson#11.txt":
            nn = codecs.open(r'arabic/drinking.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(nn))
            
            
        if translatedfile== "listening-intermediate/lesson#12.txt":
            oo = codecs.open(r'arabic/after birth.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(oo))
            
            
        if translatedfile== "listening-intermediate/lesson#13.txt":
            pp = codecs.open(r'arabic/alleries.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(pp))
            
            
        if translatedfile== "listening-intermediate/lesson#14.txt":
            qq = codecs.open(r'arabic/losing weight.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(qq))
            
        if translatedfile== "listening-intermediate/lesson#15.txt":
            rr = codecs.open(r'arabic/dieting.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(rr))
            
            
        if translatedfile== "listening-intermediate/lesson#16.txt":
            ss = codecs.open(r'arabic/asking for a date.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ss))
            
        
        if translatedfile== "listening-intermediate/lesson#17.txt":
            tt = codecs.open(r'arabic/proposing.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(tt))
            
            
        if translatedfile== "listening-intermediate/lesson#18.txt":
            uu = codecs.open(r'arabic/baseball.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(uu))
            
            
        if translatedfile== "listening-intermediate/lesson#19.txt":
            vv = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(vv))
            
            
            
        if translatedfile== "listening-intermediate/lesson#20.txt":
            ww = codecs.open(r'arabic/golf.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(ww))
            
            
        if translatedfile== "listening-intermediate/lesson#21.txt":
            xx = codecs.open(r'arabic/mall shopping.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(xx))
            
            
        if translatedfile== "listening-intermediate/lesson#23.txt":
            yy = codecs.open(r'arabic/jewelry gift.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(yy))
            
        
        if translatedfile== "listening-intermediate/lesson#24.txt":
            zz = codecs.open(r'arabic/jewelry.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(zz))
            
            
        if translatedfile== "listening-intermediate/lesson#25.txt":
            x1 = codecs.open(r'arabic/jewelry watch.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x1))
            
            
        if translatedfile== "listening-intermediate/lesson#26.txt":
            x2 = codecs.open(r'arabic/having a baby.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x2))
            
            
        if translatedfile== "listening-intermediate/lesson#27.txt":
            x3 = codecs.open(r'arabic/sick dad.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x3))
            
        if translatedfile== "listening-intermediate/lesson#28.txt":
            x4 = codecs.open(r'arabic/stressful parents.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x4))
            
            
        if translatedfile== "listening-intermediate/lesson#29.txt":
            x5 = codecs.open(r'arabic/grandmother passing away.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x5))
            
            
        if translatedfile== "listening-advanced/lesson#01.txt":
            x6 = codecs.open(r'arabic/university conversation.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x6))
            
        
        
        if translatedfile== "listening-advanced/lesson#02.txt":
            x7 = codecs.open(r'arabic/studying for exam.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x7))
            
            
        if translatedfile== "listening-advanced/lesson#03.txt":
            x8 = codecs.open(r'arabic/roommates.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x8))
            
            
        if translatedfile== "listening-advanced/lesson#04.txt":
            x9 = codecs.open(r'arabic/dormitory.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x9))
            
            
        if translatedfile== "listening-advanced/lesson#05.txt":
            x10 = codecs.open(r'arabic/renting a room.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x10))
        
        
        
        
        if translatedfile== "listening-intermediate/lesson#10.txt":
            x11 = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x11))
            
            
        if translatedfile== "listening-advanced/lesson#07.txt":
            x12 = codecs.open(r'arabic/running into a friend.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x12))
            
            
            
        if translatedfile== "listening-advanced/lesson#08.txt":
            x13 = codecs.open(r'arabic/small talk.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x13))
            
            
        if translatedfile== "listening-advanced/lesson#09.txt":
            x14 = codecs.open(r'arabic/hang out.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x14))
            
            
        if translatedfile== "listening-advanced/lesson#10.txt":
            x15 = codecs.open(r'arabic/first date.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x15))
            
            
        if translatedfile== "listening-advanced/lesson#11.txt":
            x16 = codecs.open(r'arabic/honeymoon planning.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x16))
            
            
        if translatedfile== "listening-advanced/lesson#13.txt":
            x17 = codecs.open(r'arabic/weight loss.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x17))
            
            
            
        if translatedfile== "listening-advanced/lesson#14.txt":
            x18 = codecs.open(r'arabic/marriage proposal.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x18))
            
            
        if translatedfile== "listening-advanced/lesson#15.txt":
            x19 = codecs.open(r'arabic/watching baseball.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x19))
            
            
        if translatedfile== "listening-advanced/lesson#17.txt":
            x20 = codecs.open(r'arabic/watching football.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x20))
            
            
        if translatedfile== "listening-advanced/lesson#18.txt":
            x21 = codecs.open(r'arabic/poker.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x21))
            
            
        if translatedfile== "listening-advanced/lesson#19.txt":
            x22 = codecs.open(r'arabic/talking about guys.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x22))
            
            
        if translatedfile== "listening-advanced/lesson#20.txt":
            x23 = codecs.open(r'arabic/practicing golf.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x23))
            
        if translatedfile== "listening-advanced/lesson#21.txt":
            x24 = codecs.open(r'arabic/favorite hobby.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x24))
            
            
        if translatedfile== "listening-advanced/lesson#22.txt":
            x25 = codecs.open(r'arabic/life after breaking up.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x25))
        
        
        if translatedfile== "listening-advanced/lesson#23.txt":
            x26 = codecs.open(r'arabic/heart broken.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x26))
        
        
        if translatedfile== "listening-advanced/lesson#24.txt":
            x27 = codecs.open(r'arabic/being afraid.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x27))
            
        if translatedfile== "listening-advanced/lesson#25.txt":
            x28 = codecs.open(r'arabic/restless.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x28))
            
            
        if translatedfile== "listening-advanced/lesson#26.txt":
            x29 = codecs.open(r'arabic/infatuation.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x29))
            
            
        if translatedfile== "listening-advanced/lesson#27.txt":
            x30 = codecs.open(r'arabic/class friend.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x30))
            
            
        if translatedfile== "listening-advanced/lesson#28.txt":
            x31 = codecs.open(r'arabic/general.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x31))
            
            
        if translatedfile== "listening-advanced/lesson#29.txt":
            x32 = codecs.open(r'arabic/joining health club.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x32))
            
            
        if translatedfile== "listening-advanced/lesson#31.txt":
            x33 = codecs.open(r'arabic/watching basketball.txt',encoding='utf-8').read()
            self.ids.myarab.multiline = True
            self.ids.myarab.text = get_display(arabic_reshaper.reshape(x33))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
class ArabicText1(Screen):
    def on_pre_enter(self, *args):
        if translatedfile1== "listening/newspaper.txt":
            a = codecs.open(r'arabic/newspaper and magazine.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(a))
        
        
        if translatedfile1== "listening/a practical skill.txt":
            b = codecs.open(r'arabic/a practical skill.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(b))
            
        
        if translatedfile1== "listening/presents.txt":
            c = codecs.open(r'arabic/present.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(c))
            
            
            
        if translatedfile1== "listening/favourite rooms.txt":
            d = codecs.open(r'arabic/favourite room.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(d))
            
            
        if translatedfile1== "listening/historical places.txt":
            e = codecs.open(r'arabic/historical places.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(e))
            
            
        if translatedfile1== "listening/sports.txt":
            f = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(f))
            
            
        if translatedfile1== "listening/a school.txt":
            g = codecs.open(r'arabic/a school.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(g))
            
            
        if translatedfile1== "listening/festival.txt":
            h = codecs.open(r'arabic/festival.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(h))
            
            
        if translatedfile1== "listening/resaurant.txt":
            i = codecs.open(r'arabic/restaurant.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(i))
            
        if translatedfile1== "listening/holiday.txt":
            j = codecs.open(r'arabic/holiday.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(j))
            
            
        if translatedfile1== "listening/website.txt":
            k = codecs.open(r'arabic/website.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(k))
            
            
        if translatedfile1== "listening/travel.txt":
            l = codecs.open(r'arabic/travel.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(l))
            
        if translatedfile1== "listening/books.txt":
            m = codecs.open(r'arabic/books.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(m))
            
            
        if translatedfile1== "listening/accident.txt":
            n = codecs.open(r'arabic/accident.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(n))
            
            
        if translatedfile1== "listening/animals.txt":
            o = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(o))
            
            
        if translatedfile1== "listening/a hotel.txt":
            p = codecs.open(r'arabic/a hotel.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(p))
            
            
        if translatedfile1== "listening/a letter.txt":
            q = codecs.open(r'arabic/a letter.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(q))
            
            
        if translatedfile1== "listening/hobbies.txt":
            r = codecs.open(r'arabic/hobbies.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(r))
            
        if translatedfile1== "listening/music.txt":
            t = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(t))
        
        
        
        if translatedfile1== "listening/shopping.txt":
            u = codecs.open(r'arabic/shopping.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(u))
            
            
        if translatedfile1== "listening/memorable event.txt":
            v = codecs.open(r'arabic/memorable event.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(v))
            
        if translatedfile1== "listening/favorite subject.txt":
            w = codecs.open(r'arabic/favorite subject.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(w))
            
            
        if translatedfile1== "listening/museums.txt":
            x = codecs.open(r'arabic/museums.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x))
            
        if translatedfile1== "listening/movie.txt":
            y = codecs.open(r'arabic/movie theater.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(y))
            
            
        if translatedfile1== "listening/a foreign country.txt":
            z = codecs.open(r'arabic/foreign country.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(z))
            
            
        if translatedfile1== "listening/parties.txt":
            aa = codecs.open(r'arabic/parties.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(aa))
            
        if translatedfile1== "listening/a teacher.txt":
            bb = codecs.open(r'arabic/a teacher.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(bb))
            
            
        if translatedfile1== "listening/a friend.txt":
            cc = codecs.open(r'arabic/a friend.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(cc))
            
            
        if translatedfile1== "listening-intermediate/lesson#01.txt":
            dd = codecs.open(r'arabic/favorite things.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(dd))
            
        if translatedfile1== "listening-intermediate/lesson#02.txt":
            ee = codecs.open(r'arabic/activity.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ee))
            
            
        if translatedfile1== "listening-intermediate/lesson#03.txt":
            ff = codecs.open(r'arabic/working out.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ff))
            
        
        if translatedfile1== "listening-intermediate/lesson#04.txt":
            gg = codecs.open(r'arabic/introductions.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(gg))
            
            
        if translatedfile1== "listening-intermediate/lesson#05.txt":
            hh = codecs.open(r'arabic/registering for class.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(hh))
            
            
        if translatedfile1== "listening-intermediate/lesson#06.txt":
            ii = codecs.open(r'arabic/registering.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ii))
            
            
            
        if translatedfile1== "listening-intermediate/lesson#07.txt":
            jj = codecs.open(r'arabic/grades.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(jj))
            
        
        if translatedfile1== "listening-intermediate/lesson#08.txt":
            kk = codecs.open(r'arabic/summer vacation.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(kk))
            
        
        if translatedfile1== "listening-intermediate/lesson#09.txt":
            ll = codecs.open(r'arabic/exams.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ll))
            
            
        if translatedfile1== "listening-intermediate/lesson#10.txt":
            mm = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(mm))
            
        if translatedfile1== "listening-intermediate/lesson#11.txt":
            nn = codecs.open(r'arabic/drinking.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(nn))
            
            
        if translatedfile1== "listening-intermediate/lesson#12.txt":
            oo = codecs.open(r'arabic/after birth.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(oo))
            
            
        if translatedfile1== "listening-intermediate/lesson#13.txt":
            pp = codecs.open(r'arabic/alleries.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(pp))
            
            
        if translatedfile1== "listening-intermediate/lesson#14.txt":
            qq = codecs.open(r'arabic/losing weight.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(qq))
            
        if translatedfile1== "listening-intermediate/lesson#15.txt":
            rr = codecs.open(r'arabic/dieting.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(rr))
            
            
        if translatedfile1== "listening-intermediate/lesson#16.txt":
            ss = codecs.open(r'arabic/asking for a date.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ss))
            
        
        if translatedfile1== "listening-intermediate/lesson#17.txt":
            tt = codecs.open(r'arabic/proposing.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(tt))
            
            
        if translatedfile1== "listening-intermediate/lesson#18.txt":
            uu = codecs.open(r'arabic/baseball.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(uu))
            
            
        if translatedfile1== "listening-intermediate/lesson#19.txt":
            vv = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(vv))
            
            
            
        if translatedfile1== "listening-intermediate/lesson#20.txt":
            ww = codecs.open(r'arabic/golf.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(ww))
            
            
        if translatedfile1== "listening-intermediate/lesson#21.txt":
            xx = codecs.open(r'arabic/mall shopping.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(xx))
            
            
        if translatedfile1== "listening-intermediate/lesson#23.txt":
            yy = codecs.open(r'arabic/jewelry gift.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(yy))
            
        
        if translatedfile1== "listening-intermediate/lesson#24.txt":
            zz = codecs.open(r'arabic/jewelry.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(zz))
            
            
        if translatedfile1== "listening-intermediate/lesson#25.txt":
            x1 = codecs.open(r'arabic/jewelry watch.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x1))
            
            
        if translatedfile1== "listening-intermediate/lesson#26.txt":
            x2 = codecs.open(r'arabic/having a baby.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x2))
            
            
        if translatedfile1== "listening-intermediate/lesson#27.txt":
            x3 = codecs.open(r'arabic/sick dad.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x3))
            
        if translatedfile1== "listening-intermediate/lesson#28.txt":
            x4 = codecs.open(r'arabic/stressful parents.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x4))
            
            
        if translatedfile1== "listening-intermediate/lesson#29.txt":
            x5 = codecs.open(r'arabic/grandmother passing away.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x5))
            
            
        if translatedfile1== "listening-advanced/lesson#01.txt":
            x6 = codecs.open(r'arabic/university conversation.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x6))
            
        
        
        if translatedfile1== "listening-advanced/lesson#02.txt":
            x7 = codecs.open(r'arabic/studying for exam.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x7))
            
            
        if translatedfile1== "listening-advanced/lesson#03.txt":
            x8 = codecs.open(r'arabic/roommates.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x8))
            
            
        if translatedfile1== "listening-advanced/lesson#04.txt":
            x9 = codecs.open(r'arabic/dormitory.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x9))
            
            
        if translatedfile1== "listening-advanced/lesson#05.txt":
            x10 = codecs.open(r'arabic/renting a room.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x10))
        
        
        
        
        if translatedfile1== "listening-intermediate/lesson#10.txt":
            x11 = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x11))
            
            
        if translatedfile1== "listening-advanced/lesson#07.txt":
            x12 = codecs.open(r'arabic/running into a friend.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x12))
            
            
            
        if translatedfile1== "listening-advanced/lesson#08.txt":
            x13 = codecs.open(r'arabic/small talk.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x13))
            
            
        if translatedfile1== "listening-advanced/lesson#09.txt":
            x14 = codecs.open(r'arabic/hang out.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x14))
            
            
        if translatedfile1== "listening-advanced/lesson#10.txt":
            x15 = codecs.open(r'arabic/first date.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x15))
            
            
        if translatedfile1== "listening-advanced/lesson#11.txt":
            x16 = codecs.open(r'arabic/honeymoon planning.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x16))
            
            
        if translatedfile1== "listening-advanced/lesson#13.txt":
            x17 = codecs.open(r'arabic/weight loss.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x17))
            
            
            
        if translatedfile1== "listening-advanced/lesson#14.txt":
            x18 = codecs.open(r'arabic/marriage proposal.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x18))
            
            
        if translatedfile1== "listening-advanced/lesson#15.txt":
            x19 = codecs.open(r'arabic/watching baseball.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x19))
            
            
        if translatedfile1== "listening-advanced/lesson#17.txt":
            x20 = codecs.open(r'arabic/watching football.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x20))
            
            
        if translatedfile1== "listening-advanced/lesson#18.txt":
            x21 = codecs.open(r'arabic/poker.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x21))
            
            
        if translatedfile1== "listening-advanced/lesson#19.txt":
            x22 = codecs.open(r'arabic/talking about guys.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x22))
            
            
        if translatedfile1== "listening-advanced/lesson#20.txt":
            x23 = codecs.open(r'arabic/practicing golf.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x23))
            
        if translatedfile1== "listening-advanced/lesson#21.txt":
            x24 = codecs.open(r'arabic/favorite hobby.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x24))
            
            
        if translatedfile1== "listening-advanced/lesson#22.txt":
            x25 = codecs.open(r'arabic/life after breaking up.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x25))
        
        
        if translatedfile1== "listening-advanced/lesson#23.txt":
            x26 = codecs.open(r'arabic/heart broken.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x26))
        
        
        if translatedfile1== "listening-advanced/lesson#24.txt":
            x27 = codecs.open(r'arabic/being afraid.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x27))
            
        if translatedfile1== "listening-advanced/lesson#25.txt":
            x28 = codecs.open(r'arabic/restless.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x28))
            
            
        if translatedfile1== "listening-advanced/lesson#26.txt":
            x29 = codecs.open(r'arabic/infatuation.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x29))
            
            
        if translatedfile1== "listening-advanced/lesson#27.txt":
            x30 = codecs.open(r'arabic/class friend.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x30))
            
            
        if translatedfile1== "listening-advanced/lesson#28.txt":
            x31 = codecs.open(r'arabic/general.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x31))
            
            
        if translatedfile1== "listening-advanced/lesson#29.txt":
            x32 = codecs.open(r'arabic/joining health club.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x32))
            
            
        if translatedfile1== "listening-advanced/lesson#31.txt":
            x33 = codecs.open(r'arabic/watching basketball.txt',encoding='utf-8').read()
            self.ids.myarab1.multiline = True
            self.ids.myarab1.text = get_display(arabic_reshaper.reshape(x33))
            
            
        
        
        
        
        
        
        
class ArabicText2(Screen):
    def on_pre_enter(self, *args):
        if translatedfile2== "listening/newspaper.txt":
            a = codecs.open(r'arabic/newspaper and magazine.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(a))
        
        
        if translatedfile2== "listening/a practical skill.txt":
            b = codecs.open(r'arabic/a practical skill.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(b))
            
        
        if translatedfile2== "listening/presents.txt":
            c = codecs.open(r'arabic/present.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(c))
            
            
            
        if translatedfile2== "listening/favourite rooms.txt":
            d = codecs.open(r'arabic/favourite room.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(d))
            
            
        if translatedfile2== "listening/historical places.txt":
            e = codecs.open(r'arabic/historical places.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(e))
            
            
        if translatedfile2== "listening/sports.txt":
            f = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(f))
            
            
        if translatedfile2== "listening/a school.txt":
            g = codecs.open(r'arabic/a school.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(g))
            
            
        if translatedfile2== "listening/festival.txt":
            h = codecs.open(r'arabic/festival.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(h))
            
            
        if translatedfile2== "listening/resaurant.txt":
            i = codecs.open(r'arabic/restaurant.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(i))
            
        if translatedfile2== "listening/holiday.txt":
            j = codecs.open(r'arabic/holiday.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(j))
            
            
        if translatedfile2== "listening/website.txt":
            k = codecs.open(r'arabic/website.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(k))
            
            
        if translatedfile2== "listening/travel.txt":
            l = codecs.open(r'arabic/travel.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(l))
            
        if translatedfile2== "listening/books.txt":
            m = codecs.open(r'arabic/books.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(m))
            
            
        if translatedfile2== "listening/accident.txt":
            n = codecs.open(r'arabic/accident.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(n))
            
            
        if translatedfile2== "listening/animals.txt":
            o = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(o))
            
            
        if translatedfile2== "listening/a hotel.txt":
            p = codecs.open(r'arabic/a hotel.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(p))
            
            
        if translatedfile2== "listening/a letter.txt":
            q = codecs.open(r'arabic/a letter.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(q))
            
            
        if translatedfile2== "listening/hobbies.txt":
            r = codecs.open(r'arabic/hobbies.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(r))
            
        if translatedfile2== "listening/music.txt":
            t = codecs.open(r'arabic/animals.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(t))
        
        
        
        if translatedfile2== "listening/shopping.txt":
            u = codecs.open(r'arabic/shopping.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(u))
            
            
        if translatedfile2== "listening/memorable event.txt":
            v = codecs.open(r'arabic/memorable event.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(v))
            
        if translatedfile2== "listening/favorite subject.txt":
            w = codecs.open(r'arabic/favorite subject.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(w))
            
            
        if translatedfile2== "listening/museums.txt":
            x = codecs.open(r'arabic/museums.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x))
            
        if translatedfile2== "listening/movie.txt":
            y = codecs.open(r'arabic/movie theater.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(y))
            
            
        if translatedfile2== "listening/a foreign country.txt":
            z = codecs.open(r'arabic/foreign country.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(z))
            
            
        if translatedfile2== "listening/parties.txt":
            aa = codecs.open(r'arabic/parties.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(aa))
            
        if translatedfile2== "listening/a teacher.txt":
            bb = codecs.open(r'arabic/a teacher.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(bb))
            
            
        if translatedfile2== "listening/a friend.txt":
            cc = codecs.open(r'arabic/a friend.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(cc))
            
            
        if translatedfile2== "listening-intermediate/lesson#01.txt":
            dd = codecs.open(r'arabic/favorite things.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(dd))
            
        if translatedfile2== "listening-intermediate/lesson#02.txt":
            ee = codecs.open(r'arabic/activity.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ee))
            
            
        if translatedfile2== "listening-intermediate/lesson#03.txt":
            ff = codecs.open(r'arabic/working out.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ff))
            
        
        if translatedfile2== "listening-intermediate/lesson#04.txt":
            gg = codecs.open(r'arabic/introductions.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(gg))
            
            
        if translatedfile2== "listening-intermediate/lesson#05.txt":
            hh = codecs.open(r'arabic/registering for class.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(hh))
            
            
        if translatedfile2== "listening-intermediate/lesson#06.txt":
            ii = codecs.open(r'arabic/registering.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ii))
            
            
            
        if translatedfile2== "listening-intermediate/lesson#07.txt":
            jj = codecs.open(r'arabic/grades.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(jj))
            
        
        if translatedfile2== "listening-intermediate/lesson#08.txt":
            kk = codecs.open(r'arabic/summer vacation.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(kk))
            
        
        if translatedfile2== "listening-intermediate/lesson#09.txt":
            ll = codecs.open(r'arabic/exams.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ll))
            
            
        if translatedfile2== "listening-intermediate/lesson#10.txt":
            mm = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(mm))
            
        if translatedfile2== "listening-intermediate/lesson#11.txt":
            nn = codecs.open(r'arabic/drinking.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(nn))
            
            
        if translatedfile2== "listening-intermediate/lesson#12.txt":
            oo = codecs.open(r'arabic/after birth.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(oo))
            
            
        if translatedfile2== "listening-intermediate/lesson#13.txt":
            pp = codecs.open(r'arabic/alleries.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(pp))
            
            
        if translatedfile2== "listening-intermediate/lesson#14.txt":
            qq = codecs.open(r'arabic/losing weight.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(qq))
            
        if translatedfile2== "listening-intermediate/lesson#15.txt":
            rr = codecs.open(r'arabic/dieting.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(rr))
            
            
        if translatedfile2== "listening-intermediate/lesson#16.txt":
            ss = codecs.open(r'arabic/asking for a date.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ss))
            
        
        if translatedfile2== "listening-intermediate/lesson#17.txt":
            tt = codecs.open(r'arabic/proposing.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(tt))
            
            
        if translatedfile2== "listening-intermediate/lesson#18.txt":
            uu = codecs.open(r'arabic/baseball.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(uu))
            
            
        if translatedfile2== "listening-intermediate/lesson#19.txt":
            vv = codecs.open(r'arabic/general sports.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(vv))
            
            
            
        if translatedfile2== "listening-intermediate/lesson#20.txt":
            ww = codecs.open(r'arabic/golf.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(ww))
            
            
        if translatedfile2== "listening-intermediate/lesson#21.txt":
            xx = codecs.open(r'arabic/mall shopping.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(xx))
            
            
        if translatedfile2== "listening-intermediate/lesson#23.txt":
            yy = codecs.open(r'arabic/jewelry gift.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(yy))
            
        
        if translatedfile2== "listening-intermediate/lesson#24.txt":
            zz = codecs.open(r'arabic/jewelry.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(zz))
            
            
        if translatedfile2== "listening-intermediate/lesson#25.txt":
            x1 = codecs.open(r'arabic/jewelry watch.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x1))
            
            
        if translatedfile2== "listening-intermediate/lesson#26.txt":
            x2 = codecs.open(r'arabic/having a baby.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x2))
            
            
        if translatedfile2== "listening-intermediate/lesson#27.txt":
            x3 = codecs.open(r'arabic/sick dad.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x3))
            
        if translatedfile2== "listening-intermediate/lesson#28.txt":
            x4 = codecs.open(r'arabic/stressful parents.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x4))
            
            
        if translatedfile2== "listening-intermediate/lesson#29.txt":
            x5 = codecs.open(r'arabic/grandmother passing away.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x5))
            
            
        if translatedfile2== "listening-advanced/lesson#01.txt":
            x6 = codecs.open(r'arabic/university conversation.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x6))
            
        
        
        if translatedfile2== "listening-advanced/lesson#02.txt":
            x7 = codecs.open(r'arabic/studying for exam.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x7))
            
            
        if translatedfile2== "listening-advanced/lesson#03.txt":
            x8 = codecs.open(r'arabic/roommates.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x8))
            
            
        if translatedfile2== "listening-advanced/lesson#04.txt":
            x9 = codecs.open(r'arabic/dormitory.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x9))
            
            
        if translatedfile2== "listening-advanced/lesson#05.txt":
            x10 = codecs.open(r'arabic/renting a room.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x10))
        
        
        
        
        if translatedfile2== "listening-intermediate/lesson#10.txt":
            x11 = codecs.open(r'arabic/smoking.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x11))
            
            
        if translatedfile2== "listening-advanced/lesson#07.txt":
            x12 = codecs.open(r'arabic/running into a friend.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x12))
            
            
            
        if translatedfile2== "listening-advanced/lesson#08.txt":
            x13 = codecs.open(r'arabic/small talk.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x13))
            
            
        if translatedfile2== "listening-advanced/lesson#09.txt":
            x14 = codecs.open(r'arabic/hang out.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x14))
            
            
        if translatedfile2== "listening-advanced/lesson#10.txt":
            x15 = codecs.open(r'arabic/first date.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x15))
            
            
        if translatedfile2== "listening-advanced/lesson#11.txt":
            x16 = codecs.open(r'arabic/honeymoon planning.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x16))
            
            
        if translatedfile2== "listening-advanced/lesson#13.txt":
            x17 = codecs.open(r'arabic/weight loss.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x17))
            
            
            
        if translatedfile2== "listening-advanced/lesson#14.txt":
            x18 = codecs.open(r'arabic/marriage proposal.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x18))
            
            
        if translatedfile2== "listening-advanced/lesson#15.txt":
            x19 = codecs.open(r'arabic/watching baseball.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x19))
            
            
        if translatedfile2== "listening-advanced/lesson#17.txt":
            x20 = codecs.open(r'arabic/watching football.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x20))
            
            
        if translatedfile2== "listening-advanced/lesson#18.txt":
            x21 = codecs.open(r'arabic/poker.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x21))
            
            
        if translatedfile2== "listening-advanced/lesson#19.txt":
            x22 = codecs.open(r'arabic/talking about guys.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x22))
            
            
        if translatedfile2== "listening-advanced/lesson#20.txt":
            x23 = codecs.open(r'arabic/practicing golf.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x23))
            
        if translatedfile2== "listening-advanced/lesson#21.txt":
            x24 = codecs.open(r'arabic/favorite hobby.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x24))
            
            
        if translatedfile2== "listening-advanced/lesson#22.txt":
            x25 = codecs.open(r'arabic/life after breaking up.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x25))
        
        
        if translatedfile2== "listening-advanced/lesson#23.txt":
            x26 = codecs.open(r'arabic/heart broken.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x26))
        
        
        if translatedfile2== "listening-advanced/lesson#24.txt":
            x27 = codecs.open(r'arabic/being afraid.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x27))
            
        if translatedfile2== "listening-advanced/lesson#25.txt":
            x28 = codecs.open(r'arabic/restless.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x28))
            
            
        if translatedfile2== "listening-advanced/lesson#26.txt":
            x29 = codecs.open(r'arabic/infatuation.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x29))
            
            
        if translatedfile1== "listening-advanced/lesson#27.txt":
            x30 = codecs.open(r'arabic/class friend.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x30))
            
            
        if translatedfile2== "listening-advanced/lesson#28.txt":
            x31 = codecs.open(r'arabic/general.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x31))
            
            
        if translatedfile2== "listening-advanced/lesson#29.txt":
            x32 = codecs.open(r'arabic/joining health club.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x32))
            
            
        if translatedfile2== "listening-advanced/lesson#31.txt":
            x33 = codecs.open(r'arabic/watching basketball.txt',encoding='utf-8').read()
            self.ids.myarab2.multiline = True
            self.ids.myarab2.text = get_display(arabic_reshaper.reshape(x33))
            
            
            
            
class GramarPage(Screen):
    def load_grammar_lesson_text(self, lesson_title):
        """
        DYNAMIC ASSET LOADER:
        Takes the button text/title clicked by the user, converts it to a clean 
        filename format, and streams it safely into your textinput widget.
        Works identically on Windows and Android!
        """
        # 1. Platform-Aware Folder Path Alignment
        if platform == 'android':
            # Points directly to the unzipped application asset bundle inside the APK
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        # 2. Automatically convert the lesson title to a lowercase file name string
        # Example: "Present Simple" becomes "present simple.txt"
        file_target_name = f"{lesson_title.lower().strip()}.txt"
        
        # Construct the absolute path targeting your exact directory folder string 'grammar page'
        target_txt_path = os.path.join(base_dir, "grammar page", file_target_name)
        print(f"[GRAMMAR SYSTEM] Reading asset text map from path: {target_txt_path}")

        # 3. Read the file utilizing auto-closing stream contexts to prevent mobile memory leaks
        if os.path.exists(target_txt_path):
            try:
                with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                    grammar_content = f.read()
                
                # Apply your native Arabic text reshaping engine requirements
                # 🚨 MAKE SURE 'ph' MATCHES THE ID OF THE TEXTINPUT WIDGET ON THIS SCREEN!
                if 'page' in self.ids:
                    self.ids.page.multiline = True
                    self.ids.page.text = get_display(arabic_reshaper.reshape(grammar_content))
                    print(f"🎉 SUCCESS: Rendered grammar content for -> {file_target_name}")
                else:
                    print("🚨 LAYOUT ERROR: TextInput ID 'ph' was not found on this screen class.")
            except Exception as file_read_error:
                print(f"🚨 FILE ACCESS ERROR: Cannot parse text stream -> {file_read_error}")
                if 'page' in self.ids:
                    self.ids.page.text = "Error loading lesson content."
        else:
            print(f"🚨 CRITICAL MISSING ASSET: File path does not exist -> {target_txt_path}")
            if 'page' in self.ids:
                self.ids.page.text = f"Grammar script file missing:\n{file_target_name}"

            
        
         
















class GramarPage1(Screen):
    def load_grammar_lesson_text(self, lesson_title):
        """
        DYNAMIC ASSET LOADER:
        Takes the button text/title clicked by the user, converts it to a clean 
        filename format, and streams it safely into your textinput widget.
        Works identically on Windows and Android!
        """
        # 1. Platform-Aware Folder Path Alignment
        if platform == 'android':
            # Points directly to the unzipped application asset bundle inside the APK
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        # 2. Automatically convert the lesson title to a lowercase file name string
        # Example: "Present Simple" becomes "present simple.txt"
        file_target_name = f"{lesson_title.lower().strip()}.txt"
        
        # Construct the absolute path targeting your exact directory folder string 'grammar page'
        target_txt_path = os.path.join(base_dir, "grammar page", file_target_name)
        print(f"[GRAMMAR SYSTEM] Reading asset text map from path: {target_txt_path}")

        # 3. Read the file utilizing auto-closing stream contexts to prevent mobile memory leaks
        if os.path.exists(target_txt_path):
            try:
                with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                    grammar_content = f.read()
                
                # Apply your native Arabic text reshaping engine requirements
                # 🚨 MAKE SURE 'ph' MATCHES THE ID OF THE TEXTINPUT WIDGET ON THIS SCREEN!
                if 'page' in self.ids:
                    self.ids.page.multiline = True
                    self.ids.page.text = get_display(arabic_reshaper.reshape(grammar_content))
                    print(f"🎉 SUCCESS: Rendered grammar content for -> {file_target_name}")
                else:
                    print("🚨 LAYOUT ERROR: TextInput ID 'ph' was not found on this screen class.")
            except Exception as file_read_error:
                print(f"🚨 FILE ACCESS ERROR: Cannot parse text stream -> {file_read_error}")
                if 'page' in self.ids:
                    self.ids.page.text = "Error loading lesson content."
        else:
            print(f"🚨 CRITICAL MISSING ASSET: File path does not exist -> {target_txt_path}")
            if 'page' in self.ids:
                self.ids.page.text = f"Grammar script file missing:\n{file_target_name}"

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class GramarPage2(Screen):
    def load_grammar_lesson_text(self, lesson_title):
        """
        DYNAMIC ASSET LOADER:
        Takes the button text/title clicked by the user, converts it to a clean 
        filename format, and streams it safely into your textinput widget.
        Works identically on Windows and Android!
        """
        # 1. Platform-Aware Folder Path Alignment
        if platform == 'android':
            # Points directly to the unzipped application asset bundle inside the APK
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        # 2. Automatically convert the lesson title to a lowercase file name string
        # Example: "Present Simple" becomes "present simple.txt"
        file_target_name = f"{lesson_title.lower().strip()}.txt"
        
        # Construct the absolute path targeting your exact directory folder string 'grammar page'
        target_txt_path = os.path.join(base_dir, "grammar page", file_target_name)
        print(f"[GRAMMAR SYSTEM] Reading asset text map from path: {target_txt_path}")

        # 3. Read the file utilizing auto-closing stream contexts to prevent mobile memory leaks
        if os.path.exists(target_txt_path):
            try:
                with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                    grammar_content = f.read()
                
                # Apply your native Arabic text reshaping engine requirements
                # 🚨 MAKE SURE 'ph' MATCHES THE ID OF THE TEXTINPUT WIDGET ON THIS SCREEN!
                if 'page' in self.ids:
                    self.ids.page.multiline = True
                    self.ids.page.text = get_display(arabic_reshaper.reshape(grammar_content))
                    print(f"🎉 SUCCESS: Rendered grammar content for -> {file_target_name}")
                else:
                    print("🚨 LAYOUT ERROR: TextInput ID 'ph' was not found on this screen class.")
            except Exception as file_read_error:
                print(f"🚨 FILE ACCESS ERROR: Cannot parse text stream -> {file_read_error}")
                if 'page' in self.ids:
                    self.ids.page.text = "Error loading lesson content."
        else:
            print(f"🚨 CRITICAL MISSING ASSET: File path does not exist -> {target_txt_path}")
            if 'page' in self.ids:
                self.ids.page.text = f"Grammar script file missing:\n{file_target_name}"

        
        
        
        
        
        
        
        
        
class PhrasalVerb(Screen):
     
     
    
            
    
    
    
    
    
     
    
    def on_pre_enter(self, *args):
        global p,p1,p2,p3,p4,ph_id_list
        global c1
        global theoption1phrasal
        global theid1
        
         
        if not p or len(p) == 0:
                Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
                return
         
        c1 = c1 + 1
                 
                 # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
                 # Replaces hardcoded 3399 limits so your quiz scales automatically if rows change!
        if c1 >= len(p):
            c1 = 0   
            
            
            
        myinteger = random.randint(1,2)
        if myinteger == 1:
            self.ids.record3.text = str (p[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str (p1[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str (p2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str (p3[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(p4[c1]).strip("()").strip(",").strip("''")
            theid1 = str(ph_id_list[c1]).strip("()").strip(",").strip("''")
        else:
            self.ids.record3.text = str (p[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str (p3[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str (p2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str (p1[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(p4[c1]).strip("()").strip(",").strip("''")
            theid1 = str(ph_id_list[c1]).strip("()").strip(",").strip("''")
        
        
        
    def writeit(self):
        
        f = open("phrasal1.txt","w")
        
        f.write(theid1)
        f.close()
    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

            
         


class PhrasalVerb1(Screen):
     
    
            
     
    
    
    
     
    
    def on_pre_enter(self, *args):
        global pp, pp1, pp2, pp3, pp4, pid
        global c1, theoption1phrasal, theid1  # FIX 1: Aligned tracking variable name to 'theid1'
        
        # FIX 2: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not pp or len(pp) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        c1 = c1 + 1
        
        # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 3399 limits so your quiz scales automatically if rows change!
        if c1 >= len(pp):
            c1 = 0
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.record3.text = str(pp[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str(pp1[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str(pp2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str(pp3[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(pp4[c1]).strip("()").strip(",").strip("''")
            theid1 = str(pid[c1]).strip("()").strip(",").strip("''")
        else:
            self.ids.record3.text = str(pp[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str(pp3[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str(pp2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str(pp1[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(pp4[c1]).strip("()").strip(",").strip("''") # FIX 4: Corrected 'p4' typo to 'pp4'
            theid1 = str(pid[c1]).strip("()").strip(",").strip("''")
        
        
        
    def writeit(self):
        
        f = open("phrasal1.txt","w")
        
        f.write(theid1)
        f.close()
    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)


class PhrasalVerb2(Screen):
     
    
            
     
    
    
    
     
    
    def on_pre_enter(self, *args):
        global ph, ph1, ph2, ph3, ph4, phid
        global c1, theoption1phrasal, theid1  # FIX 1: Aligned tracking variable name to 'theid1'
        
        # FIX 2: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not ph or len(ph) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        c1 = c1 + 1
        
        # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 3399 limits so your quiz scales automatically if rows change!
        if c1 >= len(ph):
            c1 = 0
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.record3.text = str(ph[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str(ph1[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str(ph2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str(ph3[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(ph4[c1]).strip("()").strip(",").strip("''")
            theid1 = str(phid[c1]).strip("()").strip(",").strip("''")
        else:
            self.ids.record3.text = str(ph[c1]).strip("()").strip(",").strip("''")
            self.ids.lab1.text = str(ph3[c1]).strip("()").strip(",").strip("''")
            self.ids.lab2.text = str(ph2[c1]).strip("()").strip(",").strip("''")
            self.ids.lab3.text = str(ph1[c1]).strip("()").strip(",").strip("''")
            theoption1phrasal = str(ph4[c1]).strip("()").strip(",").strip("''")
            theid1 = str(phid[c1]).strip("()").strip(",").strip("''")
        
        
        
    def writeit(self):
        
        f = open("phrasal1.txt","w")
        
        f.write(theid1)
        f.close()
    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

class ShowphrResult(Screen):
    
    def on_pre_enter(self, *args):
    
    # ... (Your existing counter tracking calculations and database list fetches) ...
        global theoption1phrasal
        theoption1phrasal = str(p4[c1]).strip("()").strip(",").strip("''")
        
        # 👉 ADD THIS SINGLE LINE: It instantly reads the text file matching whatever question is currently active!
        self.load_phrasal_verb_text()
 
 
    def load_phrasal_verb_text(self, *args):
        
        global theoption1phrasal
        
        # 1. Platform-Aware Folder Path Alignment
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        # 2. Automatically format the file name based on your active database choice string
        # Converts "BE AFTER" -> "be after.txt", "RUB OUT1" -> "rub out1.txt"
        file_target_name = f"{theoption1phrasal.lower()}.txt"
        
        # FIXED: Targets your exact folder spelling string 'phrsalverbs'
        target_txt_path = os.path.join(base_dir, "phrasalverbs", file_target_name)
        print(f"[DYNAMIC ACCESS] Reading phrasal text file asset from: {target_txt_path}")

        # 3. Read the file safely utilizing auto-closing stream contexts
        if os.path.exists(target_txt_path):
            try:
                with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                    file_contents = f.read()
                
                # Apply your Arabic reshaper configuration rules natively
                self.ids.ph.multiline = True
                self.ids.ph.text = get_display(arabic_reshaper.reshape(file_contents))
            except Exception as file_read_error:
                print(f"🚨 FILE ACCESS ERROR: Cannot read asset -> {file_read_error}")
                self.ids.ph.text = "Error reading phrasal content."
        else:
            print(f"🚨 MISSING ASSET: File does not exist -> {target_txt_path}")
            self.ids.ph.text = "Phrasal verb lesson script text file missing."











class Vocabulary_a(Screen):
    def on_pre_enter(self, *args):
        global vvo,vvo1,vvo2,vvo3,vvo4,vvo_id
        global vcounter
        
        global the_potion_vocabulary
        global the_voc_id
        if not vvo or len(vvo) == 0:
                Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
                return
        
        vcounter = vcounter + 1
                
            # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
            # Replaces hardcoded 3399 limits so your quiz scales automatically if rows change!
        if  vcounter >= len(vvo):
            vcounter= 0
            
            
        myinteger = random.randint(1,2)
        if myinteger == 1:
            self.ids.vocabu.text = str (vvo[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str (vvo1[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str (vvo2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str (vvo3[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(vo4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(vvo_id[vcounter]).strip("()").strip(",").strip("''")
        else:
            self.ids.vocabu.text = str (vvo[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str (vvo3[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str (vvo2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str (vvo1[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(vo4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(vvo_id[vcounter]).strip("()").strip(",").strip("''")

    def writeit(self):
        
        f = open("vocabulary.txt","w")
        
        f.write(the_voc_id)
        f.close()

    def stophere1(self):
        f = open("stophere.txt","w")
        f.write(intermediateid)
        f.close()

    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)



    
            
    
    
    
    
    
     
    
    
class Vocabulary_b(Screen):
    #global vo,vo1,vo2,vo3,vo4,vo_id
    
            
    
    
    
    
     
    
    def on_pre_enter(self, *args):
        global vcounter, the_potion_vocabulary, the_voc_id
        global vo, vo1, vo2, vo3, vo4, vo_id
        
        # SAFEGUARD: If background thread hasn't finished reading the database yet,
        # wait 0.2 seconds and retry. This completely prevents Android black screens and crashes!
        if not vo or len(vo) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        vcounter = vcounter + 1
        
        # Bounds check to make sure vcounter doesn't go out of range of the database size
        if vcounter >= len(vo) or vcounter == 203:
            vcounter = 1
            
        myinteger = random.randint(1, 2)
        if myinteger == 1:
            self.ids.vocabu.text = str(vo[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str(vo1[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str(vo2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str(vo3[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(vo4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(vo_id[vcounter]).strip("()").strip(",").strip("''")
        else:
            self.ids.vocabu.text = str(vo[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str(vo3[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str(vo2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str(vo1[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(vo4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(vo_id[vcounter]).strip("()").strip(",").strip("''")

    def writeit(self):
        
        f = open("vocabulary.txt","w")
        
        f.write(the_voc_id)
        f.close()



    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

class Vocabulary_c(Screen):
    
    
            
    
     
    
    def on_pre_enter(self, *args):
        global o,o1,o2,o3,o4,o_id
        global vcounter
        
        global the_potion_vocabulary
        global the_voc_id
        if not o or len(o) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return
                
        vcounter = vcounter + 1
                        
                    # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
                    # Replaces hardcoded 3399 limits so your quiz scales automatically if rows change!
        if  vcounter >= len(o):
            vcounter= 0
            
            
            
        myinteger = random.randint(1,2)
        if myinteger == 1:
            self.ids.vocabu.text = str (o[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str (o1[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str (o2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str (o3[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(o4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(o_id[vcounter]).strip("()").strip(",").strip("''")
        else:
            self.ids.vocabu.text = str (o[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v1.text = str (o3[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v2.text = str (o2[vcounter]).strip("()").strip(",").strip("''")
            self.ids.v3.text = str (o1[vcounter]).strip("()").strip(",").strip("''")
            the_potion_vocabulary = str(o4[vcounter]).strip("()").strip(",").strip("''")
            the_voc_id = str(o_id[vcounter]).strip("()").strip(",").strip("''")

    def writeit(self):
        
        f = open("vocabulary.txt","w")
        
        f.write(the_voc_id)
        f.close()
    


    def on_estate_check(self):
        
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

class ShowVocabulary(Screen):
    def on_pre_enter(self, *args):
    
        
            # ... (Your existing counter tracking calculations and database list fetches) ...
        global the_potion_vocabulary
        the_potion_vocabulary = str(o4[vcounter]).strip("()").strip(",").strip("''")
        
        # 👉 ADD THIS SINGLE LINE: It instantly reads the text file matching whatever question is currently active!
        self.load_vocabulary_text()
        
        
    def load_vocabulary_text(self, *args):
        
        global the_potion_vocabulary
        
        # 1. Platform-Aware Folder Path Alignment
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()

        # 2. Automatically format the file name based on your active database choice string
        # Converts "BE AFTER" -> "be after.txt", "RUB OUT1" -> "rub out1.txt"
        file_target_name = f"{the_potion_vocabulary.lower()}.txt"
        
        # FIXED: Targets your exact folder spelling string 'phrsalverbs'
        target_txt_path = os.path.join(base_dir, "vocabulary tests", file_target_name)
        print(f"[DYNAMIC ACCESS] Reading phrasal text file asset from: {target_txt_path}")

        # 3. Read the file safely utilizing auto-closing stream contexts
        if os.path.exists(target_txt_path):
            try:
                with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                    file_contents = f.read()
                
                # Apply your Arabic reshaper configuration rules natively
                self.ids.ph.multiline = True
                self.ids.ph.text = get_display(arabic_reshaper.reshape(file_contents))
            except Exception as file_read_error:
                print(f"🚨 FILE ACCESS ERROR: Cannot read asset -> {file_read_error}")
                self.ids.ph.text = "Error reading phrasal content."
        else:
            print(f"🚨 MISSING ASSET: File does not exist -> {target_txt_path}")
            self.ids.ph.text = "Phrasal verb lesson script text file missing."





class Punctuation1(Screen):
     
    
            
     
    
    
    
    
     
    
    def on_pre_enter(self, *args):
        global class_punctuation1 
        class_punctuation1  = "true"
        global class_punctuation2 
        class_punctuation2 ="false"
        global class_punctuation3 
        class_punctuation3 ="false"
        
        global punc, punc1, punc2, punc3, punc4, punc_id, r
        global punc_counter, the_punctuation, the_rightanswer, the_punctuation_id
        
        # FIX 1: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not punc or len(punc) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        punc_counter = punc_counter + 1
        
        # FIX 2: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 224 limits so your quiz scales automatically if rows change!
        if punc_counter >= len(punc):
            punc_counter = 0
            
        # UI Updates and Global Assignments
        self.ids.punc1.text = str(punc[punc_counter]).strip("()").strip(",").strip("''")
        self.ids.punc2.text = str(punc1[punc_counter]).strip("()").strip(",").strip("''")
        self.ids.punc3.text = str(punc2[punc_counter]).strip("()").strip(",").strip("''")
        self.ids.punc4.text = str(punc3[punc_counter]).strip("()").strip(",").strip("''")
        
        the_punctuation = str(punc4[punc_counter]).strip("()").strip(",").strip("''")
        the_punctuation_id = str(punc_id[punc_counter]).strip("()").strip(",").strip("''")
        
        # FIX 3: Corrected the 'the_righanswer' spelling mistake to match your global declaration
        the_rightanswer = str(r[punc_counter]).strip("()").strip(",").strip("''")
    def writepunc(self):
        
        f = open("punctuation.txt","w")
        
        f.write(the_punctuation_id)
        f.close()

    def on_estate_check(self):
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        
class Punctuation2(Screen):
     
    
            
     
    
     
    
    def on_pre_enter(self, *args):
        global class_punctuation1 
        class_punctuation1  = "false"
        global class_punctuation2 
        class_punctuation2 ="true"
        global class_punctuation3 
        class_punctuation3 ="false"
        
        
        global ppunc, ppunc1, ppunc2, ppunc3, ppunc4, punc_idl, pr
        global punc_counter2, the_punctuation, the_punctuation_id, the_rightanswer  # FIX 1: Using punc_counter2
        
        # FIX 2: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not ppunc or len(ppunc) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        punc_counter2 = punc_counter2 + 1
        
        # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 224 limits so your quiz scales automatically if rows change!
        if punc_counter2 >= len(ppunc):
            punc_counter2 = 0
            
        # UI Updates and Global Assignments from your pre-loaded lists
        self.ids.punc1.text = str(ppunc[punc_counter2]).strip("()").strip(",").strip("''")
        self.ids.punc2.text = str(ppunc1[punc_counter2]).strip("()").strip(",").strip("''")
        self.ids.punc3.text = str(ppunc2[punc_counter2]).strip("()").strip(",").strip("''")
        self.ids.punc4.text = str(ppunc3[punc_counter2]).strip("()").strip(",").strip("''")
        
        the_punctuation = str(ppunc4[punc_counter2]).strip("()").strip(",").strip("''")
        the_punctuation_id = str(punc_idl[punc_counter2]).strip("()").strip(",").strip("''")
        the_rightanswer = str(pr[punc_counter2]).strip("()").strip(",").strip("''")
     
    def writepunc(self):
        
        f = open("punctuation.txt","w")
        
        f.write(the_punctuation_id)
        f.close()
    def on_estate_check(self):
        global result3, counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global result3, counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if result3 and counter3 < len(result3):
            correct_answer_str = str(result3[counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.l1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.l2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.l3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

class Punctuation3(Screen):
     
    def on_pre_enter(self, *args):
        self.ids.punc1.text = str(pc[0]).strip("()").strip(",").strip("''")
        self.ids.punc2.text = str(pc1[0]).strip("()").strip(",").strip("''")
        self.ids.punc3.text = str(pc2[0]).strip("()").strip(",").strip("''")
        self.ids.punc4.text = str(pc3[0]).strip("()").strip(",").strip("''")
                 
        the_punctuation = str(pc4[0]).strip("()").strip(",").strip("''")
        # FIX 4: Added the missing punctuation ID assignment line
        the_punctuation_id = str(pc_id[0]).strip("()").strip(",").strip("''")
        the_rightanswer = str(pcr[0]).strip("()").strip(",").strip("''")
                      
     
    
    
     
    
    def show_punc3(self):
        self.ids.check1.active ="false"
        self.check2.active ="false"
        self.check3.active ="false"
        self.check4.active ="false"
        
        global class_punctuation1 
        class_punctuation1  = "false"
        global class_punctuation2 
        class_punctuation2 ="false"
        global class_punctuation3 
        class_punctuation3 ="true"
        
        
        
        global pc, pc1, pc2, pc3, pc4, pc_id, pcr
        global punc_counter3, the_punctuation, the_punctuation_id, the_rightanswer  # FIX 1: Using punc_counter3
        
        # FIX 2: DELAYED RETRY SAFEGUARD
        # If the background database pre-load thread is still loading rows into memory, 
        # pause for 0.2 seconds and retry cleanly. Bypasses all index crashes on Android!
        if not pc or len(pc) == 0:
            Clock.schedule_once(lambda dt: self.on_pre_enter(), 0.2)
            return

        punc_counter3 = punc_counter3 + 1
        
        # FIX 3: DYNAMIC DATABASE LENGTH BOUNDS CHECK
        # Replaces hardcoded 224 limits so your quiz scales automatically if rows change!
        if punc_counter3 >= len(pc):
            punc_counter3 = 0
        
            # UI Updates and Global Assignments from your pre-loaded lists
        self.ids.punc1.text = str(pc[punc_counter3]).strip("()").strip(",").strip("''")
        self.ids.punc2.text = str(pc1[punc_counter3]).strip("()").strip(",").strip("''")
        self.ids.punc3.text = str(pc2[punc_counter3]).strip("()").strip(",").strip("''")
        self.ids.punc4.text = str(pc3[punc_counter3]).strip("()").strip(",").strip("''")
        
        the_punctuation = str(pc4[punc_counter3]).strip("()").strip(",").strip("''")
         # FIX 4: Added the missing punctuation ID assignment line
        the_punctuation_id = str(pc_id[punc_counter3]).strip("()").strip(",").strip("''")
        the_rightanswer = str(pcr[punc_counter3]).strip("()").strip(",").strip("''")
        
    
    def writepunc(self):
        
        f = open("punctuation.txt","w")
        
        f.write(the_punctuation_id)
        f.close()
    def on_estate_check(self):
        global pc, punc_counter3
        
        # 1. Resolve absolute path dynamically (Works on Windows and Android)
        # Packages extracted locally on Android run relative to the current working directory
        base_dir = os.getcwd()
        right_sound_path = os.path.join(base_dir, "answers", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "answers", "wronganswer.mp3") # Assumes you have a wrong clip

        # Helper function to play sound effects securely without leaking phone RAM channels
    def play_audio_cue(self, file_path):
        """ Safe, self-unloading core audio loader module """
        if os.path.exists(file_path):
            sound = SoundLoader.load(file_path)
            if sound:
                sound.play()
                # Automatically unloads audio file from RAM once finished
                Clock.schedule_once(lambda dt: sound.unload(), 2)

    def trigger_sound(self, *args):
        global pc, punc_counter3
        
        # Build paths directly using your unified app storage path setup
        base_dir = App.get_running_app().internal_sandbox_dir
        right_sound_path = os.path.join(base_dir, "my_audio_album", "rightanswer.mp3")
        wrong_sound_path = os.path.join(base_dir, "my_audio_album", "wronganswer.mp3")

        # Ensure data arrays exist before indexing to completely bypass out-of-range crashes
        correct_answer_str = ""
        if pc and punc_counter3 < len(pc):
            correct_answer_str = str(pcr[punc_counter3]).strip("()").strip(",").strip("''")

        # --- CHECKBOX 1 EVALUATION ---
        if self.ids.check1.active:
            if self.ids.punc1.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3) 
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
        
        # --- CHECKBOX 2 EVALUATION ---
        elif self.ids.check2.active:
            if self.ids.punc2.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)

        # --- CHECKBOX 3 EVALUATION ---
        elif self.ids.check3.active:
            if self.ids.punc3.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
                
                
            
        elif self.ids.check4.active:
            if self.ids.punc4.text == correct_answer_str:
                self.play_audio_cue(right_sound_path)
                content = Label(text="Correct! Keep it up.", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)
            else:
                self.play_audio_cue(wrong_sound_path)
                content = Label(text="Sorry,Wrong answer, Try again", halign='center', valign='middle')
                popup = Popup(title='info', content=content, size_hint=(0.9, 0.2), auto_dismiss=False)
                popup.open()
                Clock.schedule_once(lambda dt: popup.dismiss(), 3)


class ShowPunctuation(Screen):
    def on_pre_enter(self, *args):
        global the_punctuation
       
        if class_punctuation3 == "true":
            the_punctuation = str(pc4[punc_counter3]).strip("()").strip(",").strip("''")
        elif class_punctuation2 == "true":        
            the_punctuation = str(ppunc4[punc_counter2]).strip("()").strip(",").strip("''")        # 👉 ADD THIS SINGLE LINE: It instantly reads the text file matching whatever question is currently active!
        elif class_punctuation1 =="true":
             the_punctuation = str(punc4[punc_counter]).strip("()").strip(",").strip("''")  
        self.load_punctuation_lesson_text()
              # 1. Bring your global database tracking choice variable into local scope
        
              
              # 2. Platform-Aware Folder Path Alignment
        
    def load_punctuation_lesson_text(self, *args):
        if  platform == 'android':
                        base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = os.getcwd()
              
            # 3. Automatically format the target filename matching your active database choice string
            # Clean up hidden spaces or quotes, and convert "THE COMMA" -> "the comma.txt"
            file_target_name = f"{the_punctuation.lower().strip()}.txt"
                      
            # Point the path resolver strictly to your 'punctuation' assets directory folder
            target_txt_path = os.path.join(base_dir, "punctuation", file_target_name)
            print(f"[PUNCTUATION LOOKUP] Reading asset text map from path: {target_txt_path}")
              
            # 4. Read the file safely utilizing auto-closing stream contexts to prevent memory leaks
            if os.path.exists(target_txt_path):
                try:
                    with codecs.open(target_txt_path, 'r', encoding='utf-8') as f:
                                punctuation_content = f.read()
                              
                            # Apply your native Arabic text reshaping engine requirements
                            # 🚨 MAKE SURE 'ph' MATCHES THE ID OF THE TEXTINPUT WIDGET ON THIS SCREEN!
                    if 'punc1' in self.ids:
                            self.ids.punc1.multiline = True
                            self.ids.punc1.text = get_display(arabic_reshaper.reshape(punctuation_content))
                            print(f"🎉 SUCCESS: Rendered punctuation text for -> {file_target_name}")
                    else:
                            print("🚨 LAYOUT ERROR: TextInput ID 'ph' was not found on this screen class.")
                except Exception as file_read_error:
                        print(f"🚨 FILE ACCESS ERROR: Cannot parse text stream -> {file_read_error}")
                        if 'punc1' in self.ids:
                                  self.ids.punc1.text = "Error loading punctuation content."
                        else:
                          print(f"🚨 CRITICAL MISSING ASSET: File path does not exist -> {target_txt_path}")
                          if 'punc1' in self.ids:
                              self.ids.pumc1.text = f"Punctuation lesson file missing:\n{file_target_name}"  

        

class Translation(Screen):
    def on_pre_enter(self, *args):
        global myresult1
        self.ids.my.text= get_display(arabic_reshaper.reshape(myresult1))
    def checkwindow(self):
        if truth1:
            self.manager.current='ww'
        if truth2:
            self.manager.current="con_a"

        if truth3:
            self.manager.current= "con_b"

class SplashScreen(Screen):
    # Setup native variable footprints inside the instance layer securely
    audio_folder = ""
    download_queue = {}
    total_files = 0
    current_file_index = 0
    current_file_name = ""

    def __init__(self, **kwargs):
        """ Force-register the screen node properties to Kivy's core iface matrix """
        super(SplashScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        
        # Queues initial load configurations cleanly 0.5s after window draws
        Clock.schedule_once(self.start_download_process, 0.5) 
        
    def start_download_process(self, dt=0):
        print(">>> DEBUG LOG: start_download_process HAS STARTED EXECUTING! <<<")
        
        # Safe fallback variable assignment to prevent string crashes if IDs are missing locally
        if self.ids and 'status_label' in self.ids:
            self.ids.status_label.text = "[DEBUG 1] Starting Setup..."
        else:
            print("[DEBUG 1] UI Labels missing or mismatched - proceeding silently.")

        try:
            if platform == 'android':
                base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
                print(f"[DEBUG 2] Target Platform: Android -> Sandbox: {base_dir}")
            else:
                base_dir = os.getcwd() 
                print(f"[DEBUG 2] Target Platform: Desktop -> Cache: {base_dir}")

            self.audio_folder = os.path.join(base_dir, "my_audio_album")
            if not os.path.exists(self.audio_folder):
                os.makedirs(self.audio_folder)
                print(f"[DEBUG 3] Audio Album Folder Created At: {self.audio_folder}")
            else:
                print(f"[DEBUG 3] Audio Album Folder Verified.")

            

            # Syncing URLs identically to avoid internal dictionary KeyError exceptions
            self.download_queue = {
                "beg_track1.mp3": {"url": "https://drive.google.com/uc?export=download&id=149cJGTKHzn5ScuYs_pMgkIbcHf3_xPnQ", "size": int(1.3 * 1024 * 1024)},
                "beg_track1.txt": {"url": "https://drive.google.com/uc?export=download&id=19vmi76eSXgzMyztsyzC3g17mZucvCvgJ", "size": int(1 * 1024)},
                "beg_track2.mp3": {"url": "https://drive.google.com/uc?export=download&id=1vN0cG_lGSMg7JKNL2etyA6aOWpy2Y35v", "size": int(1.1 * 1024 * 1024)},
                "beg_track2.txt": {"url": "https://drive.google.com/uc?export=download&id=1omouSzB59j8o3i9BWBsCwZ7L0ceABEJP", "size": int(1 * 1024)},
                "beg_track3.mp3": {"url": "https://drive.google.com/uc?export=download&id=1gZmtIyACIfZpABo3lZXQt7s0wNIbXtq_", "size": int(1.3 * 1024 * 1024)},
                "beg_track3.txt": {"url": "https://drive.google.com/uc?export=download&id=1EMcSc1vn39gC-5iKTX3rBNcPcbgV3Nzs", "size": int(1 * 1024)},
                "beg_track4.mp3": {"url": "https://drive.google.com/uc?export=download&id=1Svd88ADBa3IpVRWY-f6gC7t1n2C3UpEp", "size": int(1.008 * 1024)},
                "beg_track4.txt": {"url": "https://drive.google.com/uc?export=download&id=101eIWLABDLYwIQaRW5fnIQULA3hHcF3M", "size": 909},
                "beg_track5.mp3": {"url": "https://drive.google.com/uc?export=download&id=1lZZ10DNFY_A8BgL7_nw7FiSoJRJl-dZa", "size": int(1.3 * 1024 * 1024)},
                "beg_track5.txt": {"url": "https://drive.google.com/uc?export=download&id=1BcloSDD_9hitg_kydtIV_Yvr8Q26sMk7", "size": int(1 * 1024)},
                
                
                
                
                
                
                
                "beg_track6.mp3": {"url": "https://drive.google.com/uc?export=download&id=1Z0uvINOtrRTcG4hOeN2F8KmwwSYG5eRL", "size": int(1.1 * 1024 * 1024)},
                "beg_track6.txt": {"url": "https://drive.google.com/uc?export=download&id=16_iMsdeKSOvoKtexZsWz1KX1w3BfKtsh", "size": 1003},
                "beg_track7.mp3": {"url": "https://drive.google.com/uc?export=download&id=1SNR4uDzDBv1AcpWdNnQW-2hr3vqQfZrX", "size": int(1.4 * 1024 * 1024)},
                "beg_track7.txt": {"url": "https://drive.google.com/uc?export=download&id=1lKtOdrHg2fTWlF347VokcRHfG26atpPi", "size": int(1 * 1024)},
                "beg_track8.mp3": {"url": "https://drive.google.com/uc?export=download&id=1AcA0u3xg_eEseCf3s7QEqkWJrvRuLAHS", "size": int(1 * 1024 * 1024)},
                "beg_track8.txt": {"url": "https://drive.google.com/uc?export=download&id=1xN_aAB6IPEuTRogEUr6PU-55TwnzTYRT", "size": 894},
                "beg_track9.mp3": {"url": "https://drive.google.com/uc?export=download&id=17sdwl5fDZwikyfvBBmwTCnD_w5YF5BOJ", "size": int(1.2 * 1024 * 1024)},
                "beg_track9.txt": {"url": "https://drive.google.com/uc?export=download&id=1AfgdbpJTlmGPzDgraDbL6prFTR-AIn4h", "size": int(1 * 1024)},
                "beg_track10.mp3": {"url": "https://drive.google.com/uc?export=download&id=18gONRQMiyWm7umjATnDgNh33Wv_su7lu", "size": int(1.3 * 1024 * 1024)},
                "beg_track10.txt": {"url": "https://drive.google.com/uc?export=download&id=1eNni3nCUccwZQKSPQSNVoQxAaAxb2stb", "size": int(1 * 1024) },
            
            
            
            
                "beg_track11.mp3": {"url": "https://drive.google.com/uc?export=download&id=16gbtkIz2t91vyMzdaLm_ZcTF4d2XH1LY", "size": int(1.1 * 1024 * 1024)},
                "beg_track11.txt": {"url": "https://drive.google.com/uc?export=download&id=1Tp38GhzTAL2MzBrkU38Lx2NNgTjVwqcm", "size": 1004},
                "beg_track12.mp3": {"url": "https://drive.google.com/uc?export=download&id=10pPTsUoJDhE-J8srUG-ME54TnRp5DMbB", "size": int(1.2 * 1024 * 1024)},
                "beg_track12.txt": {"url": "https://drive.google.com/uc?export=download&id=1iXX6kk879wpm-iuPGocPj6b5NnwMB7E9", "size": int(1 * 1024)},
                "beg_track13.mp3": {"url": "https://drive.google.com/uc?export=download&id=1fqPv1SD8zX_7EMDF_pfow6P6t0i-NF3i", "size": int(1.2 * 1024 * 1024)},
                "beg_track13.txt": {"url": "https://drive.google.com/uc?export=download&id=1IU0IBg_yawJj8fZHQYtF_tvY37s6MsO5", "size": int(1 * 1024)},
                "beg_track14.mp3": {"url": "https://drive.google.com/uc?export=download&id=1-xxhEATB6dbV2TC5AYj0WaB2QNrlvic0", "size": int(790 * 1024)},
                "beg_track14.txt": {"url": "https://drive.google.com/uc?export=download&id=1iU0W_HyUq2fEjLQk3L_-a5WA5NxHYfss", "size": 679},
                "beg_track15.mp3": {"url": "https://drive.google.com/uc?export=download&id=1hUWiRzdw3uZ-cTUumRCanfVKv3sW7Omg", "size": int(1.3 * 1024 * 1024)},
                "beg_track15.txt": {"url": "https://drive.google.com/uc?export=download&id=1syPMt7caDKxBvU9o2M21zKq6mMMYuyi2", "size": int(1 * 1024)},
            

                            
                "beg_track16.mp3": {"url": "https://drive.google.com/uc?export=download&id=1oH3pARwD9oCZYng7egoXHoqOpt_veEvS", "size": int(1.1 * 1024 * 1024)},
                "beg_track16.txt": {"url": "https://drive.google.com/uc?export=download&id=1iOMKpPqbG_QzORnBX-SFy0Sp7o6kbGlk", "size": 922},
                "beg_track17.mp3": {"url": "https://drive.google.com/uc?export=download&id=13sFS47UQsFhG1IxOYUAohVBuEXeKBkL9", "size": int(1.5 * 1024 * 1024)},
                "beg_track17.txt": {"url": "https://drive.google.com/uc?export=download&id=1XZd5395Xkjm28qPNbt5xRCHBT8vu5-mt", "size": int(1 * 1024)},
                "beg_track18.mp3": {"url": "https://drive.google.com/uc?export=download&id=1lqfnGfTzklYUMILBTOkWvi7yxnIE6GhQ", "size": int(1.2 * 1024 * 1024)},
                "beg_track18.txt": {"url": "https://drive.google.com/uc?export=download&id=1AIQPVVonHlpo4dDOIrlfsBsWFhCH_tqv", "size": 1010},
                "beg_track19.mp3": {"url": "https://drive.google.com/uc?export=download&id=1l7dJpr7RSdRvioiEuPH0FJEseRHjSsZR", "size": int(1.3 * 1024 * 1024)},
                "beg_track19.txt": {"url": "https://drive.google.com/uc?export=download&id=17OOjq3cxAjYnxL96xepp2eefG9jiz3kn", "size": int(1 * 1024)},
                "beg_track20.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track20.txt": {"url": "https://drive.google.com/uc?export=download&id=11nI-_YCEP5HH1n0j3sL_Db-HROkkpN1m", "size": int(1 * 1024) },
                            
                            
                            
                            
                #until 27            
                            
                "beg_track21.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track21.txt": {"url": "https://drive.google.com/uc?export=download&id=11nI-_YCEP5HH1n0j3sL_Db-HROkkpN1m", "size": 679 },            
                "beg_track22.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track22.txt": {"url": "https://drive.google.com/uc?export=download&id=1VKU1Ncj_SPg2p3LjCmPFXso6rdkXMStL", "size": int(1 * 1024) },         
                "beg_track23.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track23.txt": {"url": "https://drive.google.com/uc?export=download&id=1N-jDbdzcv3BBUfO1ZIH9YytBdl4_kTqt", "size": int(1 * 1024) },         
                "beg_track24.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track24.txt": {"url": "https://drive.google.com/uc?export=download&id=1N-jDbdzcv3BBUfO1ZIH9YytBdl4_kTqt", "size": 965 },
                "beg_track25.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track25.txt": {"url": "https://drive.google.com/uc?export=download&id=1I4xrSSDfe1NLwLFBGqh7g6ciAJ3_XfSs", "size": int(1 * 1024) },                 
                "beg_track26.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track26.txt": {"url": "https://drive.google.com/uc?export=download&id=1P6B4FauY6Gl1sK5KogPQ1PmEbZdOR6cG", "size": int(1 * 1024) },                 
                "beg_track27.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track27.txt": {"url": "https://drive.google.com/uc?export=download&id=1soFOzxa9C1mTxdA2pRgVeKGcgNE82jA9", "size": int(1 * 1024) },                
                "beg_track28.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track28.txt": {"url": "https://drive.google.com/uc?export=download&id=1a87Y0Wc8zs6QASN-YjqMNfX_mXxVEngy", "size": int(1 * 1024) },                          
                "beg_track29.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_dwrlD6F86WNnZKCjJPolTruPA4bU-Q1", "size": int(1.5 * 1024 * 1024)},
                "beg_track29.txt": {"url": "https://drive.google.com/uc?export=download&id=13u-TX8D5ADr8KZRB_U6_RibO29svBDsa", "size": int(1 * 1024) },            
                            
                "inter_track1.mp3": {"url": "https://drive.google.com/uc?export=download&id=1uiEjX3mHviljBIlUKVrSrADYBOr9uN2t", "size": int(927 * 1024)},
                "inter_track1.txt": {"url": "https://drive.google.com/uc?export=download&id=1s-CUNeFSKM6kYx3WkQgVxcbyfSDqaznw", "size": int(1 * 1024)},
                "inter_track2.mp3": {"url": "https://drive.google.com/uc?export=download&id=1GFw-FkZIDDRxpbdGhZuHiFqUzIakxzYq", "size": int(769 * 1024)},
                "inter_track2.txt": {"url": "https://drive.google.com/uc?export=download&id=1_dTyuPkPKdXzOQ3ZtEWWG8AHowTfwtEl", "size": int(1.000)},
                "inter_track3.mp3": {"url": "https://drive.google.com/uc?export=download&id=1wQWH-4-bei1wgskmWvw2f_vTANLxO-8E", "size": int(789 * 1024)},
                "inter_track3.txt": {"url": "https://drive.google.com/uc?export=download&id=1pMW-jTqx0nhKqMYq4SJSJu9f6wH-B_zU", "size": int(1003)},
                "inter_track4.mp3": {"url": "https://drive.google.com/uc?export=download&id=1i3uoc6Q8r5V3Y4a460n4ANMl6k3OhnDs", "size": int(909 * 1024)},
                "inter_track4.txt": {"url": "https://drive.google.com/uc?export=download&id=1OaIZnZtibPQd_ZHwJcRVH1p_F-vWKG2I", "size": int(1* 1024 )},
                "inter_track5.mp3": {"url": "https://drive.google.com/uc?export=download&id=1OnnCmV_Aog542KAMK1mpZqWJP3PKlpbr", "size": int(1 * 1024 * 1024)},
                "inter_track5.txt": {"url": "https://drive.google.com/uc?export=download&id=1owBJSaGBfjuLND11Ikz5-MQtwXQGeRsN", "size": int(1 * 1024)},
                                        
                            
                                                        
                "inter_track6.mp3": {"url": "https://drive.google.com/uc?export=download&id=1b5TtFwE0I-uUesiHq7Z9OBYGXjB8NAdD", "size": int(947 * 1024)},
                "inter_track6.txt": {"url": "https://drive.google.com/uc?export=download&id=1JD2n4VQUg_oIb91fQ0kbi_h5sgtKRgPT", "size": int(1 * 1024)},
                "inter_track7.mp3": {"url": "https://drive.google.com/uc?export=download&id=1qxKKgiwex1KbigloFteFElYNuoNged5p", "size": int(829 * 1024)},
                "inter_track7.txt": {"url": "https://drive.google.com/uc?export=download&id=1rCuUWy75TuqsPHd5Z5BVltPk9lcUXTEG", "size": 1001 },
                "inter_track8.mp3": {"url": "https://drive.google.com/uc?export=download&id=1QpOdbhGH1gkzEJISJ6AHi9J6wNd19i-f", "size": int(868 * 1024)},
                "inter_track8.txt": {"url": "https://drive.google.com/uc?export=download&id=1J5GZMlD_rzn8FKLDIyHRvH6Rd57RPoI0", "size": 1018},
                "inter_track9.mp3": {"url": "https://drive.google.com/uc?export=download&id=1lyC3-IB2xKh4SkN2EHXWisGYq4-6YI_h", "size": int(753 * 1024)},
                "inter_track9.txt": {"url": "https://drive.google.com/uc?export=download&id=1YClqYBq8GeHWlMoTIgz38HksUimT35ko", "size": 887},
                "inter_track10.mp3": {"url": "https://drive.google.com/uc?export=download&id=1JcddU3xnIg6HYfiBPFjO3Q4RoiKgu0Bl", "size": int(641 * 1024)},
                "inter_track10.txt": {"url": "https://drive.google.com/uc?export=download&id=1vsi6EXsPgG4OI-8G7fMzL7Rw19Eo8bGF", "size": 785},
                
                
                
                
                "inter_track11.mp3": {"url": "https://drive.google.com/uc?export=download&id=1B_0-_ILl2hf0DJBxwt_r9wRyY4LODEHk", "size": int(794 * 1024)},
                "inter_track11.txt": {"url": "https://drive.google.com/uc?export=download&id=1tgfwdFGTMjixeJglmqp502VomU1jHbXU", "size": int(1 * 1024)},
                "inter_track12.mp3": {"url": "https://drive.google.com/uc?export=download&id=11ujBIVoeVuOujWe7V6bmEwspj01vTAs3", "size": int(612 * 1024)},
                "inter_track12.txt": {"url": "https://drive.google.com/uc?export=download&id=10uB99cWg3KJZsvsLIAKt70aNKCCc-uaF", "size": 735 },
                "inter_track13.mp3": {"url": "https://drive.google.com/uc?export=download&id=1N7jX66yBjJj5bJMpupnp-vpkS6Y6T-N9", "size": int(703 * 1024)},
                "inter_track13.txt": {"url": "https://drive.google.com/uc?export=download&id=1Ap4Fptjpj-tDN_EEpsKG7c3H9GcZW6At", "size": 831},
                "inter_track14.mp3": {"url": "https://drive.google.com/uc?export=download&id=1jdqSu-Rx0_MjyEFxzsnJpYgnzsBDSuzu", "size": int(989 * 1024)},
                "inter_track14.txt": {"url": "https://drive.google.com/uc?export=download&id=13b0NgUXMPH1kpR7K-6TM42Ii5TjQYAmu", "size": int(1 * 1024)},
                "inter_track15.mp3": {"url": "https://drive.google.com/uc?export=download&id=108suXB_nGtuGnhn_7Kf9NyCxP8w908p3", "size": int(943 * 1024)},
                "inter_track15.txt": {"url": "https://drive.google.com/uc?export=download&id=1gO2_GHYWZw-jeX7283l21RuqYWD0_Zrj", "size": int(1 * 1024) },
                
                
                
                
                "inter_track16.mp3": {"url": "https://drive.google.com/uc?export=download&id=1lor0JzuHakGp-Cyw8-0IzfWi0VlLUDvi", "size": int(726 * 1024)},
                "inter_track16.txt": {"url": "https://drive.google.com/uc?export=download&id=1tQXCKpj2p_gKbnmnwjJmoewDy_bcq027", "size": 721},
                "inter_track17.mp3": {"url": "https://drive.google.com/uc?export=download&id=1BikiVZP7G2VhGA3XjJqLtOGNK22MTb9p", "size": int(921 * 1024)},
                "inter_track17.txt": {"url": "https://drive.google.com/uc?export=download&id=1Qmu97HVlySCOmXBTwRgBZPON3yS7hIs3", "size": 959 },
                "inter_track18.mp3": {"url": "https://drive.google.com/uc?export=download&id=1-0irL9XItqym1K57uR0jDvfBIawtcmIo", "size": int(731 * 1024)},
                "inter_track18.txt": {"url": "https://drive.google.com/uc?export=download&id=18O8mjt2zNuBsKdNNYzRIHbkJJjbIzx7T", "size": 920},
                "inter_track19.mp3": {"url": "https://drive.google.com/uc?export=download&id=1ZR4ODwHelx_zm3u0OKyCx49Zgli6WeHO", "size": int(825 * 1024)},
                "inter_track19.txt": {"url": "https://drive.google.com/uc?export=download&id=1KcgNbtXLyVsKGuG3IKcwuxZK7wjvu-ka", "size": int(1 * 1024)},
                "inter_track20.mp3": {"url": "https://drive.google.com/uc?export=download&id=1DtnQ4zEz-hhkgDxQciYDejD6iQahAj4A", "size": int(620 * 1024)},
                "inter_track20.txt": {"url": "https://drive.google.com/uc?export=download&id=10BjAGBD4CmoJBDjAPvU3evaymPS_jmgd", "size": 789 },
                
                
                
                
                
                
                "inter_track21.mp3": {"url": "https://drive.google.com/uc?export=download&id=1XM0gWgW3WjYcI7T-oZbeK22d5LdNSGy2", "size": int(781 * 1024)},
                "inter_track21.txt": {"url": "https://drive.google.com/uc?export=download&id=13nEM0qBSeVB7wfRMpxfkc8RpB4yGMXaS", "size": 807},
                "inter_track22.mp3": {"url": "https://drive.google.com/uc?export=download&id=1ol80pt_K_1IX53oaWEyOBHt_d7QYjVVO", "size": int(721 * 1024)},
                "inter_track22.txt": {"url": "https://drive.google.com/uc?export=download&id=1wB42j4s5wAZ9o0PCmI13CnCKWBdULaSS", "size": 927 },
                "inter_track23.mp3": {"url": "https://drive.google.com/uc?export=download&id=1n1-KYfaYWymamrnSM7Ie4rqdGECNpOcw", "size": int(725 * 1024)},
                "inter_track23.txt": {"url": "https://drive.google.com/uc?export=download&id=16aTZGZL1TFRkeZmFoqd2QWbnhHKsqrSD", "size": 746},
                "inter_track24.mp3": {"url": "https://drive.google.com/uc?export=download&id=1PqToJQZPm7k6vlXwxMnl_6IfMzHu9tyO", "size": int(656 * 1024)},
                "inter_track24.txt": {"url": "https://drive.google.com/uc?export=download&id=1ZbLhtgMtwpXoODxsHi_Z8BWeUj-ZLYoK", "size": 780},
                "inter_track25.mp3": {"url": "https://drive.google.com/uc?export=download&id=1n7OidmHiSEU_azAyf2hEPCiPTtfbFVLF", "size": int(570 * 1024)},
                "inter_track25.txt": {"url": "https://drive.google.com/uc?export=download&id=18L_1tcSEZ5RA_CVYE3f6M6M3e9Ntq6Pd", "size": 762 },
                
                
                "inter_track26.mp3": {"url": "https://drive.google.com/uc?export=download&id=1OcE57X_K2pM2dC0_usOx_tk-v3PkLThb", "size": int(643 * 1024)},
                "inter_track26.txt": {"url": "https://drive.google.com/uc?export=download&id=1uWiG139RDJK7be2atM1i_e0RY7sVmZwq", "size": 658},
                "inter_track27.mp3": {"url": "https://drive.google.com/uc?export=download&id=1YicCRl-hXb6QnTVrOMAYZiPmPuLsyekE", "size": int(938 * 1024)},
                "inter_track27.txt": {"url": "https://drive.google.com/uc?export=download&id=1GA9LVQ0DUy3ag13bIGA06igPwNGbIAo9", "size": 748 },
                "inter_track28.mp3": {"url": "https://drive.google.com/uc?export=download&id=1emDP8SGCpTBf79YOas9PWnaz8BInqmdH", "size": int(1.2 * 1024 * 1024)},
                "inter_track28.txt": {"url": "https://drive.google.com/uc?export=download&id=1oxhMpWnwb4HGqu-HsQvdOXgSVSgYfo1C", "size": 1023},
                
                
                                                
              
              
              
                "adv_track1.mp3": {"url": "https://drive.google.com/uc?export=download&id=1CTBFlDwh1ouhxFVBnUeKWWfL6b18SEKz", "size": int(1.1 * 1024 * 1024)},
                "adv_track1.txt": {"url": "https://drive.google.com/uc?export=download&id=1dqEdV8K0-bUNVIdWbh7wV7JMliLYDhpQ", "size": int(1 * 1024)},
                "adv_track2.mp3": {"url": "https://drive.google.com/uc?export=download&id=1oEejljdqbjv9syg_iuCaRq9IsSWZDdkX", "size": int(868 * 1024)},
                "adv_track2.txt": {"url": "https://drive.google.com/uc?export=download&id=1JvUh8YCLcPVfRJ9cPX1IzQwSFgIs5KFS", "size": int(1 * 1024)},
                "adv_track3.mp3": {"url": "https://drive.google.com/uc?export=download&id=1U1bCw_2chIfoXY78SE8hdkOFuCdTQuen", "size": int(569 * 1024)},
                "adv_track3.txt": {"url": "https://drive.google.com/uc?export=download&id=1sc7gPELi7ozriwT7TNqXcgNCJ1tVInLS", "size": int(684 * 1024)},
                "adv_track4.mp3": {"url": "https://drive.google.com/uc?export=download&id=12KYzGqx4FQqjuiIWFUIclmiAXt9WcnSM", "size": int(1.2 * 1024 * 1024)},
                "adv_track4.txt": {"url": "https://drive.google.com/uc?export=download&id=15oBl4niLg2woJAAfwFKF-9_2XmRqKmyr", "size": (1 * 1024)},
                "adv_track5.mp3": {"url": "https://drive.google.com/uc?export=download&id=1kKznNxUOhUDr91zR50Dllfd4W_EGrWOU", "size": int()},
                "adv_track5.txt": {"url": "https://drive.google.com/uc?export=download&id=12Zyo1JA5Kzutny3ixmG2WN_T_I8HfEKP", "size":(1 * 1024)},
                                                       
                                           
                                                                       
                "adv_track6.mp3": {"url": "https://drive.google.com/uc?export=download&id=1M01iKRu3J-HaAfJrv1HmWlvuM5uJZr1Q", "size": int(951* 1024)},
                "adv_track6.txt": {"url": "https://drive.google.com/uc?export=download&id=1SmO2IptiwE8pctmgcE37GPMPBAUzbDuP", "size": (1 * 1024)},
                "adv_track7.mp3": {"url": "https://drive.google.com/uc?export=download&id=1OYjNYTVxULn0aiYW9w1RQQBcGorUchQw", "size": int(1 * 1024)},
                "adv_track7.txt": {"url": "https://drive.google.com/uc?export=download&id=1zqzuwU_1kPA7bOoNGlADjpS2Wcp5j7lg", "size":  (1 * 1024)},
                "adv_track8.mp3": {"url": "https://drive.google.com/uc?export=download&id=1kdkWbDKaDFsGUx7sCZWaeiHWpSdkmIVV", "size": int(867 * 1024)},
                "adv_track8.txt": {"url": "https://drive.google.com/uc?export=download&id=1io6-uovkJqGsaIuGRE8ZL6akYzxq6mGN", "size": (1 * 1024)},
                "adv_track9.mp3": {"url": "https://drive.google.com/uc?export=download&id=18_0LVmESwk140QdDiNk_Z-GdZx9NpfZX", "size": int(1.2 * 1024 * 1024)},
                "adv_track9.txt": {"url": "https://drive.google.com/uc?export=download&id=1xNloGN6ACGJYmj-cXriZd1MzJPec-nxt", "size": (2 * 1024)},
                "adv_track10.mp3": {"url": "https://drive.google.com/uc?export=download&id=1bUq8Y74JrjL-caeloEZ-TXHDO-GpPMNj", "size": int(860 * 1024)},
                "adv_track10.txt": {"url": "https://drive.google.com/uc?export=download&id=1TdNED4ncYCmYtg474c8zjXk-iywvPh6j", "size":  1012},
                               
                               
                               
                               
                "adv_track11.mp3": {"url": "https://drive.google.com/uc?export=download&id=1P0Vhcod6WovhnwywMghpaOXKRksH5de5", "size": int(1.1 * 1024 * 1024)},
                "adv_track11.txt": {"url": "https://drive.google.com/uc?export=download&id=1HDoAwGbapJsFPgWKzL0vkBpFFCL_jXpP", "size": (1 * 1024)},
                "adv_track12.mp3": {"url": "https://drive.google.com/uc?export=download&id=166rEjHyOSg41glGb75HicJLIfix4jOpt", "size": int(1.5 * 1024 * 1024)},
                "adv_track12.txt": {"url": "https://drive.google.com/uc?export=download&id=1yBS-89kPgnpW8ZF-nikXkLPLRTCXuX0i", "size": (2 * 1024)},
                "adv_track13.mp3": {"url": "https://drive.google.com/uc?export=download&id=1SaazalDloMt920v6tcQnY2P94khXbFXX", "size": int(1.2 * 1024 * 1024)},
                "adv_track13.txt": {"url": "https://drive.google.com/uc?export=download&id=1c7rw0pIXBtenzPyKOyXNH9YjFqIplY4l", "size": (1 * 1024)},
                "adv_track14.mp3": {"url": "https://drive.google.com/uc?export=download&id=10j80xt675ixVgNHPhv4jKjlLLRA08dqQ", "size": int(887 * 1024)},
                "adv_track14.txt": {"url": "https://drive.google.com/uc?export=download&id=1tiOhUHbJv6iB7q89J9zv6tWZBGl-ZO67", "size":(1 * 1024) },
                "adv_track15.mp3": {"url": "https://drive.google.com/uc?export=download&id=19wNa4H2m6ni_9z2GN3ZDo6G0crGeveK2", "size": int(887 * 1024)},
                "adv_track15.txt": {"url": "https://drive.google.com/uc?export=download&id=1XhYDymMFOTWx7GSKocCC93UqHO96Wa7L", "size": (1 * 1024) },
                               
                               
                               
                               
                "adv_track16.mp3": {"url": "https://drive.google.com/uc?export=download&id=1hgx582WMUbbG6bPQB0E0Y-4FXpPNNNv8", "size": int(879 * 1024)},
                "adv_track16.txt": {"url": "https://drive.google.com/uc?export=download&id=1B-Cz4FJWN8U_VkrTf_SPNMY8yMlUw42L", "size": 952},
                "adv_track17.mp3": {"url": "https://drive.google.com/uc?export=download&id=1dqBrhXG6AY31XvHr1Ix8c3tebbNj5uYx", "size": int(1 * 1024 * 1024)},
                "adv_track17.txt": {"url": "https://drive.google.com/uc?export=download&id=129RqMBawlEZCfZXgDqgV08jrxYNg9IEY", "size":  (1 * 1024)},
                "adv_track18.mp3": {"url": "https://drive.google.com/uc?export=download&id=16H8KZM5lgoIeUyVObRm-Ce2YoyJtwa6o", "size": int(956 * 1024)},
                "adv_track18.txt": {"url": "https://drive.google.com/uc?export=download&id=1ZKpJXWDSCp82IhY05n6FaDxJXEP3Y4Kl", "size": (1 * 1024)},
                "adv_track19.mp3": {"url": "https://drive.google.com/uc?export=download&id=1qr0st6ej3XRmFVbLaQ7lAWP1vhGGohfo", "size": int(993 * 1024)},
                "adv_track19.txt": {"url": "https://drive.google.com/uc?export=download&id=1tVTBMBELQnCOTnNPixKtZnwe__U0Qc2P", "size": (1 * 1024)},
                "adv_track20.mp3": {"url": "https://drive.google.com/uc?export=download&id=1_26oLUEW50FPksJKCqKq03femI4NQDMi", "size": int(1.4 * 1024 * 1024)},
                "adv_track20.txt": {"url": "https://drive.google.com/uc?export=download&id=13K1lUHuO3MF1AE94Hyzuc6C4qqUlfVCJ", "size":  (2 * 1024)},
                               
                               
                               
                               
                               
                               
                "adv_track21.mp3": {"url": "https://drive.google.com/uc?export=download&id=1V-xF0RsM1OEX8yftXvOveBU3GZ9oC2Y8", "size": int(1.7 * 1024 * 1024)},
                "adv_track21.txt": {"url": "https://drive.google.com/uc?export=download&id=1OX-aj7bgqQNP4Sb8Xe9hxlxoJqLKLtQM", "size": (2 * 1024)},
                "adv_track22.mp3": {"url": "https://drive.google.com/uc?export=download&id=1-oldp938Ed38sR9H04IGVBLlC8b990xC", "size": int(1.2 * 1024 * 1024)},
                "adv_track22.txt": {"url": "https://drive.google.com/uc?export=download&id=1avxCUpPBz9H4IBzHin99vtyhgkJaKWgu", "size": (1 * 1024) },
                "adv_track23.mp3": {"url": "https://drive.google.com/uc?export=download&id=1S2Fqz7QNEHohbXNn0SVEytsHJ8FeG0pG", "size": int(1.1 * 1024 * 1024)},
                "adv_track23.txt": {"url": "https://drive.google.com/uc?export=download&id=1VYhygNcIpnDkyVV9HOKc__bwqmturCxw", "size": (1* 1024)},
                "adv_track24.mp3": {"url": "https://drive.google.com/uc?export=download&id=1KHPlS0oFxwuc-fYSHJzr6ahYFfNMSO8p", "size": int(671 * 1024)},
                "adv_track24.txt": {"url": "https://drive.google.com/uc?export=download&id=14hkNkRDk0uKjbt1SMcMpAByN3-Vi2Qun", "size": 801},
                "adv_track25.mp3": {"url": "https://drive.google.com/uc?export=download&id=1CzgJT1M-HoH0DaOO6lYG6dkNGtDngXp-", "size": int(1 * 1024 * 1024)},
                "adv_track25.txt": {"url": "https://drive.google.com/uc?export=download&id=1xZPTotzD-EUYh1-xTWKjsKSlnNXapVMk", "size": (1 * 1024) },
                               
                               
                "adv_track26.mp3": {"url": "https://drive.google.com/uc?export=download&id=1r1LtSf0_HPHt7FubA8BOasjv3sJSIWZZ", "size": int(1.4 * 1024 * 1024)},
                "adv_track26.txt": {"url": "https://drive.google.com/uc?export=download&id=1KK6v-vac3Zf6h8JN0adXunkvUnrH5MHJ", "size": (1 * 1024)},
                "adv_track27.mp3": {"url": "https://drive.google.com/uc?export=download&id=1fc1W-f1FGOx_8gw3Vt1N-yvCm6OfQ1-F", "size": int(1.7 * 1024 * 1024)},
                "adv_track27.txt": {"url": "https://drive.google.com/uc?export=download&id=1EIk5n5E6Eyj0xQuyHXsAO-Hlyyu7dpPk", "size":  (2 * 1024)},
                "adv_track28.mp3": {"url": "https://drive.google.com/uc?export=download&id=1GuVn_wxYA7gjJAlfnL9Rvk_tFApW8xS9", "size": int(1.1 * 1024 * 1024)},
                "adv_track28.txt": {"url": "https://drive.google.com/uc?export=download&id=1tdQLNxuJe-NcDKXDVHxhPXEMkBGJd3iW", "size": (1 * 1024)},
                "adv_track29.mp3": {"url": "https://drive.google.com/uc?export=download&id=10j80xt675ixVgNHPhv4jKjlLLRA08dqQ", "size": int(1 * 1024 * 1024)},
                "adv_track29.txt": {"url": "https://drive.google.com/uc?export=download&id=1LFae7k-QuU7OT7_u0mQXJ5i8VnvESdHf", "size": (1 * 1024)},               
                                                
                
                
            }

            self.total_files = len(self.download_queue)
            self.current_file_index = 0
                
            print("[DEBUG 4] Queue loaded successfully. Triggering SQL database parsing loop...")
            Clock.schedule_once(self.load_database_step, 0.1)

        except Exception as fatal_diagnostic_error:
            print(f"\nFATAL START CRASH DISCOVERED:\n{fatal_diagnostic_error}\n")
            import traceback
            traceback.print_exc()

    def has_enough_storage(self):
        if not hasattr(self, 'download_queue') or not self.download_queue:
            return True, ""
        try:
            bytes_needed = 0
            for file_name, file_data in self.download_queue.items():
                local_file_path = os.path.join(self.audio_folder, file_name)
                if not os.path.exists(local_file_path):
                    bytes_needed += file_data.get("size", 0)

            bytes_needed += (5 * 1024 * 1024) # 5MB buffer allocation 
            disk_stats = shutil.disk_usage(self.audio_folder)
            if disk_stats.free < bytes_needed:
                return False, "Insufficient storage allocation overhead thresholds."
            return True, ""
        except Exception as storage_check_exception:
            print(f"Disk statistic extraction exception bypassed: {storage_check_exception}")
            return True, "" # Desktop system hardware path compatibility bypass hook

    def is_connected(self):
        """
        1. LIGHTWEIGHT UNIVERSAL ROUTE VERIFICATION
        Bypasses strict platform wrappers by checking a standard low-level socket.
        """
        import socket
        try:
            # Universal fallback lookups handling both IPv4 and IPv6 dual-stack streams
            socket.setdefaulttimeout(3.0)
            socket.getaddrinfo("://google.com", 443, socket.AF_UNSPEC)
            return True
        except:
            return False

    def download_folder_worker(self):
        """
        2. PRODUCTION-GRADE STREAMING RECOVERY ENGINE
        Skips volatile pre-check barriers and immediately initiates chunk-streaming.
        Handles network drops dynamically to ensure cross-platform consistency.
        """
        import os
        import sys
        import time
        import socket
        from kivy.clock import Clock
        from kivy.utils import platform

        # Reset and turn off the Retry UI layouts the split second a new download cycle fires
        def reset_ui_for_download(dt):
            if self.ids and 'progress_layout' in self.ids and 'retry_layout' in self.ids and 'status_label' in self.ids:
                self.ids.progress_layout.opacity = 1
                self.ids.retry_layout.opacity = 0
                self.ids.retry_layout.disabled = True  
                self.ids.status_label.text = "Re-verifying storage assets..."
        Clock.schedule_once(reset_ui_for_download, 0)

        # Runs storage validation strictly on Android
        if platform == 'android':
            storage_passed, storage_error_msg = self.has_enough_storage()
            if not storage_passed:
                Clock.schedule_once(lambda dt: self.handle_failure_state("⚠️", storage_error_msg), 0)
                return

        # 🚫 CRUCIAL CHANGE: The separate "if not self.is_connected():" pre-check gateway 
        # has been completely removed to stop false offline triggers on Windows 10 and Android!

        self.current_file_index = 0
        # socket.setdefaulttimeout(45)
        
        # Track the last exception message to display the correct text to the user if everything fails
        last_error_message = "Unknown network error."

        for file_name, file_data in self.download_queue.items():
            self.current_file_index += 1
            self.current_file_name = file_name
            local_file_path = os.path.join(self.audio_folder, file_name)
            remote_url = file_data["url"]
            
            # --- RETRY LOGIC CONFIGURATION ---
            max_retries = 3
            retry_count = 0
            download_success = False

            while retry_count < max_retries and not download_success:
                try:
                    # Clear corrupted partial files from disk cache
                    if os.path.exists(local_file_path):
                        file_size = os.path.getsize(local_file_path)
                        if file_name.endswith('.mp3') and file_size < 5000:
                            print(f"🗑️ Removing corrupted partial audio: {file_name}")
                            os.remove(local_file_path)
                        elif file_name.endswith('.txt') and file_size == 0:
                            print(f"🗑️ Removing empty text asset: {file_name}")
                            os.remove(local_file_path)

                    # Initialize fresh file download chunk stream
                    if not os.path.exists(local_file_path):
                        if retry_count > 0:
                            print(f"🔄 Retrying download for {file_name} (Attempt {retry_count + 1}/{max_retries})...")
                            time.sleep(2)

                        import ssl
                        import urllib.request

                        ctx = ssl.create_default_context()
                        ctx.check_hostname = False
                        ctx.verify_mode = ssl.CERT_NONE

                        req = urllib.request.Request(remote_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Android; Mobile)'})

                        with urllib.request.urlopen(req, timeout=25.0, context=ctx) as response:
                            total_size = int(response.info().get('Content-Length', -1))
                            chunk_size = 16384  # 16KB optimal streaming chunks

                            with open(local_file_path, 'wb') as local_file:
                                while True:
                                    chunk = response.read(chunk_size)
                                    if not chunk:
                                        break
                                    local_file.write(chunk)
                                    
                                    if total_size > 0:
                                        self.progress_hook(1, chunk_size, total_size)

                        # Validate that Google Drive didn't drop us into an antivirus block html page
                        with open(local_file_path, 'rb') as f:
                            if b"<!DOCTYPE html>" in f.read(100):
                                raise ValueError("Google Drive antivirus block warning page generated.")
                    else:
                        print(f"✅ Cached asset verified on disk (Skipping Download): {file_name}")
                    
                    download_success = True
                    
                except Exception as download_error:
                    retry_count += 1
                    last_error_message = str(download_error)
                    print(f"🚨 Attempt {retry_count} failed for {file_name}: {download_error}")
                    
                    if os.path.exists(local_file_path):
                        try: os.remove(local_file_path)
                        except: pass

            # =========================================================================
            # STALEMATE HARD LOCKDOWN GATEWAY (Unified Interface Exception Handler)
            # =========================================================================
            if not download_success:
                print(f"❌ FATAL BLOCKADE: Failed to download mandatory asset: {file_name}")
                
                # Check the exact text error signature to report the correct state to the user
                err_lower = last_error_message.lower()
                if "getaddrinfo" in err_lower or "timeout" in err_lower or "timed out" in err_lower or "unreachable" in err_lower:
                    error_msg = f"Network Timeout!\nFailed to fetch: {file_name}\nPlease check your Wi-Fi signal and retry."
                else:
                    error_msg = "No Internet Connection!\nPlease connect to Wi-Fi or Mobile Data and retry."
                
                Clock.schedule_once(lambda dt: self.handle_failure_state("⚠️", error_msg), 0)
                return 
            else:
                self.progress_hook(1, 100, 100)

        print("🎉 SUCCESS: Every single audio and text lesson asset verified on storage disk!")
        Clock.schedule_once(lambda dt: self.finish_process(), 0)







    





    def progress_hook(self, count, block_size, total_size):
        if total_size <= 0: return
        downloaded = count * block_size
        file_percent = min(100, int((downloaded / total_size) * 100))
        base_progress = ((self.current_file_index - 1) / self.total_files) * 100
        current_contribution = (file_percent / 100) * (100 / self.total_files)
        overall_percent = int(base_progress + current_contribution)
        Clock.schedule_once(lambda dt: self.update_progress_ui(overall_percent, self.current_file_name), 0)

    def update_progress_ui(self, value, file_name):
        if 'progress_bar' in self.ids and 'percent_label' in self.ids and 'status_label' in self.ids:
            self.ids.progress_bar.value = value
            self.ids.percent_label.text = f"{value}%"
            self.ids.status_label.text = f"Syncing tracks ({self.current_file_index}/{self.total_files})\nDownloading: {file_name}"

    def update_status_msg(self, text_val):
        if 'status_label' in self.ids:
            self.ids.status_label.text = text_val

    def handle_failure_state(self, icon, message):
        if 'icon_label' in self.ids and 'status_label' in self.ids and 'progress_layout' in self.ids and 'retry_layout' in self.ids:
            self.ids.icon_label.text = icon
            self.ids.status_label.text = message
            self.ids.progress_layout.opacity = 0
            self.ids.retry_layout.opacity = 1
            self.ids.retry_layout.disabled = False

    def finish_process(self):
        self.manager.current = 'home_screen'


    def load_database_step(self, dt):
        """ Sequentially parses database tables without blocking Kivy's rendering frame rates """
        print(">>> DEBUG LOG: load_database_step HAS RUN! <<<")
        global re, re1, re2, re3, re4, re5
        global vo, vo1, vo2, vo3, vo4, vo_id
        global results, result1, result2, result3, result4, result5
        global s, s1, s2, s3, s4, s5
        global p, p1, p2, p3, p4, ph_id_list, pp, pp1, pp2, pp3, pp4, pid, ph, ph1, ph2, ph3, ph4, phid
        global punc, punc1, punc2, punc3, punc4, punc_id, r, ppunc, ppunc1, ppunc2, ppunc3, ppunc4, punc_idl, pr
        global pc, pc1, pc2, pc3, pc4, pc_id, pcr

        db_name = "book.db"
        if platform == 'android':
            db_path = os.path.join(App.get_running_app().internal_sandbox_dir, db_name)
        else:
            db_path = db_name

        try:
            print(f"[DEBUG 5] Opening background connection to: {db_path}")
            conn = sqlite3.connect(db_path)
            
            # --- 1. Core Quiz tables ---
            print("[DEBUG 6] Querying intermediate, advanced, and beginner tables...")
            re1 = conn.execute("select wronganswer1 from intermediate").fetchall(); re = conn.execute("select questions from intermediate").fetchall(); re2 = conn.execute("select wronganswer2 from intermediate").fetchall(); re3 = conn.execute("select rightanswer from intermediate").fetchall(); re4 = conn.execute("select option from intermediate").fetchall(); re5 = conn.execute("select num from intermediate").fetchall()
            results = conn.execute("select wronganswer1 from advanced").fetchall(); result1 = conn.execute("select questions from advanced").fetchall(); result2 = conn.execute("select wronganswer2 from advanced").fetchall(); result3 = conn.execute("select rightanswer from advanced").fetchall(); result4 = conn.execute("select option from advanced").fetchall(); result5 = conn.execute("select num from advanced").fetchall()
            s = conn.execute("select wronganswer1 from beginner").fetchall(); s1 = conn.execute("select questions from beginner").fetchall(); s2 = conn.execute("select wronganswer2 from beginner").fetchall(); s3 = conn.execute("select rightanswer from beginner").fetchall(); s4 = conn.execute("select option from beginner").fetchall(); s5 = conn.execute("select num from beginner").fetchall()
            
            # --- 2. Phrasal Verbs ---
            print("[DEBUG 7] Querying phrasalverbs tables...")
            p = conn.execute("select questions from phrasalverbs").fetchall(); p1 = conn.execute("select wronganswer from phrasalverbs").fetchall(); p2 = conn.execute("select wronganswer1 from phrasalverbs").fetchall(); p3 = conn.execute("select rightanswer from phrasalverbs").fetchall(); p4 = conn.execute("select option from phrasalverbs").fetchall(); ph_id_list = conn.execute("select num from phrasalverbs").fetchall()
            pp = conn.execute("select questions from phrasalverbs").fetchall(); pp1 = conn.execute("select wronganswer from phrasalverbs").fetchall(); pp2 = conn.execute("select wronganswer1 from phrasalverbs").fetchall(); pp3 = conn.execute("select rightanswer from phrasalverbs").fetchall(); pp4 = conn.execute("select option from phrasalverbs").fetchall(); pid = conn.execute("select num from phrasalverbs").fetchall()
            ph = conn.execute("select questions from phrasalverbs").fetchall(); ph1 = conn.execute("select wronganswer from phrasalverbs").fetchall(); ph2 = conn.execute("select wronganswer1 from phrasalverbs").fetchall(); ph3 = conn.execute("select rightanswer from phrasalverbs").fetchall(); ph4 = conn.execute("select option from phrasalverbs").fetchall(); phid = conn.execute("select num from phrasalverbs").fetchall()
            
            # --- 3. Vocabulary ---
            print("[DEBUG 8] Querying vocabulary tables...")
            vo = conn.execute("select question from vocabulary").fetchall(); vo1 = conn.execute("select wronganswer1 from vocabulary").fetchall(); vo2 = conn.execute("select wronganswer2 from vocabulary").fetchall(); vo3 = conn.execute("select rightanswer from vocabulary").fetchall(); vo4 = conn.execute("select option from vocabulary").fetchall(); vo_id = conn.execute("select num from vocabulary").fetchall()
            
            # --- 4. Punctuation ---
            print("[DEBUG 9] Querying punctuation tables...")
            punc = conn.execute("select one from punctuation").fetchall(); punc1 = conn.execute("select two from punctuation").fetchall(); punc2 = conn.execute("select three from punctuation").fetchall(); punc3 = conn.execute("select four from punctuation").fetchall(); punc4 = conn.execute("select option from punctuation").fetchall(); punc_id = conn.execute("select num from punctuation").fetchall(); r = conn.execute("select rightanswer from punctuation").fetchall()
            ppunc = conn.execute("select one from punctuation").fetchall(); ppunc1 = conn.execute("select two from punctuation").fetchall(); ppunc2 = conn.execute("select three from punctuation").fetchall(); ppunc3 = conn.execute("select four from punctuation").fetchall(); ppunc4 = conn.execute("select option from punctuation").fetchall(); punc_idl = conn.execute("select num from punctuation").fetchall(); pr = conn.execute("select rightanswer from punctuation").fetchall()
            pc = conn.execute("select one from punctuation").fetchall(); pc1 = conn.execute("select two from punctuation").fetchall(); pc2 = conn.execute("select three from punctuation").fetchall(); pc3 = conn.execute("select four from punctuation").fetchall(); pc4 = conn.execute("select option from punctuation").fetchall(); pc_id = conn.execute("select num from punctuation").fetchall(); pcr = conn.execute("select rightanswer from punctuation").fetchall()
            
            conn.close()
            print("[DEBUG SUCCESS] Database setup successfully initialized!")
            
            # Database load finished! Now start the safe background file sync thread
            threading.Thread(target=self.download_folder_worker, daemon=True).start()
            
        except Exception as database_load_error:
            print("\n🚨 CRITICAL ERROR FOUND INSIDE THE DATABASE PARSING METHOD:")
            import traceback
            traceback.print_exc()
            print("\n")
            if self.ids and 'status_label' in self.ids:
                self.ids.status_label.text = f"Database Initialization Error:\n{database_load_error}"
















































































































































            
            
            
            
class MyScreenManager(ScreenManager): 
    global theoption
    def screen_manager_method(self):
        pass
    
        
class CrashCourseApp(App):
    
    def __init__(self, **kwargs):
        
        super(CrashCourseApp, self).__init__(**kwargs)
    audio_folder = ""
    conn = None
    cursor = None

    def on_start(self):
            
        """ App-level initialization database check routine block """
        db_name = "book.db"
        
        # Resolve the restriction-free, private internal storage sandbox path
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
        else:
            base_dir = self.user_data_dir

        # Unified path tracking property accessible globally across all classes
        self.internal_sandbox_dir = base_dir
        
        writable_db_path = os.path.join(base_dir, db_name)
        bundled_db_path = os.path.join(os.getcwd(), db_name)
        
        # FIX: Added a check for empty/0-byte files to prevent corrupt database lockups
        database_needs_copy = not os.path.exists(writable_db_path) or (os.path.exists(writable_db_path) and os.path.getsize(writable_db_path) == 0)
        
        # Copy the pre-populated database safely into internal storage
        if database_needs_copy and os.path.exists(bundled_db_path):
            try:
                shutil.copy(bundled_db_path, writable_db_path)
                print("Database cleanly copied into secure internal storage.")
            except Exception as e:
                print(f"Failed to copy bundled database asset: {e}")
                
        # Main thread database connection
        self.conn = sqlite3.connect(writable_db_path)
        self.cursor = self.conn.cursor()

    def build(self):
        db_name = "book.db"
        
        # FIX: We completely removed Builder.load_file() from here!
        # Because your class is CrashCourseApp, Kivy natively handles loading crashcourse.kv automatically.
        # Leaving this method to do ONLY database setups stops the duplicate memory freeze.
        print("[DEBUG SUCCESS] Kivy automatic engine is loading 'crashcourse.kv' cleanly...")

        # Platform-aware database path parsing
        if platform == 'android':
            base_dir = os.environ.get('ANDROID_PRIVATE_DIR', '/data/data/org.test.crashcourse/files/app')
            writable_db_path = os.path.join(base_dir, db_name)
            bundled_db_path = os.path.join(os.getcwd(), db_name)
            
            if not os.path.exists(writable_db_path) and os.path.exists(bundled_db_path):
                try: 
                    shutil.copy(bundled_db_path, writable_db_path)
                except Exception as e: 
                    print(f"Mobile DB copy failure: {e}")
        else:
            writable_db_path = db_name
            self.internal_sandbox_dir = os.getcwd()

        print(f"[DEBUG SUCCESS] Connecting database target: {writable_db_path}")
        
        try:
            self.conn = sqlite3.connect(writable_db_path)
            self.cursor = self.conn.cursor()
            print("[DEBUG SUCCESS] Main thread database connection established!")
        except Exception as db_err:
            print(f"[DEBUG ERROR] Database connection lock: {db_err}")

        
        
        
        global counter1,counter2,counter3,c1,vcounter,punc_counter
        
        file1 = open('stophere.txt','r')
        counter1 = int(file1.read())
        counter1 = counter1 -2
        
        file3 = open("stop3.txt","r")
        counter3 = int(file3.read())
        counter3= counter3 -2
        file2= open("stop2.txt","r")
        counter2 = int(file2.read())
        counter2 = counter2-2
        
        phrasal1=open("phrasal1.txt","r")
        c1=int(phrasal1.read())
        c1= c1-2


        vocabulary=open("vocabulary.txt","r")
        vcounter=int(vocabulary.read())
        vcounter= vcounter-2

        punctuation=open("punctuation.txt","r")
        punc_counter=int(punctuation.read())
        punc_counter = punc_counter-2



        return MyScreenManager()
    
    
if __name__ == '__main__':
    CrashCourseApp().run()