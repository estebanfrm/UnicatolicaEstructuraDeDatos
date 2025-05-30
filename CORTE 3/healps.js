class MinHeap {
    (maxSize){
        this.heap=new Array(maxSize)
        this.size=0;
        this maxSize=maxSize;
    }

    parentIndix(i){
        return Math.floor((i-1)/2);
    }
    leftChildIndex(i){
        return 1*2+1;

    }
    rightChildIndex(i){
        return 1*2+2;
    }
    isLeaf(i){
        return (
            this.leftChildIndex(i) >=this.size &&
            this.rightChildIndex(i) >=this.size
        );
    }
    swap(i, j){
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    insert(element){
        if (this.size >= this.maxSize) {
            return;
        }
        this.heap[this.size] = element;
        let current = this.size;

        while (
            current > 0 &&
            this.heap[current] < this.heap[]
        )
    }
}