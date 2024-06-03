
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/phpinfo-file-leaks-tool%20(1).png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/phpinfo-file-leaks)
![PyPI - Downloads](https://img.shields.io/pypi/dm/phpinfo-file-leaks)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/phpinfo-file-leaks/total)
<a href="https://github.com/Cappricio-Securities/phpinfo-file-leaks/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/phpinfo-file-leaks"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install phpinfo-file-leaks 
        ```
   - Run bellow command to check
     - `phpinfo-file-leaks -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          phpinfo-file-leaks --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          phpinfo-file-leaks -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          phpinfo-file-leaks -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          phpinfo-file-leaks -i urls.txt -o out.txt
        ```
   - Want to Learn about [`phpinfo-file-leaks`](https://blogs.cappriciosec.com/blog/178/phpinfo-file-leaks)? Then Type Below command
      - ```bash
          phpinfo-file-leaks -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-06-03%20at%204.04.30%20PM.png)](https://asciinema.org/a/MXbtZcg3WCtJ5wxVVu2BSUbrt)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                                                             v1.0
           __          _       ____            _____ __          __           __
    ____  / /_  ____  (_)___  / __/___        / __(_) /__       / /__  ____ _/ /_______
   / __ \/ __ \/ __ \/ / __ \/ /_/ __ \______/ /_/ / / _ \_____/ / _ \/ __ `/ //_/ ___/
  / /_/ / / / / /_/ / / / / / __/ /_/ /_____/ __/ / /  __/____/ /  __/ /_/ / ,< (__  )
 / .___/_/ /_/ .___/_/_/ /_/_/  \____/     /_/ /_/_/\___/    /_/\___/\__,_/_/|_/____/
/_/         /_/

                                     Developed By https://cappriciosec.com

phpinfo-file-leaks : Bug scanner for WebPentesters and Bugbounty Hunters 

$ phpinfo-file-leaks [option]

Usage: phpinfo-file-leaks [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | phpinfo-file-leaks -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | phpinfo-file-leaks -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | phpinfo-file-leaks -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | phpinfo-file-leaks --chatid yourid |
| `-b` | `--blog` | To Read about phpinfo-file-leaks Bug | phpinfo-file-leaks -b |
| `-h` | `--help` | Help Menu | phpinfo-file-leaks -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
