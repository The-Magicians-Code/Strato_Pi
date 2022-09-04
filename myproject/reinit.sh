#!/bin/bash
# Restart the web services with this script after making changes to the anything

# Colours
red="0;31"
yel="1;33"
grn="1;32"
bold=$(tput bold)
normal=$(tput sgr0)

if [[ $# -ne 0 ]] #Check if any args given
then
    if [[ $1 == "start" ]]
    then
        sudo systemctl restart myproject.service
        sudo systemctl restart nginx.service
        printf "\033[${yel}mWeb server restarted\n"
    elif [[ $1 == "stop" ]]
    then
        sudo systemctl stop myproject.service
        sudo systemctl stop nginx.service
        printf "\033[${yel}mWeb server stopped\n"
    else
        printf "Args:\n\033[${yel}m[*] \033[0m${bold}start${normal} - start server\n\033[${yel}m[*] \033[0m${bold}stop${normal} - stop server\n"
    fi
else
    printf "\033[${red}mNo args given\n"
fi


printf "\033[${grn}mDone!\n"
