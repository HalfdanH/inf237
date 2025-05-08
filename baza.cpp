#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct TrieNode {
    TrieNode* children[26];
    int prefix_count;     // Like t[0]
    int full_word_score;  // Like t[1]
    bool is_word;         // Marks end of word

    TrieNode() {
        for (int i = 0; i < 26; ++i) children[i] = nullptr;
        prefix_count = 0;
        full_word_score = 0;
        is_word = false;
    }
};

void insert(TrieNode* root, const string& word) {
    TrieNode* node = root;
    int count = 0;
    for (char ch : word) {
        int idx = ch - 'a';
        if (!node->children[idx])
            node->children[idx] = new TrieNode();
        node = node->children[idx];
        node->prefix_count += 1;
        count += node->prefix_count;
    }
    node->full_word_score = count;
    node->is_word = true;
}

int query(TrieNode* root, const string& word) {
    TrieNode* node = root;
    int count = 0;
    for (char ch : word) {
        int idx = ch - 'a';
        if (!node->children[idx])
            return count;
        node = node->children[idx];
        count += node->prefix_count;
    }
    return node->is_word ? node->full_word_score : count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; ++i)
        cin >> words[i];

    TrieNode* root = new TrieNode();
    for (const string& word : words)
        insert(root, word);

    int m;
    cin >> m;
    string query_word;
    for (int i = 0; i < m; ++i) {
        cin >> query_word;
        cout << query(root, query_word) << '\n';
    }

    return 0;
}
