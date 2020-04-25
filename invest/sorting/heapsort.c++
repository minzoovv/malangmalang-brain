#include <algorithm>
#include <iostream>

using namespace std;

void heapify(int arr[], int p_idx, int n){
  
  int lc, rc, mc;
  lc = p_idx * 2 + 1;
  if (lc >= n) return;

  rc = lc + 1;
  mc = (rc >= n) ? lc : (arr[lc] > arr[rc]) ? lc : rc;  

  if (arr[p_idx] < arr[mc]){
    swap(arr[p_idx], arr[mc]);  
    heapify(arr, mc, n);
  }

  return;
}

int main(){
  int arr[] = {4,6,2,1,8};
  int size = sizeof(arr)/sizeof(int);

  for (int i = (size/2)-1; i > -1 ; i--){
    heapify(arr, i, size);
  }

  for (int i = 0 ; i < size ; i++){
    cout << arr[i] << " ";
  }
  cout << "\n";
  
  for (int i = size-1; i >= 0 ; i--){
    swap(arr[0], arr[i]);
    heapify(arr, 0, i);
  }

  for (int i = 0 ; i < size ; i++){
    cout << arr[i] << " ";
  }
  cout << "\n";
}
