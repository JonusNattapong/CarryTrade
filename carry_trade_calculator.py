# Carry Trade

def calculate_carry_trade_return(high_interest_rate, low_interest_rate, principal):
    """
    คำนวณผลตอบแทนจากกลยุทธ์ Carry Trade

    Args:
    - high_interest_rate (float): อัตราดอกเบี้ยสูง
    - low_interest_rate (float): อัตราดอกเบี้ยต่ำ
    - principal (float): เงินต้น

    Returns:
    - float: ผลตอบแทนจากกลยุทธ์ Carry Trade
    """
    return (high_interest_rate - low_interest_rate) * principal

def calculate_risk(high_interest_rate, low_interest_rate):
    """
    คำนวณความเสี่ยงจากกลยุทธ์ Carry Trade

    Args:
    - high_interest_rate (float): อัตราดอกเบี้ยสูง
    - low_interest_rate (float): อัตราดอกเบี้ยต่ำ

    Returns:
    - float: ความเสี่ยงจากกลยุทธ์ Carry Trade
    """
    import numpy as np
    return np.std([high_interest_rate, low_interest_rate])

def plot_return_and_risk(high_interest_rates, low_interest_rates, principal):
    """
    แสดงกราฟผลตอบแทนและความเสี่ยงจากกลยุทธ์ Carry Trade

    Args:
    - high_interest_rates (list): รายการอัตราดอกเบี้ยสูง
    - low_interest_rates (list): รายการอัตราดอกเบี้ยต่ำ
    - principal (float): เงินต้น
    """
    import matplotlib.pyplot as plt
    import numpy as np

    # Set font to support Thai characters
    plt.rcParams['font.family'] = 'Tahoma'

    returns = [calculate_carry_trade_return(high, low, principal) for high, low in zip(high_interest_rates, low_interest_rates)]
    risks = [calculate_risk(high, low) for high, low in zip(high_interest_rates, low_interest_rates)]

    plt.plot(returns, label='ผลตอบแทน')
    plt.plot(risks, label='ความเสี่ยง')
    plt.xlabel('ลำดับข้อมูล') # Changed label for clarity as x-axis is just index
    plt.ylabel('ค่า')
    plt.title('ผลตอบแทนและความเสี่ยงจากกลยุทธ์ Carry Trade')
    plt.legend()
    plt.grid(True) # Add grid for better readability
    plt.show()

# ตัวอย่างการใช้งาน
high_interest_rates = [0.04, 0.05, 0.06]  # 4.00%, 5.00%, 6.00%
low_interest_rates = [-0.001, 0.001, 0.002]  # -0.10%, 0.10%, 0.20%
principal = 100000  # 100,000 หน่วย

returns = [calculate_carry_trade_return(high, low, principal) for high, low in zip(high_interest_rates, low_interest_rates)]
risks = [calculate_risk(high, low) for high, low in zip(high_interest_rates, low_interest_rates)]
print(f"ผลตอบแทนจากกลยุทธ์ Carry Trade: {returns}")
print(f"ความเสี่ยงจากกลยุทธ์ Carry Trade: {risks}")
plot_return_and_risk(high_interest_rates, low_interest_rates, principal)