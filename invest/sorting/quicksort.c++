#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int partition (int arr[], int start, int end){
 int pivot = arr[start];
  int k = start; 
  for(int i = k+1; i < end ; i++ ){
    if (pivot > arr[i]) {
      k++;
      swap(arr[i], arr[k]);
    }
  }  
  swap(arr[k], arr[start]);
  return k;
}

void quicksort(int arr[], int start, int end) {
  if (start < end){
    int k = partition(arr, start, end);

    quicksort(arr, start, k-1);
    quicksort(arr, k+1, end);
  }
}


int main(void){

  int arr[] = {4,6,2,1,8};

  quicksort(arr, 0, sizeof(arr)/sizeof(int));

  for (int i = 0 ; i < sizeof(arr)/sizeof(int); i++){
    cout << arr[i] << " ";
  }

  return 0;
}