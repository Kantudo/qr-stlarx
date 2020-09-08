#!/bin/sh
GREEN='\033[0;32m'
CYAN='\033[1;36m'
NOCOLOR='\033[0m'

show_spinner(){
  local -r pid="${1}"
  local -r delay='0.2'
  local spinstr='\|/-'
  local temp
  while ps a | awk '{print $1}' | grep -q "${pid}"; do
    temp="${spinstr#?}"
    printf " [%c]  " "${spinstr}"
    spinstr=${temp}${spinstr%"${temp}"}
    sleep "${delay}"
    printf "\b\b\b\b\b\b"
  done
  printf "    \b\b\b\b"
}

clean(){

  for dir in "${Dirs2Clean[@]}"; do
    rm -rf $dir &
    printf "\nRemoving $dir "
    show_spinner "$!"
  done
}

mkdirs() {
  for dir in "${Dirs2Make[@]}"; do
    mkdir -p $dir &
    printf "\nMaking dir $dir "
    show_spinner "$!"
  done
}

printf "${CYAN}Cleaning dirs${NOCOLOR}"

declare -a Dirs2Clean=("./qr_stlarx/*/__pycache__" "./qr_stlarx/static/*/" "./qr_stlarx/independent/pdf_archive/" "./qr_stlarx/independent/cachedqr")

clean $Dirs2Clean

printf "\n${CYAN}Creating dirs${NOCOLOR}"

declare -a Dirs2Make=("./qr_stlarx/independent/cachedqr" "./qr_stlarx/independent/pdf_archive" )

mkdirs $Dirs2Make

echo -e "\n${GREEN}Done${NOCOLOR}"
#django-admin.py startproject qr_stlarx

