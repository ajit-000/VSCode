// Let the meter rent be 200 rupees

#include <stdio.h>
int main()
{
    int last = 123456, present = 123789, result;
    float total_bill, bill, gst;

    result = present - last;
    if (result <= 150)
    {
        bill = 200 + result * 4.56;
        gst = (bill * 2.5) / 100;
        total_bill = bill + gst;
        printf("Your bill is : %.2f", total_bill);
    }
    else
    {
        bill = 200 + (result - 100) * 7.54;
        gst = (bill * 2.5) / 100;
        total_bill = bill + gst;
        printf("Your bill is : %.2f", total_bill);
    }

    return 0;
}