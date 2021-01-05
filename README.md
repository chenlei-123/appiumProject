# appiumProject
- adb logcat |grep -i displayed
- adb shell dumpsys activity top 查看栈顶activity信息
- aapt dump badging name.apk |grep launchable-activity		只有apk的情况下，查看启动activity
- adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S		启动activity