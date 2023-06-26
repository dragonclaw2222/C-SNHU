#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
float intInv, intDepo, intYear, months, years;

float intTotal, intAmt, yearInt;


cout << "********************************\n";
cout << "********** Data Input **********\n";
cout << "Initial Investment Amount: \n";
cout << "Monthly Deposit: \n";
cout << "Annual Interest: \n";
cout << "Number of years: \n";

system("PAUSE");

cout << "********************************\n";
cout << "********** Data Input **********\n";
cout << "Initial Investment Amount: $";
cin >> intInv;
cout << "Monthly Deposit: $";
cin >> intDepo;
cout << "Annual Interest: %";
cin >> intYear;
cout << "Number of years: ";
cin >> years;
months = years * 12;

system("PAUSE");


intTotal = intInv;


cout << "\nBalance and Interest Without Additional Monthly Deposits\n";
cout << "==============================================================\n";
cout << "Year\t\tYear End Balance\tYear End Earned Interest\n";
cout << "--------------------------------------------------------------\n";


for (int i = 0; i < years; i++) {


intAmt = (intTotal) * ((intYear / 100));


intTotal = intTotal + intAmt;


cout << (i + 1) << "\t\t$" << fixed << setprecision(2) << intTotal << "\t\t\t$" << intAmt << "\n";

}

intTotal = intInv;

cout << "\n\nBalance and Interest With Additional Monthly Deposits\n";
cout << "==============================================================\n";
cout << "Year\t\tYear End Balance\tYear End Earned Interest\n";
cout << "--------------------------------------------------------------\n";

for (int i = 0; i < years; i++) {

yearInt = 0;

for (int j = 0; j < 12; j++) {

intAmt = (intTotal + intDepo) * ((intYear / 100) / 12);

yearInt = yearInt + intAmt;

intTotal = intTotal + intDepo + intAmt;

}

cout << (i + 1) << "\t\t$" << fixed << setprecision(2) << intTotal << "\t\t\t$" << yearInt << "\n";


}

return 0;
}
