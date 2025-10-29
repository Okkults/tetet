from broker import go_long, go_short

def main():
    print("Alpaca Paper Trading CLI")
    print("Commands: long | short")
    print("Press Ctrl+C to exit\n")
    
    while True:
        try:
            cmd = input("> ").strip().lower()
            
            if cmd == "long":
                try:
                    order = go_long()
                    print(f"Order ID: {order.get('id')}, Status: {order.get('status')}")
                except Exception as e:
                    print(f"Error: {e}")
            
            elif cmd == "short":
                try:
                    order = go_short()
                    print(f"Order ID: {order.get('id')}, Status: {order.get('status')}")
                except Exception as e:
                    print(f"Error: {e}")
            
            else:
                print("unknown command")
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
