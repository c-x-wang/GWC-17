// flashing 2 red and 1 blue in middle 
for (int i = 0; i < 16; i++) {
  digitalWrite(11, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(7, HIGH);
  delay(437.5);
  digitalWrite(11, LOW);
  digitalWrite(9, LOW);
  digitalWrite(7, LOW);
  delay(437.5);
}
