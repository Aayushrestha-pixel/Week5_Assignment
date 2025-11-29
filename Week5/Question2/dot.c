// c code for dot
int dot_calc(int *a, int *b, int n) {
    int s = 0;  // store sum
    for(int i=0;i<n;i++){
        s += a[i] * b[i]; // multiply each
    }
    return s;
}