import subprocess 
import os
import random
# import vlc 
# vlcInstance = vlc.Instance()
# player = vlcInstance.media_player_new()
# Media = vlcInstance.media_new('Settings 05-11-2018 16_22_02.mp4')
# Media.get_mrl()
# player.set_media(Media)
# print(media.get_mrl()) # File location to get title 
# print(player.get_length()) #Time duration of file -1 means there is no media
# print(player.get_state())
# player.play()
# p = subprocess.Popen([os.path.join("C:/", "Program Files", "VideoLAN", "VLC", "vlc.exe"),
# 	os.path.join("C:/", "Users", "Developer", "Videos", "Captures", "Settings.mp4")])
# title = 'Settings 05-11-2018 16_22_02'
#p = subprocess.Popen(["C:/Program Files/VideoLAN/VLC"])#,"C:/Users/Developer/Videos/Captures" + title + '.mp4'])

# -*- coding: utf-8 -*-

# import vlc , os

# class newPlayer(object):
#     def __init__(self):
#         self.Instance = vlc.Instance()
#         self.player = self.Instance.media_player_new()
    
#     def Open(self):
#         dirname = "C:\\Users\\Developer\\Videos\\Captures"
#         filename = "Settings 05-11-2018 16_22_02.mp4"

#         self.Media = self.Instance.media_new(unicode(os.path.join(dirname, filename)))
#         self.player.set_media(self.Media)
        
#         title = self.player.get_title()
#         print(title)         
        
#     def Play(self):
#         self.player.get_media()
#         self.player.play()
        
# Spelar = newPlayer()
# Spelar.Open()
# Spelar.Play()

# x = subprocess.Popen('dir', stdout=subprocess.PIPE, shell=True)
# x.communicate(stdout)


seasons = ['season 1','season 2','season 3','season 4','season 5','season 6']
random_season = random.choice(seasons)
print(random_season)

episode = ['1','2','3','4','5']	
rand_episode = random.choice(episode)
print(rand_episode)

cmd = 'vlc'+' F:\\movies\\tvshows\\F.R.I.E.N.D.S\\'+random_season+'\\'+rand_episode+'.mp4' 
print(cmd)
os.system(cmd)