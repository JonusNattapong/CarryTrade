# Carry Trade
import numpy as np
import matplotlib.pyplot as plt

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
    return np.std([high_interest_rate, low_interest_rate])

def calculate_interest_differential(high_interest_rate, low_interest_rate):
    """
    คำนวณส่วนต่างของอัตราดอกเบี้ย

    Args:
    - high_interest_rate (float): อัตราดอกเบี้ยสูง
    - low_interest_rate (float): อัตราดอกเบี้ยต่ำ

    Returns:
    - float: ส่วนต่างของอัตราดอกเบี้ย
    """
    return high_interest_rate - low_interest_rate

def identify_best_carry_trades(currency_data):
    """
    ระบุคู่สกุลเงินที่เหมาะสมที่สุดสำหรับ Carry Trade

    Args:
    - currency_data (dict): ข้อมูลสกุลเงินและอัตราดอกเบี้ย format: {'CUR': interest_rate}

    Returns:
    - list: คู่สกุลเงินที่เหมาะสมที่สุดพร้อมข้อมูลส่วนต่างของอัตราดอกเบี้ย
    """
    pairs = []
    currencies = list(currency_data.keys())
    
    for i in range(len(currencies)):
        for j in range(i+1, len(currencies)):
            cur1 = currencies[i]
            cur2 = currencies[j]
            rate1 = currency_data[cur1]
            rate2 = currency_data[cur2]
            
            if rate1 > rate2:
                high_cur, low_cur = cur1, cur2
                high_rate, low_rate = rate1, rate2
            else:
                high_cur, low_cur = cur2, cur1
                high_rate, low_rate = rate2, rate1
            
            differential = high_rate - low_rate
            pairs.append({
                'pair': f"{high_cur}/{low_cur}",
                'high_currency': high_cur,
                'low_currency': low_cur,
                'high_rate': high_rate,
                'low_rate': low_rate,
                'differential': differential
            })
    
    # เรียงลำดับตามค่าส่วนต่างของอัตราดอกเบี้ยจากมากไปน้อย
    return sorted(pairs, key=lambda x: x['differential'], reverse=True)

def simulate_carry_trade(high_currency, low_currency, high_rate, low_rate, 
                         principal, days, exchange_rate_volatility=0.0005):
    """
    จำลองผลตอบแทนของ Carry Trade ตลอดช่วงเวลาที่กำหนด

    Args:
    - high_currency (str): สกุลเงินที่มีอัตราดอกเบี้ยสูง
    - low_currency (str): สกุลเงินที่มีอัตราดอกเบี้ยต่ำ
    - high_rate (float): อัตราดอกเบี้ยของสกุลเงินที่มีอัตราดอกเบี้ยสูง
    - low_rate (float): อัตราดอกเบี้ยของสกุลเงินที่มีอัตราดอกเบี้ยต่ำ
    - principal (float): เงินต้น
    - days (int): จำนวนวันในการจำลอง
    - exchange_rate_volatility (float): ความผันผวนของอัตราแลกเปลี่ยน

    Returns:
    - tuple: (ผลตอบแทนสะสมรายวัน, ความเสี่ยงสะสมรายวัน)
    """
    daily_high_rate = (1 + high_rate) ** (1/365) - 1
    daily_low_rate = (1 + low_rate) ** (1/365) - 1
    
    # จำลองอัตราแลกเปลี่ยนเริ่มต้น
    exchange_rate = 1.0
    
    cumulative_returns = [0]
    cumulative_risks = [0]
    
    for day in range(1, days + 1):
        # จำลองการเปลี่ยนแปลงของอัตราแลกเปลี่ยน
        exchange_rate_change = np.random.normal(0, exchange_rate_volatility)
        exchange_rate *= (1 + exchange_rate_change)
        
        # คำนวณผลตอบแทนรายวัน
        daily_return = ((daily_high_rate - daily_low_rate) * principal) / exchange_rate
        
        # คำนวณความเสี่ยงรายวัน
        daily_risk = np.abs(exchange_rate_change * principal)
        
        # สะสมผลตอบแทนและความเสี่ยง
        cumulative_returns.append(cumulative_returns[-1] + daily_return)
        cumulative_risks.append(cumulative_risks[-1] + daily_risk)
    
    return cumulative_returns, cumulative_risks

def analyze_carry_trade_metrics(currency_data, principal=100000, simulation_days=180):
    """
    วิเคราะห์เมตริกของกลยุทธ์ Carry Trade สำหรับคู่สกุลเงินต่างๆ

    Args:
    - currency_data (dict): ข้อมูลสกุลเงินและอัตราดอกเบี้ย format: {'CUR': interest_rate}
    - principal (float): เงินต้น
    - simulation_days (int): จำนวนวันในการจำลอง

    Returns:
    - dict: ผลการวิเคราะห์คู่สกุลเงินทั้งหมด
    """
    best_pairs = identify_best_carry_trades(currency_data)
    results = {}
    
    for pair_data in best_pairs[:5]:  # วิเคราะห์เฉพาะ 5 คู่สกุลเงินที่ดีที่สุด
        pair = pair_data['pair']
        returns, risks = simulate_carry_trade(
            pair_data['high_currency'],
            pair_data['low_currency'],
            pair_data['high_rate'],
            pair_data['low_rate'],
            principal,
            simulation_days
        )
        
        # คำนวณอัตราส่วนผลตอบแทนต่อความเสี่ยง (Sharpe ratio)
        final_return = returns[-1]
        final_risk = risks[-1] if risks[-1] > 0 else 1  # ป้องกันการหารด้วย 0
        sharpe_ratio = final_return / final_risk
        
        results[pair] = {
            'final_return': final_return,
            'final_risk': final_risk,
            'sharpe_ratio': sharpe_ratio,
            'returns': returns,
            'risks': risks
        }
    
    return results

def plot_return_and_risk(high_interest_rates, low_interest_rates, principal):
    """
    แสดงกราฟผลตอบแทนและความเสี่ยงจากกลยุทธ์ Carry Trade

    Args:
    - high_interest_rates (list): รายการอัตราดอกเบี้ยสูง
    - low_interest_rates (list): รายการอัตราดอกเบี้ยต่ำ
    - principal (float): เงินต้น
    """
    # Set font to support Thai characters
    plt.rcParams['font.family'] = 'Tahoma'

    returns = [calculate_carry_trade_return(high, low, principal) for high, low in zip(high_interest_rates, low_interest_rates)]
    risks = [calculate_risk(high, low) for high, low in zip(high_interest_rates, low_interest_rates)]

    plt.figure(figsize=(10, 6))
    plt.plot(returns, label='ผลตอบแทน')
    plt.plot(risks, label='ความเสี่ยง')
    plt.xlabel('ลำดับข้อมูล') # Changed label for clarity as x-axis is just index
    plt.ylabel('ค่า')
    plt.title('ผลตอบแทนและความเสี่ยงจากกลยุทธ์ Carry Trade')
    plt.legend()
    plt.grid(True) # Add grid for better readability
    plt.show()

def plot_carry_trade_simulation(metrics, title="ผลการจำลอง Carry Trade"):
    """
    แสดงกราฟผลการจำลองกลยุทธ์ Carry Trade

    Args:
    - metrics (dict): ผลการวิเคราะห์จากฟังก์ชัน analyze_carry_trade_metrics
    - title (str): ชื่อกราฟ
    """
    plt.figure(figsize=(12, 8))
    
    for pair, data in metrics.items():
        plt.plot(data['returns'], label=f"{pair} (Sharpe: {data['sharpe_ratio']:.2f})")
    
    plt.xlabel('จำนวนวัน')
    plt.ylabel('ผลตอบแทนสะสม')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_risk_return_scatter(metrics):
    """
    แสดงกราฟกระจายความสัมพันธ์ระหว่างผลตอบแทนและความเสี่ยง

    Args:
    - metrics (dict): ผลการวิเคราะห์จากฟังก์ชัน analyze_carry_trade_metrics
    """
    plt.figure(figsize=(10, 8))
    
    returns = []
    risks = []
    labels = []
    
    for pair, data in metrics.items():
        returns.append(data['final_return'])
        risks.append(data['final_risk'])
        labels.append(pair)
    
    plt.scatter(risks, returns, s=100)
    
    # เพิ่มป้ายกำกับให้กับแต่ละจุด
    for i, label in enumerate(labels):
        plt.annotate(label, (risks[i], returns[i]), textcoords="offset points", 
                     xytext=(0, 10), ha='center')
    
    plt.xlabel('ความเสี่ยง')
    plt.ylabel('ผลตอบแทน')
    plt.title('ความสัมพันธ์ระหว่างความเสี่ยงและผลตอบแทนของ Carry Trade')
    plt.grid(True)
    plt.show()

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    # ตัวอย่างข้อมูลอัตราดอกเบี้ยของสกุลเงินต่างๆ (ณ วันที่ 8 เมษายน 2025 - ตัวอย่าง)
    currency_interest_rates = {
        'AUD': 0.04,    # ออสเตรเลีย 4.00%
        'NZD': 0.035,   # นิวซีแลนด์ 3.50%
        'TRY': 0.08,    # ตุรกี 8.00%
        'JPY': -0.001,  # ญี่ปุ่น -0.10%
        'EUR': 0.001,   # ยูโร 0.10%
        'CHF': 0.002,   # สวิตเซอร์แลนด์ 0.20%
        'USD': 0.05     # สหรัฐอเมริกา 5.00%
    }
    
    principal = 100000  # 100,000 หน่วย
    
    # ระบุคู่สกุลเงินที่เหมาะสมที่สุดสำหรับ Carry Trade
    best_pairs = identify_best_carry_trades(currency_interest_rates)
    print("\nคู่สกุลเงินที่เหมาะสมที่สุดสำหรับ Carry Trade:")
    for i, pair in enumerate(best_pairs[:5]):  # แสดงเฉพาะ 5 คู่แรก
        print(f"{i+1}. {pair['pair']}: ส่วนต่างอัตราดอกเบี้ย {pair['differential']*100:.2f}% ({pair['high_currency']}: {pair['high_rate']*100:.2f}%, {pair['low_currency']}: {pair['low_rate']*100:.2f}%)")
    
    # วิเคราะห์และจำลองผลการทำ Carry Trade
    print("\nกำลังจำลองผลการทำ Carry Trade สำหรับคู่สกุลเงินที่ดีที่สุด...")
    metrics = analyze_carry_trade_metrics(currency_interest_rates, principal, simulation_days=180)
    
    # แสดงผลการวิเคราะห์
    print("\nผลการวิเคราะห์ Carry Trade สำหรับระยะเวลา 180 วัน:")
    for pair, data in metrics.items():
        print(f"{pair}: ผลตอบแทน {data['final_return']:.2f}, ความเสี่ยง {data['final_risk']:.2f}, Sharpe Ratio {data['sharpe_ratio']:.2f}")
    
    # แสดงกราฟผลการจำลอง
    plot_carry_trade_simulation(metrics)
    
    # แสดงกราฟความสัมพันธ์ระหว่างความเสี่ยงและผลตอบแทน
    plot_risk_return_scatter(metrics)
    
    # ตัวอย่างการใช้งานแบบเดิม
    high_interest_rates = [0.04, 0.05, 0.06]  # 4.00%, 5.00%, 6.00%
    low_interest_rates = [-0.001, 0.001, 0.002]  # -0.10%, 0.10%, 0.20%
    
    print("\nตัวอย่างการคำนวณแบบเดิม:")
    returns = [calculate_carry_trade_return(high, low, principal) for high, low in zip(high_interest_rates, low_interest_rates)]
    risks = [calculate_risk(high, low) for high, low in zip(high_interest_rates, low_interest_rates)]
    print(f"ผลตอบแทนจากกลยุทธ์ Carry Trade: {returns}")
    print(f"ความเสี่ยงจากกลยุทธ์ Carry Trade: {risks}")
    plot_return_and_risk(high_interest_rates, low_interest_rates, principal)