import subprocess
import configparser
import errno
import getpass
import os
import grp
import platform
from . import TorConfigTool

class ShowConfigDetail:
  def set_env(self,src_file):
    # config.iniから設定を読み込むよう改修
    config_ini = configparser.ConfigParser()
    #config_ini_path = './config/config.ini'
    # 個人環境ini読み込み
    config_ini_path = './config/my_config.ini'
    # config.iniの有無を確認
    if not os.path.exists(config_ini_path):
      raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)
    config_ini.read('config.ini', encoding='utf-8')

    # Source path set valiable
    #src_path = "./config/"
    # mod用path
    src_path = self.config_ini['PATH']['src_torrc_path']
    dst_file = self.config_ini['FILE']['tor_config']

    # Destinationpath set valiable
    # get platform os
    pf = platform.system()
    print(pf)
    if pf == 'Windows':
        print('on Windows')
        #windows用path
        dst_path = config_ini['PATH']['dst_torrc_windows_path']
    elif pf == 'Darwin':
        print('on Mac')
        #Mac用path
        dst_path = config_ini['PATH']['dst_torrc_mac_path']
    elif pf == 'Linux':
        print('on Linux')
        #Linux用path
        dst_path = config_ini['PATH']['dst_torrc_linux_path']
    
    input_config = src_path + src_file
    output_config = dst_path + dst_file
    return input_config,output_config
    
  def show_conf_now(self,output_config):
    cmd = "cat " + output_config
    subprocess.run(cmd,shell=True)
    
  def show_conf(self,input_config):
    cmd = "cat " + input_config
    subprocess.run(cmd,shell=True)
    
  def run(self):
    menu_msg = """=============== MENU ===============
Please select the config file to reference
=======================================
[0]torrc_level0
setting[entry:{jp}only,include:{jp}only,exit:{jp}only]

[1]torrc_level1
setting[entry:{jp}only,include:1hop country,exit:{jp}only]

[2]torrc_level2
setting[entry:{jp}only,include:1hop country,exit:1hop country]

[3]torrc_level3
setting[entry:1hop country,include:1hop country,exit:1hop country]

[4]torrc_level4
setting[entry:tor default,include:tor default,exit:tor default]

[5]torrc_5eyes
setting[exclude:5eyes]

[6]torrc_9eyes
setting[exclude:9eyes]

[7]torrc_14eyes
setting[exclude:14eyes]

[8]torrc_41eyes
setting[exclude:41eyes]

[9]torrc_levelMAX
setting[exclude:41eyes + dangerous country]

[10]torrc_levelCustom
setting[exclude:14eyes + mycountry + EntryGuargs 15]

[s]:Show running config
Check the current settings .

[q]:Cancel selection
======================================="""
    print(menu_msg)

    while True:
      print('--- ShowConfigDetail Menu ---')
      num = input('Please enter the menu number : ')
      print("Selected menu number : " + num)
      if num == "0":
        src_file = "torrc_level0.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "1":
        src_file = "torrc_level1.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "2":
        src_file = "torrc_level2.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "3":
        src_file = "torrc_level3.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "4":
        src_file = "torrc_level4.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "5":
        src_file = "torrc_5eyes.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "6":
        src_file = "torrc_9eyes.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "7":
        src_file = "torrc_14eyes.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "8":
        src_file = "torrc_41eyes.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "9":
        src_file = "torrc_levelMax.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "10":
        src_file = "torrc_levelCustom.txt"
        env_data = self.set_env(src_file)
        input_config = env_data[0]
        self.show_conf(input_config)
        continue
      elif num == "s":
        src_file = "torrc_.txt"
        env_data = self.set_env(src_file)
        output_config = env_data[1]
        self.show_conf_now(output_config)
        continue
      elif num == "q": 
        print("--- Quit ---")
        break
      else:
        print("--- INPUT ERROR ---")