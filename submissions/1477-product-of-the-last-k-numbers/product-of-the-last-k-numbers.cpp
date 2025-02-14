class ProductOfNumbers {
private:
    vector<int> prefixProducts;

public:
    ProductOfNumbers() {
        prefixProducts = {1}; // Initialize with 1 to handle multiplication correctly
    }
    
    void add(int num) {
        if (num == 0) {
            prefixProducts = {1}; // Reset prefix product because of zero
        } else {
            prefixProducts.push_back(prefixProducts.back() * num);
        }
    }
    
    int getProduct(int k) {
        int n = prefixProducts.size();
        if (k >= n) return 0; // If k is larger than the stored prefix products, it means there was a zero
        return prefixProducts[n - 1] / prefixProducts[n - k - 1];
    }
};
