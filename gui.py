import easygui as g

from imageRecognition import get_img_rec
from speechRecognition import get_speech_rec
from textRecognition import get_text_rec

# img = g.diropenbox(msg="请选择需要识别的图像",title="图像识别",default=None)

flag = True
while flag:
    choice = g.choicebox(msg="请选择系统功能", title="无障碍人机对话系统", choices=["图像识别", "文字识别", "语音识别", "人机对话"])
    if choice == "图像识别":
        choice = g.choicebox(msg="请选择需要识别图像的类别", title="图像识别", choices=["动物识别", "植物识别", "红酒识别", "货币识别", "通用识别"])
        # 读取图片
        img_path = g.fileopenbox(msg="请选择需要识别的图像", title="图像识别", filetypes=["*.png", "*.jpg", "*.jpeg"])
        if img_path is not None:
            img_rec = g.msgbox(image=img_path, msg=get_img_rec(img_path, choice), title="图像识别", ok_button="确定并返回")
        if not g.boolbox(msg="是否继续进行智能交互?"):
            flag = False
    elif choice == "文字识别":
        # 读取文字图片
        img_path = g.fileopenbox(msg="请选择需要识别的图像", title="文字识别", filetypes=["*.png", "*.jpg", "*.jpeg"])
        if img_path is not None:
            txt_rec = g.msgbox(image=img_path, msg=get_text_rec(img_path), title="文字识别", ok_button="确定并返回")
        if not g.boolbox(msg="是否继续进行智能交互?"):
            flag = False
    elif choice == "语音识别":
        # 读取语音
        audio_path = g.fileopenbox(msg="请上传需要识别(转换)的录音", title="语音识别", filetypes=["*.pcm", "*.wav", "*.amr"])
        if audio_path is not None:
            audio_rec = g.msgbox(msg=get_speech_rec(audio_path), title="语音识别", ok_button="确定并返回")
        if not g.boolbox(msg="是否继续进行智能交互?"):
            flag = False
