import streamlit as st
from PIL import Image
import os

# 页面基础设置
st.set_page_config(page_title="趣味问答", page_icon="🐷", layout="centered")

# 标题和问题
st.title("🐷 趣味问答")
st.subheader("郑雨晴是小猪吗？")

# ========== 关键：替换图片路径 ==========
# 方式1：用你上传到Streamlit Cloud的本地图片（推荐）
# 确保图片和代码文件在同一目录，比如图片叫 pig.jpg / 小猪.png
IMG_PATH = "pig.jpg"  # 改成你的图片文件名（含后缀）

# 方式2：用图片网址（不用上传图片，更方便）
# 把下面的链接换成你的小猪图片网络地址（比如图床链接）
# IMG_PATH = "https://xxx.xxx/pig.jpg"  # 取消注释并替换

# 并排显示yes/no按钮
col1, col2 = st.columns(2)

# YES按钮逻辑
with col1:
    if st.button("yes", type="primary", use_container_width=True):
        st.success("🐷")  # 显示提示文字
        # 显示小猪图片
        try:
            # 本地图片
            if os.path.exists(IMG_PATH):
                img = Image.open(IMG_PATH)
                st.image(img, width=400, caption="小猪来啦～")
            # 网络图片（如果用方式2，删掉上面的if，保留下面这行）
            # st.image(IMG_PATH, width=400, caption="小猪来啦～")
        except Exception as e:
            st.error(f"图片加载失败：{str(e)}")
            st.info("请检查图片文件名/网址是否正确")

# NO按钮逻辑
with col2:
    if st.button("no", use_container_width=True):

        st.warning("请重新选择！")
