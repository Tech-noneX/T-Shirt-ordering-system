sizes = ['S','M','L','XL','XXL']
def make_shirt(size='L', text='I love you'):
    size = size.upper()
    order =(
        f"The size of T-shirt you chose is {size}."
        f"The text you chose is'{text}'."
        f"Summarizing your order\nSize-{size}\nText-{text} "
        "Thank you for your order. We will email you when parcel dispatched."
        )
    return order

def customer():
    while True :
        print("For quit press 'q' .")
        size = input("Chose a size of T-shirt the sizes are: S,M,L,XL,XXL.\n:").strip()
        if size == 'q':
            break
        if size.upper() not in sizes :
            print("Your chosen size is not recognized.")
            continue
        print("For quit press 'q' .")
        text = input("Chose any text no longer than 20 characters.\n:")
        if text == 'q':
            break
        if len(text) > 20 :
            print("Too many characters chosen.")
            continue
        print(make_shirt(size=size,text=text))
        break
customer()