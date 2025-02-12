from sys import exit


def main() -> None:
    while True:
        try:
            user_input: str = input('Enter a positive integer: ')
            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()
            start: int = int(user_input)
            if start <= 0:
                print('Integer must be positive...')
                continue
            
            string: str = user_input
            sum: int = 0
            flag: bool = True
            lst: list[int] = []
            while sum != 1:
                sum = 0
                for char in string:
                    sum += int(char) ** 2
                lst.append(sum)
                string = str(sum)
                print(sum)
                if len(set(lst)) != len(lst):
                    flag = False
                    break
            if flag:
                print(f'{start} is a happy number!')
            else:
                print(f'{start} is not a happy number!')
        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
