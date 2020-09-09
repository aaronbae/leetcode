// you can use includes, for example:
// #include <algorithm>
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int recurse(tree * current, int prevMax ){
    if(current == NULL){
        return 0;
    }
    int result = 0;
    if(prevMax <= current->x){
      result += 1;
    }
    result += recurse(current->l, max(prevMax, current->x));
    result += recurse(current->r, max(prevMax, current->x));
    return result;
}


int solution(tree * T) {
    // write your code in C++14 (g++ 6.2.0)
    return recurse(T, -100000);
}
