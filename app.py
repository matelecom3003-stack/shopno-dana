import streamlit as st
import pandas as pd

# ১. পেজ সেটআপ এবং আইকন
st.set_page_config(page_title="স্বপ্ন ডানা ড্যাশবোর্ড", layout="wide", page_icon="📈")

# ২. ডিজাইন উন্নত করতে কাস্টম CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# ৩. গুগল শিট লিংক
sheet_url = "https://docs.google.com/spreadsheets/d/1gnN42cqglWAeMki5E1xppYhDNwyQ8tGRLd3Ze5QZLJc/export?format=csv"

# ৪. সাইডবার ডিজাইন
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.title("কন্ট্রোল প্যানেল")
    st.info("আপনার গুগল শিটে ডাটা যোগ করলে এখানে অটোমেটিক আপডেট হবে।")
    if st.button('🔄 ডাটা রিফ্রেশ করুন'):
        st.rerun()

# ৫. মূল ড্যাশবোর্ড শিরোনাম
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚀 স্বপ্ন ডানা - ফিন্যান্সিয়াল ড্যাশবোর্ড</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>লাইভ ডাটা ট্র্যাকিং সিস্টেম</p>", unsafe_allow_html=True)
st.divider()

try:
    # ডাটা লোড করা
    df = pd.read_csv(sheet_url)
    df.columns = df.columns.str.strip().str.capitalize()

    # ৬. স্টাইলিশ মেট্রিক কার্ডস
    m1, m2, m3 = st.columns(3)
    
    total_fund = df['Amount'].sum()
    total_members = len(df)
    avg_deposit = total_fund / total_members if total_members > 0 else 0

    with m1:
        st.metric(label="💰 মোট জমা তহবিল", value=f"{total_fund:,} ৳", delta="বর্তমান ব্যালেন্স")
    with m2:
        st.metric(label="👥 মোট সদস্য সংখ্যা", value=f"{total_members} জন")
    with m3:
        st.metric(label="📊 গড় জমা", value=f"{avg_deposit:,.0f} ৳")

    st.divider()

    # ৭. ডাটা টেবিল এবং চার্ট
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📝 বিস্তারিত লেনদেনের তালিকা")
        st.dataframe(df, use_container_width=True, height=400)

    with col_right:
        st.subheader("🥧 জমার অনুপাত")
        # একটি ছোট বার চার্ট
        st.bar_chart(df.set_index('Name')['Amount'])

except Exception as e:
    st.error("ডাটা পড়তে সমস্যা হচ্ছে। অনুগ্রহ করে গুগল শিটের কলাম চেক করুন।")