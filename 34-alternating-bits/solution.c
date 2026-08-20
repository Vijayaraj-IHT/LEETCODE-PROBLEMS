#include <stdbool.h>

bool hasAlternatingBits(int n) {
    long xor_result = n ^ (n >> 1);
    return (xor_result & (xor_result + 1)) == 0;
}
