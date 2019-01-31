int alarm = 2;
int sw200D = 4;

void setup()
{
  pinMode(sw200D, INPUT);
  pinMode(alarm, OUTPUT);
}

void loop()
{
  if(digitalRead(sw200D) == HIGH)
    digitalWrite(alarm, LOW);
  else
    digitalWrite(alarm, HIGH);
}

void setup (){
Serial.begin (9600);
        pinMode (A0, INPUT);
}

void loop (){
        Serial.println (analogRead (A0));
        delay (1000);
}

int pomiar = 0;
int odleglosc = 0;

void setup(){
Serial.begin(9600);
        pinMode(A0, INPUT);
}

void loop(){
    pomiar = analogRead (A0);
    odleglosc = ((67870 / (pomiar - 3)) - 40);
    if (odleglosc > 800){
        Serial.println("Obiekt zbyt daleko czujnika!");
    }
    else{
        Serial.print (odleglosc);
        Serial.println(" mm");
    }
    delay (1000);
}
