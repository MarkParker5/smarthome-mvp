#include <merlin.h>
#include <FastLED.h>

Merlin device;
bool is_on = false;

#define DATA_PIN 3
#define LED_TYPE NEOPIXEL 
#define NUM_LEDS 300

CRGB leds[NUM_LEDS];
int brightness = 200;

void setup() {
    urdi my_urdi = {0x02, 0x00, 0x00, 0x00, 0xff};
    device = Merlin(my_urdi, &execute);
    
    FastLED.addLeds<LED_TYPE, DATA_PIN>(leds, NUM_LEDS);         
    FastLED.setDither(false);
    FastLED.setCorrection(TypicalLEDStrip);
    FastLED.setBrightness(brightness);
    FastLED.setMaxPowerInVoltsAndMilliamps(5, 1000);
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
}

void loop() {
    device.tick();
}

void execute(byte f, byte x) {
    if (f == 1) {
        if (x < 2) {
            is_on = x;
        } else if (x == 2) {
            is_on = !is_on;
        }
        fill_solid(leds, NUM_LEDS, is_on ? CRGB::White : CRGB::Black);
    } else if (f == 2) {
        is_on = true;
        if (x == 1) {
            fill_solid(leds, NUM_LEDS, CRGB::Red);
        } else if (x == 2) {
            fill_solid(leds, NUM_LEDS, CRGB::Green);
        } else if (x == 3) {
            fill_solid(leds, NUM_LEDS, CRGB::Blue);
        }
    } else {
        return;
    }
    FastLED.show();
}