#!/usr/bin/env python

"""
 * phpinfo-files-leaks
 * phpinfo-files-leaks Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */

"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
           __          _       ____            _____ __                __           __
    ____  / /_  ____  (_)___  / __/___        / __(_) /__  _____      / /__  ____ _/ /_______
   / __ \/ __ \/ __ \/ / __ \/ /_/ __ \______/ /_/ / / _ \/ ___/_____/ / _ \/ __ `/ //_/ ___/
  / /_/ / / / / /_/ / / / / / __/ /_/ /_____/ __/ / /  __(__  )_____/ /  __/ /_/ / ,< (__  )
 / .___/_/ /_/ .___/_/_/ /_/_/  \____/     /_/ /_/_/\___/____/     /_/\___/\__,_/_/|_/____/
/_/         /_/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mphpinfo-files-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mphpinfo-files-leaks\033[0m [option]

Usage: \033[92mphpinfo-files-leaks\033[0m [options]

Options:
  -u, --url     URL to scan                                phpinfo-files-leaks -u https://target.com
  -i, --input   <filename> Read input from txt             phpinfo-files-leaks -i target.txt
  -o, --output  <filename> Write output in txt file        phpinfo-files-leaks -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             phpinfo-files-leaks --chatid yourid
  -b, --blog    To Read about phpinfo-files-leaks Bug      phpinfo-files-leaks -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
           __          _       ____            _____ __                __           __
    ____  / /_  ____  (_)___  / __/___        / __(_) /__  _____      / /__  ____ _/ /_______
   / __ \/ __ \/ __ \/ / __ \/ /_/ __ \______/ /_/ / / _ \/ ___/_____/ / _ \/ __ `/ //_/ ___/
  / /_/ / / / / /_/ / / / / / __/ /_/ /_____/ __/ / /  __(__  )_____/ /  __/ /_/ / ,< (__  )
 / .___/_/ /_/ .___/_/_/ /_/_/  \____/     /_/ /_/_/\___/____/     /_/\___/\__,_/_/|_/____/
/_/         /_/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mphpinfo-files-leaks : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
