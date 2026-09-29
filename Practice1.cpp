#include <iostream>
using namespace std;

int main(){
     
    char arr[11];   // array to store the inputs and max_len is 10
    int num;    // index of element to remove from the array
    
    cin >> arr;
    cin >> num;

    // length of the arr
    int len = 0;
    for (int i = 0; i < 11; i++){
        // if the length of array is 0
        if(arr[i] == '\0'){
            len = i;
            break;
        }
    }


    // remove the num from the array and print the array
    // for loop -> num ~ len-1
    for (int i = num; i < len-1; i++){
        arr[i] = arr[i+1];
    }

    len--;
    arr[len] = '\0'; // set the last letter in array as a null

    // print the array
    cout << arr << endl;
    // print the array in reverse order
    for(int i = len -1; i >=0; i--){
        cout << arr[i];
    }

    return 0;
} 