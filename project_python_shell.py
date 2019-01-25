#!/usr/bin/env python3

import sys
import os
import shutil

# 获取当前文件名字
print(sys.argv[0])
# 获取昂前目录
currentPath = os.getcwd()
print(currentPath)

path = 'CarCrm'
if not os.path.exists(path):
    os.mkdir(path)

if os.path.exists(path):
    os.chdir(path)
    currentPath = os.getcwd()
projectPath = currentPath
print(currentPath)

# 拉取carCrm库
os.system('git clone git@gitlab.mljr.com:android/car_crm.git')
carCrmPath = projectPath + '/car_crm'
if os.path.exists(carCrmPath):
    os.chdir(carCrmPath)
    os.system('git checkout -b dev origin/dev')

projectModulePath = currentPath + '/car_crm/script/config/init_files'
print(projectModulePath)
if os.path.exists(projectModulePath):
    os.chdir(projectModulePath)
    currentPath = os.getcwd()
print(currentPath)

files = os.listdir(projectModulePath)
for file in files:
    shutil.move(file, projectPath)

print(os.getcwd())
os.chdir(projectPath)
print(os.getcwd())
# 拉取moon_sdk_app
os.system('git clone git@gitlab.mljr.com:moon-android/moon_sdk_app.git')
# 切换dev分支
moonSdkAppPath = projectPath + '/moon_sdk_app'
if os.path.exists(moonSdkAppPath):
    os.chdir(moonSdkAppPath)
    os.system('git checkout -b dev origin/dev')
# 拉取moon_sdk_base
os.chdir(projectPath)
os.system('git clone git@gitlab.mljr.com:moon-android/moon_sdk_base.git')
# 切换dev分支
moonSdkBasePath = projectPath + '/moon_sdk_base'
if os.path.exists(moonSdkBasePath):
    os.chdir(moonSdkBasePath)
    os.system('git checkout -b dev origin/dev')
os.chdir(projectPath)
