#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <stack>
#include <algorithm>
using namespace std;

struct Node {
    int depth;
    Node* parent;
    unordered_map<char, Node*> children;
    Node* jump[18];

    Node(Node* p, int d): depth(d), parent(p){
        fill(jump, jump+18, nullptr);
    }
};
vector<Node*> word_end;
Node* root;

Node* build_trie(const vector<string>& words){
    root = new Node(nullptr, 0);
    for (const string& word : words){
        Node* curr = root;
        for (char c : word){
            if(!curr->children.count(c)){
                curr->children[c] = new Node(curr, curr->depth+1);
            }
            curr = curr->children[c];
        }
        word_end.push_back(curr);

    }
    return root;
}

void build_table(Node* root){
    stack<Node*> stk;
    stk.push(root);
    while (!stk.empty()){
        Node* node = stk.top(); stk.pop();
        if(node->parent) {
            node->jump[0]=node->parent;
            for (int i = 1; i < 17; i++){
                Node* curr = node->jump[i-1];
                if (curr && curr->jump[i-1]){
                    node->jump[i] = curr->jump[i-1];
                }
            }
        }
        for (auto& [_, child]: node->children){
            stk.push(child);
        }
    }
}

Node* lca(Node* node1, Node* node2){
    if(node1->depth < node2->depth){
        swap(node1, node2);
    }
    for (int i = 17; i >= 0; i--){
        if (node1->jump[i] && node1->jump[i]->depth >= node2->depth){
            node1 = node1->jump[i];
        }
    }
    if (node1 == node2){
        return node1;
    }
    for (int i = 17; i >= 0; i--){
        if (node1->jump[i] && node2->jump[i] && node1->jump[i] != node2->jump[i]){
            node1 = node1->jump[i];
            node2 = node2->jump[i];
        }
       
    }
    return node1->parent;
}

int main(){
    int n, q;
    cin >> n >> q;
    vector<string> pokemons(n);
    for (int i = 0; i < n; i++){
        cin >> pokemons[i];
    }
    build_trie(pokemons);
    build_table(root);

    while (q--){
        int k, l;
        cin >> k >> l;
        vector<int> indexes(k);
        for (int i = 0; i < k; i++){
            cin >> indexes[i];
            indexes[i] = indexes[i]-1;
        }
        vector<pair<string, int>> sorted;
        for (int i : indexes){
            sorted.emplace_back(pokemons[i], i);
        }
        sort(sorted.begin(), sorted.end());
        vector<Node*> selected;
        for (auto& [_, idx]:sorted){
            selected.push_back(word_end[idx]);
        }

        long total = 0;
        for (int j = 0; j <= k-l; j++){
            Node* p1 = selected[j];
            Node* p2 = selected[j+l-1];
            Node* lca_m = lca(p1, p2);

            Node* lca_l = nullptr;
            if (j>0){
                lca_l = lca(lca_m, selected[j-1]);
            }
            if (j+l<k){
                Node* lca_r = lca(lca_m, selected[j+l]);
                if (!lca_l || (lca_r && lca_r->depth > lca_l->depth)){
                    lca_l = lca_r;
                }
            }
            
            if (lca_l != nullptr){
                total += lca_m-> depth - lca_l->depth;
            }
            else{
                total += lca_m->depth;
            }
        }
        cout << total << "\n";
    }
    return 0;
}