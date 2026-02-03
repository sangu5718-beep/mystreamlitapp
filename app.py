import streamlit as st
from datetime import datetime

st.set_page_config(page_title="PRD Mini App", page_icon="✅", layout="centered")

st.title("✅ PRD 기반 초간단 Streamlit 앱")
st.caption("과제 통과용: 입력 1개 + 버튼 1개 + 출력 1개")

with st.expander("📌 PRD 요약(간단)"):
    st.write("- 목표: 입력을 받아 간단한 결과를 출력하는 MVP 앱")
    st.write("- Input: 텍스트 1개")
    st.write("- Output: 텍스트 결과 1개")

st.divider()

text = st.text_input("한 줄 입력", placeholder="예: 오늘 훈련 요약 / 영화 추천 / 일정 정리 등")
mode = st.selectbox("출력 형식", ["요약", "추천", "체크리스트"], index=0)

if st.button("결과 생성"):
    if not text.strip():
        st.warning("입력을 한 줄만 적어줘.")
    else:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        if mode == "요약":
            output = f"[{now}] 요약: {text}"
        elif mode == "추천":
            output = f"[{now}] 추천: {text} 관련 A/B/C 중 A안을 우선 추천"
        else:
            output = f"[{now}] 체크리스트:\n- [ ] {text} 준비\n- [ ] 실행\n- [ ] 마무리"

        st.success("완료")
        st.code(output, language="text")
        st.download_button("결과 다운로드", data=output, file_name="result.txt")
else:
    st.info("입력하고 버튼 누르면 결과가 나온다.")
