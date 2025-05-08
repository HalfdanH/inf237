#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;


class Tree{
public:
    unordered_map<char, Tree*> children;
    int count = 0;
    int end_count = 0;
};

Tree create_tree(string* words, int n){
    Tree root;
    for (int i = 0; i < n; i++){
        root.count += 1;
        Tree* current = &root;
        int count = root.count;

        for (char letter : words[i]){
            if (current->children.find(letter) == current->children.end()){
                current->children[letter] = new Tree();
            }
            current = current->children[letter];
            current->count += 1;
            count += current->count;
        }
        current->end_count = count;
    }
    return root;
}


int main(){

    int n;
    string word;
    cin >> n;
    string words[n];
    for (int i = 0; i < n; i++){
        cin >> words[i];
    }

    Tree t = create_tree(words, n);
    return 0;
}