import os
import shutil

def Cleaner(dir):
    if not os.path.isdir(dir+'\ScreenshotCleaner_LevelUp'):
        os.makedirs(dir+'\ScreenshotCleaner_LevelUp')
    if not os.path.isdir(dir+'\ScreenshotCleaner_ects'):
        os.makedirs(dir+'\ScreenshotCleaner_ects')
    
    for fn in os.listdir(dir):
        if fn.startswith('Maple_A_') and fn.endswith('.png'):
            pass
        elif fn.startswith('Maple_') and fn.endswith('.png'):
            shutil.move(dir+'\\'+fn, dir+'\ScreenshotCleaner_ects'+'\\'+fn)
