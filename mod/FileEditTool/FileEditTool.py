import os
import glob
import shutil
import string
import random
import pprint #use...?
from PIL import Image
import codecs

'''
・rename
・random_rename(auto_path)
・random_rename(select_path)
・resize
・conv_tool
'''

class  FileEditTool:
  def set_env(self):
    # target path
    src_dir = "../../src"
    dst_dir = "../../dst"
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dst_dir, exist_ok=True)
    # target files
    target_files = glob.glob(os.path.join(src_dir + '/*'))
    target_files.sort()
    pprint.pprint(target_files)
    return src_dir,dst_dir,target_files

  #rename proc
  def rename(self,target_files,dst_dir):
    new_name = input('Please enter a new file name : ')
    # index number count
    for i, f in enumerate(target_files, 1):
      root, ext = os.path.splitext(f)
      print(ext)
      re_name = new_name + '_' + '{0:03d}'.format(i) + ext
      print(re_name)
      copy_path = os.path.join(dst_dir + '/' + re_name)   
      print(f + ' => ' + dst_dir + '/' + re_name)
      shutil.copy(f,copy_path)

  #random rename proc
  def rename_random_auto(self,target_files,dst_dir,length):
    for f in target_files:
      new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
      root, ext = os.path.splitext(f)
      print(ext)
      re_name = new_name + ext
      print(re_name)
      copy_path = os.path.join(dst_dir + '/' + re_name)   
      print(f + ' => ' + dst_dir + '/' + re_name)
      shutil.copy(f,copy_path)
  
  def rename_random_select(self,length):
    target_path = input('Please enter the target path : ')
    # target files
    target_files = glob.glob(os.path.join(target_path + '/*'))
    target_files.sort()
    pprint.pprint(target_files)

    for f in target_files:
      new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
      root, ext = os.path.splitext(f)
      #print(ext)
      re_name = new_name + ext
      #print(re_name)
      #print(os.path.isdir(f))
      if not os.path.isdir(f):
        print(f + ' => ' + target_path + '/' + re_name)
        os.rename(f,target_path + '/' + re_name)
  
  def conversion_character_code(self,target_files,dst_dir):
    # cov_cmd = "find ./src -name '*.txt' -type f -print0 | xargs -0 nkf -u --overwrite -w -Lu"
    for f in target_files:
      dst_file_name = os.path.basename(f)
      src_file = codecs.open(f ,'r', 'shift_jis')
      dst_file = codecs.open(dst_dir  +'/' + dst_file_name, "w", "utf-8")
      print(f + '->' + dst_dir + '/' + dst_file_name)
      for row in src_file:
        dst_file.write(row)
        src_file.close()
        dst_file.close()
                
  # resize proc
  def resize(self,target_files,dst_dir):
    wsize = input('Please enter the width of the image: ')
    if wsize=='':
        wsize=700 
    else:
        wsize = int(wsize)
    for f in target_files:
        img = Image.open(f)
        if wsize >= img.width:
          continue
        rate = wsize / img.width
        hsize = int(img.height * rate)
        img_resize = img.resize((wsize, hsize))
        resize_name = os.path.basename(f)
        img_resize.save(dst_dir + '/' + resize_name,quality = 100)
        print(resize_name + ' => resize => ' + dst_dir)

  # running proc
  def run(self):
    # set env proc
    env_data = self.set_env()
    src_dir = env_data[0] #未使用変数
    dst_dir = env_data[1]
    target_files = env_data[2]
    # DEBUG
    #print('env_data : ' + str(env_data))
    #print('stc_dir : ' + src_dir)
    #print('dst_dir : ' + dst_dir)
    #print('target_files : ' + str(target_files))
    # select process menu
    while True:
        print('=== select menu ===')
        print('[1] : rename')
        print('[2] : resize')
        print('[3] : rename random auto path')
        print('[4] : rename random select path')
        print('[5] : conversion character code')
        print('[q] : quit')
        print('===================')
        ans_menu = input('Enter the menu number to execute : ')
        if ans_menu == '1':
            print('===== start rename process =====')
            self.rename(target_files,dst_dir)
            print('=== completion of the rename process ===')
            break
        elif ans_menu == '2':
            print('=== start resize process ===')
            self.resize(target_files,dst_dir)
            print('=== completion of the resize process ===')
            break
        elif ans_menu =='3':
            print('=== start rename random auto path process ===')
            self.rename_random_auto(target_files,dst_dir,8)
            print('=== completion of the rrename random auto path process ===')
            break
        elif ans_menu == '4':
            print('=== start rename random select path process ===')
            self.rename_random_select(8)
            print('=== completion of the rename random select path process ===')
            break
        elif ans_menu == '5':
            print('=== start conversion character code process ===')
            self.conversion_character_code(target_files,dst_dir)
            print('=== completion of the conversion character code process ===')
            break
        elif ans_menu == 'q':
            print('Exited from processing.')
            break
        else:
            print('Enter it again')
    print('=== All processing completed !! ===')

if __name__ == "__main__":
    file_edit = FileEditTool()
    file_edit.run()