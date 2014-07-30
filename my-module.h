void MyModuleDoAction (void);

class Rectangle {
    int width, height;
    int *pointer;
  public:
    void set_values (int,int);
    int area() {return width*height;}
    void set_pointer (int* = 0);

};
