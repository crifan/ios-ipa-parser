# ios-ipa-parser


* Update: `20250119`

## Repo

* Current
  * https://github.com/crifan/ios-ipa-parser
    * https://github.com/crifan/ios-ipa-parser.git
* Origin
  * https://github.com/jiania/ios-ipa-parser

## History

* 20250117
  * Update code to support Python 3.x
  * fix some bug: save binary file, etc.

## Example

test code:

```py
    testIpadFullPath = "/xxx/WhatsApp_v23.25.85.ipa"
    # print("testIpadFullPath=%s" % testIpadFullPath)
    parse = IpaParse(testIpadFullPath)

    ipaAllInfo = parse.all_info()
    print("ipaAllInfo=%s" % ipaAllInfo)
    # print(json.dumps(ipaAllInfo, default = lambda o: o.__dict__))
    print("app_name=%s" % parse.app_name())
    print("bundle_identifier=%s" % parse.bundle_identifier())
    print("target_os_version=%s" % parse.target_os_version())
    print("minimum_os_version=%s" % parse.minimum_os_version())
    print("icon_file_name=%s" % parse.icon_file_name())
    print("icon_file_path=%s" % parse.icon_file_path())
    # print("mv_icon_to=%s" % parse.mv_icon_to('test.png'))
```

output:

```
ipaAllInfo={'MinimumOSVersion': '13.0', 'NSAppTransportSecurity': {'NSAllowsArbitraryLoads': True}, 'NSFaceIDUsageDescription': '\u200eUse Face ID to authenticate on WhatsApp.', 'NSLocalNetworkUsageDescription': '\u200eThis will let you use WhatsApp to place and receive calls through devices that are on the same Wi-Fi or local access networks.', 'DTXcodeBuild': '15A240d', 'NSMicrophoneUsageDescription': '\u200eThis lets you make calls, send voice messages, and record videos with sound.', 'UISupportedDevices': ['iPhone10,1', 'iPhone10,4', 'iPhone12,8', 'iPhone8,1', 'iPhone8,4', 'iPhone9,1', 'iPhone9,3', 'iPod9,1'], 'DTAppStoreToolsBuild': '15C5065a', 'CFBundleName': 'WhatsApp', 'CFBundleSupportedPlatforms': ['iPhoneOS'], 'FBBuildNumber': '548039364', 'NSCalendarsUsageDescription': '\u200eThis lets you create events on your calendar.', 'CFBundleDisplayName': '\u200eWhatsApp', 'NSSpeechRecognitionUsageDescription': 'WhatsApp does on-device recognition for Voice Messages. In this mode, no voice data is sent to Apple despite this alert, which is unexpected. Select "Don\'t Allow" and report to WhatsApp.', 'UISupportedInterfaceOrientations~ipad': ['UIInterfaceOrientationPortrait', 'UIInterfaceOrientationLandscapeLeft', 'UIInterfaceOrientationLandscapeRight', 'UIInterfaceOrientationPortraitUpsideDown'], 'ITSDRMScheme': 'v2', 'DTPlatformBuild': '21A325', 'NSRemindersUsageDescription': '\u200eThis lets you set reminders to call your friends back.', 'CFBundleDocumentTypes': [{'CFBundleTypeName': 'WhatsApp Image', 'LSHandlerRank': 'Alternate', 'LSItemContentTypes': ['public.image'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}, {'CFBundleTypeName': 'WhatsApp Image Exclusive', 'LSHandlerRank': 'Owner', 'LSItemContentTypes': ['net.whatsapp.image'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}, {'CFBundleTypeName': 'WhatsApp Audio', 'LSHandlerRank': 'Alternate', 'LSItemContentTypes': ['public.mp3', 'public.mpeg-4-audio', 'public.aif-audio', 'public.aifc-audio', 'com.apple.coreaudio-format'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}, {'CFBundleTypeName': 'WhatsApp Audio Exclusive', 'LSHandlerRank': 'Owner', 'LSItemContentTypes': ['net.whatsapp.audio'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}, {'CFBundleTypeName': 'WhatsApp Movie', 'LSHandlerRank': 'Alternate', 'LSItemContentTypes': ['public.movie'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}, {'CFBundleTypeName': 'WhatsApp Movie Exclusive', 'LSHandlerRank': 'Owner', 'LSItemContentTypes': ['net.whatsapp.movie'], 'CFBundleTypeIconFiles': ['Icon', 'Icon@2x']}], 'CFBundleSignature': '????', 'DTXcode': '1500', 'DTSDKName': 'iphoneos17.0', 'CFBundleVersion': '548039364', 'UIDeviceFamily': [1], 'UIBackgroundModes': ['bluetooth-peripheral', 'bluetooth-central', 'audio', 'fetch', 'location', 'processing', 'remote-notification', 'voip'], 'NSBonjourServices': ['_logger._tcp', '_stellabus._tcp', '_wa-fpm-i2i-transfer._tcp'], 'CFBundleIcons': {'CFBundlePrimaryIcon': {'CFBundleIconName': 'AppIcon', 'CFBundleIconFiles': ['AppIcon60x60']}}, 'NSLocationUsageDescription': '\u200eThis lets you send your current location or nearby places in chats.', 'DTPlatformName': 'iphoneos', 'CFBundleDevelopmentRegion': 'en', 'NSLocationWhenInUseUsageDescription': '\u200eThis lets you send your current location or nearby places in chats.', 'NSLocationAlwaysAndWhenInUseUsageDescription': "\u200eIf you always allow access to your location, you can choose to share your live location, and it will update even when you're not using the app. If you only allow access while using the app, you can only send your current location or a nearby place.", 'CFBundleURLTypes': [{'CFBundleURLSchemes': ['upi', 'whatsapp', 'whatsapp-consumer', 'fb306069495113'], 'CFBundleTypeRole': 'Editor', 'CFBundleURLName': 'net.whatsapp.WhatsApp'}], 'CFBundleIdentifier': 'net.whatsapp.WhatsApp', 'LSRequiresIPhoneOS': True, 'NSPhotoLibraryAddUsageDescription': '\u200eThis lets you save photos and videos to your library.', 'CFBundleExecutable': 'WhatsApp', 'NSPhotoLibraryUsageDescription': '\u200eThis lets you send photos and videos from your library and save the ones you capture.', 'ITSAppUsesNonExemptEncryption': False, 'BuildMachineOSBuild': '22G91', 'CFBundleIcons~ipad': {'CFBundlePrimaryIcon': {'CFBundleIconName': 'AppIcon', 'CFBundleIconFiles': ['AppIcon60x60', 'AppIcon76x76']}}, 'CFBundlePackageType': 'APPL', 'PHPhotoLibraryPreventAutomaticLimitedAccessAlert': True, 'LSApplicationQueriesSchemes': ['here-route', 'here-location', 'googlegmail', 'ms-outlook', 'inbox-gmail', 'comgooglemaps', 'yandexmaps', 'waze', 'googlechrome', 'googlechromes', 'googlechrome-x-callback', 'yandexnavi', 'comwainmaps', 'instagram', 'fb', 'whatsapp-smb', 'facebook-stories-list', 'novi', 'tez', 'phonepe', 'paytmmp', 'bhim', 'rblmobank'], 'NSContactsUsageDescription': "\u200eUpload your contacts to WhatsApp's servers to help you quickly get in touch with your friends and help us provide a better experience.", 'UTExportedTypeDeclarations': [{'UTTypeTagSpecification': {'public.mime-type': 'image/*', 'public.filename-extension': 'wai'}, 'UTTypeDescription': 'WhatsApp Image Exclusive', 'UTTypeIdentifier': 'net.whatsapp.image'}, {'UTTypeTagSpecification': {'public.mime-type': 'audio/*', 'public.filename-extension': 'waa'}, 'UTTypeDescription': 'WhatsApp Audio Exclusive', 'UTTypeIdentifier': 'net.whatsapp.audio'}, {'UTTypeTagSpecification': {'public.mime-type': 'video/*', 'public.filename-extension': 'wam'}, 'UTTypeDescription': 'WhatsApp Movie Exclusive', 'UTTypeIdentifier': 'net.whatsapp.movie'}], 'DTCompiler': 'com.apple.compilers.llvm.clang.1_0', 'UIRequiredDeviceCapabilities': {'telephony': True, 'arm64': True}, 'NSLocationAlwaysUsageDescription': "\u200eIf you always allow access to your location, you can choose to share your live location, and it will update even when you're not using the app. This also lets you send your current location or a nearby place.", 'NSSiriUsageDescription': '\u200eThis lets you use Siri to quickly send and read messages and make calls.', 'NSUserActivityTypes': ['INStartCallIntent', 'INSendMessageIntent', 'INSearchForMessagesIntent', 'INStartAudioCallIntent', 'INStartVideoCallIntent'], 'NSCameraUsageDescription': '\u200eThis lets you make video calls, take photos, and record videos.', 'NSBluetoothAlwaysUsageDescription': 'This lets you connect to supported Bluetooth devices', 'UISupportedInterfaceOrientations': ['UIInterfaceOrientationPortrait', 'UIInterfaceOrientationLandscapeLeft', 'UIInterfaceOrientationLandscapeRight'], 'AVUseSoftwareDecoderForAssetImageGenerator': True, 'CFBundleInfoDictionaryVersion': '6.0', 'UIAppFonts': ['WhatsAppPaymentsIcons.ttf', 'Optimistic_DisplayVF_A_Wght.ttf'], 'BGTaskSchedulerPermittedIdentifiers': ['com.whatsapp.background_fetch', 'com.whatsapp.message_search_engine_indexing', 'com.whatsapp.icloud_backup', 'com.whatsapp.db_maintenance', 'com.whatsapp.db_migration'], 'NSLocationTemporaryUsageDescriptionDictionary': {'ShareLiveLocation': '\u200eYour precise live location will be shared in the chat.', 'SendLiveLocation': '\u200eYour precise live location will be shared in the chat.', 'SendStaticLocation': '\u200eYour precise location will be sent to the chat.', 'MapButton': "\u200eYou'll be able to see your precise location and share it to the chat"}, 'DTSDKBuild': '21A325', 'UIStatusBarTintParameters': {'UINavigationBar': {'Style': 'UIBarStyleDefault', 'Translucent': False}}, 'UILaunchStoryboardName': 'LaunchScreen', 'NSBluetoothPeripheralUsageDescription': 'This lets you connect to supported Bluetooth devices', 'DTPlatformVersion': '17.0', 'LSSupportsOpeningDocumentsInPlace': 'NO', 'CFBundleShortVersionString': '23.25.85', 'UIRequiresPersistentWiFi': True}
app_name=WhatsApp
bundle_identifier=net.whatsapp.WhatsApp
target_os_version=17.0
minimum_os_version=13.0
icon_file_name=AppIcon60x60
icon_file_path=Payload/WhatsApp.app/AppIcon60x60@2x.png
```

---

A iOS IPA information parser, can get name, bundle id, logo and almost all the information. 

一个iOS IPA包信息提取工具，包括几乎所有的信息。
