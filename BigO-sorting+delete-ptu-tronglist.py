'''Dữ liệu nhập
Dòng thứ nhất gồm NN (1 \leq N \leq 1000)(1≤N≤1000) là số lượng sinh viên và kk (1 \leq k \leq N)(1≤k≤N) là số sinh viên cần lấy điểm cao nhất cách nhau bởi một khoảng trắng.
NN dòng tiếp theo, mỗi dòng gồm mã số sinh viên và điểm của sinh viên đó, điểm của sinh viên là một số thực xx (0 \leq x \leq 10)(0≤x≤10).

Dữ liệu xuất
Gồm kk dòng, mỗi dòng là một mã số của k sinh viên có điểm cao nhất.
Khi hai sinh viên có điểm bằng nhau thì ưu tiên sinh viên có mã số sinh viên nhỏ hơn.
Được biết rằng: Mã số của các sinh viên khác nhau là khác nhau.'''
# https://docs.python.org/3/howto/sorting.html

from operator import itemgetter
def multisort(xs, specs):
  for key, reverse in specs:
    xs.sort(key=itemgetter(key), reverse=reverse)
  return xs
n,k = map(int, input().split())
l = []
for i in range(n):
  a,b = map(float, input().split()) 
  l.append([a,b])
#l = sorted(l, key=itemgetter(1), reverse=True)
l = multisort(l, ((0, False), (1, True)))
for i in range(k):
  print(int(l[i][0])

# Nhập n, nhập mảng a, nhập ptu y muốn xóa
n = int(input())
a = list(map(int, input().split()))
y = int(input())
for i in range(n):
    while a[i]==y:
        for j in range(i,n-1):
            a[j]=a[j+1]
        n = n-1
for j in range(0,n):
    print(a[j],end =' ')  
        

# Làm thuần C++, hỉu nha
//SẮP XẾP ĐIỂM

#include <iostream>
using namespace std;

struct Student{
  int id;
  float score;
};

void merge(Student L[], int nL, Student R[], int nR, Student a[], int n){
  int i, j, k;
  i = j = k = 0;

  while (i < nL && j < nR ){
    if (L[i].score > R[j].score || (L[i].score == R[j].score && L[i].id < R[j].id)){
      a[k] = L[i];
      i++;
      k++;
    }
    else{
      a[k] = R[j];
      j++;
      k++;
    }
  }
  
  while (i < nL){
    a[k] = L[i];
    i++;
    k++;
  }
  while (j < nR){
    a[k]  = R[j];
    j++;
    k++;
  }
}

void mergeSort(Student a[], int n){
  if (n <= 1) return;
  
  Student L[500];
  Student R[500];
  int nL = n/2;
  int nR = n-nL;
  
  for (int i = 0; i < nL; i++){
    L[i] = a[i];
  }
  for (int i = 0; i < nR; i++){
    R[i] = a[i + nL];
  }
  
  mergeSort(L, nL);
  mergeSort(R, nR);
  merge(L, nL, R, nR, a, n);
}

int main()
{
// int L[] = {2, 4};
// int R[] = {3, 5, 7};

// int a[1000];

// merge(L, 2, R, 3, a, 5);

int n, k;
cin >> n >> k;

Student a[1000];
for (int i = 0; i < n; i ++){
  cin >> a[i].id >> a[i].score;
}

mergeSort(a,n);

for(int i = 0; i < k; i++){
  cout << a[i].id << endl;
}  
  
  
return 0;
}
        
