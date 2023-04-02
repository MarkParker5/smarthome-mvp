#include <merlin.h>

Merlin device;
bool is_on = false;

void setup() {
    urdi my_urdi = {0x01, 0x00, 0x00, 0x00, 0xff};
    device = Merlin(my_urdi, &execute);
    pinMode(3, OUTPUT);
}

void loop() {
    device.tick();
}

void execute(byte f, byte x) {
    if (f == 1) {
        if (x < 2) {
            is_on = x;
            digitalWrite(3, is_on);
        } else if (x == 2) {
            is_on = !is_on;
            digitalWrite(3, is_on);
        }
    }
}