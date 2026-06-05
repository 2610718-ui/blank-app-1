import streamlit as st

# 웹 페이지 제목 설정
st.title("🎢 놀이기구 탑승 가능 여부 확인기")

# 구분선
st.divider()

# 스트림릿의 number_input 또는 slider를 사용하여 키 입력 받기
# 기본값은 150, 최소 50에서 최대 250까지 입력 가능하도록 설정
height = st.number_input("당신의 키를 입력하세요 (cm):", min_value=50, max_value=250, value=150, step=1)

# 또는 직관적인 슬라이더를 원하시면 아래 주석을 해제하고 사용하세요.
# height = st.slider("당신의 키를 선택하세요 (cm):", min_value=50, max_value=250, value=150)

# 결과 확인 버튼
if st.button("탑승 가능 여부 확인하기"):
    # 조건문 판별 및 결과 출력
    if height < 100:
        st.error("❌ 탑승 불가")
    elif height < 130:
        st.warning("⚠️ 보호자 동행 시 탑승 가능")
    elif height < 195:
        st.success("✅ 탑승 가능")
    else:
        st.error("❌ 탑승 불가 (신장 초과)")