# EmilMind_infra
## Подключение через бастион хост


Адреса машин:
- bastion_IP = 178.154.205.192 
- someinternalhost_IP = 10.128.0.21


Подключение к машине someinternalhost в одну комманду можно выполнить по шаблону:
- ssh -J appuser@bastion_ip appuser@privat_someinternalhost_ip
- ssh -J appuser@178.154.205.192 appuser@10.128.0.21