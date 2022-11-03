import os
from datetime import datetime

#set source folder of folder to be sorted. E.g. C:/Users/[User]/Downloads
source_folder = 'CHANGE_TO_SOURCE_PATH' #set this
target_folder = 'CHANGE_TO_TARGET_PATH' #set this

now = datetime.now()

def walk_error_handler(exception_instance):
	print("it looks like this file already exists in the destination folder.")
	

#for each file in source folder
#if files are present
#for each file in the source folder
#if file isn't already in target folder, change the path and move from source to target
def move_files(source, target):
	try:
		for path, dir, files in os.walk(source, onerror=walk_error_handler):
			if files:
				for file in files:
					if not os.path.isfile(target + file):
						os.rename(path + '\\' + file, target + file)
						#Log the change. append so at end of file and doesn't overwrite
						#log file & timestamp
						with open('output.txt', 'a') as f:
							print('File: ' + file + ' moved to ' + target_folder + 'at ' + now.strftime('%m/%d/%Y %H:%M:%S'), file=f)
						f.close()
					else:
						print('file already exists in destination')
						print('file will be removed from source. You can find the saved file in: ' + target + path)
						os.remove(source + file)
					break
					
	#catch
	except Exception as e:
		print(e)


#perform move_files function
while True:
	move_files(source_folder, target_folder)