import sys
import os
import shutil
import subprocess

all_module_list = ['git clone git@gitlab.mljr.com:moon-android/moon_sdk_app.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_base.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_kit.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_web_bridge.git',
                   'git clone git@gitlab.mljr.com:android/common-idcard.git',
                   'git clone git@gitlab.mljr.com:android/common-bankcard.git',
                   'git clone git@gitlab.mljr.com:android/finance-ocr_card-online.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_common_ui.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_cache.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_db.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_network.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_sdk_page_router.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_ui_dialog.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_ui_form_edit.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_upload_img_base.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_ui_img_picker.git',
                   'git clone git@gitlab.mljr.com:moon-android/moon_vin.git']

all_module_name_list = ['moon_sdk_app', 'moon_sdk_base', 'moon_sdk_kit', 'moon_sdk_web_bridge',
                        'common-idcard', 'common-bankcard', 'finance-ocr_card-online', 'moon_common_ui',
                        'moon_sdk_cache', 'moon_sdk_db', 'moon_sdk_network', 'moon_sdk_page_router',
                        'moon_ui_dialog', 'moon_ui_form_edit', 'moon_upload_img_base', 'moon_ui_img_picker',
                        'moon_vin']

print('当前文件名称:' + sys.argv[0])
current_path = os.getcwd()
print('当前目录名称:' + current_path)

assert ('脚本运行参数:' + str(sys.argv))
argv_count = len(sys.argv)
assert ('脚本运行参数个数:' + str(argv_count))

if argv_count == 2:
    argument_1 = str(sys.argv[1])
    assert ('第一个参数:' + str(argument_1))
    if argument_1 == '-h' or argument_1 == '--help':
        print('''此脚本仅可下载car_crm项目，脚本后面暂时仅支持最多两个参数，最少无参
脚本后不写参数(默认无参):仅下载car_crm,moon_sdk_base,moon_sdk_app三个模块，并且切换到dev(开发分支)分支，例如:(python car_crm_shell.py)
-h(--help)   :帮助提示（仅可放在第一个参数中，例如:python car_crm_shell.py -h;python car_crm_shell.py --help）
-a(--all)    :下载包括项目的所有模块（仅可放在第一个参数中，例如:python car_crm_shell.py -a;python car_crm_shell.py --all）
-n(--need)   :下载项目必须的模块（仅可放在第一个参数中），例如:python car_crm_shell.py -n;python car_crm_shell.py --need）
-m(--master) :默认为master分支，所有模块切换到master分支（仅可放在第二个参数中），例如:python car_crm_shell.py --all -m;python car_crm_shell.py -n --master
-d(--dev)    :dev(开发)分支,所有模块切换到dev分支（仅可放在第二个参数中），例如:python car_crm_shell.py --all --dev;python car_crm_shell.py -n -d''')
        os._exit(0)

path = 'CarCrm'
if not os.path.exists(path):
    os.mkdir(path)

if os.path.exists(path):
    os.chdir(path)
    current_path = os.getcwd()

project_path = current_path
print('当前目录名称:' + current_path)

# 拉取carCrm库
car_crm_module = 'git clone git@gitlab.mljr.com:android/car_crm.git'
car_crm_name = 'car_crm'
car_crm_path = project_path + '/' + car_crm_name
if os.path.exists(car_crm_path):
    os.chdir(car_crm_path)
else:
    os.system(car_crm_module)
    os.chdir(car_crm_path)

out_put = os.system('git checkout -b dev origin/dev')
if out_put != 0:
    print(car_crm_name + ' module切换远程dev分支失败，请查看上方log')
else:
    print(car_crm_name + ' module切换远程dev分支成功!')

project_module_path = current_path + '/car_crm/script/config/init_files'
print('脚本初始化文件路径:' + project_module_path)
if os.path.exists(project_module_path):
    os.chdir(project_module_path)
    current_path = os.getcwd()

files = os.listdir(project_module_path)
for file in files:
    if not os.path.exists(project_path + '/' + file):
        shutil.move(file, project_path)

# 切换到project path
os.chdir(project_path)

if os.path.exists(project_path + '/build.gradle.backup') and not os.path.exists(project_path + '/build.gradle'):
    shutil.copy(project_path + '/build.gradle.backup', project_path + '/build.gradle')

if argv_count == 2:
    argument_1 = str(sys.argv[1])
    print('第一个参数:' + str(argument_1))
    if argument_1 == '-h' or argument_1 == '--help':
        print('''此脚本仅可下载car_crm项目，脚本后面暂时仅支持最多两个参数，最少无参
脚本后不写参数(默认无参):仅下载car_crm,moon_sdk_base,moon_sdk_app三个模块，并且切换到dev(开发分支)分支，例如:(python car_crm_shell.py)
-h(--help)   :帮助提示（仅可放在第一个参数中，例如:python car_crm_shell.py -h;python car_crm_shell.py --help）
-a(--all)    :下载包括项目的所有模块（仅可放在第一个参数中，例如:python car_crm_shell.py -a;python car_crm_shell.py --all）
-n(--need)   :下载项目必须的模块（仅可放在第一个参数中），例如:python car_crm_shell.py -n;python car_crm_shell.py --need）
-m(--master) :默认为master分支，所有模块切换到master分支（仅可放在第二个参数中），例如:python car_crm_shell.py --all -m;python car_crm_shell.py -n --master
-d(--dev)    :dev(开发)分支,所有模块切换到dev分支（仅可放在第二个参数中），例如:python car_crm_shell.py --all --dev;python car_crm_shell.py -n -d''')
    elif argument_1 == '-a' or argument_1 == '--all':
        print('下载所有的模块')
        for index in range(len(all_module_list)):
            module = all_module_list[index]
            print('git clone 地址:' + module)
            module_name = all_module_name_list[index]
            print('module name:' + module_name)
            moon_path = project_path + '/' + module_name
            if os.path.exists(moon_path):
                os.chdir(moon_path)
            else:
                os.system(module)
                os.chdir(moon_path)
            out_put = os.system('git checkout -b dev origin/dev')
            if out_put != 0:
                print(car_crm_name + ' module切换远程dev分支失败，请查看上方log')
            else:
                print(module_name + ' module切换远程dev分支成功!')
            os.chdir(project_path)

    elif argument_1 == '-n' or argument_1 == '--need':
        print('仅下载所需要的模块')
        for index in range(2):
            module = all_module_list[index]
            print('git clone 地址:' + module)
            module_name = all_module_name_list[index]
            print('module name:' + module_name)
            moon_path = project_path + '/' + module_name
            if os.path.exists(moon_path):
                os.chdir(moon_path)
            else:
                os.system(module)
                os.chdir(moon_path)
            os.chdir(project_path)

    else:
        print('请检查参数输入是否正确')

elif argv_count == 3:
    argument_1 = sys.argv[1]
    argument_2 = sys.argv[2]
    if argument_1 == '-a' or argument_1 == '--all':
        if argument_2 == '-m' or argument_2 == '--master':
            for index in range(len(all_module_list)):
                module = all_module_list[index]
                print('git clone 地址:' + module)
                module_name = all_module_name_list[index]
                print('module name:' + module_name)
                moon_path = project_path + '/' + module_name
                if os.path.exists(moon_path):
                    os.chdir(moon_path)
                else:
                    os.system(module)
                    os.chdir(moon_path)
                os.chdir(project_path)
            print('所有module均在master分支上')
        elif argument_2 == '-d' or argument_2 == '--dev':
            for index in range(len(all_module_list)):
                module = all_module_list[index]
                print('git clone 地址:' + module)
                module_name = all_module_name_list[index]
                print('module name:' + module_name)
                moon_path = project_path + '/' + module_name
                if os.path.exists(moon_path):
                    os.chdir(moon_path)
                else:
                    os.system(module)
                    os.chdir(moon_path)
                out_put = os.system('git checkout -b dev origin/dev')
                if out_put != 0:
                    print(car_crm_name + ' module切换远程dev分支失败，请查看上方log')
                else:
                    print(module_name + ' module切换远程dev分支成功!')
                os.chdir(project_path)
        else:
            print('请输入正确的参数')
    elif argument_1 == '-n' or argument_1 == '--need':
        if argument_2 == '-m' or argument_2 == '--master':
            for index in range(2):
                module = all_module_list[index]
                print('git clone 地址:' + module)
                module_name = all_module_name_list[index]
                print('module name:' + module_name)
                moon_path = project_path + '/' + module_name
                if os.path.exists(moon_path):
                    os.chdir(moon_path)
                else:
                    os.system(module)
                    os.chdir(moon_path)
                os.chdir(project_path)
        elif argument_2 == '-d' or argument_2 == '--dev':
            for index in range(2):
                module = all_module_list[index]
                print('git clone 地址:' + module)
                module_name = all_module_name_list[index]
                print('module name:' + module_name)
                moon_path = project_path + '/' + module_name
                if os.path.exists(moon_path):
                    os.chdir(moon_path)
                else:
                    os.system(module)
                    os.chdir(moon_path)
                out_put = os.system('git checkout -b dev origin/dev')
                if out_put != 0:
                    print(car_crm_name + ' module切换远程dev分支失败，请查看上方log')
                else:
                    print(module_name + ' module切换远程dev分支成功!')
                os.chdir(project_path)
        else:
            print('请输入正确的参数')
    else:
        print('请输入正确的参数')

elif argv_count == 1:
    argument_0 = sys.argv[0]
    print('下载所需要的模块，并且切换到dev分支')
    for index in range(2):
        module = all_module_list[index]
        print('git clone 地址:' + module)
        module_name = all_module_name_list[index]
        print('module name:' + module_name)
        moon_path = project_path + '/' + module_name
        if os.path.exists(moon_path):
            os.chdir(moon_path)
        else:
            os.system(module)
            os.chdir(moon_path)
        out_put = os.system('git checkout -b dev origin/dev')
        if out_put != 0:
            print(car_crm_name + ' module切换远程dev分支失败，请查看上方log')
        else:
            print(module_name + ' module切换远程dev分支成功!')
        os.chdir(project_path)

else:
    print('请输入正确的参数')

print('脚本执行完毕!!!')
