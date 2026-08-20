/* Includes added so this file compiles standalone. */
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int subarrayBitwiseORs(int* A, int n) {
    int* res = (int*)malloc(sizeof(int) * n * 32);
    int len = 0, l = 0, r;
    
    for (int i = 0; i < n; i++) {
        r = len;
        res[len++] = A[i];
        for (int j = l; j < r; j++) {
            int val = res[j] | A[i];
            if (res[len - 1] != val) {
                res[len++] = val;
            }
        }
        l = r;
    }
    
    qsort(res, len, sizeof(int), cmp);
    if (len == 0) { free(res); return 0; }
    
    int cnt = 1;
    for (int i = 1; i < len; i++) {
        if (res[i] != res[i - 1]) cnt++;
    }
    
    free(res);
    return cnt;
}
