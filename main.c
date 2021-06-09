
int func6(int a) {
	int c[10] = {0};
	printf("%d",c[10000]);
	printf("result = 120");
}
int func7(int a) {
	int c[10] = {0};
	printf("result = 220");
}
void func5(int a) {
	printf("result > 100.\n");
	if (a == 120) {
		func6(a);
	}
    else if (a == 220){
        func7(a);
    }
}
void func4(int a) {
	printf("result > 50.\n");
	if (a > 100) {
		func5(a);
	}
}
int func1(int a) 
{
	printf("result > 10.\n");
	if (a > 50) {
		func4(a);
	}
	return 0;
}

int func3() {
   	int c[10] = {0};
	printf("%d",c[99999]);
	printf("result = 10.\n");
	return 0;
}

void func2();

int main()
{
	int a, b;
	scanf_s("%d,%d",&a,&b);
	if (a > 10)
	{
		func1(a);
	}
	else if (a < 10)
	{
		func2();
	}
	else
	{
		func3();
	}
	return 0;
}

void func2() {
	printf("result < 10.\n");
}