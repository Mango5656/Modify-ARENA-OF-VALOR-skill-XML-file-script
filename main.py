import os
import xml.etree.ElementTree as ET
import re

current_path = os.path.dirname(os.path.realpath(__file__))

folder_path = os.path.join(current_path, "skill")


skin = input("造型代號 例:1055 or 10515 請輸入:")


if len(skin) not in (4, 5):
    print("輸入的數字長度應該為 4 或 5。程式終止運行。")
    exit()

    
if len(skin) == 4:
    result = skin[-1]
elif len(skin) == 5:
    result = skin[-2:]

def modify_xml_file(file_path):
    try:
        # 解析XML檔案
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 查找包含PlayHeroSoundTick的Track元素
        for track in root.iter('Track'):
            track_name = track.attrib.get('trackName', '')
            if 'PlayHeroSoundTick' in track_name:
                for event in track.iter('Event'):
                    for string_elem in event.iter('String'):
                        if string_elem.attrib.get('name') == 'eventName':
                            print(f"Before Modification: {string_elem.attrib['value']}")
                            string_elem.attrib['value'] += '_skin' + result
                            print(f"After Modification: {string_elem.attrib['value']}")
                            
                          
    except Exception as e:
                print(f"處理檔案 '{file_path}' 時發生錯誤：{str(e)}")
                return
    tree.write(file_path, encoding='utf-8')
    

    

def process_folder(folder_path):
    try:
        # 確保資料夾存在
        if not os.path.exists(folder_path):
            print(f"資料夾 '{folder_path}' 不存在。")
            return

        # 遍歷資料夾中的所有檔案
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # 只處理XML檔案
            if file_name.lower().endswith('.xml'):
                modify_xml_file(file_path)

        print("處理完成。")

    except Exception as e:
        print(f"發生錯誤：{str(e)}")



# 執行處理資料夾的腳本
process_folder(folder_path)






#第二部分
folder_path=r"C:\Users\rudys\OneDrive\桌面\aov 腳本\skill"
if len(skin) == 4:
    skin_1 = skin[:3] + '0' + skin[-1]
elif len(skin) == 5:
    skin_1 = skin
def modify_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 使用正規表達式修改 value 屬性的路徑
        for element in root.iter():
            if 'value' in element.attrib and 'prefab_skill_effects/hero_skill_effects/' in element.attrib['value']:
                updated_value = re.sub(r'(prefab_skill_effects/hero_skill_effects/)(\w+/)(\w+)', r'\g<1>\g<2>{}/\g<3>'.format(skin_1), element.attrib['value'])
                element.attrib['value'] = updated_value

        # 修改 Event 元素下的 String 元素中的 resourceName 屬性
        for track_element in root.iter('Track'):
            for event_element in track_element.iter('Event'):
                updated_value = None  # 初始化 updated_value
                for string_element in event_element.iter('String'):
                    if 'resourceName' in string_element.attrib and 'prefab_skill_effects/hero_skill_effects/' in string_element.attrib['resourceName']:
                        updated_resource_name = re.sub(r'(prefab_skill_effects/hero_skill_effects/)(\w+/)(\w+)', r'\g<1>\g<2>{}/\g<3>'.format(skin_1), string_element.attrib['resourceName'])
                        string_element.attrib['resourceName'] = updated_resource_name
                        updated_value = updated_resource_name

                # 將更新後的值設定給 updated_value，以便後續使用
                if updated_value is not None:
                    element.attrib['value'] = updated_value

    except ET.ParseError as e:
        print(f"處理檔案 '{file_path}' 時發生 XML 解析錯誤：{str(e)}")
        return
    except Exception as e:
        print(f"處理檔案 '{file_path}' 時發生錯誤：{str(e)}")
        return

    # 將更新後的內容寫回檔案
    tree.write(file_path, encoding='utf-8')




def process_folder(folder_path):
    try:
        # 確保資料夾存在
        if not os.path.exists(folder_path):
            print(f"資料夾 '{folder_path}' 不存在。")
            return

        # 遍歷資料夾中的所有檔案
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # 只處理XML檔案
            if file_name.lower().endswith('.xml'):
                modify_xml_file(file_path)

        print("處理完成。")

    except Exception as e:
        print(f"發生錯誤：{str(e)}")



# 執行處理資料夾的腳本
process_folder(folder_path)



def modify_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # 使用正規表達式修改 value 屬性的路徑
        for element in root.iter():
            if 'value' in element.attrib and 'Prefab_Skill_Effects/Hero_Skill_Effects/' in element.attrib['value']:
                updated_value = re.sub(r'(Prefab_Skill_Effects/Hero_Skill_Effects/)(\w+/)(\w+)', r'\g<1>\g<2>{}/\g<3>'.format(skin_1), element.attrib['value'])
                element.attrib['value'] = updated_value

        # 修改 Event 元素下的 String 元素中的 resourceName 屬性
        for track_element in root.iter('Track'):
            for event_element in track_element.iter('Event'):
                updated_value = None  # 初始化 updated_value
                for string_element in event_element.iter('String'):
                    if 'resourceName' in string_element.attrib and 'Prefab_Skill_Effects/Hero_Skill_Effects/' in string_element.attrib['resourceName']:
                        updated_resource_name = re.sub(r'(Prefab_Skill_Effects/Hero_Skill_Effects/)(\w+/)(\w+)', r'\g<1>\g<2>{}/\g<3>'.format(skin_1), string_element.attrib['resourceName'])
                        string_element.attrib['resourceName'] = updated_resource_name
                        updated_value = updated_resource_name
                    

                # 將更新後的值設定給 updated_value，以便後續使用
                if updated_value is not None:
                    element.attrib['value'] = updated_value

    except ET.ParseError as e:
        print(f"處理檔案 '{file_path}' 時發生 XML 解析錯誤：{str(e)}")
        return
    except Exception as e:
        print(f"處理檔案 '{file_path}' 時發生錯誤：{str(e)}")
        return

    # 將更新後的內容寫回檔案
    tree.write(file_path, encoding='utf-8')




def process_folder(folder_path):
    try:
        # 確保資料夾存在
        if not os.path.exists(folder_path):
            print(f"資料夾 '{folder_path}' 不存在。")
            return

        # 遍歷資料夾中的所有檔案
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # 只處理XML檔案
            if file_name.lower().endswith('.xml'):
                modify_xml_file(file_path)

        print("處理完成。")

    except Exception as e:
        print(f"發生錯誤：{str(e)}")



# 執行處理資料夾的腳本
process_folder(folder_path)
