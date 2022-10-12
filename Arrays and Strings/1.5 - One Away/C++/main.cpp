#include <iostream>
#include <string>
#include <unordered_map>
#include <cstdlib>
using namespace std;

bool isOneAway(string One, string Two);

int main(){

    string s1 = "pale";
    string s2 = "paless";

    std::cout<< "Are the two strings " << s1 << " " << s2 <<" one away?\n";
    if(isOneAway(s1, s2)){
        printf("True");
    } else {
        printf("False");
    }



}

bool isOneAway(string One, string Two){

    unordered_map<char, int> charTable;
    int count = 0;

    for(int i = 0; i < One.size(); ++i){
        charTable[ One[i] ]++;
        std::cout<< "\n"<< charTable[ One[i] ] << One[i] << "\n";
    }
    for(int i = 0; i < Two.size(); ++i){
        charTable[ Two[i] ]--;
        std::cout<< "\n" << charTable[ Two[i] ]<< Two[i] << "\n";
    }


    for( auto i : charTable){

        if(i.second != 0){
            count += abs(i.second);
        }
        std::cout<< "\n" <<count;
    }


    if(count == 1){
        return true;
    }

    return false;

}