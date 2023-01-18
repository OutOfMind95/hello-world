(4 byte) Int -> incorpora tutti i numeri in 32 bit, circa 4 milioni tra positivi e negativi

con la qualifica "unsigned" considero solo i numeri positivi, al costo dei negativi

(1 byte) char -> incorpora solo un carattere (1 bit)

(4 byte) float -> numeri reali, quindi anche decimali (32 bit consumabili) - ha un problema di precisione per i numeri lunghi

(8 byte) double -> numeri reali con 64 bit consumabili

void -> è un tipo, non un tipo di dato, non ritorna un valore. Come un placeholder vuoto, nessun parametro.

(1 byte) bool -> Boolean value, true or false, 1 or 0 (solitamente utilizzato per loop e condizioni)

Logical operator -> && risulta true solo se entrambi gli operandi sono true
                 -> || risulta true se almeno uno dei due operandi è true
                 -> ! inverte il valore di un operando, da true a false e viceversa
Relational operator < > <= >= -> stesse regole aritmetiche
                    == uguale != non uguale | = è operatore di assegnazione

string -> può contenere una sequenza di caratteri, paragrafi brevi o lunghi

per creare una variabile anzitutto dichiari il data type (int, char, float...) dopo di che gli dai un nome
puoi anche creare più variabili dello stesso tipo semplicemente -> int altezza, larghezza (stesso data type, separato da virgola)


librerie C - <stdio.h> - <cs50.h> - <math.h>

int number // declaration  char letter  || int number = 17 // initialization
numer = 17 // assignment  letter = 'A' (con singolo ')

espressioni condizionali (branch) - if (boolean expression) { all interno va il codice che verrà eseguito se true }
else { nel caso in cui la condizione if è false, parte questa parte di codice }
else if { aggiunge una condizione che deve essere true per far partire il codice }

switch () - permette di cambiare il risultato di un codice a seconda dei 'case', uso break per bloccare il codice una volta dato un input
se non uso break; il codice continua a funzionare top to bottom
?: un modo più semplice ed elegante di scrivere if () {} else {} -> es. int x = (expr) ? 5 : 6 | ? = if : = else

LOOPS - for - do ... while - while

while (true) - ripeterà il codice sempre finché la condizione è true
while (boolean expression) - ""
do { } while (boolean expression) - parte il codice e poi valuta se continuare il loop con while (true or false)
for (int i; i < 10;i++ ) {code} - ripete il codice finche la seconda espressione tra parentesi risulta true
for (start; boolean expression; increment/decrement)
il contatore di i verrà incrementato di 1 (++), il codice smetterà di ripetersi finché i < 10

Terminale
ls -> lista tutti i file e le cartelle nella mia posizione attuale
cd -> change directory, cambia cartella
pwd -> mi dice dove mi trovo attualmente
mkdir -> make directory, crea una cartella
cp -> copy and paste (-r per copiare tutto il contenuto della cartella) - cp "cosa copiare" "destinazione"
rm -> rimuove un file | -r per eliminare tutta la cartella | -f per eliminare senza richiedere conferma (force)
mv -> rinomina il file "file" "nuovo nome"
chmod
ln
touch
rmdir
man
diff
sudo
clear
telnet


Array -> permette di contenere tante variabili dello stesso tipo, salvando memoria
NUL -> \0 -> per riconoscere la fine di una string