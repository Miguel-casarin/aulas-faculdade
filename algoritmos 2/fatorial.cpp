#include <iostream>

using namespace std;

int fat(int num) {
    if (num == 0) {
        return 1;
    } else {
        return num * fat(num - 1);
    }
}

int main() {
    int entrada;
    cout << "Entre com seu numero: ";
    cin >> entrada;
    int fatorial = fat(entrada);
    cout << "Fatorial e: " << fatorial << endl;
    return 0;
}
