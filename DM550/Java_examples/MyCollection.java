public interface MyCollection<E> {
    //Ensures that this collection contains e.
    public void add(E e);

    //Removes all elements in this collection.
    public void clear();

    //Checks whether this collection contains e.
    public boolean contains(E e);

    //Checks whether this collection is empty.
    public boolean isEmpty();

    //Returns the number of elements in this collection.
    public int size();
}