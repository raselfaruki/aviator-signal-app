import random
import numpy as np

def generate_multiplier():
    return round(random.expovariate(1 / 2), 2)

def analyze_signal(data):
    if len(data) < 5:
        return "🔄 পর্যাপ্ত ডেটা নেই"
    avg = np.mean(data[-5:])
    if avg > 2.0:
        return "📈 হাই স্ট্রীক"
    elif avg < 1.5:
        return "📉 লো স্ট্রীক"
    else:
        return "🔄 স্পষ্ট ট্রেন্ড নেই"
