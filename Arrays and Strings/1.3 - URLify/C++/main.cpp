#include <iostream>
#include <string>
using namespace std;

string urlify(string InputString);

int main(){

    string s1 = "the man matthew";

    std::cout << "\nBefore " << s1 << "\n";

    s1 = urlify(s1);

    std::cout << "\nAfter " << s1 << "\n";

}

string urlify(string InputString){
    
    int size = InputString.size();
    string rep = "%20";
    for(int i = 0; i < size; ++i){
        if(InputString[i] == ' '){

            InputString.replace(i,1,rep);

        }

    }

    return InputString;
}