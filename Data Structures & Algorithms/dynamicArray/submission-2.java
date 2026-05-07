class DynamicArray {
    private int[] arr;
    private int size;
    private int cap;
    public DynamicArray(int capacity) {
        arr = new int[capacity];
        cap = capacity;
        this.size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == cap){
            this.resize();
        }
        arr[size] = n;
        size ++;
    }

    public int popback() {
        if (size >0) {
            size--;
        }
        return arr[size];
        
    }

    private void resize() {
        this.cap = cap*2;
        int[] temp = new int[cap];
        for (int i = 0; i < size; i++){
            temp[i] = arr[i];
        }
        arr = temp;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return cap;
    }
}
