# SCKP-auto-test-client-app
E2E test for client app, i.e., family app

## Readme file:  

Enable Android Emulator to test Iroodoki Mobile Application

### 1. Download Android Studio
### 2. Download Appium GUI server
### 3. Download Appium Inspector
### 4. Download Pycharm

===================

## 1. Download Android Studio

### 1.1 Download the latest Android Studio by URL: https://developer.android.com/studio
### 1.2 Scroll down and Download Commandline tools by `Command line tools only`
### 1.3 Download Sdkmanager follow this doc: https://developer.android.com/tools/sdkmanager
### 1.4 Install the compatible device in “Device Manager”, after install all the package, run the device.
### 1.5 Run `adb devices` to make sure there’s a device is running.


## 2. Download Appium GUI server

### 2.1 Download the compatible file and extract the file from URL: https://github.com/appium/appium-desktop/releases 
### 2.2. Open the Appium GUI Server and follow the instruction:
- In Advanced, make sure to check “Relaxed Security”
- In Advanced, make sure to check “Allow CORS” to run with Emulator device
- In Simple → Host: 127.0.0.1  → Port: 4723
- App Configuration → Environment Variable

Eg. ANDROID_HOME: C:\Users\msi\AppData\Local\Android\Sdk 
    JAVA_HOME: C:\Program Files\Java\jdk-22

- Click on “startServer”

## 3. Download Appium Inspector

### 3.1 Download the compatible file and extract the file from URL: https://github.com/appium/appium-inspector/releases
### 3.2 Open the Appium Inspector and follow below instruction:
- Remote Host: Default (127.0.0.1)
- Remote Port: Default (4723)
- Remote Path: /wd/hub
- No check at “SSL”
- Check the box for “Allow Unauthorized Certificates” in Advanced Setting
- Connect the Emulator’s info device with the sample below:
Eg. JSON Presentation

```
{
  "platformName": "android",
  "appium:platformVersion": "7",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "Pixel 2 API 25",
  "appium:appPackage": "com.irodoki.sckp_client_app.stg",
  "appium:appActivity": "com.irodoki.sckp_client_app.MainActivity"
}
```
- Start the session

## 4. Download Pycharm

### 4.1 Download **PyCharm Community Edition** on URL: [https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download/?section=windows)
### 4.2 Open PyCharm and open terminal to download flutter by URL: https://docs.flutter.dev/get-started/install/windows/mobile?tab=vscode
- Run `flutter doctor` to make sure it’s fully download all the requirement tools
- Install packages below and apply:  → Setting → Search: Python Interpreter
    - Appium-Python-Client
    - Urillib3
    - pip
    - setuptools
    - selenium
- Make sure you are running Android Emulator in the background and run this cmd:
    - `flutter build appbundle --target=lib/main_stg.dart --flavor staging` for Stage env
    - `flutter run --target=lib/main_stg.dart --flavor staging`  for Stage env (run: to run the mobile app in Emulator with Flutter)
    - `flutter build appbundle --target=lib/main_prod.dart --flavor production`  for Production env
    - `flutter build apk --target=lib/main_prod.dart --flavor production` for Production env

For more info, read Readme instruction in: https://github.com/kirirom-digital/SCKP-client-app?tab=readme-ov-file#build-apk 

- Create a new Folder in a Project and name it as “Basic”
    - In this folder, create a python package
    - In this folder, create a python file and start your very first “Test Case” there
    - Sample: https://appium.io/docs/en/2.1/quickstart/test-py/

# Notes

When you run reg_mobile_3.py, please execute following control beforehand.
Because this test case requres a picture, we need to prepare it and import it to virtual Android device:

1. launch Android Studio on your PC
2. launch virtual Android device
3. launch terminal on  your PC
4. run command on the terminal: `adb push path/to/picture/on/your/pc /sdcard/Pictures`
    1. For example: `adb push C:\Users\hs_se\PycharmProjects\SCKP-auto-test-client-app\resource\kid_photo_2024_01_13_001.png /sdcard/Pictures`

You can double-check if the picture is actually imported to the virtual Android device by executing this command on the terminal: `adb shell ls sdcard/Pictures`

* reference: https://stackoverflow.com/questions/5151744/upload-picture-to-emulator-gallery
* reference: https://kiriromdigital.slack.com/archives/C06RQ0ZTU6N/p1717389076885469

<img src="https://github.com/kirirom-digital/SCKP-auto-test-client-app/assets/5344774/545204da-c7de-44f6-9928-deb0ae855fab" width="30%" height="30%">

# Troubleshooting

You might face following error messages if you execute `flutter run --target=lib/main_stg.dart --flavor staging` command:

```
E/AndroidRuntime(26019): FATAL EXCEPTION: main
E/AndroidRuntime(26019): Process: com.irodoki.sckp_client_app.stg, PID: 26019
E/AndroidRuntime(26019): java.lang.NoSuchMethodError: No interface method addWindowLayoutInfoListener(Landroid/app/Activity;Lj$/util/function/Consumer;)V in class Landroidx/window/extensions/layout/WindowLayoutComponent; or its super classes (declaration of 'androidx.window.extensions.layout.WindowLayoutComponent' appears in /system_ext/framework/androidx.window.extensions.jar)
E/AndroidRuntime(26019):        at androidx.window.layout.WindowInfoTrackerImpl$windowLayoutInfo$1.invokeSuspend(WindowInfoTrackerImpl.kt:52)
E/AndroidRuntime(26019):        at androidx.window.layout.WindowInfoTrackerImpl$windowLayoutInfo$1.invoke(Unknown Source:8)
E/AndroidRuntime(26019):        at androidx.window.layout.WindowInfoTrackerImpl$windowLayoutInfo$1.invoke(Unknown Source:4)
E/AndroidRuntime(26019):        at kotlinx.coroutines.flow.SafeFlow.collectSafely(Builders.kt:61)
E/AndroidRuntime(26019):        at kotlinx.coroutines.flow.AbstractFlow.collect(Flow.kt:230)
E/AndroidRuntime(26019):        at androidx.window.java.layout.WindowInfoTrackerCallbackAdapter$addListener$1$1.invokeSuspend(WindowInfoTrackerCallbackAdapter.kt:96)
E/AndroidRuntime(26019):        at kotlin.coroutines.jvm.internal.BaseContinuationImpl.resumeWith(ContinuationImpl.kt:33)
E/AndroidRuntime(26019):        at kotlinx.coroutines.DispatchedTask.run(DispatchedTask.kt:106)
E/AndroidRuntime(26019):        at android.os.Handler.handleCallback(Handler.java:942)
E/AndroidRuntime(26019):        at android.os.Handler.dispatchMessage(Handler.java:99)
E/AndroidRuntime(26019):        at android.os.Looper.loopOnce(Looper.java:201)
E/AndroidRuntime(26019):        at android.os.Looper.loop(Looper.java:288)
E/AndroidRuntime(26019):        at android.app.ActivityThread.main(ActivityThread.java:7872)
E/AndroidRuntime(26019):        at java.lang.reflect.Method.invoke(Native Method)
E/AndroidRuntime(26019):        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:548)
E/AndroidRuntime(26019):        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:936)
E/AndroidRuntime(26019):        Suppressed: kotlinx.coroutines.DiagnosticCoroutineContextException: [StandaloneCoroutine{Cancelling}@f1f7546, android.os.HandlerExecutor@447307]
Error connecting to the service protocol: failed to connect to http://127.0.0.1:65328/43IM4I8fuZk=/
```

On this case, please add following lines into android/app/build.gradle file:

```
implementation 'androidx.window:window:1.0.0'
implementation 'androidx.window:window-java:1.0.0'
```

Finally, android/app/build.gradle should be like:

```
dependencies {
    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
    implementation 'androidx.window:window:1.0.0'
    implementation 'androidx.window:window-java:1.0.0'
    coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:1.2.2'
}
```

Then, please execute `flutter run --target=lib/main_stg.dart --flavor staging` command again.
