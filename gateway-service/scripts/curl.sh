# curl 'https://auto.ru/-/ajax/desktop-search/getRichVinReport/' \
#   -H 'content-type: application/json' \
#   -H 'cookie: _csrf_token=7caab4b74db0b923f6cbe36f33266757920e418d11447c0c; spravka=dD0xNzI5MTg3NzIxO2k9ODkuMjA3LjIyMS4xMDI7RD03QUIzMUMzNTIxNjIzOEFGRDU4NzQzQTU4MkIwQzEyOTZCMEJCQzQ5QzlGNzM4MDMxNjJEMTgzQTY3RDBGNzRGRjQwQTVFMjcxMzk2MEQyQTc2REVCM0IxNEI4REUwRTUxODIzM0ZEREE1NjAwQkE2OEJGQTQ1Q0YzRDA4MDVFRDI2MDUzRDJCQTcwMUQ5QTdFNkFFRUEyRDt1PTE3MjkxODc3MjEyODUyNzgxNTg7aD1jMmRjZDcxYjViMTQzNmM4YzU5YzE1ZjAwYTllNWEzYw==' \
#   -H 'x-csrf-token: 7caab4b74db0b923f6cbe36f33266757920e418d11447c0c' \
#   --data-raw '{"offerID":"1125106753-40922ec8","pow":{"hash":"00000192ab06594c1070da69b031a515","timestamp":1729446172829,"payload":"1125106753-40922ec8"}}'


# curl 'https://auto.ru/cars/used/sale/ford/mustang/1125399844-18893495/' \
#   -H 'cookie: _csrf_token=7caab4b74db0b923f6cbe36f33266757920e418d11447c0c'

# curl 'https://auto.ru/cars/used/sale/audi/q5/1125106753-40922ec8/' \
#   -H 'cookie: _csrf_token=7caab4b74db0b923f6cbe36f33266757920e418d11447c0c'


curl 'https://auto.ru/cars/used/sale/audi/q5/1125106753-40922ec8/' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9,ru;q=0.8,ru-RU;q=0.7,bg;q=0.6' \
  -H 'cookie: suid=eec274a9dfded979365b3aca4ac2f40e.22dea761db8c4ae6d55e12b0d7640844; _csrf_token=7caab4b74db0b923f6cbe36f33266757920e418d11447c0c; yandexuid=7748754001716060082; fp=d2e5910128173b57a29d3c36613db999%7C1729073066053; los=1; bltsr=1; coockoos=1; from=direct; i=hT/H9UjZvtOD2GsMVakXrcUiq3zorSwlIp7wjpf/c7mslPiZgdx0/O8ito7ciNnmBrPIuEGYueiQbGXJXwlbFTNQllE=; autoruuid=g67150dce2i4149e04b49oq5q3ccsptu.6956040c0477bf5fa5ef73cf8347225a; autoru_sso_blocked=1; Session_id=3:1729950477.5.0.1729513225739:kfDaJQ:145a.1.2:1|2005754463.0.2.3:1729513225|61:10026918.551760.TZfuxBM7vKQrWhX1iDscF-eSu2g; sessar=1.1195.CiCdylUbU7_hEEO6b2XyBOnrz_V1SHidJFyTOPR2t3xrDQ.BIy5N--DvAL0fYuLnkf85slOH2P9hccvsnEc2hv0u34; yandex_login=simulative-yd; ys=udn.cDpzaW11bGF0aXZlLXlk#c_chck.4039047141; L=aC5VWVdRCQ1+bAFOXUV3VFFCcEQCAV4AQBgrBR4LLAIxNxw/AA==.1729513225.15926.348866.cd369efc413d4b9915929bc673e1e15f; mda2_beacon=1729950477918; autoru_sso_redirect_blocked=1; crookie=A+nHbQnSa+nACXvPZZPYRKN7wZabtH1F7/qljbM6fEmXYK3eRn4I01zF0d5VC8q0+VAsgAd2DFt2zmmHu7eqHfbjP0w=; cmtchd=MTcyOTk1MDQ3ODk3MQ==; autoru-visits-count=8; autoru-visits-session-unexpired=1; sso_status=sso.passport.yandex.ru:synchronized_no_beacon; yaPassportTryAutologin=1; autoru_sid=126517384%7C1729950479631.7776000.8tA2W_wzErisy9awCI5BHQ.7mEGMo7Zt_F84kesFYt7MDICF_sG7ZiWcWDgvDIHEDs; layout-config={"screen_height":1440,"screen_width":2560,"win_width":1649,"win_height":1279}; spravka=dD0xNzI5OTUxMDAzO2k9ODkuMjA3LjIyMS4xMDI7RD0xQzgyMEUyNTI0MTBEQkE3NTg4QUM2MDJDNDY1NTExMkU0NkY0NTMzOTBCREM1RTQ1RUFCNTlGNjY2OEY1NTdEMjM1NjQwNkRCOTZEQ0EwQUI5QTFEQ0M1NzQyMjYyMkQ4MjlDQ0M0MDY1QzEwMUYwMDZDMDRDMjk4NDhCQTQ5QUExNEJDNTUzOEEzMTY1QzY1MTVBQUJCNjt1PTE3Mjk5NTEwMDM4MzAwMTMxMDk7aD0wZDMzODU4MjZjM2M0MDhhODgyN2Y2YzhjYTJmZDAxNw==; _yasc=M3pYr3eEbv3LToV4114cf9Z5SielyM991YaYgg2Cl4JFSd6zmQckw7t1xT2QHJJpn53+nxmG30nV; count-visits=5; from_lifetime=1729951058470' \
  -H 'priority: u=0, i' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'