import os
import shutil
from isLevelup import isLevelup

def Cleaner(dir):
    if not os.path.isdir(dir+'\ScreenshotCleaner'):
        os.makedirs(dir+'\ScreenshotCleaner')

    for fn in os.listdir(dir):
        if fn.endswith('.png') or fn.endswith('.jpg'):
            shutil.move(dir+'\\'+fn, dir+'\ScreenshotCleaner'+'\\'+fn)

def LevelupCleaner(dir):
    if not os.path.isdir(dir+'\ScreenshotCleaner_LevelUp'):
        os.makedirs(dir+'\ScreenshotCleaner_LevelUp')
    if not os.path.isdir(dir+'\ScreenshotCleaner_ects'):
        os.makedirs(dir+'\ScreenshotCleaner_ects')
    
    for fn in os.listdir(dir):
        if fn.startswith('Maple_A_') and (fn.endswith('.png') or fn.endswith('.jpg')):
            if isLevelup(dir+'\\'+fn):
                shutil.move(dir+'\\'+fn, dir+'\ScreenshotCleaner_LevelUp'+'\\'+fn)
            else:
                shutil.move(dir+'\\'+fn, dir+'\ScreenshotCleaner_ects'+'\\'+fn)
        elif fn.startswith('Maple_') and (fn.endswith('.png') or fn.endswith('.jpg')):
            shutil.move(dir+'\\'+fn, dir+'\ScreenshotCleaner_ects'+'\\'+fn)