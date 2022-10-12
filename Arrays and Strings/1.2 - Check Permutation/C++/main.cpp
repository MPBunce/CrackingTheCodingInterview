#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

bool isAnagram(string StringOne, string StringTwo);

int main(){

    string s1 = "apples";
    string s2 = "aaples";

    if( isAnagram(s1, s2) ){
        printf("\nThe Strings are anagrams!\n");
    } else {
        printf("\nThe Strings are not anagrams :(\n");
    }

    return 0;

}

bool isAnagram(string StringOne, string StringTwo){

    unordered_map<char, int> table;

    if(StringOne.size() != StringTwo.size()){
        return false;
    }

    for(int i=0; i < StringOne.size(); ++i){
        table[ StringOne[i] ]++;
        table[ StringTwo[i] ]--;
    }

    for( auto i : table){

        if(i.second > 0){
            return false;
        }

    }


    return true;
}