# Polymarket-trading-skill - Data Freshness Guard
import datetime

def verify_data_timeliness(data_summary):
    """【Gemini-3 Flash】: 强制校验数据是否属于 2026 年"""
    current_year = "2026"
    if current_year in data_summary:
        print(f"✅ 数据校验通过: 确认为 {current_year} 最新情报。")
        return True
    else:
        print("❌ 警告: 发现陈旧数据，拒绝推送给分析小弟！")
        return False
