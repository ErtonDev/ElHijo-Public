# Modules
import os
import io
import sys
import colorama
from colorama import Fore, Back, Style

# Modules setup
os.system('clear')
colorama.init(autoreset=True)


# Functions
class Database:

    def __init__(self):
        # Visuals
        self.standard = Style.RESET_ALL
        self.title = Fore.LIGHTBLUE_EX + "----- Database -----"
        self.prompt = Fore.LIGHTBLUE_EX + "//: " + self.standard
        self.p_deci = Fore.LIGHTBLUE_EX + "[s/n]: " + self.standard
        self.barrier = Fore.WHITE + "----- ----- ----- ----- ----- -----"
        self.fail_msg = Fore.LIGHTRED_EX + " Command failed -> help"
        self.cancel_msg = Fore.LIGHTRED_EX + "OPERATION CANCELLED"
        self.die_msg = Fore.LIGHTBLUE_EX + "----- * Closed -----\n"

        # Errors
        self.valueerror = Fore.LIGHTRED_EX + "ValueError: Use a valid value\n"
        self.iderror = Fore.LIGHTRED_EX + "IDError: ID not available\n"

        # Information
        self.commands_list  = ["help", "clear", "reg", "regcls", "mer", "profls", "prof", "quit"]
        self.pcommands_list = ["help", "clear", "det", "exit"]

    def welcome(self):
        print(self.title)

    def command_prompt(self):
        command = str(input(self.prompt))
        return command.lower()

    def fail(self, wrong_command):
        print(self.barrier)
        print(Back.LIGHTRED_EX + " " + wrong_command + " " + self.standard + self.fail_msg + '\n')

    # Commands
    def c_help(self):
        print(self.barrier)
        print("Commands list: " + Fore.LIGHTYELLOW_EX + str(self.commands_list) + '\n')

    def c_clear(self):
        os.system('clear')
        print(self.title)

    def c_reg(self):
        open_reg = io.open("registro.txt", 'r')
        text_reg = open_reg.read()
        open_reg.close()

        print(self.barrier)
        print(text_reg + '\n')

    def c_regcls(self):
        print(self.barrier)
        print("Data from " + Fore.LIGHTBLUE_EX + "registro.txt" + self.standard + " will be deleted:" + '\n')

        decision = input(str(self.p_deci))

        if decision.lower() == "s":
            cls_r = io.open("registro.txt", 'w')
            cls_r.write("REGISTRO:")
            cls_r.close()

            print(self.barrier)
            print("Data from " + Fore.LIGHTBLUE_EX + "registro.txt" + self.standard + " has been deleted\n")

        elif decision.lower() == "n":
            print(self.barrier)
            print(self.cancel_msg + '\n')

        else:
            self.fail(decision)

    def c_mer(self):
        # 1
        read_stock_emprs1 = io.open(f"bolsa/cant/cant_emprs1.txt", 'r')
        actual_stock_emprs1 = read_stock_emprs1.readlines()
        read_stock_emprs1.close()
        cant_e_1 = actual_stock_emprs1[0]

        read_cr_emprs1 = io.open(f"bolsa/cr/cr_emprs1.txt", 'r')
        actual_cr_emprs1 = read_cr_emprs1.readlines()
        read_cr_emprs1.close()
        e_1 = actual_cr_emprs1[0]

        # 2
        read_stock_emprs2 = io.open(f"bolsa/cant/cant_emprs2.txt", 'r')
        actual_stock_emprs2 = read_stock_emprs2.readlines()
        read_stock_emprs2.close()
        cant_e_2 = actual_stock_emprs2[0]

        read_cr_emprs2 = io.open(f"bolsa/cr/cr_emprs2.txt", 'r')
        actual_cr_emprs2 = read_cr_emprs2.readlines()
        read_cr_emprs2.close()
        e_2 = actual_cr_emprs2[0]

        # 3
        read_stock_emprs3 = io.open(f"bolsa/cant/cant_emprs3.txt", 'r')
        actual_stock_emprs3 = read_stock_emprs3.readlines()
        read_stock_emprs3.close()
        cant_e_3 = actual_stock_emprs3[0]

        read_cr_emprs3 = io.open(f"bolsa/cr/cr_emprs3.txt", 'r')
        actual_cr_emprs3 = read_cr_emprs3.readlines()
        read_cr_emprs3.close()
        e_3 = actual_cr_emprs3[0]

        # 4
        read_stock_emprs4 = io.open(f"bolsa/cant/cant_emprs4.txt", 'r')
        actual_stock_emprs4 = read_stock_emprs4.readlines()
        read_stock_emprs4.close()
        cant_e_4 = actual_stock_emprs4[0]

        read_cr_emprs4 = io.open(f"bolsa/cr/cr_emprs4.txt", 'r')
        actual_cr_emprs4 = read_cr_emprs4.readlines()
        read_cr_emprs4.close()
        e_4 = actual_cr_emprs4[0]

        # n_1
        read_stock_emprs_n_1 = io.open(f"bolsa/cant/cant_emprs_n_1.txt", 'r')
        actual_stock_emprs_n_1 = read_stock_emprs_n_1.readlines()
        read_stock_emprs_n_1.close()
        cant_e_n1 = actual_stock_emprs_n_1[0]

        read_cr_emprs_n_1 = io.open(f"bolsa/cr/cr_emprs_n_1.txt", 'r')
        actual_cr_emprs_n_1 = read_cr_emprs_n_1.readlines()
        read_cr_emprs_n_1.close()
        e_n1 = actual_cr_emprs_n_1[0]

        # n_2
        read_stock_emprs_n_2 = io.open(f"bolsa/cant/cant_emprs_n_2.txt", 'r')
        actual_stock_emprs_n_2 = read_stock_emprs_n_2.readlines()
        read_stock_emprs_n_2.close()
        cant_e_n2 = actual_stock_emprs_n_2[0]

        read_cr_emprs_n_2 = io.open(f"bolsa/cr/cr_emprs_n_2.txt", 'r')
        actual_cr_emprs_n_2 = read_cr_emprs_n_2.readlines()
        read_cr_emprs_n_2.close()
        e_n2 = actual_cr_emprs_n_2[0]

        print(self.barrier)
        print("Normal (CR): " + Fore.LIGHTYELLOW_EX + f"    {e_1} | {e_2} | {e_3} | {e_4}\n" + Fore.LIGHTWHITE_EX +
              "Normal (CANT): " + Fore.LIGHTYELLOW_EX + f"  {cant_e_1} | {cant_e_2} | {cant_e_3} | {cant_e_4}\n")

        print("Negro (CR): " + Fore.LIGHTYELLOW_EX + f"     {e_n1} | {e_n2}\n" + Fore.LIGHTWHITE_EX +
              "Negro (CANT): " + Fore.LIGHTYELLOW_EX + f"   {cant_e_n1} | {cant_e_n2}\n")

    def c_profls(self):
        print(self.barrier)

        allprofs = os.listdir(path='./profile')
        for i in allprofs:
            print(i)

        print("")

    # PROFILE commands

    def p_help(self):
        print(self.barrier)
        print("Commands list: " + Fore.LIGHTYELLOW_EX + str(self.pcommands_list) + '\n')

    # PROFILE commands

    def c_prof(self):
        try:
            print(self.barrier)
            profile_id = int(input(Fore.LIGHTBLUE_EX + "[Profile·ID]: "))

            # enter profile
            allprofs = os.listdir(path='./profile')
            found = False
            for i in allprofs:
                if int(i[:18]) == profile_id:
                    found = True

            # session
            if found == True:
                print(Fore.LIGHTYELLOW_EX + f"[(1): {profile_id}_profile]!\n")

                while True:
                    user_pinput = str(input(Fore.LIGHTBLUE_EX + f"*p·//{profile_id}/: " + self.standard))

                    if user_pinput == self.pcommands_list[0]:
                        self.p_help()

                    elif user_pinput == self.pcommands_list[1]:
                        # TODO: Code functionality for clear command
                        pass

                    elif user_pinput == self.pcommands_list[2]:
                        # TODO: Code functionality for det command
                        pass

                    elif user_pinput == self.pcommands_list[3]:
                        break

                    else:
                        self.fail(wrong_command=user_pinput)

                print(Fore.LIGHTYELLOW_EX + f"[(0): {profile_id}_profile]!\n")

            else:
                print(self.iderror)

        except ValueError:
            print(self.valueerror)

    def c_quit(self):
        print(self.die_msg)
        sys.exit()


# Database setup
database = Database()
database.welcome()

# Loop
while True:
    user_input = database.command_prompt()

    if user_input == database.commands_list[0]:
        database.c_help()

    elif user_input == database.commands_list[1]:
        database.c_clear()

    elif user_input == database.commands_list[2]:
        database.c_reg()

    elif user_input == database.commands_list[3]:
        database.c_regcls()

    elif user_input == database.commands_list[4]:
        database.c_mer()

    elif user_input == database.commands_list[5]:
        database.c_profls()

    elif user_input == database.commands_list[6]:
        database.c_prof()

    elif user_input == database.commands_list[7]:
        database.c_quit()

    else:
        database.fail(wrong_command=user_input)
