# Appium Android Calculator Automation

Automated mobile UI tests for Android calculator app using Appium and Python.

## 🎯 Overview
This project demonstrates mobile test automation using the Appium framework. It automates basic calculator operations on Android to validate functionality.

## 🛠️ Technologies
- **Appium** 3.1.1 - Mobile automation framework
- **Python** 3.14 - Test scripting
- **Android Emulator** (API 36) - Test environment
- [**OpenCalc**](https://f-droid.org/en/packages/com.darkempire78.opencalculator/) - F-Droid open-source calculator app

## 📋 Test Coverage
- ✅ Addition 
- ✅ Subtraction 
- ✅ Multiplication 
- ✅ Division 
- ✅ Result validation
- ✅ UI element interaction

## 🚀 Setup Instructions

### Prerequisites
- Python 3.x
- Node.js (for Appium)
- Android Studio with emulator
- Appium server (`npm install -g appium`)
- Appium UiAutomator2 driver (`appium driver install uiautomator2`)

### Installation

1. Clone repository:
```bash
git clone https://github.com/vndlgd/appium-android-automation.git
cd appium-android-automation
```

2. Create virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start Android emulator with OpenCalc installed

5. Start Appium server (separate terminal):
```bash
appium --allow-cors (flag necessary if using Appium Inspector via Browser)
```

6. Run test:
```bash
python3 tests/test_calc.py
```

## 📱 App Details
- **Package:** `com.darkempire78.opencalculator`
- **Activity:** `com.darkempire78.opencalculator.activities.MainActivity`
- **Source:** F-Droid (open-source)

## 📝 Notes
- Tests require active Appium server on `http://127.0.0.1:4723`
- Emulator must be running before test execution

## 📄 License
MIT License - Open source project for educational purposes
