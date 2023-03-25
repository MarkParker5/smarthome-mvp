#ifndef Merlin_h
#define Merlin_h

#include <RF24.h>

#define urdi_length 5
typedef byte urdi[urdi_length];
typedef void (*func)(byte, byte);

class Merlin {
  private:
    urdi own_id;
    func callback;
    RF24 radio;

  public:
    Merlin();
    Merlin(urdi id, func on_receive);
    bool send(urdi receiver, byte f, byte x);
    void tick();
};

#endif
