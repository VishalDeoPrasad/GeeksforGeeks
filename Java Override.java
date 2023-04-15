class Child extends Parent
{
    @Override
    void show(int p) { System.out.print(p+" "); }
    
    @Override
    void print(int q)
    {
        System.out.println(q*q+" ");
    }
}