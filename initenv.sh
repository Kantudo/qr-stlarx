#!/bin/sh
tput civis


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

create_venv(){
  if test -d ./env; then
    rm -rf ./env
    virtualenv env
  else
    virtualenv env
fi
}

install_pipdeps(){

  for dep in "${pipdeps[@]}"; do
    pip install $dep &>/dev/null &
    printf "\nInstalling $dep "
    show_spinner "$!"
  done
}

create_venv &>/dev/null &
printf "Creating virtual env "

show_spinner "$!"

source ./env/bin/activate
printf "\nActivated virtual env"

declare -a pipdeps=("Django" "uwsgi" "libsass" "django-compressor" "django-sass-processor" "django-bootstrap4" "django-bootstrap-modal-forms" "django-widget-tweaks" "django-recaptcha")

printf "\n${CYAN}Installing pip dependencies${NOCOLOR}"
install_pipdeps $pipdeps

echo -e "\n${GREEN}Done"
#django-admin.py startproject qr_stlarx
tput cnorm
