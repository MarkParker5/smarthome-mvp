#include "merlin.h"

Merlin::Merlin() {}

Merlin::Merlin(urdi id, func on_receive) {

    for(int i = 0; i < urdi_length; i++) own_id[i] = id[i];
    callback = on_receive;

    radio = RF24(9, 10);
    radio.begin();
    radio.setPALevel(RF24_PA_HIGH);
    radio.setDataRate(RF24_2MBPS);
    radio.setChannel(0x60);
    radio.setPayloadSize(2);
    radio.setAutoAck(true);
    // radio.enableAckPayload();
    radio.openReadingPipe(1, own_id);
    radio.powerUp();
    radio.startListening();
}

bool Merlin::send(urdi receiver, byte f, byte x) {
    byte msg[2];
    msg[0] = f;
    msg[1] = x;

    radio.stopListening();
    radio.openWritingPipe(receiver);
    radio.write(msg, radio.getPayloadSize());
    radio.startListening();
}

void Merlin::tick() {
    byte msg[radio.getPayloadSize()];
    while(radio.available()) {
        radio.read(&msg, radio.getPayloadSize());
        byte f = msg[0];
        byte x = msg[1];
        callback(f, x);
    }
}
