#!/usr/bin/env python

"""
 * phpinfo-files-leaks
 * phpinfo-files-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""


class Data:
    blog = 'https://blogs.cappriciosec.com/blog/178/phpinfo-files-leaks'
    api = 'https://api.cappriciosec.com/Telegram/cappriciosecbot.php'
    config_path = '~/.config/cappriciosec-tools/cappriciosec.yaml'
    payloadurl = 'https://raw.githubusercontent.com/Cappricio-Securities/PayloadAllTheThings/main/phpinfo-files-leaks.txt'
    bugname = "PHPinfo Page - Leaking"

    rheaders = {
        "Tool-Name": "phpinfo-files-leaks",
        "Developed-by": "cappriciosec.com",
        "Contact-us": "contact@cappriciosec.com"
    }


class Colors:
    RED = '\x1b[31;1m'
    BLUE = '\x1b[34;1m'
    GREEN = '\x1b[32;1m'
    RESET = '\x1b[0m'
    MAGENTA = '\x1b[35;1m'
