### Problemstillingen
Problemstillingen er at OptiLogic ikke vil micro-manage sine el enheder for at spare/tjene på strøm. Vi løser den ene halvdel af problemet, som består af indsamling af tarif, vejrdata og elpriser. 

### Afgrænsning
- Vi vil have en mySQL database til at køre, som kan få data, og man skal kunne få data fra den.
- Vi vil opsætte en esp32 som kan hente data og sende det videre.
- En form for interface

### Afgrænsning_2

- SQL database for strømpris, tarif og vejrdata
- ESP32 der kan hente data fra database og agere baseret på denne
- NodeRed der facilitere kommunikationen og interface
- TLS kryptering på MQTT kommunikation
