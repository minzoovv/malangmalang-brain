#include <algorithm>
#include <iostream>

using namespace std;

void merge(int arr[], int start, int mid, int end){
  int n1 = mid - start + 1;
  int n2 = end - mid;
    
  int left[n1], right[n2];

  for (int i=0 ; i < n1; i++) left[i] = arr[start+i];
  for (int i=0 ; i < n2 ; i++) right[i] = arr[mid+1+i];

  int i = 0;
  int j = 0;
  int k = start;
  while (i < n1 && j < n2){
      if (left[i] <= right[j]){
        arr[k] = left[i];
        i++;
      }
      else {
        arr[k] = right[j];
        j++;
      }
      k++;
  }
    
  while (i < n1) { 
    arr[k] = left[i]; 
      i++; 
      k++; 
  } 
    
  while (j < n2) { 
      arr[k] = right[j]; 
      j++; 
      k++; 
    }
}


void mergesort(int arr[], int start, int end){
  if (start < end){
    int mid = (start + (end-1)) / 2;
    mergesort(arr, start, mid);
    mergesort(arr, mid+1, end);

    merge(arr, start, mid, end);
  }
}

int main(){

  int arr[] = {5,2,6,3,1};
  int size = sizeof(arr)/sizeof(arr[0]);
  
  mergesort(arr, 0, size-1);

  for (int i= 0 ; i < size ; i++){
    cout << arr[i] << " "; 
  }
  return 0;
}