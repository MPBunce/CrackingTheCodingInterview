#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

//Declaring Function
bool isUnique(string inputString);
bool isUniqueTwo(string inputString);

int main() {

    string testString = "Teeeest";
    if(isUniqueTwo(testString)){
        std::cout << "\n" <<testString << " is a unqiue string!\n";
    } else {
        std::cout << "\n" << testString << " is not a unqiue string :(\n";
    }

    return 0;
}

//this is faster doe
bool isUnique(string inputString){

    unordered_map<char, int> table;
    string used = (inputString);
    for(int i = 0; i < used.size(); ++i){

        table[ used[i] ]++;

        if(table[ used[i] ] > 1){
            return false;
        }

    }
    return true;
}

//using no additional data scructures
bool isUniqueTwo(string inputString){

    for(int i = 0; i < inputString.size(); ++i){
        for(int j = i + 1; j < inputString.size(); ++j){

            if(inputString[i] == inputString[j]){
                return false;
            }

        }
    }
    return true;
}